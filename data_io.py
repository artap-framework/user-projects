from artap.problem import ProblemViewDataStore
from artap.results import Results

from artap.operators import RandomGenerator

import os


def read_datastore():
    # Path to this script file location
    problem = ProblemViewDataStore(database_name='database_pt_pur.sqlite')

    print(problem.name)

    res = Results(problem)
    fig, ax = res.get_pareto_plot()
    fig.show()
    individuals = problem.last_population()
    data = []

    for ind in individuals:
        line = ind.vector
        line.extend(ind.costs)
        data.append(line)
        del line

    import csv
    file = open('database_pt_pur.csv', 'w+', newline='')

    # writing the data into the file
    with file:
        write = csv.writer(file)
        write.writerows(data)
    print(individuals)

if __name__ == '__main__':
    read_datastore()
