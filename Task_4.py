from funcs import *

kappa_arr=np.array([1,0.01])
u_str4='sin(x)*cos(y)*exp(-4*kappa*t)'

Lx, Ly = 16*np.pi, 16*np.pi
Nx, Ny = 64, 64
Nt_arr4=np.array([100,200,400,800,1600,3200])

x = np.linspace(-Lx/2, Lx/2, Nx, endpoint=False)
y = np.linspace(-Ly/2, Ly/2, Ny, endpoint=False)
X, Y = np.meshgrid(x, y, sparse=True)
t0, T = 0,1

for kappa in kappa_arr:  
    index=0
    u_ex4, g4=manufacture_solution_cahn_hillard_be(u_str4, kappa)
    U0_4=u_ex4(X,Y,0)

    # Error array setup
    max_err_arr=np.zeros(len(Nt_arr4))

    for Nt in Nt_arr4:
        max_err=0
        solver = cahn_hilliard_backward_euler( 
                                kappa=kappa, 
                                X=X, Y=Y, U0=U0_4, 
                                t0=t0, T=T, Nt=Nt,
                                g=g4)

        for U4, t in solver:
            U_ex4=u_ex4(X,Y,t)  # Exact solution for whole grid at time t
            U_err_4=U4-U_ex4
            err_t=np.amax(abs(U_err_4)) # Max error at time t
            # Evaluate maximum error for entire period T for a specific Nt
            if err_t>max_err:
                max_err=err_t

        max_err_arr[index]=max_err
        index+=1

    # Compute EOC after going through all Nt for one theta-value
    EOC4=np.log(max_err_arr[:-1]/max_err_arr[1:])/np.log(Nt_arr4[1:]/Nt_arr4[:-1])
    EOC4 = np.insert(EOC4, 0, np.inf)

    print('\n EOC for task 4 kappa = '+str(kappa))
    print('\n')
    table32 = pd.DataFrame({'Nt': Nt_arr4, 'Error': max_err_arr, 'EOC': EOC4})
    print(table32) # Use 'display' when transferring to Jupyter!
    print('\n \n')