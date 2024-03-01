# simple examples

```
[ HG ] Hadamard gate
        ┌───┐ ░ ┌─┐
     q: ┤ H ├─░─┤M├
        └───┘ ░ └╥┘
meas: 1/═════════╩═



[ bc ] bell circuit
     ┌───┐     ┌─┐   
q_0: ┤ H ├──■──┤M├───
     └───┘┌─┴─┐└╥┘┌─┐
q_1: ─────┤ X ├─╫─┤M├
          └───┘ ║ └╥┘
c: 2/═══════════╩══╩═
                0  1 

```

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
