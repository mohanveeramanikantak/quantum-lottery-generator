from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def generate_quantum_number(bits: int = 8) -> int:
    circuit = QuantumCircuit(bits, bits)

    for i in range(bits):
        circuit.h(i)

    circuit.measure(range(bits), range(bits))

    simulator = AerSimulator()
    result = simulator.run(circuit, shots=1).result()
    counts = result.get_counts()

    binary_number = list(counts.keys())[0]
    decimal_number = int(binary_number, 2)

    return decimal_number