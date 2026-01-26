The time derivative of the total mass of a Cahn-Hilliard solution $u(\boldsymbol{x},y)$, which is periodic on a rectangular domain $\Omega = [0, L_x) \times [0, L_y)$ can be written as

$$\begin{equation}
\frac{d}{dt} \int_\Omega u(\boldsymbol{x},t) \,d\boldsymbol{x} = \int_\Omega \partial_{t} u(\boldsymbol{x},t) \,d\boldsymbol{x} \\
=\int_\Omega \nabla (M \nabla \mu) \,d\boldsymbol{x}.

\end{equation}$$

The divergence theorem tells us that for a vector field $\boldsymbol{F}$ and a two-dimensional surface $D$, we have

$$\begin{equation}
\int_D \nabla \boldsymbol{F} \,dA = \int_{\partial D} \boldsymbol{F} \,d\boldsymbol{S},

\end{equation}$$
where $\partial D$ denotes the boundary of $D$ and $d\boldsymbol{S}$ is always perpendicular to $\partial D$. Applying the divergence theorem to eq. $(1)$ we get

$$\begin{equation}
\int_\Omega \nabla (M \nabla \mu) \,d\boldsymbol{x} = \int_{\partial \Omega} M \nabla \mu \,d\boldsymbol{S} = \int_{\partial \Omega} M \left( \frac{\partial \mu}{\partial x}, \frac{\partial \mu}{\partial y} \right) \,d\boldsymbol{S}

\end{equation}$$

It is possible to find $d\boldsymbol{S}$ by taking advantage of the fact that $\Omega$ is rectangular. Four sides requre four $d\boldsymbol{S}$. Assuming that $x \in [0,L_x]$ and $y \in [0,L_y]$, the four boundaries are loacted at $x=0$, $x=L_x$, $y=0$, $y=L_y$ and the corresponding $d\boldsymbol{S}$ are as follows:

$$\begin{align}
x=0 : d\boldsymbol{S} =(-1,0)dS \nonumber \\
x=L_x : d\boldsymbol{S} =(1,0)dS \nonumber \\
y=0 : d\boldsymbol{S} =(0,-1)dS \nonumber \\
y=L_y : d\boldsymbol{S} =(0,1)dS. \\

\end{align}$$

Inserting this into eq. $(3)$ we get

$$\begin{align}

\int_{\partial \Omega} M \nabla \mu \,d\boldsymbol{S} = M \left[ -\int_{0}^{L_y} \left .\frac{\partial \mu}{\partial x} \right|_{x=0} \,dy +\int_{0}^{L_y} \left .\frac{\partial \mu}{\partial x} \right|_{x=L_x} \,dy -\int_{0}^{L_x} \left .\frac{\partial \mu}{\partial y} \right|_{y=0} \,dx +\int_{0}^{L_x} \left .\frac{\partial \mu}{\partial y} \right|_{y=L_y} \,dx\right].

\end{align}$$

Since $\mu$ is periodic, i.e. repeats itself for every $L_x$, $L_y$, the derivatives of $\mu$ should be the same in $x=L_x$ and $y=L_y$ as in $x=0$ and $y=0$, respectively. Therefore, the integrals in eq. $(5)$ cancel out and we conclude that

$$\begin{equation}
\frac{d}{dt} \int_\Omega u(\boldsymbol{x},t) \,d\boldsymbol{x} =0.

\end{equation}$$