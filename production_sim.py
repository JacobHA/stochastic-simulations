from gillespie import Gillespie
import matplotlib.pyplot as plt
from parameters import initials, stoichiometry, t, deltas, alpha, beta, gamma, k_a, k_b, k_c

# Loop over all deltas
for delta in deltas:

    # a -> b, Propensity: alpha * a
    # b -> a, Propensity: beta * b
    # b -> c, Propensity: gamma * b
    # c -> b, Propensity: delta * c

    propensities = [lambda a, b, c, na, nb, nc: alpha * a,
                    lambda a, b, c, na, nb, nc: beta * b,
                    lambda a, b, c, na, nb, nc: gamma * b,
                    lambda a, b, c, na, nb, nc: delta * c,
                    lambda a, b, c, na, nb, nc: k_a * a,
                    lambda a, b, c, na, nb, nc: k_b * b,
                    lambda a, b, c, na, nb, nc: k_c * c]

    # run simulation
    gill = Gillespie(initials, propensities, stoichiometry)

    times, all_states = gill.simulate(t)
    a, b, c, na, nb, nc = zip(*all_states)

    # plt.plot(times, na, label=r"$A$")
    # plt.plot(times, nb, label=r"$B$")
    # plt.plot(times, nc, label=r"$C$")
    # Plot the sum of all produts
    plt.plot(times, [na[i] + nb[i] + nc[i]
             for i in range(len(na))], label=r"$\Delta$ = " + str(delta))

    plt.title("Simple expression network")
    plt.xlabel("Time")
    plt.ylabel("Number of products")
    # plt.xlim(0, t+1)
    # plt.ylim(0, 30)
    plt.legend(loc="upper right")
    plt.savefig(f'./figures/prodxn{round(delta, 3)}.png')

    plt.clf()
    # Delete the variables
    del all_states, a, b, c, na, nb, nc, gill

    # Show which delta we're on
    print(f"{round(100 * delta/deltas.max(),2)}% complete...",
          end="\r", flush=True)
