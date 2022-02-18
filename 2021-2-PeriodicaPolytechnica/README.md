## Robust Design Optimization with Ārtap Framework

This directory contains the shared projects from the Special Issue: Robust Design Optimization with the Artap
Framework [Vol. 65 No. 2 (2021)](https://pp.bme.hu/eecs/issue/view/1115)

### TEAM35

Pavel Karban, David Pánek, Tamás Orosz, Ivo Doležel,
[Semi-analytical Solution for a Multi-objective TEAM Benchmark Problem](https://pp.bme.hu/eecs/article/view/16093)

This project shows a semi-analytical and a FEM-based solution of the TEAM Benchmark #35 test problem, where the shape of
a coil should be optimized. The goal of the optimization is to find a homogenous magnetic field distribution inside the
coil, while its losses or the robustness of the solution should be maximized.

### HV Cable Parameters

Mustafa, E., Németh, R. M., Afia, R. S. A., Tamus, Z. Ádám,
[Parameterization of Debye Model for Dielectrics Using Voltage Response Measurements and a Benchmark Problem ](https://pp.bme.hu/eecs/article/view/16399)

The proposed example shows a genetic algorithm based function fitting methodology to find the R-C parameters of the
Debye-model of a high voltage cable. The connecting paper contains the detailed description of the measurement and the
benchmarking results.

### Transformer Model Identification

Kuczmann, M., Szücs, A., Kovács, G.,
[Transformer Model Identification by Ārtap](https://doi.org/10.3311/PPee.17606)

The paper presents how Ārtap can be used for determining the equivalent circuit parameters of a one phase transformer as
a benchmark problem. The following unknown parameters of the equivalent circuit are identified: primary resistance and
primary leakage reactance, secondary resistance and secondary leakage reactance, finally magnetizing resistance, and
magnetizing reactance. The known quantities from measurement are the primary voltage, primary current, power factor,
secondary voltage, and the load resistance. Algorithms implemented in Ārtap are used for determining the transformer
parameters and the results are compared with the analytical solution.

### Optimization of Magnetic Clutch

Andriushchenko, E., Kaska, J., Kallaste, A., Belahcen, A., Vaimann, T., Rassõlkin, A.
[Design Optimization of Permanent Magnet Clutch with Ārtap Framework](https://pp.bme.hu/eecs/article/view/17007)

The paper shows an optimization of a magnetic clutch with COMSOL. The goal of the proposed task is to create a reduced
sized magnetic clutch by using 3D printing technology.

### Axial Flux PMSM with FEMM

Nyitrai, A., Orosz, T.,
[FEM-Based Benchmark Problem for Cogging Torque Minimization of Axial Flux Permanent-Magnet Motors in Artap Framework](https://pp.bme.hu/eecs/article/view/17755)

The aim of the study was to create a method for the axial-flux motor optimization based on the open-circuit finite
element model using the Ārtap software. By applying the described method, it is possible to use local and global
optimization algorithms, such as evolutionary and genetic algorithms, directly using the finite element analysis
results. The proposed finite element model can be used for benchmarking and selecting the most appropriate evolutionary
and genetic algorithms for this kind of optimization problems.