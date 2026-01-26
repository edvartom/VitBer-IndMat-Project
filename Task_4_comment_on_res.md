From the error-EOC table we see that the EOC of the numerical solution of the Cahn-Hilliard equation using this IMEX-solver converges to $1$ for both $\kappa$ -values, though it converges slightly faster for $\kappa=1$. This EOC-value is expected, as the IMEX-solver is a combination of the forward and backward Euler method, both of whom were shown to have an order of convergence of $1$ in task $3$. 
The reason why it converges slower for $\kappa=0.01$ could be because smaller $\kappa$ -values cause sharper interfaces between the substances and a lower interface energy $\mathcal{E}(u)_{int}$, which can make the IMEX-solver a little less stable. For instance, if one pours some oil into a water container, the oil droplets will separate from the water, creating a sharp interface between the substances, and causing a discontinuity in the water. It is possible to imagine that such discontinuities could cause instability in numerical solvers. Indeed, if we set $\kappa = 10^{-6}$ in our program, the error plateaus after $N_t=1600$, and the EOC gradually sinks.


## Reformulation

The table above shows the error-EOC for two solutions of the Cahn-Hillard, solved numerically with an IMEX-solver. From the table, we see that the EOC converges towards $1$ for both $\kappa$-values, with $\kappa=1$ convergning slightly faster. Given that the IMEX-solver combines the forwards and backwards Euler methods, both of which demonstrated ordere of convergence of $1$ (task 3), this EOC-value in this task was therefore to be expected.

The reason for the slower convergence when $\kappa=0.01$ might be that smaller the $\kappa$-values cause sharper the interface between the substances and lower interface energy $\mathcal{E}(u)_{int}$. Hence, this result in a less stable IMEX-solver.  

For instance, when oil is poured into a countainer of water, the oil droplets will separate from the water, forming sharp boundaries between the two substances. This boundary results in discontinuity. It is conceivable to assume that such discontinuities may result in instability in the numerical solver. That is, if we for instance set $\kappa = 10^{-6}$, the error plateaus after $N_t=1600$, and the EOC will gradually fall.

