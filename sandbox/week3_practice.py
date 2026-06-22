# Task : build a tiny 1-qubit circuit and apply H gates(twice) to watch the interference happen in real-time. 

# quantum circuit  class to build circuit
from qiskit import QuantumCircuit

# statevector class 
from qiskit.quantum_info import Statevector

# for finding amplitude
import numpy as np

print(f'Demonstarting interference')

# create a quantum circuit with 1 qubit (similar to python indexing from 0)
interference_demo = QuantumCircuit(1)

# pic of circuit
print(interference_demo.draw())


# state vector to measure at this point [similar to how we solved quantum circuit with psi1, psi2, ... to get final psi(i)]
state_1 = Statevector(interference_demo)  
# ∣ψ⟩=1∣0⟩+0∣1⟩ = |0>

# getting amplitudes rounded to 3 decimal places, from this state
print(f'Initially : ')
print(f'Amplitudes of |0> : {np.round(state_1[0].data,3)} Amplitudes of |1> : {np.round(state_1.data[1],3)}')
print(f'Probablility of |0> : {pow(abs(state_1.data[0]),2)*100}% Probablility of |1> : {pow(abs(state_1.data[1]),2)*100}%')

# pic of  state 1
print(state_1.draw())


# Qiskit default qubit in |0> (100% peace)=> apply 1st H gate
interference_demo.h(0)

# pic of circuit
print(interference_demo.draw())


# state vector to measure at this point [similar to how we solved quantum circuit with psi1, psi2, ... to get final psi(i)]
# qiskit.quantum_info.Statevector(data, dims=None) here parameter data = Data from which the statevector can be constructed. This can be either a complex vector, another statevector, a Operator with only one column or a QuantumCircuit or Instruction.
#  If the data is a circuit or instruction, the statevector is constructed by assuming that all qubits are initialized to the zero state.

state_2= Statevector(interference_demo)
# ∣ψ⟩=0.707∣0⟩+0.707∣1⟩
 
# getting amplitudes rounded to 3 decimal places, from this state
print(f'aFTER 1ST H gate : ')
print(f'Amplitudes of |0> : {np.round(state_2[0].data,3)} Amplitudes of |1> : {np.round(state_2.data[1],3)}')
print(f'Probablility of |0> : {pow(abs(state_2.data[0]),2)*100:.3f}% Probablility of |1> : {pow(abs(state_2.data[1]),2)*100:.3f}%')




# pic of state 2
print(state_2.draw())


# apply 2nd H gate
interference_demo.h(0)

# pic of circuit
print(interference_demo.draw())


# checking state vector after applying H gate again
state_3 = Statevector(interference_demo)
# ∣ψ⟩=1∣0⟩+0∣1⟩ = |0> , we get |0> back since H^2 = I (since H is unitary n hermitian both)

# getting amplitudes rounded to 3 decimal places, from this state
print(f'aFTER 2ND H gate : ')
print(f'Amplitudes of |0> : {np.round(state_3[0].data,3)} Amplitudes of |1> : {np.round(state_3.data[1],3)}')
print(f'Probablility of |0> : {pow(abs(state_3.data[0]),2)*100:.3f}% Probablility of |1> : {pow(abs(state_3.data[1]),2)*100:.3f}%')




# pic of state 3
print(state_3.draw())



