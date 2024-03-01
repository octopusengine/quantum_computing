from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Pauli
from qiskit_ibm_runtime import QiskitRuntimeService, Estimator, Options
from qiskit.providers.basic_provider import BasicSimulator


num_qubits = 3
num_bits = 3
# Create a new circuit with two qubits (first argument) and two classical / bits (second argument)
# qc = QuantumCircuit(num_qubits) ## ok hello world
qc = QuantumCircuit(num_qubits, num_bits)

qc.h(0) # Add a Hadamard gate to qubit 0
qc.h(1)
qc.h(2)
##qc.cx(0, 1) # Perform a controlled-X gate on qubit 1, controlled by qubit 0
 
qc.measure(range(3),range(3)) 

#qc.draw("mpl") / #qc.draw()
print(qc)


#sim = Aer.get_backend("qasm_simulator")
print("[ Simulator ] roll of the eight-sided dice")
sim_backend = BasicSimulator()

print("-"*16,"(3 x 3)")
for _ in range(3):
    job = sim_backend.run(transpile(qc, sim_backend), shots=3)
    result = job.result()
    print(result.get_counts(qc))

print("-"*16,"(6 x 1)")
for _ in range(6):
    job = sim_backend.run(transpile(qc, sim_backend), shots=1)
    result = job.result()
    print(result.get_counts(qc))

"""

     ┌───┐┌─┐      
q_0: ┤ H ├┤M├──────
     ├───┤└╥┘┌─┐   
q_1: ┤ H ├─╫─┤M├───
     ├───┤ ║ └╥┘┌─┐
q_2: ┤ H ├─╫──╫─┤M├
     └───┘ ║  ║ └╥┘
c: 3/══════╩══╩══╩═
           0  1  2 
[ Simulator ] roll of the dice
---------------- (3 x 3)
{'011': 1, '100': 1, '110': 1}
{'110': 1, '010': 1, '011': 1}
{'111': 1, '011': 1, '000': 1}
---------------- (6 x 1)
{'101': 1}
{'001': 1}
{'100': 1}
{'011': 1}
{'011': 1}
{'110': 1}

"""