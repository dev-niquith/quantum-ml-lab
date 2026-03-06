from qiskit import QuantumCircuit
from qiskit.visualization import circuit_drawer

# Create a quantum circuit with 1 qubit
qc = QuantumCircuit(1)

# Apply Hadamard gate
qc.h(0)

# Draw the circuit
print(qc)
