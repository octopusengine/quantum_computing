from qiskit import QuantumCircuit, transpile
from qiskit.providers.basic_provider import BasicSimulator


SHOTS = 2048  # 1024
num_qubits = 1
num_bits = 0
# Create a new circuit with two qubits (first argument) and two classical / bits (second argument)
qc = QuantumCircuit(num_qubits)

qc.h(0) # Add a Hadamard gate to qubit 0 - creates an equal superposition state...
##qc.cx(0, 1) # Perform a controlled-X gate on qubit 1, controlled by qubit 0

qc.measure_all() 

#qc.draw("mpl") / #qc.draw()
print("[ HG ] Hadamard gate")
print(qc)


print("[ Simulator ]")
sim_backend = BasicSimulator()

print("Basic simulator results: ")

for test5 in range(5):
    job = sim_backend.run(transpile(qc, sim_backend), shots=SHOTS)
    result = job.result()

    print(result.get_counts(qc))

"""
[ HG ] Hadamard gate
        ┌───┐ ░ ┌─┐
     q: ┤ H ├─░─┤M├
        └───┘ ░ └╥┘
meas: 1/═════════╩═
                 0 
[ Simulator ]
Basic simulator results: 
{'0': 1038, '1': 1010}
{'0': 1032, '1': 1016}
{'0': 1042, '1': 1006}
{'1': 1001, '0': 1047}
{'1': 1031, '0': 1017}

"""