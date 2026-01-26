As seen in the error-EOC tables, a different solution to the time-dependent biharmonic equation once again makes the EOC-values converge to $1$ and $2$ for $\theta=1$ and $\theta=0.5$, respectively.
However we would like to point out the absnormal EOC-value for $\theta=0.5$, $N_t=640$. While all the other EOC-values in the table from $N_t=20$ onward are around $2$, the EOC-value suddenly drops to around $1.5$ for $N_t=640$. If one would have computed the EOC for even larger $N_t$, one would have seen a gradual decline in the EOC-values. The reason for the drop in EOC is that for this particular solution of the time-dependent biharmonic equation, the error as a result of discrete timesteps is practically zero for $N_t\geq 640$, so increasing $N_t$ will not reduce the error that much anymore. If one wishes to reduce the error of the numerical solution even further, one would have to reduce the spatial steps, i.e. increase $N_x$ and $N_y$. When $N_x=N_y=20$ and $N_t=640$, the spatial sampling frequency is very low compared to the temporal sampling frequency, making the former the principal contributor to the numerical error. Therefore, if we had increased $N_x$ and $N_y$, the abnormal EOC-value for $\theta=0.5$ would have disappeared. 

<br>

## Reformulation (in progress)

From the error-EOC tables, we see that the for our manufractured soluton, the EOC of the transient biharmonic equation converte to $1$ and $2$ for $\theta=1$ and $\theta=0.5$, respectively.

