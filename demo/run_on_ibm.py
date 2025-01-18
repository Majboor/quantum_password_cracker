from qiskit import IBMQ, QuantumCircuit, transpile, assemble, execute
from qiskit.visualization import plot_histogram

# Load IBM Quantum account
IBMQ.load_account()

# Create a simple quantum circuit
qc = QuantumCircuit(2)
qc.h(0)  # Apply Hadamard gate to qubit 0
qc.cx(0, 1)  # Apply CNOT gate with control qubit 0 and target qubit 1
qc.measure_all()

# Choose a backend (real quantum computer)
provider = IBMQ.get_provider('ibm-q')
backend = provider.get_backend('ibmq_16_melbourne')  # Replace with your preferred backend

# Execute the circuit on the real quantum computer
job = execute(qc, backend)
result = job.result()

# Get and print the results
counts = result.get_counts(qc)
print("Measurement results:", counts)

# Plot the results
plot_histogram(counts)
