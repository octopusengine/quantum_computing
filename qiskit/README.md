# simple examples

```
[ HG ] Hadamard gate / only (single) quibit in superposition
        ┌───┐ ░ ┌─┐
     q: ┤ H ├─░─┤M├
        └───┘ ░ └╥┘
meas: 1/═════════╩═

Basic simulator results: {'0': 1038, '1': 1010}
```
The Hadamard or Walsh-Hadamard gate, acts on a single qubit. It maps the basis states "1-0" (it creates an equal **superposition state** if given a computational basis state).

https://en.wikipedia.org/wiki/Quantum_logic_gate
---

```
[ bc ] bell circuit
     ┌───┐     ┌─┐   
q_0: ┤ H ├──■──┤M├───
     └───┘┌─┴─┐└╥┘┌─┐
q_1: ─────┤ X ├─╫─┤M├
          └───┘ ║ └╥┘
c: 2/═══════════╩══╩═
                0  1 
Basic simulator result: {'11': 269, '00': 243}
0 "collapse caused by measurement" > "teleport"
```
**Controlled** [x] gates act on 2 or more qubits, where one or more qubits act as a control for some operation.
For example, the controlled NOT gate (or CNOT or CX) acts on 2 qubits, and performs the NOT operation on the second qubit only when the first qubit is |1⟩, and otherwise leaves it unchanged. 

---
### roll of the eight-sided dice / randome "input test" generator

https://github.com/octopusengine/quantum_computing/blob/main/qiskit/example06_sim_8dice.py
```
     ┌───┐┌─┐      
q_0: ┤ H ├┤M├──────
     ├───┤└╥┘┌─┐   
q_1: ┤ H ├─╫─┤M├───
     ├───┤ ║ └╥┘┌─┐
q_2: ┤ H ├─╫──╫─┤M├
     └───┘ ║  ║ └╥┘
c: 3/══════╩══╩══╩═
           0  1  2 

[ Simulator ] roll of the eight-sided dice

---------------- (1 x 8000)
{'100': 1014, '110': 1002, '111': 930, '010': 992, '101': 1062, '011': 959, '000': 1023, '001': 1018}
---------------- (6 x 1)
{'000': 1}
{'000': 1}
{'111': 1}
{'010': 1}
{'001': 1}
{'101': 1}
```
