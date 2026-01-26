The EOC-values for $\theta=1$ and $\theta=0.5$ are consistent with what is written in task 3.1 theoretical. 
In that task we concluded that with $\theta=1$, the method reduced to the implicit or backward Euler method, which has an order of convergence of $1$. Indeed, we can see from the table for $\theta=1$ that the EOC does seem to converge to $1$ for increasing $N_t$. 

Similarly, we concluded in task 3.1 theoretical that the $\theta$ method reduces to the Crank-Nicolson method for $\theta=0.5$. The EOC-values for $\theta=0.5$ given in a table of increasing $N_t$ seems to converge to $2$, which is exactly the order of convergence of the Crank-Nicolson method.

Following this logic, one would expect the EOC to converge to $1$ for $\theta=0$ as this is the order of convergence for the explicit or forward Euler method. Instead, the error only grows larger and the EOC does not converge at all. The explanation for that is simply that the timesteps $\tau$ are too large, or in other words, $N_t$ is too small. The stability function of the forward Euler method is in this case

$$\begin{equation}

R(z)=1+z=1+\tau \lambda = 1-\tau \kappa \tilde{k}_4,

\end{equation}$$

which only converges if 

$$\begin{equation}

\lvert R(z) \rvert < 1 \Leftrightarrow \tau <\frac{2}{\lvert \kappa \tilde{k}_4 \rvert} \Leftrightarrow N_t > \frac{\lvert \kappa \tilde{k}_4 \rvert \cdot (T-t_0)}{2}=N_{CFL}.

\end{equation}$$

In essence, we need larger $N_t$ to find the EOC for $\theta=0$. In this case $N_{CFL}=20000$ and for $N_t$ above this value, the EOC does seem to converge to $1$.