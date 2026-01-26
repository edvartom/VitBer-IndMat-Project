In this task we solve the biharmonic equation with a $0$-th order term $f$:

$$\begin{align}

\Delta^2 u(x,y)+cu(x,y)=f(x,y) \qquad \text{in } \Omega=[0,L_x) \times [0, L_y),

\end{align}$$

where $c\geq 0$. One can compute the solution $u$ by using fast Fourier transform on the entire equation so that

$$\begin{align}

\mathcal{F}[u(x,y)](k_x,k_y)=\hat{u}(k_x,k_y) \\
\mathcal{F}[f(x,y)](k_x,k_y)=\hat{f}(k_x,k_y).

\end{align}$$

Since we know that $u$ is periodic, we can calculate $\mathcal{F}[\Delta^2 u]$ as follows:

$$\begin{align}

\mathcal{F}[\Delta^2 u]= \mathcal{F}[{\partial_x}^4 u]+\mathcal{F}[{\partial_y}^4 u]+2\mathcal{F}[{\partial_x}^2{\partial_y}^2 u] \nonumber \\
= \left( \frac{-i2\pi k_x}{L_x} \right)^4 \hat{u}+\left( \frac{-i2\pi k_y}{L_y} \right)^4 \hat{u}+ 2\left( \frac{-i2\pi k_x}{L_x} \right)^2 \left( \frac{-i2\pi k_y}{L_y} \right)^2 \hat{u} \nonumber \\
=\left[\left( \frac{2\pi k_x}{L_x} \right)^4+\left( \frac{2\pi k_y}{L_y} \right)^4 +2\left( \frac{2\pi k_x}{L_x} \right)^2 \left( \frac{2\pi k_x}{L_x} \right)^2 \right] \hat{u} \nonumber \\
=(\tilde{k}_x^4+\tilde{k}_y^4+2\tilde{k}_x^2 \tilde{k}_y^2) \hat{u} \nonumber \\
=\tilde{k}_4 \hat{u},

\end{align}$$

where $\tilde{k}_x=\frac{2\pi k_x}{L_x}$, $\tilde{k}_y=\frac{2\pi k_y}{L_y}$, and $\tilde{k}_4=\tilde{k}_x^4+\tilde{k}_y^4+2\tilde{k}_x^2 \tilde{k}_y^2$. This notation will be used in the rest of the project. Hence, the Fourier transform of eq. $(1)$ can be written as

$$\begin{align}

\hat{u}=\frac{\hat{f}}{\tilde{k}_4+c},

\end{align}$$

which can be inversely transformed to find $u$. However, we need to consider the case where $c=0$. To avoid division by zero, we set $\tilde{k}_4=1$ when $k_x=k_y=0$. Furthermore, since $\hat{u}(0,0)=\mu{u}$, i.e. the mean value of $u$, we set $\hat{u}(0,0)$ to a predetermined mean value multiplied by the number of spatial timesteps $N_x \cdot N_y$. The last part is due to division by $N_x \cdot N_y$ in the inverse FFT.
