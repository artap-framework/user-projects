import math
from artap.problem import Problem
from artap.individual import Individual
from artap.algorithm_genetic import NSGAII, EpsMOEA
from artap.algorithm_swarm import SMPSO
from artap.results import Results

try:
    from agrossuite import agros as a2d

except ImportError:
    print("Agros is not present test skipped")


class AgrosSimple(Problem):

    def set(self):

        self.name = "Agros-solution"

        self.parameters = [{'name': 'N1', 'bounds': [0, 1000], 'parameter_type': 'integer'},
                           {'name': 'N2', 'bounds': [0, 1000], 'parameter_type': 'integer'},
                           {'name': 'N3', 'bounds': [0, 1000], 'parameter_type': 'integer'},
                           {'name': 'N4', 'bounds': [0, 1000], 'parameter_type': 'integer'},
                           {'name': 'N5', 'bounds': [0, 1000], 'parameter_type': 'integer'},
                           {'name': 'N6', 'bounds': [0, 1000], 'parameter_type': 'integer'},
                           {'name': 'N7', 'bounds': [0, 1000], 'parameter_type': 'integer'},
                           {'name': 'N8', 'bounds': [0, 1000], 'parameter_type': 'integer'},
                           {'name': 'N9', 'bounds': [0, 1000], 'parameter_type': 'integer'},
                           {'name': 'N10', 'bounds': [0, 1000], 'parameter_type': 'integer'},
                           {'name': 'Ip', 'bounds': [0.1, 10]}]

        self.costs = [{'name': 'F1', 'criteria': 'minimize'}]

    def evaluate(self, individual):
        S = 0.001 * 0.005

        N1 = individual.vector[0]
        N2 = individual.vector[1]
        N3 = individual.vector[2]
        N4 = individual.vector[3]
        N5 = individual.vector[4]
        N6 = individual.vector[5]
        N7 = individual.vector[6]
        N8 = individual.vector[7]
        N9 = individual.vector[8]
        N10 = individual.vector[9]
        Ip = individual.vector[10]

        J1 = N1 * Ip / S
        J2 = N2 * Ip / S
        J3 = N3 * Ip / S
        J4 = N4 * Ip / S
        J5 = N5 * Ip / S
        J6 = N6 * Ip / S
        J7 = N7 * Ip / S
        J8 = N8 * Ip / S
        J9 = N9 * Ip / S
        J10 = N10 * Ip / S

        # problem
        problem = a2d.problem(clear=True)
        problem.coordinate_type = "planar"
        problem.mesh_type = "triangle"

        # fields
        # magnetic
        magnetic = problem.field("magnetic")
        magnetic.analysis_type = "steadystate"
        # magnetic.matrix_solver = "mumps"
        magnetic.number_of_refinements = 1
        magnetic.polynomial_order = 2
        magnetic.adaptivity_type = "disabled"
        magnetic.solver = "linear"

        # boundaries
        magnetic.add_boundary("Close", "magnetic_potential", {"magnetic_potential_real": 0})
        magnetic.add_boundary("Sym", "magnetic_surface_current", {"magnetic_surface_current_real": 0})

        # materials
        magnetic.add_material("Iron",
                              {"magnetic_permeability": 4000, "magnetic_conductivity": 0, "magnetic_remanence": 0,
                               "magnetic_remanence_angle": 0, "magnetic_velocity_x": 0, "magnetic_velocity_y": 0,
                               "magnetic_velocity_angular": 0, "magnetic_current_density_external_real": 0,
                               "magnetic_total_current_prescribed": 0, "magnetic_total_current_real": 0})
        magnetic.add_material("Air", {"magnetic_permeability": 1, "magnetic_conductivity": 0, "magnetic_remanence": 0,
                                      "magnetic_remanence_angle": 0, "magnetic_velocity_x": 0, "magnetic_velocity_y": 0,
                                      "magnetic_velocity_angular": 0, "magnetic_current_density_external_real": 0,
                                      "magnetic_total_current_prescribed": 0, "magnetic_total_current_real": 0})
        magnetic.add_material("J1", {"magnetic_permeability": 1, "magnetic_conductivity": 0, "magnetic_remanence": 0,
                                     "magnetic_remanence_angle": 0, "magnetic_velocity_x": 0, "magnetic_velocity_y": 0,
                                     "magnetic_velocity_angular": 0, "magnetic_current_density_external_real": J1,
                                     "magnetic_total_current_prescribed": 0, "magnetic_total_current_real": 0})
        magnetic.add_material("J2", {"magnetic_permeability": 1, "magnetic_conductivity": 0, "magnetic_remanence": 0,
                                     "magnetic_remanence_angle": 0, "magnetic_velocity_x": 0, "magnetic_velocity_y": 0,
                                     "magnetic_velocity_angular": 0, "magnetic_current_density_external_real": J2,
                                     "magnetic_total_current_prescribed": 0, "magnetic_total_current_real": 0})
        magnetic.add_material("J3", {"magnetic_permeability": 1, "magnetic_conductivity": 0, "magnetic_remanence": 0,
                                     "magnetic_remanence_angle": 0, "magnetic_velocity_x": 0, "magnetic_velocity_y": 0,
                                     "magnetic_velocity_angular": 0, "magnetic_current_density_external_real": J3,
                                     "magnetic_total_current_prescribed": 0, "magnetic_total_current_real": 0})
        magnetic.add_material("J4", {"magnetic_permeability": 1, "magnetic_conductivity": 0, "magnetic_remanence": 0,
                                     "magnetic_remanence_angle": 0, "magnetic_velocity_x": 0, "magnetic_velocity_y": 0,
                                     "magnetic_velocity_angular": 0, "magnetic_current_density_external_real": J4,
                                     "magnetic_total_current_prescribed": 0, "magnetic_total_current_real": 0})
        magnetic.add_material("J5", {"magnetic_permeability": 1, "magnetic_conductivity": 0, "magnetic_remanence": 0,
                                     "magnetic_remanence_angle": 0, "magnetic_velocity_x": 0, "magnetic_velocity_y": 0,
                                     "magnetic_velocity_angular": 0, "magnetic_current_density_external_real": J5,
                                     "magnetic_total_current_prescribed": 0, "magnetic_total_current_real": 0})
        magnetic.add_material("J6", {"magnetic_permeability": 1, "magnetic_conductivity": 0, "magnetic_remanence": 0,
                                     "magnetic_remanence_angle": 0, "magnetic_velocity_x": 0, "magnetic_velocity_y": 0,
                                     "magnetic_velocity_angular": 0, "magnetic_current_density_external_real": J6,
                                     "magnetic_total_current_prescribed": 0, "magnetic_total_current_real": 0})
        magnetic.add_material("J7", {"magnetic_permeability": 1, "magnetic_conductivity": 0, "magnetic_remanence": 0,
                                     "magnetic_remanence_angle": 0, "magnetic_velocity_x": 0, "magnetic_velocity_y": 0,
                                     "magnetic_velocity_angular": 0, "magnetic_current_density_external_real": J7,
                                     "magnetic_total_current_prescribed": 0, "magnetic_total_current_real": 0})
        magnetic.add_material("J8", {"magnetic_permeability": 1, "magnetic_conductivity": 0, "magnetic_remanence": 0,
                                     "magnetic_remanence_angle": 0, "magnetic_velocity_x": 0, "magnetic_velocity_y": 0,
                                     "magnetic_velocity_angular": 0, "magnetic_current_density_external_real": J8,
                                     "magnetic_total_current_prescribed": 0, "magnetic_total_current_real": 0})
        magnetic.add_material("J9", {"magnetic_permeability": 1, "magnetic_conductivity": 0, "magnetic_remanence": 0,
                                     "magnetic_remanence_angle": 0, "magnetic_velocity_x": 0, "magnetic_velocity_y": 0,
                                     "magnetic_velocity_angular": 0, "magnetic_current_density_external_real": J9,
                                     "magnetic_total_current_prescribed": 0, "magnetic_total_current_real": 0})
        magnetic.add_material("J10", {"magnetic_permeability": 1, "magnetic_conductivity": 0, "magnetic_remanence": 0,
                                      "magnetic_remanence_angle": 0, "magnetic_velocity_x": 0, "magnetic_velocity_y": 0,
                                      "magnetic_velocity_angular": 0, "magnetic_current_density_external_real": J10,
                                      "magnetic_total_current_prescribed": 0, "magnetic_total_current_real": 0})

        # geometry
        geometry = problem.geometry()
        geometry.add_edge(0, 0, 0, 0.00065, boundaries={"magnetic": "Sym"})
        geometry.add_edge(0, 0.00065, 0.025, 0.00065)
        geometry.add_edge(0.025, 0.00065, 0.025, 0)
        geometry.add_edge(0.025, 0, 0, 0, boundaries={"magnetic": "Close"})
        geometry.add_edge(0.15, 0, 0, 0.15, angle=90, boundaries={"magnetic": "Close"})
        geometry.add_edge(0.15, 0, 0.051, 0, boundaries={"magnetic": "Close"})
        geometry.add_edge(0.051, 0, 0.025, 0, boundaries={"magnetic": "Close"})
        geometry.add_edge(0, 0.007, 0.005, 0.007)
        geometry.add_edge(0.005, 0.007, 0.005, 0.006)
        geometry.add_edge(0, 0.006, 0.005, 0.006)
        geometry.add_edge(0, 0.006, 0, 0.007, boundaries={"magnetic": "Sym"})
        geometry.add_edge(0, 0.007, 0, 0.15, boundaries={"magnetic": "Sym"})
        geometry.add_edge(0.005, 0.006, 0.01, 0.006)
        geometry.add_edge(0.01, 0.006, 0.01, 0.007)
        geometry.add_edge(0.01, 0.007, 0.005, 0.007)
        geometry.add_edge(0.01, 0.006, 0.015, 0.006)
        geometry.add_edge(0.015, 0.006, 0.015, 0.007)
        geometry.add_edge(0.015, 0.007, 0.01, 0.007)
        geometry.add_edge(0.015, 0.006, 0.02, 0.006)
        geometry.add_edge(0.02, 0.006, 0.02, 0.007)
        geometry.add_edge(0.02, 0.007, 0.015, 0.007)
        geometry.add_edge(0.02, 0.006, 0.025, 0.006)
        geometry.add_edge(0.025, 0.006, 0.025, 0.007)
        geometry.add_edge(0.025, 0.007, 0.02, 0.007)
        geometry.add_edge(0.025, 0.006, 0.03, 0.006)
        geometry.add_edge(0.03, 0.006, 0.03, 0.007)
        geometry.add_edge(0.03, 0.007, 0.025, 0.007)
        geometry.add_edge(0.03, 0.006, 0.035, 0.006)
        geometry.add_edge(0.035, 0.006, 0.035, 0.007)
        geometry.add_edge(0.035, 0.007, 0.03, 0.007)
        geometry.add_edge(0.035, 0.006, 0.04, 0.006)
        geometry.add_edge(0.04, 0.006, 0.04, 0.007)
        geometry.add_edge(0.04, 0.007, 0.035, 0.007)
        geometry.add_edge(0.04, 0.006, 0.045, 0.006)
        geometry.add_edge(0.045, 0.006, 0.045, 0.007)
        geometry.add_edge(0.045, 0.007, 0.04, 0.007)
        geometry.add_edge(0.045, 0.006, 0.051, 0.006)
        geometry.add_edge(0.051, 0.006, 0.051, 0.007)
        geometry.add_edge(0.051, 0.007, 0.045, 0.007)
        geometry.add_edge(0, 0.0013, 0.025, 0.0013)
        geometry.add_edge(0.025, 0.0013, 0.025, 0.00065)
        geometry.add_edge(0, 0.0013, 0, 0.00065, boundaries={"magnetic": "Sym"})
        geometry.add_edge(0.025, 0.00195, 0.025, 0.0013)
        geometry.add_edge(0, 0.00195, 0.025, 0.00195)
        geometry.add_edge(0, 0.00195, 0, 0.0013, boundaries={"magnetic": "Sym"})
        geometry.add_edge(0, 0.0026, 0, 0.00195, boundaries={"magnetic": "Sym"})
        geometry.add_edge(0, 0.0026, 0.025, 0.0026)
        geometry.add_edge(0.025, 0.0026, 0.025, 0.00195)
        geometry.add_edge(0, 0.006, 0, 0.00325, boundaries={"magnetic": "Sym"})
        geometry.add_edge(0, 0.00325, 0, 0.0026, boundaries={"magnetic": "Sym"})
        geometry.add_edge(0, 0.00325, 0.025, 0.00325)
        geometry.add_edge(0.025, 0.00325, 0.025, 0.0026)

        geometry.add_label(0.0121698, 0.000128699, materials={"magnetic": "Iron"})
        geometry.add_label(0.0542031, 0.0849051, materials={"magnetic": "Air"})
        geometry.add_label(0.00283517, 0.00648296, materials={"magnetic": "J1"})
        geometry.add_label(0.00767991, 0.00648296, materials={"magnetic": "J2"})
        geometry.add_label(0.0113064, 0.00670961, materials={"magnetic": "J3"})
        geometry.add_label(0.0170011, 0.00656795, materials={"magnetic": "J4"})
        geometry.add_label(0.0215342, 0.00673795, materials={"magnetic": "J5"})
        geometry.add_label(0.0278805, 0.0063413, materials={"magnetic": "J6"})
        geometry.add_label(0.031252, 0.00653962, materials={"magnetic": "J7"})
        geometry.add_label(0.03706, 0.00656795, materials={"magnetic": "J8"})
        geometry.add_label(0.0419331, 0.00656795, materials={"magnetic": "J9"})
        geometry.add_label(0.0461545, 0.00656795, materials={"magnetic": "J10"})
        geometry.add_label(0.0138763, 0.000916265, materials={"magnetic": "Iron"})
        geometry.add_label(0.0172431, 0.0017413, materials={"magnetic": "Iron"})
        geometry.add_label(0.0173265, 0.00235259, materials={"magnetic": "Iron"})
        geometry.add_label(0.0218278, 0.00296388, materials={"magnetic": "Iron"})

        computation = problem.computation()
        computation.solve()

        solution = computation.solution("magnetic")

        B0 = 0.5

        F = 0.0
        N = 10
        sBx = 0.0
        sBy = 0.0
        for i in range(0, N):
            x = i * 0.025 / N

            for j in range(0, 4):
                point = solution.local_values(x, 0.000325 + j * 0.00065)
                Bx = point["Brx"]
                By = point["Bry"]

                sBx = sBx + abs(Bx)
                sBy = sBy + abs(By)
                Bp = math.sqrt((Bx - B0) ** 2 + (By - 0.0) ** 2)
                F = max(F, Bp)

        sBx = sBx / N / 5.0
        sBy = sBy / N / 5.0

        print(F)
        print(Ip, N1, N2, N3, N4, N5, N6, N7, N8, N9, N10)
        del computation
        return [F]


def optim_single():
    problem = AgrosSimple()
    # optimization
    # algorithm = NSGAII(problem)
    algorithm = EpsMOEA(problem)
    # algorithm = SMPSO(problem)
    algorithm.options['max_population_number'] = 100
    algorithm.options['max_population_size'] = 100
    algorithm.run()

    results = Results(problem)
    res_individual = results.find_optimum()
    S = 0.001 * 0.005
    Ip = res_individual.vector[10]
    for i in range(len(problem.parameters)):
        print("{} : {} -> {}".format(problem.parameters[i].get("name"), res_individual.vector[i],
                                     res_individual.vector[i] * Ip / S))


if __name__ == '__main__':
    optim_single()
