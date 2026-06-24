# Let's prove this exact phenomenon using Qiskit.
# We are going to build a 2-qubit system (representing 4 geopolitical scenarios).
# We will use a special Oracle that marks the 11 scenario, 
# prove that the probability is still exactly 25%,
# and then use an interference block (called a Diffuser) to boost it to 100%.


# to create a quantum circuit
from qiskit import QuantumCircuit

# to get statevector to get info from circuit at this moment
from qiskit.quantum_info import Statevector

#  for modulus, power etc math operations on state vectors
import numpy as np

print('Simulating Oracle and Diffusion operations for Quantum Search concept...')

# create a 2 qubit-system

oracle_diffuser_demo = QuantumCircuit(2) # similar to python 0-based inddexing so qubit 1 on indexx 0 and qubit 2 on index 1

#  draw the circuit
print(oracle_diffuser_demo.draw())

# get state vector for ψ0
ψ0 = Statevector(oracle_diffuser_demo)

print('1. initialzed the system')
# get data from state vector
print(ψ0.data)
# get amplitudes/probablilites : initially in state |00> (default in qiskit)
for state in ψ0.data:
    print(f'Probablility for {state} : {np.pow(np.abs(state),2)*100:.2f}%')

print('2. Initial Superposn')

# a vertical line separting each ψi state
oracle_diffuser_demo.barrier() 

oracle_diffuser_demo.h([0,1])


#  draw the circuit
print(oracle_diffuser_demo.draw())

# get state vector for ψ1
ψ1 = Statevector(oracle_diffuser_demo)

# get data from state vector
print(ψ1.data)
# get amplitudes/probablilites : in superposn
for state in ψ1.data:
    print(f'Probablility for {state} : {np.pow(np.abs(state),2)*100:.2f}%')

print('THe oRacle : phase flip of correct ans (here |11> state)')

oracle_diffuser_demo.barrier()
# since phase flip : Z gate but sincce 2 qubitss so CZ gate
oracle_diffuser_demo.cz(0,1) # control bit on 0 qubit and target bit on qubit 1

#  draw the circuit
print(oracle_diffuser_demo.draw())

# get state vector for ψ2
ψ2 = Statevector(oracle_diffuser_demo)

# get data from state vector
print(ψ2.data)
# get amplitudes/probablilites : still in superposn but  relative phase intorduced , no change in proabablility/amplitude
for state in ψ2.data:
    print(f'Probablility for {state} : {np.pow(np.abs(state),2)*100:.2f}%')
print(f'Oracle marked the req state with relative phase (but we are blind to it)')

oracle_diffuser_demo.barrier()


# Diffusion -> Inteference -> Amplitude Amplification about average of ampltudes => H-gate to get avg, stored in |00> state
# => Flip |00> state to flip phase of average(act as mirror)[X-gate :00 to 11 => Cz on 11 => X gate : 11 to 00] => H-gate to cause amplification
print('3. DIFFUSER(Ampltiude Amplifying/ interference)')

# get avg in |00>
oracle_diffuser_demo.h([0,1])

# flip phase of avg
oracle_diffuser_demo.x([0,1]) # 00 => 11
oracle_diffuser_demo.cz(0, 1) # 11 => -11
oracle_diffuser_demo.x([0,1]) # 11 => 00

# inteference to reduce prob all states except 11 to 0 and make 11 100%, H^2 = I (relative phase)
oracle_diffuser_demo.h([0,1])

#  draw the circuit
print(oracle_diffuser_demo.draw())

# get state vector for ψ3
ψ3 = Statevector(oracle_diffuser_demo)

# get data from state vector
print(ψ3.data)
# get amplitudes/probablilites : only |11> state remains
for state in ψ3.data:
    print(f'Probablility for {state} : {np.pow(np.abs(state),2)*100:.2f}%')
print(f'Interference caused wrongs ans to destructively interfere and right ans to constructively interfere.')

