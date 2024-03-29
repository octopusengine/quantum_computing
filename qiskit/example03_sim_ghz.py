from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Pauli
from qiskit_ibm_runtime import QiskitRuntimeService, Estimator, Options
from qiskit.providers.basic_provider import BasicSimulator
from lib.octopus_qiskit_tools import create_noise_dict, sum_noise_res_dict, print_histogram

DEBUG = True
num_qubits = 2
num_bits = 2
SET_PAULI = False
SHOTS = 512

# Create a new circuit with two qubits (first argument) and two classical / bits (second argument)
# qc = QuantumCircuit(num_qubits) ## ok hello world
qc = QuantumCircuit(num_qubits, num_bits, name="ghz")

qc.h(0)     # Add a Hadamard gate to qubit 0
qc.cx(0, 1) # Perform a controlled-X gate on qubit 1, controlled by qubit 0
 
#qc.draw("mpl")
print("[ GHZ ] Greenberger–Horne–Zeilinger_state")
print(qc)

if SET_PAULI:
    print("[ Pauli ]")

    ZZ = Pauli('ZZ')
    ZI = Pauli('ZI')
    IZ = Pauli('IZ')
    XX = Pauli('XX')
    XI = Pauli('XI')
    IX = Pauli('IX')

"""
print("[ service ]")
service = QiskitRuntimeService()
 
# Run on the least-busy backend you have access to # or sim True
backend = service.least_busy(simulator=True, operational=True) 
 
options = Options()
options.resilience_level = 1
options.optimization_level = 3
 
# Create an Estimator object
estimator = Estimator(backend, options=options)
 
# Submit the circuit to Estimator
job = estimator.run(circuits=[isa_circuit]*6, observables=[IZ, IX, ZI, XI, ZZ, XX], shots = 5000)

# Run on a simulator
backend = service.get_backend("ibmq_qasm_simulator")
"""

print("[ Barrier ]")  # Insert a barrier before measurement    
qc.barrier()


print("[ Measure ]") # q2b! Measure all of the qubits in the standard basis
for i in range(num_qubits):
    if DEBUG:
        print(i,i,qc.measure(i, i))
    else:
        qc.measure(i, i)
print(qc)


print("[ Simulator ]")
sim_backend = BasicSimulator()

print("-"*32)
print("8 single steps")
for _ in range(8):
     job = sim_backend.run(transpile(qc, sim_backend), shots=1)
     result = job.result()
     print(result.get_counts(qc))


job = sim_backend.run(transpile(qc, sim_backend), shots=SHOTS)
result = job.result()

print("Basic simulator result - shots:", SHOTS)
print(result.get_counts(qc))

print("--- addition of errors caused by a General noise")
gn = create_noise_dict(2, 0.1, SHOTS)

job = sim_backend.run(transpile(qc, sim_backend), shots=SHOTS)
result = job.result()
sim = result.get_counts(qc)

final_sim = sum_noise_res_dict(gn, sim)

print("Basic simulator result - shots:", SHOTS)
print(final_sim)
print_histogram(final_sim)



"""
[ GHZ ] Greenberger–Horne–Zeilinger_state
     ┌───┐     
q_0: ┤ H ├──■──
     └───┘┌─┴─┐
q_1: ─────┤ X ├
          └───┘
c: 2/══════════
               
[ Barrier ]
[ Measure ]
0 0 <qiskit.circuit.instructionset.InstructionSet object at 0x7f792eac0fd0>
1 1 <qiskit.circuit.instructionset.InstructionSet object at 0x7f792eac0b20>
     ┌───┐      ░ ┌─┐   
q_0: ┤ H ├──■───░─┤M├───
     └───┘┌─┴─┐ ░ └╥┘┌─┐
q_1: ─────┤ X ├─░──╫─┤M├
          └───┘ ░  ║ └╥┘
c: 2/══════════════╩══╩═
                   0  1 
[ Simulator ]
Basic simulator result: 
{'11': 269, '00': 243}

--- addition of errors caused by a General noise
Basic simulator result - shots: 512
{'00': 270, '01': 12, '10': 5, '11': 266}
00: ################################################################################
01: ###
10: #
11: ##############################################################################

"""
