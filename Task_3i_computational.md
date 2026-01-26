In this task we will solve the transient biharmonic equation using the $\theta$-method and Fourier transform. The transient biharmonic equation being solved is given by  

$$\begin{align}
    \partial_t u(x,y,t) + \kappa \Delta^2 u(x,y,t)  = 
    g (x,y,t) \qquad u_0=u(x,y,0), \qquad \kappa\geq 0.
\end{align}$$

Here, $g$ is a source term and $u$ is our manufractured solution that we define.

<br>

We define the time intervals, $dt$ as 

$$
dt = \frac{T-t_0}{N_t},
$$

where $t_0$ and $T$ are the initial and final time, respectively. Hence, $T-t_0$ is the total time, and $N_t$ is the number of timesteps. 

To calculate $u_{n+1}$, for these time steps, we use the $\theta$-method given by 

$$\begin{align}
U^{n+1} = U^{n} + \tau 
\left[ 
    \theta F(t_{n+1}, U^{n+1}) + (1 - \theta) F(t_n, U^n)
\right].
\end{align}$$

<br>


Solving eq. $(1)$ directly is difficult. To simplfiy computations, we use the Fourier transform on eq. $(1)$, conveniently rewritten as 

$$\begin{align}
\partial_t u =g - \kappa \Delta^2 u.
\end{align}$$

We define 
$$
\mathcal{F}[ u(x, y, t_n )](k_x, k_y) 
= \hat{u}(k_x, k_y)_n
= \hat u_n
$$ 

and 

$$
\mathcal{F}[g(x, y, t_n)](k_x, k_y) 
= \hat{g}(k_x, k_y)_n 
= \hat g_n
\text{.}
$$ 

Then, we transform both sides of eq. $(3)$ to obtain

$$\begin{align}
\partial_t \hat{u}_n =\hat{g}_n - 
\kappa \tilde{k}_4 \hat{u}_n=F(t_n,\hat{u}_n), 
\qquad \hat{u}_0=\hat{u}(k_x,k_y,0),
\end{align}$$

where 
$$\begin{align}
\tilde{k}_4 = 
\left(
    -\frac{k_x^2}{L_x^2} -\frac{k_y^2}{L_y^2}
\right)^2.
\end{align}$$

The expression $\tilde{k}_4$ comes from the Fourier transform of the biharmonic operator $\Delta^2 = \nabla^4$. 

<br>


Substituting eq. $(4)$ into eq. $(2)$, and solving for $\hat u_{n+1}$, result is

$$\begin{align}
\hat{u}_{n + 1} = 
\left(
     1-\frac{\tau \kappa \tilde{k_4}}{1 + \theta\tau\kappa\tilde{k_4}}
\right)
\hat{u}_n + \frac{\tau}{1 + \theta \tau \kappa \tilde{k_4}} 
\left[ 
    \theta\hat{g}_{n+1} + (1-\theta)\hat{g}_n 
\right].
\end{align}$$

This equation is solved numerically by iterating for each time step, $t_{n+1}=t_n+\tau$, to compute $\hat u_{n+1}$ form $\hat u$. Thereafter, we use inverse Fourier transform to obtain the real space solution $u$. 

<br>

### Stability Analysis

If $g = 0, \ \forall t$, then eq. $(5)$ can be simplified as

$$\begin{align}
\hat{u}_{n+1}=R_{\theta}(z)^{n+1}\hat{u}_0,
\end{align}$$

where $R_{\theta}(z)$ is the stability function for the $\theta$ method given by

$$\begin{align}
R_{\theta}(z)=1+\frac{z}{1-\theta z}, \qquad z=-\tau \kappa \tilde{k}_4.
\end{align}$$

If $|R_\theta (z)| \le 1$, the solution will remain stable over time. 