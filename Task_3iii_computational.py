from funcs import *

kappa=1
u_str_33='(exp(1+sin(x)**2)+exp(1+cos(y)**2))*exp(-4*kappa*t)'
theta_arr33=np.array([1,0.5])
u_ex33, g_33=manufacture_solution_td_biharmonic(u_str_33, kappa)

# Grid and time data
Lx, Ly = 2*np.pi, 2*np.pi
Nx, Ny = 20,20
t0 , T = 0, 1
Nt_arr=np.array([10,20,40,80,160,320,640])
x = np.linspace(-Lx/2, Lx/2, Nx, endpoint=False)
y = np.linspace(-Ly/2, Ly/2, Ny, endpoint=False)
X, Y = np.meshgrid(x, y, sparse=True)

U0 = u_ex33(X,Y,0)

for theta in theta_arr33:  
    index=0
    max_err_arr=np.zeros(len(Nt_arr))
    for Nt in Nt_arr:
        max_err=0
        solver = transient_biharmonic_solver(kappa=kappa, 
                                        X=X, Y=Y, U0=U0, 
                                        t0=t0, T=T, Nt=Nt, 
                                        theta=theta,
                                        g=g_33)

        for U_hat, t in solver:
            U33=ifft2(U_hat).real
            U_ex33=u_ex33(X,Y,t)
            U_err_33=U33-U_ex33
            err_t=np.amax(abs(U_err_33)) # Max error at time t

            if err_t>max_err:
                max_err=err_t
        max_err_arr[index]=max_err
        index+=1

    EOC33=np.log(max_err_arr[:-1]/max_err_arr[1:])/np.log(Nt_arr[1:]/Nt_arr[:-1])
    EOC33 = np.insert(EOC33, 0, np.inf)
    print('\n EOC for task 3.3 theta = '+str(theta))
    print('\n')
    table33 = pd.DataFrame({'Nt': Nt_arr, 'Error': max_err_arr,'EOC': EOC33})
    print(table33) # Use 'display' when transferring to Jupyter!
    print('\n \n')