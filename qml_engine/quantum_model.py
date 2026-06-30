# to defiine paramter/variable
from qiskit.circuit import Parameter
# to create a qunatum circuit
from qiskit import QuantumCircuit
class QuantumNeuralNetwork:
    # custom constructor
    def __init__(self):
        # define a variable/parameter to store classical  I/P data
        # eg. X our i/p data in context of tension aspect
        self.x = Parameter('x (i/p data)')
        # define a variable/paramter to store weight
        # eg. theta => knob AI will twist n turn
        self.theta = Parameter('θ (Weight)')

        # create a 1-qubit circuit
        self.quantum_circuit = QuantumCircuit(1) # index from 0

        # build a basic steup to train model
        self.build_circuit()

    def build_circuit(self):
        '''creating the architecture for Quantum Neural N/W'''

        # Part 1 : Feature Map (encode data into quantum gate)
        # qubit 0 in superposn
        self.quantum_circuit.h(0)

        # for I/P data => rotate qubit 0 about z-axis with an angle = 'x' => encode this data into a qunatum state
        self.quantum_circuit.rz(self.x, 0)

        self.quantum_circuit.barrier()

        # part 2 : ansatz(calculated guess) => rotate qubit 0 about x-axis with an angle 'theta'
        self.quantum_circuit.rx(self.theta, 0)

        # both x and thetha in perpendicular axes

    def display_architecture(self):
        print(f'Quantum Neural Network')
        print(self.quantum_circuit.draw())

if __name__ == "__main__":
    qnn = QuantumNeuralNetwork()
    qnn.display_architecture()