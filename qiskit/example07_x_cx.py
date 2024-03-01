from qiskit import QuantumCircuit, transpile
from qiskit.providers.basic_provider import BasicSimulator

DEBUG = False
num_qubits = 2
num_bits = 2
SHOTS = 2048

# Create a new circuit with two qubits (first argument) and two classical / bits (second argument)
# qc = QuantumCircuit(num_qubits) ## ok hello world
qc = QuantumCircuit(num_qubits, num_bits)

qc.x(0)     # The Pauli-X gate is the quantum equivalent of the NOT gate for classical computers
qc.cx(0, 1) # Perform a controlled-X gate on qubit 1, controlled by qubit 0
 
#qc.draw("mpl")
print("[ X CX ] 11")

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

"""
print("-"*32)
print("8 single steps")
for _ in range(8):
     job = sim_backend.run(transpile(qc, sim_backend), shots=1)
     result = job.result()
     print(result.get_counts(qc))
"""

job = sim_backend.run(transpile(qc, sim_backend), shots=SHOTS)
result = job.result()

print("Basic simulator result - shots:", SHOTS)
print(result.get_counts(qc))


"""
[ X CX ] 11
[ Barrier ]
[ Measure ]
     ┌───┐      ░ ┌─┐   
q_0: ┤ X ├──■───░─┤M├───
     └───┘┌─┴─┐ ░ └╥┘┌─┐
q_1: ─────┤ X ├─░──╫─┤M├
          └───┘ ░  ║ └╥┘
c: 2/══════════════╩══╩═
                   0  1 
[ Simulator ]
Basic simulator result - shots: 2048
{'11': 2048}

reality - with noise 1/2/3:
{'00': 1,'01': 2,'10': 3,'11': 2042}

"""
