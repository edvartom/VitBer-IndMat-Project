The local truncation error for the Song-scheme is given by

$$\begin{align}

\eta=U(t_0+\tau)-U_1.

\end{align}$$

To find the conditions for the order of convergence $p$ to be $2$ we perform a Taylor-expansion of the term $U(t_0+\tau)$ around $t_0$.


$$\begin{align}

U(t_0+\tau)=U(t_0)+U'(t_0)\tau+\frac{U''(t_0)}{2!}\tau^2+\frac{U'''(t_0)}{3!}\tau^3+...

\end{align}$$

With 

$$\begin{align}

U(t_0)=U_0 \\
U'(t_0)=U'_0=\bold{L}U_0+\bold{N}(U_0) \\
U''(t_0)=U''_0=\bold{L}U'_0+\bold{N}(U'_0)=\bold{L}^2U_0+\bold{L}\bold{N}(U_0)+\bold{N}[\bold{L}U_0+\bold{N}(U_0)],

\end{align}$$

and

$$\begin{align}

U'''(t_0)=U'''_0=\bold{L}U''_0+\bold{N}(U''_0)=\bold{L}^2U'_0+\bold{LN}(U'_0)+\bold{N}[\bold{L}U'_0+\bold{N}(U'_0)]\\

= \bold{L}^3U_0+\bold{L}^2\bold{N}(U_0)+\bold{LN}[\bold{L}U_0+\bold{N}U_0]+\bold{N}[\bold{L}^2U_0+\bold{LN}(U_0)+\bold{N}(\bold{L}U_0+\bold{N}(U_0))],

\end{align}$$

we get that

$$\begin{align}

U(t_0+\tau)=U_0
+\bold{L}U_0+\bold{N}(U_0)\tau \\
+\frac{\bold{L}^2U_0+\bold{L}\bold{N}(U_0)+\bold{N}[\bold{L}U_0+\bold{N}(U_0)]}{2!}\tau^2 \\
+\frac{\bold{L}^3U_0+\bold{L}^2\bold{N}(U_0)+\bold{LN}[\bold{L}U_0+\bold{N}U_0]+\bold{N}[\bold{L}^2U_0+\bold{LN}(U_0)+\bold{N}(\bold{L}U_0+\bold{N}(U_0))]}{3!}\tau^3+...

\end{align}$$

Now we turn to $U_1$. The Song scheme defines $U_1$ as

$$\begin{align}

U_1=\frac{\alpha_{20}U_0+\alpha_{21}U^{(1)}+\alpha_{22}U^{(2)}+\beta_2\tau\bold{N}(U^{(2)})}{1-\beta_2\tau\bold{L}}.

\end{align}$$

and $U^{(1)}$ and $U^{(2)}$ are defined as

$$\begin{align}

U^{(1)}=\frac{U_0+\tau\bold{N}(U_0)}{1-\tau\bold{L}} \\

U^{(2)}=\frac{\alpha_{10}U_0+\alpha_{11}U^{(1)}+\tau\beta_1\bold{N}(U^{(1)})}{1-\tau\beta_1\bold{L}}

\end{align}$$