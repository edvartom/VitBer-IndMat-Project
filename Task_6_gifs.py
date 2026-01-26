from funcs import *
from scipy.integrate import dblquad
import matplotlib.animation as animation
import itertools
from IPython.display import HTML
from IPython.display import Image

kappa=0.0025**2 
Lx,Ly=0.5,0.5 
Nx,Ny=256,256
x_6, y_6 = np.linspace(0,Lx,Nx,endpoint=False), np.linspace(0,Ly,Ny,endpoint=False)
X_6, Y_6 = np.meshgrid(x_6,y_6,sparse=True)
t0=0 #Starting time
# Different time intervals
T1=4.0
#Tds for the different simulations
T73=0.01
T63=0.02
T77=0.015
T67=0.033

tau1=1e-3 #Time interval

# Different number of time steps
Nt1=int((T1-t0)/tau1)
Nt73=int((T73-t0)/tau1)
Nt63=int((T63-t0)/tau1)
Nt77=int((T77-t0)/tau1)
Nt67=int((T67-t0)/tau1)

# Values for alpha and beta for the solver from task 5 (Song)
alpha_arr=np.array([1.5,-0.5,0,0,1])
beta_arr=np.array([0.5,1])

# Creating different initial values for U (some noise)
rand_num_generator = np.random.default_rng(12345)
noise = 0.05
U0_61 = np.full((Nx, Ny), 0.0) + noise*rand_num_generator.standard_normal((Nx,Ny))
U0_62 = np.full((Nx, Ny), 0.0) + noise*rand_num_generator.standard_normal((Nx,Ny)) - 0.45

# IMEX Euler
Uts_63=cahn_hilliard_backward_euler(kappa=kappa, X=X_6, Y=Y_6, U0=U0_61, t0=t0, T=T63, Nt=Nt63,g=None)
Uts_67=cahn_hilliard_backward_euler(kappa=kappa, X=X_6, Y=Y_6, U0=U0_62, t0=t0, T=T67, Nt=Nt67,g=None)

#IMEX Song
Uts_73=IMEX_song(kappa=kappa,X=X_6,Y=Y_6,U0=U0_61,t0=t0,T=T73,Nt=Nt73,g=None,alpha_arr=alpha_arr,beta_arr=beta_arr)
Uts_77=IMEX_song(kappa=kappa,X=X_6,Y=Y_6,U0=U0_62,t0=t0,T=T77,Nt=Nt77,g=None,alpha_arr=alpha_arr,beta_arr=beta_arr)


# 1. Snapshots of U_73 (Song) and U_63 (BE) with U0_61 as initial condition

#Song
uts_list1=[]
frameArr=np.array([Nt73-1]) #Specify frames
for u,t in yield_chosen_frames(Uts_73,Nt73, frameArr):
        uts_list1.append((u,t))

ani1 = make_animation(uts_list1,Lx,Ly)

writer = animation.PillowWriter(fps=1,
                               metadata=dict(artist='Me'),
                               bitrate=200)
ani1.save('U_73_snapshot.gif',writer=writer)
#HTML(ani1.to_html5_video())
Image(filename='U_73_snapshot.gif')
HTML('<img src="U_73_snapshot.gif">')


#BE
uts_list2=[]
frameArr=np.array([Nt63-1]) #Specify frames
for u,t in yield_chosen_frames(Uts_63,Nt63, frameArr):
        uts_list2.append((u,t))

ani2 = make_animation(uts_list2,Lx,Ly)

writer = animation.PillowWriter(fps=1,
                               metadata=dict(artist='Me'),
                               bitrate=200)
ani2.save('U_63_snapshot.gif',writer=writer)

# 2. Snapshots of U_77 (Song) and U_67 (BE) with U0_62 as initial condition

#Song
uts_list3=[]
frameArr=np.array([Nt77-1]) #Specify frames
for u,t in yield_chosen_frames(Uts_77,Nt77, frameArr):
        uts_list3.append((u,t))

ani3 = make_animation(uts_list3,Lx,Ly)

writer = animation.PillowWriter(fps=1,
                               metadata=dict(artist='Me'),
                               bitrate=200)
ani3.save('U_77_snapshot.gif',writer=writer)

#BE
uts_list4=[]
frameArr=np.array([Nt67-1]) #Specify frames
for u,t in yield_chosen_frames(Uts_67,Nt67, frameArr):
        uts_list4.append((u,t))

ani4 = make_animation(uts_list4,Lx,Ly)

writer = animation.PillowWriter(fps=1,
                               metadata=dict(artist='Me'),
                               bitrate=200)
ani4.save('U_67_snapshot.gif',writer=writer)

# 3. Gif of U0_61 only Song in I=[0,4]
Uts_first=IMEX_song(kappa=kappa,X=X_6,Y=Y_6,U0=U0_61,t0=t0,T=T1,Nt=Nt1,g=None,alpha_arr=alpha_arr,beta_arr=beta_arr)

uts_list5=[]
frameArr=np.array([0,2,4,6,8, 10, 12, 100,500,1000,Nt1-1]) #Specify frames
for u,t in yield_chosen_frames(Uts_first,Nt1, frameArr):
        uts_list5.append((u,t))

ani5 = make_animation(uts_list5,Lx,Ly,interval=40000)

writer = animation.PillowWriter(fps=1,
                               metadata=dict(artist='Me'),
                               bitrate=200)
ani5.save('U_first.gif',writer=writer)

# 4. Gif of U0_62 only Song in I=[0,4]

Uts_second=IMEX_song(kappa=kappa,X=X_6,Y=Y_6,U0=U0_62,t0=t0,T=T1,Nt=Nt1,g=None,alpha_arr=alpha_arr,beta_arr=beta_arr)

uts_list6=[]
frameArr=np.array([0,4,6,8, 10, 12, 100,500,1000,Nt1-1]) #Specify frames
for u,t in yield_chosen_frames(Uts_second,Nt1, frameArr):
        uts_list6.append((u,t))

ani6 = make_animation(uts_list6,Lx,Ly,interval=40000)

writer = animation.PillowWriter(fps=1,
                               metadata=dict(artist='Me'),
                               bitrate=200)
ani6.save('U_second.gif',writer=writer)
