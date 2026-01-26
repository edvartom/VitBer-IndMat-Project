import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fft2, ifft, ifft2, fftfreq, fftshift
import pandas as pd
from scipy.integrate import dblquad
import matplotlib.animation as animation
import itertools

# Task 1i
theta_c=1.5
def F(u,theta,theta_c=theta_c):
    '''
    INPUT
    u:          Array or float. Substance density.
    theta:      Float. Temperature.
    theta_c:    Float. Critical temperature. Set to 1.5.
    
    OUTPUT
    Float. Helmholtz free energy density as per eq. (83). 

    '''
    return (theta_c/2)*(1-u**2)-(theta/2)*((1-u)*np.log((1-u)/2)+(1+u)*np.log((1+u)/2))

# Task 2

def biharmonic_solver(X, Y, F, c, mean=0.0):
    '''
    Solve the biharmonic equation in 2D using the spectral method.

    INPUT
        X (ndarray): 2D array of x-coordinates.
        Y (ndarray): 2D array of y-coordinates.
        F (ndarray): 2D array representing the right-hand side of the biharmonic equation.
        c (float): Constant coefficient in the biharmonic equation.
        mean (float, optional): Desired mean value of the solution in case c = 0. Default is 0.0.

    OUTPUT
        U (ndarray): 2D array representing the solution to the biharmonic equation.
    '''

    # Extract grid data
    x, y = X[0,:], Y[:,0]
    Nx, Ny = len(x), len(y)
    if Nx < 2 or Ny < 2:
        raise ValueError("Grids must have at least two points in each space direction!")
    dx, dy=x[1]-x[0], y[1]-y[0]     # Distance between samples

    # Compute wave number grid
    kx = fftfreq(Nx, d=dx)*2*np.pi
    ky = fftfreq(Ny, d=dy)*2*np.pi
    KX, KY = np.meshgrid(kx, ky, sparse=True)
    K4=KX**4+KY**4+2*(KX**2)*KY**2 # Biharmonic operator

    F_hat=fft2(F) # Fourier transform of rhs

    tol=0.0001 # Tolerance
    # Find lowest frequency in Fourier-space (in absolute value)
    kx_min=min(abs(kx))
    ky_min=min(abs(ky))
    k_min=abs(np.amin([kx_min,ky_min]))

    if c<=tol*k_min**4:         # Check if c=0
        K4[0,0]=1               # Avoid division by zero
        U_hat = F_hat / (K4)  # Find Fourier transform of U
        U_hat[0,0]=mean*Nx*Ny   # Define mean value
                                # Multiply with number of gridpoints because of division by Nx*Ny in the inverse FFT
        U = ifft2(U_hat).real   # Inverse Fourier transform of solution
        return U
    
    # If c is not 0, no danger of division by zero
    U_hat = F_hat / (K4+c)
    U = ifft2(U_hat).real
    return U
    
# Exact solution
def manufacture_solution_biharmonic(u_str,c):
    '''
    Manufacture f for the biharmonic equation with a solution u_str.

    INPUT
    u_str: String. User defined solution.
    c:     Float. Non-negative constant.

    OUTPUT
    u:     Lambda-function. u_str converted to a function.
    f:     Lambda-function. Right hand side of biharmonic equation with solution u.

    '''
    import sympy as sy
    from sympy import sin, cos, exp

    x, y = sy.symbols('x y')
    u_sy = eval(u_str)
    biharm = lambda u: sy.diff(u, x, x, x, x) + sy.diff(u, y, y, y, y)+2*sy.diff(u, x, x, y, y)+c*u
            # biharm = lhs
    f_sy = sy.simplify(biharm(u_sy)) # rhs
    print(f'u = {u_sy}')
    print(f'f = {f_sy}')

    # Turn strings into functions
    u = sy.lambdify((x, y), u_str, modules='numpy')
    f = sy.lambdify((x, y), f_sy, modules='numpy')
    return u, f

# Task 3.2 and 3.3

def transient_biharmonic_solver(*, kappa, 
                                   X, Y, U0, 
                                   t0, T, Nt, 
                                   theta=0.5,
                                   g=None):
    """
    Solve the transient biharmonic equation using the theta method.

    Parameters:
    ----------- 
    kappa (float): Diffusion coefficient.
    X (ndarray): 2D array of x-coordinates.
    Y (ndarray): 2D array of y-coordinates.
    U0 (ndarray): Initial condition array.
    t0 (float): Initial time.
    T (float): Final time.
    Nt (int): Number of time steps.
    g (callable, optional): Source term function g(X, Y, t). Defaults to None.

    Yields:
    -------
    tuple: A tuple containing the discrete Fourier transform of U at t, and the current time t.
    """

    # Extract grid data
    x, y = X[0,:], Y[:,0]
    Nx, Ny = len(x), len(y)
    if Nx < 2 or Ny < 2:
        raise ValueError("Grids must have at least two points in each space direction!")
    dx, dy = x[1] - x[0], y[1] - y[0]     # Distance between samples

    # Compute wave number grid
    kx = fftfreq(Nx, d=dx/(2*np.pi))
    ky = fftfreq(Ny, d=dy/(2*np.pi))
    KX, KY = np.meshgrid(kx, ky, sparse=True)
    K4=KX**4+KY**4+2*KX**2*KY**2 # Biharmonic operator

    U_hat = fft2(U0)    # Compute Fourier transform of the initial value

    # Time stepping 
    t = t0 
    dt = (T-t0)/Nt

    # For convenience when plotting, computing errors, etc., 
    # return the initial solution and initial time.
    yield U_hat, t 
   
    while t < T-dt/2:
        # Solve for next time step and update time
        if g is not None:
            G_hat_np1 = fft2(g(X,Y,t+dt))
            G_hat_n = fft2(g(X,Y,t))
        else:
            G_hat_np1 = 0
            G_hat_n = 0
        
        
        #U_{n+1}=R(z)*U_{n}+g_term
        g_term=dt*(theta*G_hat_np1+(1-theta)*G_hat_n)/(1+kappa*K4*theta*dt)
        R_term=1-((dt*kappa*K4)/(1+dt*theta*K4*kappa))
        U_hat=U_hat*R_term+g_term 

        t=t+dt
        yield U_hat, t

def manufacture_solution_td_biharmonic(u_str, kappa):
    import sympy as sy
    from sympy import sin, cos, exp
    x, y, t = sy.symbols('x y t')
    u_sy = eval(u_str)
    biharm = lambda u: sy.diff(u, x, x, x, x) + sy.diff(u, y, y, y, y)+2*sy.diff(u, x, x, y, y)
    g_sy =  sy.diff(u_sy, t) + kappa*sy.simplify(biharm(u_sy))
    u = sy.lambdify((x, y, t), u_sy, modules='numpy')
    g = sy.lambdify((x, y, t), g_sy, modules='numpy')
    print(f'u = {u_sy}')
    print(f'u0 = {u_sy.subs(t, 0)}')
    print(f'g = {g_sy}')
    return u, g

# Task 4

def cahn_hilliard_backward_euler(*, 
                                kappa, 
                                X, Y, U0, 
                                t0, T, Nt,
                                g, 
                                alpha=1.5):
    """
    Implements the Cahn-Hilliard equation solver using the backward Euler method 
    with a convex-concave splitting approach.

    Parameters:
    -----------
    kappa : float
        Diffusion coefficient for the biharmonic operator.
    X : ndarray
        2D array representing the x-coordinates of the grid.
    Y : ndarray
        2D array representing the y-coordinates of the grid.
    U0 : ndarray
        Initial condition for the solution.
    t0 : float
        Initial time.
    T : float
        Final time.
    Nt : int
        Number of time steps.
    g : callable or None
        Source term as a function of (X, Y, t). If None, no source term is applied.
    alpha : float, optional
        Convex-concave splitting parameter. Default is 1.5.

    Yields:
    -------
    tuple: A tuple containing the discrete Fourier transform of U at t, and the current time t.

    """

    # Extract grid data
    x, y = X[0,:], Y[:,0]
    Nx, Ny = len(x), len(y)
    if Nx < 2 or Ny < 2:
        raise ValueError("Grids must have at least two points in each space direction!")
    dx, dy = x[1] - x[0], y[1] - y[0]     # Distance between samples

    # Compute wave number grid
    kx = fftfreq(Nx, d=dx/(2*np.pi))
    ky = fftfreq(Ny, d=dy/(2*np.pi))
    KX, KY = np.meshgrid(kx, ky, sparse=True)
    K2=-KX**2-KY**2
    K4=KX**4+KY**4+2*KX**2*KY**2 # Biharmonic operator

    U_hat = fft2(U0)    # Compute Fourier transform of the initial value
    f2=U0**3-(1+alpha)*U0
    F2=fft2(f2)

    # Time stepping 
    t = t0 
    dt = (T-t0)/Nt

    # For convenience when plotting, computing errors, etc., 
    # return the initial solution and initial time.
    yield U0, t 


    while t < T-dt/2:
        # Solve for next time step and update time
        if g is not None:
            G_hat_np1 = fft2(g(X,Y,t+dt))
        else:
            G_hat_np1 = 0
        
        U_hat=(K2*F2+(U_hat/dt)+G_hat_np1)/((1/dt)+kappa*K4-alpha*K2)
        U_n=ifft2(U_hat).real
        f2=U_n**3-(1+alpha)*U_n
        F2=fft2(f2)
        t=t+dt
        yield U_n, t

# Assume M=1 
def manufacture_solution_cahn_hillard_be(u_str, kappa):
    import sympy as sy
    from sympy import sin, cos, exp
    x, y, t = sy.symbols('x y t')
    u_sy = eval(u_str)
    biharm = lambda u: sy.diff(u, x, x, x, x) + sy.diff(u, y, y, y, y)+2*sy.diff(u, x, x, y, y)
    laplacian= lambda u: -sy.diff(u**3-u,x,x)-sy.diff(u**3-u,y,y)
    g_sy =  sy.diff(u_sy, t) + kappa*sy.simplify(biharm(u_sy))+sy.simplify(laplacian(u_sy))
    u = sy.lambdify((x, y, t), u_sy, modules='numpy')
    g = sy.lambdify((x, y, t), g_sy, modules='numpy')
    print(f'u = {u_sy}')
    print(f'u0 = {u_sy.subs(t, 0)}')
    print(f'g = {g_sy}')
    return u, g

# Task 5
def IMEX_song(*, kappa, X, Y, U0, 
            t0, T, Nt, g, alpha_arr, beta_arr, alpha=1.5):
    
    """
    Implements the Cahn-Hilliard equation solver using the Song-scheme.

    Parameters:
    -----------
    kappa : float
        Diffusion coefficient for the biharmonic operator.
    X : ndarray
        2D array representing the x-coordinates of the grid.
    Y : ndarray
        2D array representing the y-coordinates of the grid.
    U0 : ndarray
        Initial condition for the solution.
    t0 : float
        Initial time.
    T : float
        Final time.
    Nt : int
        Number of time steps.
    g : callable or None
        Source term as a function of (X, Y, t). If None, no source term is applied.
    alpha_arr : (1,4) ndarray
        Alpha coefficients.
    beta_arr : (1,2) ndarray
        Beta coefficients.
    

    Yields:
    -------
    tuple: A tuple containing the discrete Fourier transform of U at t, and the current time t.

    """

    # Extract grid data
    x, y = X[0,:], Y[:,0]
    Nx, Ny = len(x), len(y)
    if Nx < 2 or Ny < 2:
        raise ValueError("Grids must have at least two points in each space direction!")
    dx, dy = x[1] - x[0], y[1] - y[0]     # Distance between samples

    # Compute wave number grid
    kx = fftfreq(Nx, d=dx/(2*np.pi))
    ky = fftfreq(Ny, d=dy/(2*np.pi))
    KX, KY = np.meshgrid(kx, ky, sparse=True)
    K2=-KX**2-KY**2
    K4=KX**4+KY**4+2*KX**2*KY**2 # Biharmonic operator

    a10, a11, a20, a21, a22=alpha_arr
    b1, b2=beta_arr

    U_hat = fft2(U0)    # Compute Fourier transform of the initial value
    f=U0**3-(1+alpha)*U0
    F=fft2(f)

    # Time stepping 
    t = t0 
    dt = (T-t0)/Nt

    # For convenience when plotting, computing errors, etc., 
    # return the initial solution and initial time.
    yield U0, t 


    while t < T-dt/2:
        # Solve for next time step and update time
        if g is not None:
            G_hat = fft2(g(X,Y,t+dt/2))
        else:
            G_hat = 0
        
        U1_hat=(U_hat+dt*(K2*F+G_hat))/(1+dt*kappa*K4-K2*dt*alpha)
        U1=ifft2(U1_hat).real
        f1=U1**3-(1+alpha)*U1
        F1=fft2(f1)

        U2_hat=(a10*U_hat+a11*U1_hat+b1*dt*(K2*F1+G_hat))/(1+b1*dt*kappa*K4-K2*dt*alpha*b1)
        U2=ifft2(U2_hat).real
        f2=U2**3-(1+alpha)*U2
        F2=fft2(f2)

        U_hat=(a20*U_hat+a21*U1_hat+a22*U2_hat+b2*dt*(K2*F2+G_hat))/(1+b2*dt*kappa*K4-K2*dt*b2*alpha)
        U_n=ifft2(U_hat).real
        f=U_n**3-(1+alpha)*U_n
        F=fft2(f)
        t=t+dt

        yield U_n, t

# Task 6
def make_animation(Uts, Lx, Ly, interval=10**(-25)):
    # Splitting the Uts into two iterables
    for_init_vals,all_Uts=itertools.tee(Uts, 2)
    # Using up the initial values from the first iterable
    U0,t0=next(for_init_vals)

    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)
    img = ax.imshow(U0,interpolation='bilinear',extent=[0,Lx,0,Ly])
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$y$')
    ax.set_title("Solution of Cahn-Hilliard")
    tx = ax.text(Lx*0.02,Ly*0.95,f"t={t0:.3f}",
                bbox=dict(boxstyle="round",ec='white',fc='white'))
    col_bar=plt.colorbar(img,ax=ax)
    img.set_clim(vmin=-1,vmax=1)

    def animate(Ut):
        U, t = Ut
        img.set_data(np.real(U))
        tx.set_text(f't={t:.3f}')
        return img
    
    full_animation = animation.FuncAnimation(fig,animate,frames=all_Uts,interval=10**(-25),blit=False,repeat=True)
    return full_animation

# Make an approximated functon F:
def F_approx(u):
    return 1/4*(u**2 - 1)**2

# Calculate total mass
def total_mass(u):
    '''
    Calculates the total mass by summing (instead of integrating)
    the substance density at each point.

    Parameters:
    -------
    u : 2D array of floats
        Substance densities at each point

    Returns: 
    ---------
    float: Total mass
    '''
    return np.sum(u)

# Calculate the interface energy
def E_interface(kappa, F_approx, u):
    '''
    Calculates the interface energy as given in equation 81 in the project description,
    (E_interface=the integral over omega of kappa/2 times (nabla*u)^2 times F(u)).
    The integral is replaced by a summation, since we are working with descrete values,
    and are only interested in energy differences between timesteps and types of energy
    (mixing or interface), and are not interested in the actual values for the energy.

    Parameters:
    --------------
    kappa : float
        constant
    F : Callable
        Function for energy density that takes u and theta as variables
    u : Array or float
        Substance density
    theta : float
        Separation parameter for F. Default value 0.5.

    Returns:
    ----------
    2D array: Interface energy
    '''
    return kappa/2*np.sum(np.array(np.abs(np.gradient(u)))**2 + F_approx(u))


# Calculate the mixing energy
def E_mix(F_approx,u):
    '''
    Calculates the mixing energy as given in equation 81 in the project description,
    (E_mix=the integral over omega of F(u)). The integral is replaced by a summation,
    since we are working with descrete values, and are only interested in energy differences
    between timesteps and types of energy (mixing or interface), and are not interested
    in the actual values for the energy.

    Parameters:
    ----------------
    F : Callable
        Function for energy density that takes u and theta as variables
    u : Array or float
        Substance density
    theta : float
        Separation parameter for F. Default value 0.5.

    Returns:
    ----------------
    2D array: Mixing energy
    '''
    return np.sum(F_approx(u))


# Calculate the total energy
def E_tot(kappa, F_approx, u):
    '''
    Calculates the total energy in the system by summing the interface and the mixing energy.

    Parameters:
    --------------
    kappa : float
        constant
    F : Callable
        Function for energy density that takes u and theta as variables
    u : Array or float
        Substance density

    Returns:
    ----------
    2D array: Interface energy
    '''
    return E_interface(kappa, F_approx, u) + E_mix(F_approx, u)


# Calculate total mass, mixing energy, interface energy and total energy
def calculate_integrals_for_task_6(Uts, kappa, F_approx):
    U_lst = [u for u, t in Uts]
    Nt = len(U_lst)
    N_samples=10
    frac = int(Nt/N_samples)
    mass_arr,E_interface_arr,E_mix_arr,E_tot_arr=np.zeros(N_samples),np.zeros(N_samples),np.zeros(N_samples),np.zeros(N_samples)
    for i in range(N_samples):
        chosen_index=int(i/frac)
        mass_arr[i]=total_mass(U_lst[chosen_index])
        E_interface_arr[i]=E_interface(kappa, F_approx, U_lst[chosen_index])
        E_mix_arr[i]=E_mix(F_approx,U_lst[chosen_index])
        E_tot_arr[i]=E_tot(kappa,F_approx,U_lst[chosen_index])
    return mass_arr,E_interface_arr,E_mix_arr,E_tot_arr

def yield_chosen_frames(Uts,Nt, frameArr):
    cycle_list=[False]*(Nt)
    for frame in frameArr:
        cycle_list[frame] =True
    from itertools import compress, cycle
    return compress(Uts, cycle(cycle_list))