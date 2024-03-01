from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Pauli
from qiskit.providers.basic_provider import BasicSimulator

DEBUG = True
num_qubits = 2
num_bits = 2
SET_PAULI = True
SHOTS = 1024

# Create a new circuit with two qubits (first argument) and two classical / bits (second argument)
qc = QuantumCircuit(num_qubits, num_bits, name="ghz")

qc.h(0)     # Add a Hadamard gate to qubit 0
qc.h(1)
#qc.cx(0, 1) # Perform a controlled-X gate on qubit 1, controlled by qubit 0
 
#qc.draw("mpl")
print("[ GHZ ] Greenberger–Horne–Zeilinger_state")

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
# No classical registers in circuit "circuit-158", counts will be empty.
sim_backend = BasicSimulator()
job = sim_backend.run(transpile(qc, sim_backend), shots=SHOTS)
result = job.result()

print("Basic simulator result: ")
print(result.get_counts(qc))


"""
[ GHZ ] Greenberger–Horne–Zeilinger_state
[ Pauli ]
[ Barrier ]
[ Measure ]
0 0 <qiskit.circuit.instructionset.InstructionSet object at 0x7f6d0167f220>
1 1 <qiskit.circuit.instructionset.InstructionSet object at 0x7f6d0167edd0>

     ┌───┐ ░ ┌─┐   
q_0: ┤ H ├─░─┤M├───
     ├───┤ ░ └╥┘┌─┐
q_1: ┤ H ├─░──╫─┤M├
     └───┘ ░  ║ └╥┘
c: 2/═════════╩══╩═
              0  1 
[ Simulator ]
Basic simulator result: 
{'01': 270, '00': 234, '11': 267, '10': 253}

"""
