from gillespie import Gillespie
import matplotlib.pyplot as plt

forward = 0.01  # forward reaction rate
backward = 0.005  # backward reaction rate
t = 15  # duration

initials = [100, 150, 0]  # X, Y, XY

# X + Y -> XY, Propensity: forward * X * Y
# XY -> X + Y, Propensity: backward * XY
propensities = [lambda x, y, xy: forward * x * y,
                lambda x, y, xy: backward * xy]

# X + Y -> XY, Population change: X - 1, Y - 1, XY + 1
# XY -> X + Y, Population change: X + 1, Y + 1, XY - 1

stoichiometry = [[-1, -1, 1],
                 [1, 1, -1]]

# run simulation
gill = Gillespie(initials, propensities, stoichiometry)

t, XYXY = gill.simulate(t)
X, Y, XY = zip(*XYXY)

plt.plot(t, X, label=r"$X$")
plt.plot(t, Y, label=r"$Y$")
plt.plot(t, XY, label=r"$XY$")

plt.title(r"Simple equilibrium reaction $X + Y \leftrightarrow XY$")
plt.xlabel("Time")
plt.ylabel("Number of molecules")
plt.legend()
plt.show()
