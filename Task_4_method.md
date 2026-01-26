## (i)

In this task, we will breif through how we can use an IMEX solver to solve the Cahn-Hilliard equation, which takes the general form 

$$\begin{align}
    \partial_t{ u(x,y,t) } -\nabla \cdot [
        M \nabla (f(u(x,y,t))-\kappa \Delta u(x,y,t))]
        = g(x,y,t) 
    \tag{1}
\end{align}$$

on the domain $\Omega \times (0,T)$. Here, $g$ is a source term, and $f(u)$ is a non-linear function defined to be

$$\begin{align}
    f(u)=u^3-u.
    \tag{2}
\end{align}$$

Additionally, $\kappa \geq 0$ and we set $M=1$. Eq. $(1)$ is solved using an IMEX time-stepping scheme based on the Euler-method with convex splitting, where the linear terms are treated implicitly on the left-hand side, while the non-linear terms are treated explicitly on the right-hand side. Before we can implement this scheme, however, we need to simplify eq. $(1)$:

$$\begin{align}

\partial_t{u}-\nabla \cdot [\nabla (f(u)-\kappa \Delta u)]=g \nonumber \\
\partial_t{u}-\Delta f(u)-\kappa \Delta^2 u=g \nonumber \\
\partial_t{u}-\kappa \Delta^2 u -g = \Delta f(u),
\tag{3}

\end{align}$$

where we have assumed that we may treat $g$ as a linear function. Eq. $(3)$ is now written in the form required by the IMEX solver. The IMEX-solver applied to this equation is given by

$$\begin{align}
u_{n+1}+\tau \kappa \Delta ^2 u_{n+1}-g_{n+1}=u_n+\tau \Delta f(u_n), \qquad u(x,y,t_n)=u_n,
\tag{4}
\end{align}$$

where $\tau=t_{n+1}-t_n$ is the length of the timestep. Since $f(u)$ consists of one linear and one non-linear term, it would be fitting to transfer the linear term over to the left-hand side. However, moving the entire linear term could cause issues later on, which is why we rather split it (convex splitting), and only move part of it to the left-hand side. Substituting 

$$\begin{aligned}
\Delta f(u)= \Delta (\alpha u - (1+\alpha) u + u^3) \\
f_1(u)=\alpha u \\
f_2(u)=u^3-(1+\alpha)u
\tag{5}
\end{aligned}$$

into eq. $(4)$ we get

$$\begin{align}
u_{n+1}+\tau \kappa \Delta ^2 u_{n+1}-g_{n+1}-\tau \alpha u_n=u_n-\tau \Delta ((1+\alpha) u_n - u_n^3).
\tag{6}
\end{align}$$

Then, we clean up so that all $u_{n+1}$ -terms end up un the left-hand side:

$$\begin{align}
\left ( \frac{1}{\tau} + \kappa \Delta^2 -\alpha \Delta \right)u_{n+1}=\frac{u_n}{\tau}+ \Delta f_2(u_n) + g_{n+1}.
\tag{7}
\end{align}$$

The easiest way to numerically deal with the $\Delta$ and $\Delta^2$ operators is, as we have seen, by using the Fourier transform on the entire equation. However, because of the non-linear term $u^3$ in $f_2(u)$, it can be computationally costly in this case. Therefore, $f_2(u)$ is first computed in real space before eq. $(7)$ undergoes Fourier transform and $\hat{u}(k_x, k_y)_{n+1}=\mathcal{F}[u(x,y)_{n+1}](k_x,k_y)$ is calculated. To find $\hat{u}_{n+2}$, $\hat{u}_{n+1}$ must undergo an inverse Fourier transform so that $f_2(u_{n+1})$ can be calculated in real space. These steps sum up our numerical method for this task:

1. Compute $f_2(u_n)$
$$\begin{align*}
f_2(u_n)=u_n^3-(1+\alpha)u_n.
\end{align*}$$

2. Fourier transform eq. $(7)$ and compute $\hat{u}_{n+1}$

$$\begin{align*}
\hat{u}_{n+1}=\frac{\hat{u}_n/ \tau+ \tilde{k}_2 \hat{f_2}(u_n) + \hat{g}_{n+1}}{1/ \tau + \kappa \tilde{k}_4 -\alpha \tilde{k}_2},
\end{align*}$$

where 

$$\begin{align*}
\tilde{k}_2 = -\frac{4\pi^2k_x^2}{L_x^2} - \frac{4\pi^2k_y^2}{L_y^2}, \qquad \tilde{k}_4={\tilde{k}_2}^2.
\end{align*}$$

3. Find $u_{n+1}$ by inverse transform

$$\begin{align*}
u_{n+1}(x,y)=\mathcal{F}^{-1}[\hat{u}(k_x,k_y)_{n+1}](x,y).

\end{align*}$$

4. Update time and yield result

$$\begin{align*}
t_{n+1}=t_n+\tau.

\end{align*}$$

Repeat until $t_n=T$.