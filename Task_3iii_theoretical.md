From 3ii theoretical, we found that the stability function for the $\theta$-method was

$$
r_{\theta}(z) = 1 + \frac{z}{1-\theta z}, \qquad z=\lambda \tau,
$$

for the eq. (INSERT EQUATION NUMBER). The exact solution to eq. (INSERT EQUATION UMUBER) is
$$
y(t)=y_0 e^{\lambda t} \text{.}
$$

For this OED to be stable, we need that $\lambda < 0$, which leads to exponential decay. The solution is then stable for all $z$ such that $|r_{\theta}(z)| \le 1$. Hence, 

$$
\begin{aligned}
\left|1 + \frac{z}{1-\theta z}\right| &< 1 \\
\left(1+ \frac{z}{1-\theta z}\right)^2 &< 1 \\
\left(\frac{1-\theta z + z}{1-\theta z}\right)^2 &< 1 \\
(1 - \theta z + z)^2 &< (1 - \theta z)^2 \\
1 - \theta z + z - \theta z + \theta^2z^2 - \theta z^2
+ z - \theta z^2 + z^2 &< 1 - 2\theta z + \theta^2 z^2 \\
\cancel{1 - 2\theta z + \theta^2 z^2} + 2z + 2\theta z^2 + z^2 &< \cancel{1 - 2\theta z + \theta^2 z^2} \\
2z\left(1-\theta z + \frac{1}{2}z\right) &< 0. \\
\end{aligned}
$$

Since $\lambda\tau = z$, and $\tau>$, we know that $z<0$. As such, 
$$
\begin{aligned}
1 - \theta z + \frac{1}{2}z &> 0 \\
1 &> \left(\theta - \frac{1}{2}\right)z \\
z &< \left(\theta - \frac{1}{2}\right)^{-1}.
\end{aligned}
$$

If we square both sizes, we arrive at 

$$\begin{equation}
|z|^2 = a^2 + b^2 < \left(\theta - \frac{1}{2}\right)^{-2} \text{.}
\end{equation}$$

where we have used $z = a + ib$. We may recognise this as as the equation for a circle with radius
$$
|z| < \frac{2}{2\theta -1} \text{.}
$$

We see that when $\theta \to \infty$, the radius of the stability region is $0$, and when $\theta = 1/2$, the radius of the stability region goes to infinity. 

We also observe that the center of the stability region does not depend on $\theta$.