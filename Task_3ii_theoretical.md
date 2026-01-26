## Info dump

Next, determine the stability function, $r_\theta(z)$ of the 
$\theta$-method and plot the stability region of the $\theta$-method in the complex plane for $0, 0.25, 0.498, 0.5, 0.502, 0.75, 1$. 

* For which values of does the $\theta$-method seem to be A-stable? 
* What do you conjecture for a general $\theta$? 
* Do you have an idea of how the stability region of $\theta$-method looks in general/depends on $\theta$?

<br>

Numerical methods are A-stable (absolute stable) if the whole left half-plane (e.g. $z<0$) is stable. If for $\Re(\theta) < 0$, we have $x'(t) = \lambda x(t)$ decays to zero, like an actual soltuon. 

For the $\theta$-method, we have $\theta\in[0.5, 1]$ -- found on a random paper. Need to check this ourselves. 

The backwards Euler and implcit midpoint are both A-stable, but they are implcit and expensive. 

<br>

## An Attempt at solving this task

Consider the following first order OED

$$\begin{equation}
\dot y = \lambda y
\end{equation}$$

where $\lambda$ may be any real or imaginary value. We now proceed to use the $\theta$-method to solve eq. (1).

$$
y_{n+1} = y_n + \tau 
\left[
    \theta f(t_{n+1}, y_{n+1}) + 
    (1 - \theta) f(t_n, y_n)
\right]
$$

where $f = \dot y$. Substituting for eq. (1) and rearranging gives 

$$
y_{n+1} = y_n \frac{1 + \tau \lambda (1-\theta)}{1 - \tau \lambda \theta}
$$

or

$$\begin{equation}
y_{n+1} = y_0 
\left(
    \frac{1 + \lambda \tau (1-\theta)}{1 - \tau \lambda \theta}
\right)^{n+1} \text{.}
\end{equation}$$

Eq. (2) is the stability function with $z = \tau \lambda$

$$\begin{equation}
r_\theta (z) = \frac{1 + z(1-\theta)}{1-z\theta} \text{.}
\end{equation}$$


<br>

### INSERT CODE

A-Stability occurs when the whole left plane, $z<0$, is stable. Based on the plots, we will have A-stability when $\theta = \{0.5,0.502, 0.75 1\}$. Hence, we conjecture that A-stability occurs for $\theta\in[0.5, 1]$. 

This conicdes with the result from the 3i theoretical, where $\theta = 1/2$ and $\theta = 1$ result in the Crank–Nicolson and Implicit Euler methods, respectively. Both methods are implicit and known to be A-stable. 
<br>

## Task 3

The $\theta$-method is stable for $|r_\theta(z)| < 1$. Hence, 


$$\begin{equation}
-1 < \frac{1 + z(1-\theta)}{1-z\theta} < 1\text{.}
\end{equation}$$

By some algebra, eq. (4) becomes 
$$
z < 0 \quad \land \quad  \theta  < \frac{2 + z}{2z} \text{.}
$$

From the inequality, we see that in general, A-stability occurs for $\theta\in[0, 0.5)$ 
