In this task we once again solve the Cahn-Hilliard equation but now with the Song scheme, a 3-stage IMEX Runge-Kutta scheme. The equation to be solved can be written as shown in the previous task:

$$\begin{align}

\partial_t{u}-\kappa \Delta^2 u -g = \Delta f(u) \\

\partial_t{u}=\kappa \Delta^2 u + \Delta f(u)+g,

\end{align}$$

where we still have that $f(u)=u^3+u$. As in the previous task, we use convex splitting on $f(u)$ so that

$$\begin{align}

\Delta f(u)=\Delta \alpha_{00} u+\Delta(u^3-(1+\alpha_{00})u), \qquad \alpha_{00}=1.5.

\end{align}$$

We now gather $\bold{L} u=(\kappa \Delta^2 + \Delta \alpha_{00}) u$ into a linear term and $\bold{N}(u)=\Delta(u^3-(1+\alpha_{00})u)$ into a non-linear term. We apply this to a Song-scheme which also takes an inhomogenous term $g$ into account, and calculate $u_{n+1}$ from $u_n$. The calculation is performed in the following steps:

1. Calculate $\bold{N}(u_n)$ in real space.

2. Fourier transform $u_n$ and $\bold{N}(u_n)$.


$$\begin{align}

\mathcal{F}[u_n]=\hat{u}_n, \qquad \mathcal{F}[\bold{N}]=\hat{\bold{N}}.

\end{align}$$

3. Calculate $g_{n+1/2}$ and Fourier transform it.

4. Fourier transform the first IMEX step and calculate $\hat{U}^{(1)}$


$$\begin{align}

\hat{U}^{(1)}=\frac{\hat{u}_n+\tau(\hat{\bold{N}}+\hat{g}_{n+1/2})}{1-\tau\kappa \tilde{k}_4 - \tau \tilde{k}_2 \alpha_{00}},

\end{align}$$

where $\tilde{k}_4$ and $\tilde{k}_2$ are defined the same as earlier.

5. Perform an inverse Fourier transform to find $U^{(1)}$ and use it to calculate $\bold{N}(U^{(1)})=\bold{N}_1$. 

6. Fourier transform $\bold{N}_1$

7. Fourier transform the second IMEX step and calculate $\hat{U}^{(2)}$

$$\begin{align}

\hat{U}^{(2)}=\frac{\alpha_{10}\hat{u}_n+\alpha_{11}\hat{U}^{(1)}+\tau\beta_1(\hat{\bold{N}}_1)+\hat{g}_{n+1/2}}{1-\tau \beta_1 \kappa\tilde{k}_4-\tau\beta_1 \alpha_{00} \tilde{k}_2}


\end{align}$$

8. Perform an inverse Fourier transform to find $U^{(2)}$ and use it to calculate $\bold{N}(U^{(2)})=\bold{N}_2$. 

9. Fourier transform $\bold{N}_2$

10. Fourier transform the final step of the IMEX method and calculate $\hat{u}_{n+1}$

$$\begin{align}

\hat{u}_{n+1}=\frac{\alpha_{20}\hat{u}_n+\alpha_{21}\hat{U}^{(1)}+\alpha_{22}\hat{U}^{(2)}+\tau \beta_2(\hat{N}_2+\hat{g}_{n+1/2})}{1-\tau \beta_2 \kappa \tilde{k}_4 - \tau \beta_2 \alpha_{00} \tilde{k}_2}


\end{align}$$

11. Perform an inverse Fourier transform to find $u_{n+1}$ and update the time $t_{n+1}=t_n+\tau$. Yield these quantities.

Repeat until $t_n=T$.