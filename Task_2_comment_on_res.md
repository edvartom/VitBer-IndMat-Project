In this task, the biharmonic equation

$$\begin{equation}
\Delta^2 u(x,y)+ cu(x,y) =f(x,y) , \qquad c\geq0
\end{equation}$$
is solved and plotted on a rectangular domain $\Omega=[0,2\pi) \times [0,4\pi)$.

We consider the two solutions

$$\begin{align}
u_1(x,y)=\sin(8(x-1))\cos(4y), \qquad c=1 \\
u_2(x,y)=\exp[\sin^2(x)+\cos(2y)], \qquad c=0.
\end{align}$$

In both plots we see that the numerical solutions for both $u_1$ and $u_2$ closely resemble the exact solutions for each, and the error is therefore minimal.

When comparing the plots of $u_1$ for $N_x=15$ and $N_x=16$ we observe a drastic change in solution values. The scale of the error also drops from around $10^{-2}$ to the machine-precision scale of $10^{-15}$. This can be explained by aliasing. The largest frequency in $u_1$ is $8$, which means that according to the Nyquist-Shannon sampling theorem, the spatial sampling frequency ($N_x$) of $u_1$ should be at least $16$ to produce an accurate and aliasing-free solution. This is known as the Nyquist frequency and is given by $N_{x, Nyquist}=2f_{max}=2\cdot 8=16$ in this case. Since $15<N_{x, Nyquist}$, the sampling rate $N_x=15$ will therefore not be sufficient to 'catch' the higher frequency, leading to aliasing and increased error.

This effect can also be observed in the table containing the error and experimental order of convergence (EOC) for $u_1$. As soon as $N_x=N_{x, Nyquist}$, the error drops to machine-precision and EOC goes up to above $500$! In other words, the numerical solution immediately becomes much more more accurate when $N_x\geq16$. Though the EOC table for $u_1$ shows that the EOC becomes negative for $N_x=20$ and $N_x=32$, one can assume that this is only due to the fact that the error scale is already on machine-precision level and can therefore not get much smaller.

From the error plot for $u_2$ we see a relatively small error scale of $10^{-8}$, and from the error-EOC table we see a large decrease in the error for increasing $N_x$. In fact, the EOC shows that only by changing $N_x$ from $36$ to $40$, the error becomes nearly $30$ times smaller! 

However, comparing the tables for $u_1$ and $u_2$ we can see that the error for $u_1$ decreases much faster than for $u_2$. This could be because the largest frequency in $u_1$ is finite, while this is not the case for $u_2$. $u_2$ is an exponential function containing trigonometric functions in the exponent. An exponential function can be written as

$$\begin{align}
\exp(x)=\lim_{n\to\infty} \left( 1+ \frac{x}{n} \right)^n,
\end{align}$$

and through trigonometric identities one can show that 

$$\begin{align}
\sin^n(\theta)= ... +a \sin(n \theta) \\
\cos^n(\theta)= ... +b \cos(n \theta),
\end{align}$$

with $n \in \mathbb{N}$, and $a,b \in \mathbb{R}$. Therefore, if $x$ in eq. $(4)$  is replaced by a trigonometric function, one ends up with an infinitely long sum of trigonometric equation where the largest frequency is not finite. This is why the numerical solution for $u_2$ will be affected by aliasing for any $N_x$, and the error will never be as low as for $u_1$.