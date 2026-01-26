from funcs import *

# Define exact solution
kappa=1
u_str_32='sin(x)*cos(y)*exp(-4*kappa*t)'
u_ex32, g_32=manufacture_solution_td_biharmonic(u_str_32, kappa)

# Grid and time data
Lx, Ly = 2*np.pi, 2*np.pi
Nx, Ny = 20,20
t0 , T = 0, 1
Nt_arr=np.array([10,20,40,80,160,320,640])
theta_arr=np.array([1,0.5,0])
x = np.linspace(-Lx/2, Lx/2, Nx, endpoint=False)
y = np.linspace(-Ly/2, Ly/2, Ny, endpoint=False)
X, Y = np.meshgrid(x, y, sparse=True)

U0_32 = u_ex32(X,Y,0) # Start value

for theta in theta_arr:  
    index=0

    # Error array setup
    max_err_arr=np.zeros(len(Nt_arr))

    for Nt in Nt_arr:
        max_err=0
        solver = transient_biharmonic_solver(kappa=kappa, 
                                        X=X, Y=Y, U0=U0_32, 
                                        t0=t0, T=T, Nt=Nt, 
                                        theta=theta,
                                        g=None)

        for U_hat, t in solver:
            U32=ifft2(U_hat).real # Inverse Fourier transform
            U_ex32=u_ex32(X,Y,t)  # Exact solution for whole grid at time t
            U_err_32=U32-U_ex32
            err_t=np.amax(abs(U_err_32)) # Max error at time t
            # Evaluate maximum error for entire period T for a specific Nt
            if err_t>max_err:
                max_err=err_t

        max_err_arr[index]=max_err
        index+=1

    # Compute EOC after going through all Nt for one theta-value
    EOC32=np.log(max_err_arr[:-1]/max_err_arr[1:])/np.log(Nt_arr[1:]/Nt_arr[:-1])
    EOC32 = np.insert(EOC32, 0, np.inf)

    print('\n EOC for task 3.2 theta = '+str(theta))
    print('\n')
    table32 = pd.DataFrame({'Nt': Nt_arr, 'Error': max_err_arr, 'EOC': EOC32})
    print(table32) # Use 'display' when transferring to Jupyter!
    print('\n \n')


# CFL condition for theta=0
dx, dy = x[1] - x[0], y[1] - y[0]
kx = fftfreq(Nx, d=dx)*2*np.pi
ky = fftfreq(Ny, d=dy)*2*np.pi
KX, KY = np.meshgrid(kx, ky, sparse=True)
# CFL condition is dt<-2/lam
# lam=-kappa*K4, the largest K4 gives the largest Nt
K4=np.amax(KX**4+KY**4+2*KX**2*KY**2) 
CFL=int(kappa*K4*(T-t0)/2) # N_CFL
Nt_CFL_arr=np.array([0.5*CFL,CFL,2*CFL,4*CFL])

index=0
max_err_arr=np.zeros(len(Nt_CFL_arr))

# Repeat computation, but with different Nt array and only for theta=0
for Nt in Nt_CFL_arr:
    max_err=0
    solver=transient_biharmonic_solver(kappa=kappa, 
                                    X=X, Y=Y, U0=U0_32, 
                                   t0=t0, T=T, Nt=Nt, 
                                   theta=0,
                                   g=None)
    for U_hat, t in solver:
        U32=ifft2(U_hat).real
        U_ex32=u_ex32(X,Y,t)
        U_err_32=U32-U_ex32
        err_t=np.amax(abs(U_err_32)) # Max error at time t

        # Evaluate maximum error for entire period T for a specific Nt
        if err_t>max_err:
            max_err=err_t

    max_err_arr[index]=max_err
    index+=1

# Calculate EOC
EOC32=np.log(max_err_arr[:-1]/max_err_arr[1:])/np.log(Nt_CFL_arr[1:]/Nt_CFL_arr[:-1])
EOC32 = np.insert(EOC32, 0, np.inf)

print('\n EOC for theta=0 with N_CFL \n')
table32 = pd.DataFrame({'Nt': Nt_CFL_arr, 'Error': max_err_arr, 'EOC': EOC32})
print(table32) # Use 'display' when transferring to Jupyter!
print('\n \n')