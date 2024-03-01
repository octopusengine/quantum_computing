# Example showing how to draw a quantum circuit using Qiskit.
from qiskit import QuantumCircuit


def build_bell_circuit(): # Create the circuit
    """Returns a circuit putting 2 qubits in the Bell state."""
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    return qc


bc = build_bell_circuit()
print("[ bc ] bell circuit")
print(bc)

""""
print("[test draw]")
bc.draw()
"""

print("[ qc ] IBM hw")
qc = QuantumCircuit(2)
qc.h(0) 
# Perform a controlled-X gate on qubit 1, controlled by qubit 0
qc.cx(0, 1)

print(qc)
"""
[ bc ] bell circuit
     ┌───┐     ┌─┐   
q_0: ┤ H ├──■──┤M├───
     └───┘┌─┴─┐└╥┘┌─┐
q_1: ─────┤ X ├─╫─┤M├
          └───┘ ║ └╥┘
c: 2/═══════════╩══╩═
                0  1 


[ qc ] IBM hello world
     ┌───┐     
q_0: ┤ H ├──■──
     └───┘┌─┴─┐
q_1: ─────┤ X ├
          └───┘

"""


