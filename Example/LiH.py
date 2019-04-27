import numpy as np
from qiskit_chemistry import QiskitChemistry
import time

start_time = time.time()


# LiH molecule specfication with orbital reduction
qiskit_chemistry_dict = {
    'driver': {'name': 'PYSCF'},
    'PYSCF': {'atom': '', 'basis': '6-31g'},
    'operator': {'name': 'hamiltonian', 'qubit_mapping': 'parity',
                 'two_qubit_reduction': True, 'freeze_core': True, 'orbital_reduction': [-3, -2]},
    'algorithm': {'name': ''},
    'optimizer': {'name': 'COBYLA' },
    'variational_form': {'name': 'UCCSD'},
    'initial_state': {'name': 'HartreeFock'}
}

def LiH_Energy(bondlength):
    d=bondlength
    molecule = 'H .0 .0 .0; Li .0 .0 {0}'
    algorithms = 'VQE'
    qiskit_chemistry_dict['PYSCF']['atom'] = molecule.format(d) 
    qiskit_chemistry_dict['algorithm']['name'] = algorithms
    solver = QiskitChemistry()
    result = solver.run(qiskit_chemistry_dict)
    energy = result['energy']

    return energy
bondlength_list = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0]
energies = []

for d in bondlength_list:
    energies.append(LiH_Energy(d))

print(energies)

print("--- %s seconds ---" % (time.time() - start_time))

