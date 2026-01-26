from funcs import *

# Gridlengths
Lx=2*np.pi
Ly=4*np.pi

# Manufacture u and f for the two cases
u_str_1='sin(8*(x-1))*cos(4*y)'
u_exact_1,f_1=manufacture_solution_biharmonic(u_str_1,1)
u_str_2='exp(sin(x)**2+cos(2*y))'
u_exact_2,f_2=manufacture_solution_biharmonic(u_str_2,0)

# Nx values for the two cases. Ny=2*Nx is defined later
Nx_1=np.array([4,8,15,16,20,32])
Nx_2=np.array([4+4*k for k in range (10)])

# Solution 1:
errs_1=np.zeros(len(Nx_1))  # Errors
ind=0 # Index
comp=0 # Computation no.
fig_1 = plt.figure(figsize=(15, 10))

for Nx in Nx_1:

    # Make grid
    x_1 = np.linspace(0, Lx, Nx, endpoint=False)
    y_1 = np.linspace(0, Ly, Nx*2, endpoint=False)
    X_1, Y_1 = np.meshgrid(x_1, y_1, sparse=True)

    #Solve equation
    F_1=f_1(X_1,Y_1)
    U_exact_1=u_exact_1(X_1,Y_1)
    U_1=biharmonic_solver(X_1, Y_1, F_1, 1)

    # Find and record difference between exact and numerical solution
    U_err_1 = U_1 - U_exact_1
    errs_1[comp]=np.linalg.norm(U_err_1,np.inf)
    comp+=1

    # Plot for Nx=15 and Nx=16
    if Nx==15 or Nx==16:
        ind+=1
        ax = fig_1.add_subplot(230+ind, projection='3d')
        surf = ax.plot_surface(X_1, Y_1, U_exact_1, cmap='viridis', antialiased=True)
        fig_1.colorbar(surf, shrink=0.6,pad=0.2)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel(r'$U_\mathrm{ex}$')

        ind+=1
        ax = fig_1.add_subplot(230+ind, projection='3d')
        surf = ax.plot_surface(X_1, Y_1,  U_1, cmap='viridis')
        fig_1.colorbar(surf, shrink=0.6,pad=0.2)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel(r'$U(X, Y)$')

        ind+=1
        ax = fig_1.add_subplot(230+ind, projection='3d')
        surf = ax.plot_surface(X_1, Y_1,  U_err_1, cmap='viridis')
        fig_1.colorbar(surf, shrink=0.6,pad=0.2)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel(r'$U-U_{\mathrm{ex}}$')

# Solution 2 (same procedure as above):
comp=0
errs_2=np.zeros(len(Nx_2))
fig_2 = plt.figure(figsize=(15, 10))

for Nx in Nx_2:

    x_2 = np.linspace(0, Lx, Nx, endpoint=False)
    y_2 = np.linspace(0, Ly, Nx*2, endpoint=False)
    X_2, Y_2 = np.meshgrid(x_2, y_2, sparse=True)

    F_2=f_2(X_2,Y_2)
    U_exact_2=u_exact_2(X_2,Y_2)
    U_2=biharmonic_solver(X_2, Y_2, F_2,0,mean=np.mean(U_exact_2))

    U_err_2 = U_2 - U_exact_2
    errs_2[comp]=np.linalg.norm(U_err_2,np.inf)
    comp+=1

    # Plot for Nx=32
    if Nx==32:
        ax = fig_2.add_subplot(131, projection='3d')
        surf = ax.plot_surface(X_2, Y_2, U_exact_2, cmap='viridis', antialiased=True)
        fig_2.colorbar(surf, shrink=0.6,pad=0.2)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel(r'$U_\mathrm{ex}$')

        ax = fig_2.add_subplot(132, projection='3d')
        surf = ax.plot_surface(X_2, Y_2,  U_2, cmap='viridis')
        fig_2.colorbar(surf, shrink=0.6,pad=0.2)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel(r'$U(X, Y)$')

        ind+=1
        ax = fig_2.add_subplot(133, projection='3d')
        surf = ax.plot_surface(X_2, Y_2,  U_err_2, cmap='viridis')
        fig_2.colorbar(surf, shrink=0.6,pad=0.2)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel(r'$U-U_{\mathrm{ex}}$')

# Find EOC for both cases and put them in a table
eocs_1=np.log(errs_1[:-1]/errs_1[1:])/np.log(Nx_1[1:]/Nx_1[:-1])
eocs_1 = np.insert(eocs_1, 0, np.inf)
eocs_2=np.log(errs_2[:-1]/errs_2[1:])/np.log(Nx_2[1:]/Nx_2[:-1])
eocs_2 = np.insert(eocs_2, 0, np.inf)

print('\n EOC for test 1 \n')
table_1 = pd.DataFrame({'Nx': Nx_1, 'Error': errs_1, 'EOC': eocs_1})
print(table_1) # Use 'display' when transferring to Jupyter!
print('\n \n')

print('\n EOC for test 2 \n')
table_2 = pd.DataFrame({'Nx': Nx_2, 'Error': errs_2, 'EOC': eocs_2})
print(table_2)

# Stylistic plot details
fig_1.suptitle('Biharmonic equation with solution $u=sin(8(x-1))cos(4y)$ \n',fontsize=15)
fig_1.text(0.02, 0.7, '$N_x=15$', fontsize=12, transform=plt.gcf().transFigure)
fig_1.text(0.02, 0.3, '$N_x=16$', fontsize=12, transform=plt.gcf().transFigure)
fig_1.text(0.20, 0.9, 'Exact', fontsize=12, transform=plt.gcf().transFigure)
fig_1.text(0.45, 0.9, 'Numerical solution', fontsize=12, transform=plt.gcf().transFigure)
fig_1.text(0.75, 0.9, 'Error', fontsize=12, transform=plt.gcf().transFigure)

fig_2.suptitle('Biharmonic equation with solution $u=exp(sin(x)^2+cos(2y))$ \n',fontsize=15)
fig_2.text(0.02, 0.5, '$N_x=32$', fontsize=12, transform=plt.gcf().transFigure)
fig_2.text(0.20, 0.8, 'Exact', fontsize=12, transform=plt.gcf().transFigure)
fig_2.text(0.45, 0.8, 'Numerical solution', fontsize=12, transform=plt.gcf().transFigure)
fig_2.text(0.75, 0.8, 'Error', fontsize=12, transform=plt.gcf().transFigure)

plt.subplots_adjust(wspace=0.2)
plt.tight_layout
plt.show()