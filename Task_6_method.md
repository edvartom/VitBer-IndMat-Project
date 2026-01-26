In this task, we calculate the total mass, the interface enrgy, the mixing energy and the total energy for each time step. 

To calculate the total mass, we need to integrate the mass over the whole domain $\Omega = [0.5]^2$. However, since our data is descrete, and we are only interested in the changes in mass, the integration is replaced by a summation. So 

$\text{Total mass} = \sum \text{mass density} = \sum u$.

The interface and mixing energies are calculated from equation 81 in the project description. Here we have also replaced the integrals by sums, for the same reason as for the mass. This gives 

$\mathcal{E}_\text{int}(u) = \kappa / 2 \cdot \sum |\nabla u|^2$

and 

$\mathcal{E}_\text{mix} = \sum F(u)$.

The total energy is just the sum of these:

$\mathcal{E}_\text{tot} = \mathcal{E}_\text{int} + \mathcal{E}_\text{mix}$.
