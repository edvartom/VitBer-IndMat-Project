## Prob. need some reformulation

To show that the Cahn-Hilliard equation is invariant under transformation $u\mapsto-u$, we substitute $u$ for $-u$ and show that the result is also a solution of the Cahn-Hilliard equation is given by (80). First, we rewrite (80) in terms of $u$.

$$
\partial_t u = \nabla \cdot 
\left( 
    M \nabla 
    \left( 
        -\kappa \Delta u + f(u)
    \right)
\right)
$$

We proceed to substitute $u$ with $-u$. First, 

$$
f(-u) = \theta_c u+ \frac{\theta}{2} \ln
\left(
    \frac{1 - u}{1 + u}
\right)=
\theta_c u - \frac{\theta}{2} \ln
\left(
    \frac{1 + u}{1 - u}
\right)
= -f(u) \text{.}
$$

Then, we have

$$
\text{LSH} = - \partial_t u 
$$

$$\begin{align*}
\text{RHS} =& \ 
\nabla \cdot 
\left( 
    M \nabla 
    \left( 
        \kappa \Delta u + f(-u)
    \right)
\right)\\
=& \ 
- \nabla \cdot 
\left( 
    M \nabla 
    \left( 
         -\kappa \Delta u + f(u)
    \right)
\right)
\end{align*}$$

Putting this together, we get

$$
- \partial_t u  
=\ 
- \nabla \cdot 
\left( 
    M \nabla 
    \left( 
        - \kappa \Delta u + f(u)
    \right)
\right)
$$

We can simply remove the $-$ signs from both sides, which leads to (80). 


Physcially, this implies that if component $1$ follows the  Cahn-Hilliard equation, then so does component $2$. 


