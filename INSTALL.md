# Installation Guide

## Prerequisites
1. Python 3.8 or higher
2. pip (Python package manager)

## Steps
1. Install Qiskit:
   ```bash
   pip install qiskit
   ```
2. Install Qiskit IBM Quantum Provider:
   ```bash
   pip install qiskit-ibm-provider
   ```
3. Set up your IBM Quantum account:
   - Sign up at [IBM Quantum Experience](https://quantum-computing.ibm.com/).
   - Get your API token from the IBM Quantum dashboard.
4. Save your IBM Quantum API token:
   ```bash
   echo 'YOUR_API_TOKEN' > ~/.qiskit/token
   ```
5. Run the demo:
   ```bash
   cd demo
   python demo_circuit.py
   ```
