from funcs import *

# Endpoints are not defined due to undefined value of log(0).
u = np.linspace(-1, 1, 1000, endpoint=False)
theta_vals = [0.7, 0.9, 1.2, 1.5, 1.6]

min_index=0
max_index=0

for theta in theta_vals:
    energy_density = F(u, theta, theta_c = theta_c)
    plt.plot(u, energy_density, label="$\Theta=$"+str(theta))

    # First index is still 'NaN'. This cleans it up and allows 
    # us to find minimum and maximum.
    clean_energy_density = np.array([x for x in energy_density if x==x]) 
                                                                         
    min_index=np.argmin(clean_energy_density)
    max_index=np.argmax(clean_energy_density)

print("Minimum at u = "+str(u[min_index]))
print("Maximum at u = "+str(u[max_index]))

# Plotting details
plt.title("Helmholtz free energy density as a function of substance consentrations")
plt.xlabel("Substance concentration $u(x,t)$")
plt.ylabel("Helmholtz energy density $F(u)$")
plt.legend()
plt.grid()
plt.show()