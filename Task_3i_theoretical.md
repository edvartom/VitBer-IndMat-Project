The $\theta$-method, given by

$$\begin{align}
U^{n+1}=U^{n}+\tau 
\left[
    \theta F(t_{n+1}, \ U^{n+1}) + (1 - \theta) F(t_n, \ U^n)
\right]
\end{align}$$

may be rewritten as a two-step Runge-Kutta method as follows,

$$\begin{align}
& k_1 = F(t_n,\ U^n) \\
& k_2 = F \left (
            t_n + \tau, \ U^n + \tau \theta k_2 + \tau (1 - \theta) k_1 
        \right) \\
& U^{n+1} = U^{n} + \tau 
\left[ 
    \theta k_2 + (1 - \theta)k_1 
\right].
\end{align}$$

This gives the butcher tableau

$$\begin{array}
{c|cc}
0 & 0 & 0\\
1 & (1-\theta) & \theta \\
\hline
& (1-\theta) & \theta 
\end{array}$$

To find the order of consistency, $p$, we check the order conditions for the Runge-Kutta method. For $p=1$,

$$\begin{align}
    \sum_{j=1}^{s} b_j = 1 \text{.}
\end{align}$$

Substituting in the values for the $\theta$-method, we obtain 

$$\begin{align}
    b_1 + b_2 = 1-\theta+\theta=1.
\end{align}$$

Since this holds for any $\theta$, the method is at least of order 1. For $p = 2$, we have

$$\begin{align}

\sum_{j=1}^{s} b_j c_j = \frac{1}{2}.

\end{align}$$

Applying this to the $\theta$ method we get

$$\begin{align}

b_1 c_1 + b_2 c_2 = (1-\theta) \cdot 0 + \theta \cdot 1=\theta,

\end{align}$$

meaning that the order condition for $p=2$ fulfilled only if $\theta = \frac{1}{2}$. Therefore, when we check the condition for $p=3$ we have to assume that $\theta$ has this specific value. However, the first order condition for $p=3$,

$$\begin{align}

\sum_{j=1}^{s} b_j {c_j}^2 = \frac{1}{3},

\end{align}$$

is not fulfilled in this case because

$$\begin{align}

b_1 {c_1}^2 + b_2 {c_2}^2 = \theta = \frac{1}{2}.

\end{align}$$

We thus conclude that the $\theta$ method has a consistancy order of $p=1$ for $\theta \in \mathbb{R} ^{\setminus \{1/2\}} $, and $p=2$ for $\theta = 1/2$.

If $\theta$ is chosen to be $1/2$, the $\theta$ method becomes identical to the Crank-Nicolson method. Furthermore, if $\theta=0$ it is reduced to the explicit Euler method, and if $\theta=1$ it becomes the implicit Euler method.




