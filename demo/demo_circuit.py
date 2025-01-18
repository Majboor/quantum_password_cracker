from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Create a simple quantum circuit
qc = QuantumCircuit(2)
qc.h(0)  # Apply Hadamard gate to qubit 0
qc.cx(0, 1)  # Apply CNOT gate with control qubit 0 and target qubit 1
qc.measure_all()

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator).result()

# Get and print the results
counts = result.get_counts(qc)
print("Measurement results:", counts)

# Plot the results
plot_histogram(counts)
