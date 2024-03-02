from qiskit import QuantumCircuit, transpile
from qiskit.providers.basic_provider import BasicSimulator
from lib.octopus_qiskit_tools import create_noise_dict, sum_noise_res_dict, print_histogram

DEBUG = True
NOISE = True
num_qubits = 5
num_bits = 5
SHOTS = 2048

secret_number = "11011"
slen = len(secret_number)

qc = QuantumCircuit(slen+1, slen)

qc.h(range(slen))
qc.x(slen)
qc.h(slen)

for _i, yesno in enumerate(reversed(secret_number)):
    if yesno == "1":
        qc.cx(_i,slen)

qc.barrier()
qc.h(range(slen))

qc.barrier()

qc.measure(range(slen),range(slen))

print(qc)

print("[ Simulator ]")
sim_backend = BasicSimulator()

job = sim_backend.run(transpile(qc, sim_backend), shots=SHOTS)
result = job.result()

print("Basic simulator result - shots:", SHOTS)
print(result.get_counts(qc))

if NOISE:
    print("--- addition of errors caused by a General noise")
    gn = create_noise_dict(5, 0.1, SHOTS)
    # print(gn)

    job = sim_backend.run(transpile(qc, sim_backend), shots=SHOTS)
    result = job.result()
    sim = result.get_counts(qc)

    final_sim = sum_noise_res_dict(gn, sim)

    print("Basic simulator result - shots:", SHOTS)
    print(final_sim)
    print_histogram(final_sim,log10=False)

"""
     ┌───┐                          ░ ┌───┐ ░ ┌─┐            
q_0: ┤ H ├───────■──────────────────░─┤ H ├─░─┤M├────────────
     ├───┤       │                  ░ ├───┤ ░ └╥┘┌─┐         
q_1: ┤ H ├───────┼────■─────────────░─┤ H ├─░──╫─┤M├─────────
     ├───┤       │    │             ░ ├───┤ ░  ║ └╥┘┌─┐      
q_2: ┤ H ├───────┼────┼─────────────░─┤ H ├─░──╫──╫─┤M├──────
     ├───┤       │    │             ░ ├───┤ ░  ║  ║ └╥┘┌─┐   
q_3: ┤ H ├───────┼────┼────■────────░─┤ H ├─░──╫──╫──╫─┤M├───
     ├───┤       │    │    │        ░ ├───┤ ░  ║  ║  ║ └╥┘┌─┐
q_4: ┤ H ├───────┼────┼────┼────■───░─┤ H ├─░──╫──╫──╫──╫─┤M├
     ├───┤┌───┐┌─┴─┐┌─┴─┐┌─┴─┐┌─┴─┐ ░ └───┘ ░  ║  ║  ║  ║ └╥┘
q_5: ┤ X ├┤ H ├┤ X ├┤ X ├┤ X ├┤ X ├─░───────░──╫──╫──╫──╫──╫─
     └───┘└───┘└───┘└───┘└───┘└───┘ ░       ░  ║  ║  ║  ║  ║ 
c: 5/══════════════════════════════════════════╩══╩══╩══╩══╩═
                                               0  1  2  3  4 


[ Simulator ]
Basic simulator result - shots: 2048
{'11011': 2048}



--- addition of errors caused by a General noise
Basic simulator result - shots: 2048
{'00000': 5, '00001': 5, '00010': 3, '00011': 3, '00100': 3, '00101': 6, '00110': 2, '00111': 1, '01000': 5, '01001': 1, '01010': 2, '01011': 5, '01100': 0, '01101': 5, '01110': 4, '01111': 2, '10000': 5, '10001': 2, '10010': 0, '10011': 1, '10100': 4, '10101': 5, '10110': 6, '10111': 2, '11000': 4, '11001': 4, '11010': 0, '11011': 2054, '11100': 2, '11101': 1, '11110': 5, '11111': 4}
00000:  5
00001:  5
00010:  3
00011:  3
00100:  3
00101:  6
00110:  2
00111:  1
01000:  5
01001:  1
01010:  2
01011:  5
01100:  0
01101:  5
01110:  4
01111:  2
10000:  5
10001:  2
10010:  0
10011:  1
10100:  4
10101:  5
10110:  6
10111:  2
11000:  4
11001:  4
11010:  0
11011: ################################################################################ 2023
11100:  2
11101:  1
11110:  5
11111:  4

"""
