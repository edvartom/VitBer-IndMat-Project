from funcs import *

kappa=0.01
u_str5='sin(x)*cos(y)*exp(-4*kappa*t)'

Lx, Ly = 16*np.pi, 16*np.pi
Nx, Ny = 64, 64
Nt_arr5=np.array([100,200,400,800,1600,3200])

x = np.linspace(0, Lx, Nx, endpoint=False)
y = np.linspace(0, Ly, Ny, endpoint=False)
X, Y = np.meshgrid(x, y, sparse=True)
t0, T = 0,1

u_ex5, g5=manufacture_solution_cahn_hillard_be(u_str5, kappa)
U0_5=u_ex5(X,Y,0)

alpha_2D=np.array([[1.5,-0.5,0,0,1],
                    [2,-1,0.5,0,0.5],
                    [2,-1,0,0.5,0.5],
                    [2.5,-1.5,2/3,0,1/3]])

beta_2D=np.array([[0.5,1],
                  [1,1],
                  [1,0.5],
                  [1.5,1]])

for i in range (len(alpha_2D)):
    index=0
    max_err_arr=np.zeros(len(Nt_arr5))

    for Nt in Nt_arr5:
        max_err=0
        solver = IMEX_song(kappa=kappa, X=X, Y=Y, U0=U0_5, 
                t0=t0, T=T, Nt=Nt, g=g5, alpha_arr=alpha_2D[i], beta_arr=beta_2D[i])
        for U5, t in solver:
            U_ex5=u_ex5(X,Y,t)  # Exact solution for whole grid at time t
            U_err_5=U5-U_ex5
            err_t=np.amax(abs(U_err_5)) # Max error at time t
            # Evaluate maximum error for entire period T for a specific Nt
            if err_t>max_err:
                max_err=err_t

        max_err_arr[index]=max_err
        index+=1

    # Compute EOC after going through all Nt for one theta-value
    EOC5=np.log(max_err_arr[:-1]/max_err_arr[1:])/np.log(Nt_arr5[1:]/Nt_arr5[:-1])
    EOC5 = np.insert(EOC5, 0, np.inf)

    print('\n EOC for task 5 with coefficients alpha= '+str(alpha_2D[i])+' and beta='+str(beta_2D[i]))
    print('\n')
    table5 = pd.DataFrame({'Nt': Nt_arr5, 'Error': max_err_arr, 'EOC': EOC5})
    print(table5) # Use 'display' when transferring to Jupyter!
    print('\n \n')