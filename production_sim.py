from gillespie import Gillespie
import matplotlib.pyplot as plt
from parameters import initials, stoichiometry, t, deltas, alpha, beta, gamma

for delta in deltas:

    # a -> b, Propensity: alpha * a
    # b -> a, Propensity: beta * b
    # b -> c, Propensity: gamma * b
    # c -> b, Propensity: delta * c

    propensities = [lambda a, b, c: alpha * a,
                    lambda a, b, c: beta * b,
                    lambda a, b, c: gamma * b,
                    lambda a, b, c: delta * c]

    # run simulation
    gill = Gillespie(initials, propensities, stoichiometry)

    times, abc = gill.simulate(t)
    a, b, c = zip(*abc)

    plt.plot(times, a, label=r"$A$")
    plt.plot(times, b, label=r"$B$")
    plt.plot(times, c, label=r"$C$")

    plt.title("Simple expression network")
    plt.xlabel("Time")
    plt.ylabel("Number of molecules")
    plt.xlim(0, t+1)
    plt.ylim(0, 30)
    plt.legend(loc="upper right")
    plt.savefig(f'./figures/prodxn{round(delta, 3)}.png')

    plt.clf()
    # Delete the variables
    del abc, a, b, c, gill

    # Show which delta we're on
    print(f"{round(100 * delta/deltas.max(),2)}% complete...",
          end="\r", flush=True)
