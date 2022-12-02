import random


class Gillespie:
    def __init__(self, initials, propensities, stoichiometry):
        self.initials = initials
        self.propensities = propensities
        self.stoichiometry = stoichiometry

        self.time = None
        self.counts = None

    def _simulate(self, initials, propensities, stoichiometry, duration):
        """
        Run a simulation with given model.
        :param initials: List of initial population counts.
        :param propensities: List of functions that take population counts
        and give transition rates.
        :param stoichiometry: List of integers, how the population counts
        change per transition.
        :param duration: Maximum simulation time.
        :return: Two lists: The time points and population counts
        per time point.
        """

        # initial values
        self.time = 0
        self.times = [self.time]
        self.counts = [initials]

        # while finish time has not been reached
        while self.time < duration:
            # get current state
            state = self.counts[-1]

            # calculate rates with respective propensities
            rates = [prop(*state) for prop in propensities]

            # stop loop if no transitions available
            if all(r == 0 for r in rates):
                break

            # randomly draw one transition
            transition = random.choices(stoichiometry, weights=rates)[0]
            next_state = [a + b for a, b in zip(state, transition)]

            # draw next time increment from random exponential distribution
            # dt = math.log(1.0 / random.random()) / sum(weights)
            dt = random.expovariate(sum(rates))

            # append new values
            self.time += dt
            self.times.append(self.time)
            self.counts.append(next_state)

        return self.times, self.counts

    def simulate(self, duration):
        return self._simulate(self.initials, self.propensities,
                              self.stoichiometry, duration)
