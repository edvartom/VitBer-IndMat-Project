The most significant difference between the results in task $4$ and $5$ are the EOC-values. The Euler-based IMEX solver in task $4$ has an order of convergence equal to the implicit and explicit Euler methods, e.g. $1$. On the other hand, the EOC in this task converges to $2$. This suggests that the Runge-Kutta-based IMEX solver have a convergence order of $2$.

Since the Runga-kutta based EOC is greater than the Euler based EOC, we conclude that the Song IMEX scheme is more efficient in solving the Cahn-Hilliard equation. That is, the Song IMEX scheme pays better (the error reduction is greater) to increasing $N_t$ compared to the Euler IMEX scheme.

From the EOC-values in this task we see that the first set of coefficients, i.e.

$$\begin{align}

\alpha_{10}=\frac{3}{2}, \qquad \alpha_{11}=-\frac{1}{2}, \qquad \alpha_{20}=0, \qquad \alpha_{21}=0, \qquad \alpha_{22}=1, \qquad  \beta_{1}=\frac{1}{2}, \qquad \beta_{2}=1

\end{align}$$

give the fastest convergimg IMEX solver, and will therefore be favored in the rest of the project. 