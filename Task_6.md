<span style='color:gray'> How does the total mass of the concentration field evolve in time?

As we can see from the mass plot the total mass for the whole domain does not change, and is conserved as expected. The negative mass represents that the mass $m_1$ of the substance we are focusing on in our calculations is less than the mass of the other substance with mass equal to $m_2=-m_1$, so that the total mass of the two substances equals zero.

<span style='color:gray'>How does the mixing energy, the interface energy and the total energy of the system evolve in time?

We expect the total energy to go down, since the system is trying to minimize its energy. Since the interface energy is small compared to the mixing energy, we expect the total energy to be similar to the mixing energy. Therefore,  if the total energy goes down, this means the mixing energy must also go down. If this is in conflict with the interface energy to go down (that is, if the interface energy must be larger in order for the mixing energy to become smaller), this will lead to the interface energy increasing somewhat. <span style='color:red'> However, to me, it seems like both the interface and mixing energy wants the system to be separated, although disagreeing explainations are given in the project description. This is because the mixing energy wants to drive the system away from the homogeneous state (at least this is what is described in the project description), and the interface energy wants the surface area between the phases to be as small as possible. This happens when the two phases are totally separated. **However, this is seen only in one of the cases for each solver ...**

<span style='color:gray'>Can you spot any differences in the evolution of the energies for the two different initial conditions? If so, can you relate those to the evolution of the snapshots?

What we expect is that the energy decreases very much in the beginning (in the spinodal decomposition), where the pattern changes very fast. We expect this, because this is when the mixing energy should be decreasing very fast, because a lot of the separation takes place in this time interval.

<span style='color:red'> How does the time step size influence the evolution of the energies <span style='color:gray'> and the snapshots?

Looking at the animations, we assume that the Ostwald ripening is beginning when the picture starts to look more or less clear. It seems like longer timesteps implies more time before the system reaches the Ostwald ripening. For the timesteps at $1\times 10^{-3}$ time units it takes about $10$ timesteps, and for timesteps at $10^{-4}$ time units, it takes about $1$ timestep. So for long time steps it also takes more time steps and thus more time. <span style='color:red'> **Why?** Does the time step size make the energies go faster to zero?

<span style='color:gray'>How does solver choice influence the evolution of the energies and the snapshots?

The choice of solver also affects the timescale for the spinodal decompotition. This we can see from the pictures below:

![U_63](U_63_snapshot.gif)
![U_73](U_73_snapshot.gif)

and 

![U_67](U_67_snapshot.gif)
![U_77](U_77_snapshot.gif)

These pictures show the transition between the spinodal decomposition and the Ostwald ripening. Looking at two similar pictures, the upper one is from solver from task 4, while the lower one is from the solver from task 5. As we can see, the shape looks the same for both solvers. Looking closer, we see that the number of timesteps taken is higher for solver from task 4. This is due to the different convergence orders of the different solvers. Since the convergence order of the solver from task 5 is higher, this solver uses less timesteps to come to the same result as the one from task 4.

<span style='color:gray'>Identify roughly when the spinodal decomposition and the Ostwald ripening occur in the simulations? At which time does the evolution slows down siginificantly? <span style='color:red'> **And when does the system reach an equilibrium state?**

The spinodal decompositnion ends at different types for each simulation. As mentioned before, it takes about $10$ timesteps for the timesteps at $1\times 10^{-3}$ time units, and about $1$ timestep for timesteps at $10^{-4}$ time units. For example, for the four pictures above, showing the transition between the spinodal decomposition and the Oswald ripening, the time at which the transition is happening is about $0.02$, $0.01$, $0.033$ and $0.015$ (in the same order as the pictures are shown). 

<br>

<span style='color:red'> **More things we see from the animations:**

From the different animations we see that the second initial condition gives the shape of droplets rather than a continuous shape. We observe that there is less of one of the colors for the second initial condition, and we observ from the mass plot that the mass is also lower for some of the simulations. This is likely due to the smaller initial mass: When calculating the random "noise" for the initial value for the second initial condition, we substract 0.45 from the density. Summing this together for all points in space, we get $250\cdot 250\cdot 0.45 = 28125 \approx 30000$, which is what we see in the mass plot.

The gifs to be attached is from the solver from task 5, with the two different initial conditions, with $T=4.0$, and $\tau = 1\times 10^{-3}$.

![U_first](U_first.gif)
![U_second](U_second.gif)

As we can see from the gifs, the interface energy is "winning" over the mixing energy. This is because the system wants to minimize its energy, and the mixing energy is high compared to the interface energy (the interface energy is low due to a very little $\kappa$-value.)