from funcs import *

kappa=0.0025**2 
Lx,Ly=0.5,0.5 #These are the right lengths!
Nx,Ny=256,256
x_6, y_6 = np.linspace(0,Lx,Nx,endpoint=False), np.linspace(0,Ly,Ny,endpoint=False)
X_6, Y_6 = np.meshgrid(x_6,y_6,sparse=True)
t0=0
# Different time intervals
T1=4.0
T2=0.01
Tsd=0.06
# Different time steps
tau1=1e-3
tau2=1e-4
# Different number of time steps
Nt1=int((T1-t0)/tau1)
Nt2=int((T1-t0)/tau2)
Nt3=int((T2-t0)/tau1)
Nt4=int((T2-t0)/tau2)
# Values for alpha and beta for the solver from task 5
alpha_arr=np.array([1.5,-0.5,0,0,1])
beta_arr=np.array([0.5,1])

# Creating different initial values for U (some noise)
rand_num_generator = np.random.default_rng(12345)
noise = 0.05
# u0_base = 0.0
# u0 = np.ones_like((Nx, Ny))       ... do not know why these are integrated in the example code
U0_61 = np.full((Nx, Ny), 0.0) + noise*rand_num_generator.standard_normal((Nx,Ny))
U0_62 = np.full((Nx, Ny), 0.0) + noise*rand_num_generator.standard_normal((Nx,Ny)) - 0.45

Uts_61=cahn_hilliard_backward_euler(kappa=kappa, X=X_6, Y=Y_6, U0=U0_61, t0=t0, T=T1, Nt=Nt1,g=None)
Uts_62=cahn_hilliard_backward_euler(kappa=kappa, X=X_6, Y=Y_6, U0=U0_61, t0=t0, T=T1, Nt=Nt2,g=None)
Uts_63=cahn_hilliard_backward_euler(kappa=kappa, X=X_6, Y=Y_6, U0=U0_61, t0=t0, T=T2, Nt=Nt3,g=None)
Uts_64=cahn_hilliard_backward_euler(kappa=kappa, X=X_6, Y=Y_6, U0=U0_61, t0=t0, T=T2, Nt=Nt4,g=None)
Uts_65=cahn_hilliard_backward_euler(kappa=kappa, X=X_6, Y=Y_6, U0=U0_62, t0=t0, T=T1, Nt=Nt1,g=None)
Uts_66=cahn_hilliard_backward_euler(kappa=kappa, X=X_6, Y=Y_6, U0=U0_62, t0=t0, T=T1, Nt=Nt2,g=None)
Uts_67=cahn_hilliard_backward_euler(kappa=kappa, X=X_6, Y=Y_6, U0=U0_62, t0=t0, T=T2, Nt=Nt3,g=None)
Uts_68=cahn_hilliard_backward_euler(kappa=kappa, X=X_6, Y=Y_6, U0=U0_62, t0=t0, T=T2, Nt=Nt4,g=None)
all_Uts_solver4=(Uts_61,Uts_62,Uts_63,Uts_64,Uts_65,Uts_66,Uts_67,Uts_68)



# ... and with solver from task 5
Uts_71=IMEX_song(kappa=kappa,X=X_6,Y=Y_6,U0=U0_61,t0=t0,T=T1,Nt=Nt1,g=None,alpha_arr=alpha_arr,beta_arr=beta_arr)
Uts_72=IMEX_song(kappa=kappa,X=X_6,Y=Y_6,U0=U0_61,t0=t0,T=T1,Nt=Nt2,g=None,alpha_arr=alpha_arr,beta_arr=beta_arr)
Uts_73=IMEX_song(kappa=kappa,X=X_6,Y=Y_6,U0=U0_61,t0=t0,T=Tsd,Nt=Nt3,g=None,alpha_arr=alpha_arr,beta_arr=beta_arr)
Uts_74=IMEX_song(kappa=kappa,X=X_6,Y=Y_6,U0=U0_61,t0=t0,T=T2,Nt=Nt4,g=None,alpha_arr=alpha_arr,beta_arr=beta_arr)
Uts_75=IMEX_song(kappa=kappa,X=X_6,Y=Y_6,U0=U0_62,t0=t0,T=T1,Nt=Nt1,g=None,alpha_arr=alpha_arr,beta_arr=beta_arr)
Uts_76=IMEX_song(kappa=kappa,X=X_6,Y=Y_6,U0=U0_62,t0=t0,T=T1,Nt=Nt2,g=None,alpha_arr=alpha_arr,beta_arr=beta_arr)
Uts_77=IMEX_song(kappa=kappa,X=X_6,Y=Y_6,U0=U0_62,t0=t0,T=T2,Nt=Nt3,g=None,alpha_arr=alpha_arr,beta_arr=beta_arr)
Uts_78=IMEX_song(kappa=kappa,X=X_6,Y=Y_6,U0=U0_62,t0=t0,T=T2,Nt=Nt4,g=None,alpha_arr=alpha_arr,beta_arr=beta_arr)
all_Uts_solver5=(Uts_71,Uts_72,Uts_73,Uts_74,Uts_75,Uts_76,Uts_77,Uts_78)

# Plotting mass and energies for sover 4:
fig_integrals4, ax_integrals4 = plt.subplots(2,2)
fig_integrals4.suptitle('Solver 4')
ax_integrals4[0][0].set_title('Total mass')
ax_integrals4[0][0].set_xlabel('Relative time interval')
ax_integrals4[0][0].set_ylabel('Mass')
ax_integrals4[0][0].grid()
ax_integrals4[0][1].set_title('Interface energy')
ax_integrals4[0][1].set_xlabel('Relative time interval')
ax_integrals4[0][1].set_ylabel('Energy')
ax_integrals4[0][1].grid()
ax_integrals4[1][0].set_title('Mixing energy')
ax_integrals4[1][0].set_xlabel('Relative time interval')
ax_integrals4[1][0].set_ylabel('Energy')
ax_integrals4[1][0].grid()
ax_integrals4[1][1].set_title('Total energy')
ax_integrals4[1][1].set_xlabel('Relative time interval')
ax_integrals4[1][1].set_ylabel('Energy')
ax_integrals4[1][1].grid()
for i in range(len(all_Uts_solver4)):
    print(i)
    if i!=1 and i!=5: #I do not have time for plotting for Nt2=40,000
        masses, int_eng, mix_eng, tot_eng = calculate_integrals_for_task_6(all_Uts_solver4[i],kappa,F_approx)
        N_samples = len(masses)
        t = np.linspace(0,1,N_samples)
        ax_integrals4[0][0].plot(t, masses, label=i+1)
        ax_integrals4[0][1].plot(t, int_eng)
        ax_integrals4[1][0].plot(t, mix_eng)
        ax_integrals4[1][1].plot(t, tot_eng)
    else:
        print('i is 1 or 5')
ax_integrals4[0][0].legend()
# Adding some space between the plots
plt.subplots_adjust(hspace=0.5)


# Plotting mass and energies for sover 5:
fig_integrals5, ax_integrals5 = plt.subplots(2,2)
fig_integrals5.suptitle('Solver 5')
ax_integrals5[0][0].set_title('Total mass')
ax_integrals5[0][0].set_xlabel('Relative time interval')
ax_integrals5[0][0].set_ylabel('Mass')
ax_integrals5[0][0].grid()
ax_integrals5[0][1].set_title('Interface energy')
ax_integrals5[0][1].set_xlabel('Relative time interval')
ax_integrals5[0][1].set_ylabel('Energy')
ax_integrals5[0][1].grid()
ax_integrals5[1][0].set_title('Mixing energy')
ax_integrals5[1][0].set_xlabel('Relative time interval')
ax_integrals5[1][0].set_ylabel('Energy')
ax_integrals5[1][0].grid()
ax_integrals5[1][1].set_title('Total energy')
ax_integrals5[1][1].set_xlabel('Relative time interval')
ax_integrals5[1][1].set_ylabel('Energy')
ax_integrals5[1][1].grid()
for i in range(len(all_Uts_solver5)):
    print(i)
    if i!=1 and i!=5: #I do not have time for plotting for Nt2=40,000
        masses, int_eng, mix_eng, tot_eng = calculate_integrals_for_task_6(all_Uts_solver5[i],kappa,F_approx)
        N_samples = len(masses)
        t = np.linspace(0,1,N_samples) # I do not know why some of the plots does not go all the way to 1 ...
        ax_integrals5[0][0].plot(t, masses, label=i+1)
        ax_integrals5[0][1].plot(t, int_eng)
        ax_integrals5[1][0].plot(t, mix_eng)
        ax_integrals5[1][1].plot(t, tot_eng)
    else:
        print('i is 1 or 5')
ax_integrals5[0][0].legend()
# Adding some space between the plots
plt.subplots_adjust(hspace=0.5)

plt.show()
