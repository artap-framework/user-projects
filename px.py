"""
Problem:
--------

lkljkjlkl
"""

from artap.problem import Problem
from artap.results import Results
from artap.algorithm_scipy import ScipyOpt
from artap.algorithm_nlopt import NLopt
from artap.algorithm_nlopt import LN_COBYLA, LN_NELDERMEAD, LN_BOBYQA
from artap.algorithm_genetic import NSGAII

import math


class PowerExchangeProblem(Problem):
    """
    The solution of this problem needs to find the maximum of the social welfare. It is  the function of bid allocations.
	Allocated supply and demand bids must be balanced and there are also network transmission limits.
	"""

    def set(self):
        self.name = "power exchange"
        self.pf = 1000  # punishment factor
        # acc - acceptance ratios of the different bids
        '''
        self.parameters = [{'name': 'ACC1', 'initial_value': 1.0, 'bounds': [0., 1.]},
                           {'name': 'ACC2', 'initial_value': 1.0, 'bounds': [0., 1.]},
                           {'name': 'ACC3', 'initial_value': 1.0, 'bounds': [0., 1.]},
                           {'name': 'ACC4', 'initial_value': 0.0, 'bounds': [0., 1.]},
                           {'name': 'ACC5', 'initial_value': 0.0, 'bounds': [0., 1.]},
                           {'name': 'ACC6', 'initial_value': 1.0, 'bounds': [0., 1.]},
                           {'name': 'ACC7', 'initial_value': 1.0, 'bounds': [0., 1.]},
                           {'name': 'ACC8', 'initial_value': 0.0, 'bounds': [0., 1.]},
                           {'name': 'ACC9', 'initial_value': 0.0, 'bounds': [0., 1.]},
                           {'name': 'ACC10', 'initial_value': 0.0, 'bounds': [0., 1.]},
                           {'name': 'ACC11', 'initial_value': 1.0, 'bounds': [0., 1.]},
                           {'name': 'ACC12', 'initial_value': 1.0, 'bounds': [0., 1.]},
                           {'name': 'ACC13', 'initial_value': 0.0, 'bounds': [0., 1.]},
                           {'name': 'ACC14', 'initial_value': 0.0, 'bounds': [0., 1.]},
                           {'name': 'ACC15', 'initial_value': 0.0, 'bounds': [0., 1.]},
                           {'name': 'ACC16', 'initial_value': 1.0, 'bounds': [0., 1.]},
                           {'name': 'ACC17', 'initial_value': 1.0, 'bounds': [0., 1.]},
                           {'name': 'ACC18', 'initial_value': 1.0, 'bounds': [0., 1.]},
                           {'name': 'ACC19', 'initial_value': 0.0, 'bounds': [0., 1.]},
                           {'name': 'ACC20', 'initial_value': 0.0, 'bounds': [0., 1.]}]
        '''
        self.parameters = [{'name': 'ACC1', 'initial_value': 0.0, 'bounds': [0, 100], 'parameter_type': 'integer'},
                           {'name': 'ACC2', 'initial_value': 0.0, 'bounds': [0, 100], 'parameter_type': 'integer'},
                           {'name': 'ACC3', 'initial_value': 0.0, 'bounds': [0, 100], 'parameter_type': 'integer'},
                           {'name': 'ACC4', 'initial_value': 0.0, 'bounds': [0, 100], 'parameter_type': 'integer'},
                           {'name': 'ACC5', 'initial_value': 0.0, 'bounds': [0, 100], 'parameter_type': 'integer'},
                           {'name': 'ACC6', 'initial_value': 0.0, 'bounds': [0, 100], 'parameter_type': 'integer'},
                           {'name': 'ACC7', 'initial_value': 0.0, 'bounds': [0, 100], 'parameter_type': 'integer'},
                           {'name': 'ACC8', 'initial_value': 0.0, 'bounds': [0, 100], 'parameter_type': 'integer'},
                           {'name': 'ACC9', 'initial_value': 0.0, 'bounds': [0, 100], 'parameter_type': 'integer'},
                           {'name': 'ACC10', 'initial_value': 0.0, 'bounds': [0, 100], 'parameter_type': 'integer'},
                           {'name': 'ACC11', 'initial_value': 0.0, 'bounds': [0, 100], 'parameter_type': 'integer'},
                           {'name': 'ACC12', 'initial_value': 0.0, 'bounds': [0, 100], 'parameter_type': 'integer'},
                           {'name': 'ACC13', 'initial_value': 0.0, 'bounds': [0, 100], 'parameter_type': 'integer'},
                           {'name': 'ACC14', 'initial_value': 0.0, 'bounds': [0, 100], 'parameter_type': 'integer'},
                           {'name': 'ACC15', 'initial_value': 0.0, 'bounds': [0, 100], 'parameter_type': 'integer'},
                           {'name': 'ACC16', 'initial_value': 0.0, 'bounds': [0, 100], 'parameter_type': 'integer'},
                           {'name': 'ACC17', 'initial_value': 0.0, 'bounds': [0, 100], 'parameter_type': 'integer'},
                           {'name': 'ACC18', 'initial_value': 0.0, 'bounds': [0, 100], 'parameter_type': 'integer'},
                           {'name': 'ACC19', 'initial_value': 0.0, 'bounds': [0, 100], 'parameter_type': 'integer'},
                           {'name': 'ACC20', 'initial_value': 0.0, 'bounds': [0, 100], 'parameter_type': 'integer'}]
        # social welfare
        self.costs = [{'name': 'SW', 'criteria': 'minimize'}]

        # parameters for the electric market model
        # price of the bids, there are 20 bids in the model
        self.price = ([5.0, 10.0, 12.0, 30.0, 40.0,
                       50.0, 40.0, 15.0, 10.0, 5.0,
                       10.0, 15.0, 25.0, 40.0, 50.0,
                       50.0, 35.0, 30.0, 20.0, 10.0])

        # quantity of the energy amount in MWh, the negative is the demand and the positive is the supply
        self.quantity = ([50.0, 50.0, 40.0, 20.0, 40.0,
                          -20.0, -20.0, -80.0, -40.0, -20.0,
                          20.0, 30.0, 30.0, 80.0, 40.0,
                          -40.0, -60.0, -50.0, -30.0, -50.0])

        # Network model zones and  parameters
        # network zones
        self.zone_map = ([1.0, 1.0, 1.0, 1.0, 1.0,
                          1.0, 1.0, 1.0, 1.0, 1.0,
                          2.0, 2.0, 2.0, 2.0, 2.0,
                          2.0, 2.0, 2.0, 2.0, 2.0])

        # power transfer distribution factor - for the 3 transmission lines
        self.ptdf = [0.33, 0.5, 0.4]

        # ram_pos, ram_neg remaining available margin
        self.ram_pos = [70.0, 100.0, 45.0]
        self.ram_neg = [80.0, 55.0, 45.0]

    def evaluate(self, individual):

        ACC = individual.vector

        # net exports
        NEX1 = 0
        NEX2 = 0
        for i in range(len(self.quantity) - 1):
            if self.zone_map[i] == 1:
                NEX1 += ACC[i] * self.quantity[i]/100.
            if self.zone_map[i] == 2:
                NEX2 += ACC[i] * self.quantity[i]/100.

        # transmitted quantities
        TQ1 = self.ptdf[0] * NEX2
        TQ2 = self.ptdf[1] * NEX2
        TQ3 = self.ptdf[2] * NEX2

        # social welfare
        SW = 0
        for i in range(len(self.quantity) - 1):
            SW = SW + ACC[i] * self.quantity[i] * self.price[i]/100.

        # supply-demand balance punishment term
        SW = SW + self.pf * abs(NEX1 + NEX2)
        # network transmission limit punishment terms
        SW = SW + self.pf * max(0, TQ1 - self.ram_pos[0]) + self.pf * max(0, -self.ram_neg[0] - TQ1)
        SW = SW + self.pf * max(0, TQ2 - self.ram_pos[1]) + self.pf * max(0, -self.ram_neg[1] - TQ2)
        SW = SW + self.pf * max(0, TQ3 - self.ram_pos[2]) + self.pf * max(0, -self.ram_neg[2] - TQ3)

        return [SW]


# Optimization with Nelder-Mead
problem_nlm = PowerExchangeProblem()

# # Perform the optimization iterating over 100 times on 100 individuals.
algorithm = NSGAII(problem_nlm)
algorithm.options['max_population_number'] = 750
algorithm.options['max_population_size'] = 300
algorithm.run()
# set the optimization method
# algorithm_nlm = NLopt(problem_nlm)
# algorithm_nlm.options['algorithm'] = LN_BOBYQA#LN_NELDERMEAD
# algorithm_nlm.options['n_iterations'] = 10000
# algorithm_nlm.options['ftol_rel'] = 1e-30
# algorithm_nlm.options['ftol_abs'] = 1e-2
# algorithm_nlm.options['xtol_rel'] = 1e-30
# algorithm_nlm.options['xtol_abs'] = 1e-2

# perform the optimization
# algorithm_nlm.run()

results_nlm = Results(problem_nlm)
opt = results_nlm.find_optimum('SW')

print('Optimal solution:', opt.costs, opt.vector)
