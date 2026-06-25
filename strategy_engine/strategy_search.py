# task : qubit 0 (economy) : |0> = sanctions, |1> = free trade
# qubit 1 (military) : |0> = arms race, |1> = peace treaty
# need to find the most optimal one (here) ; |11> using Grover Search Algorithm.

# to make circuit that helps narrow down to the most optimal strategy
from qiskit import QuantumCircuit

# to get state vector to calculate prob at each moment
from qiskit.quantum_info import Statevector

# to calculate amplitude n probability
import numpy as np


class OptimalStrategy:
    # custom constructor to initialize few req values eg. bilateral nations and the circuit that
    # decides the optimal strategy that helps improve bilateral relations
    def __init__(self, country_A, country_B):
        self.country_A = country_A
        self.country_B = country_B

        # since need to find optimal strategy based on 2 fields(economy & military) => 2 qubits
        self.self_interests = QuantumCircuit(2)

    def possible_scenarios(self):
        print(
            f"Calculating the possible outcomes of recent events btwn {self.country_A} & {self.country_B}"
        )
        print(f"|00> : Sanctions & Arms Race. (diplomatic failure)")
        print(f"|01> : Sanctions & Peace Treaty. (uneasy peace)")
        print(f"|10> : Free Trade & Arms Race. (unhealthy competition)")
        print(f"|11> : Free Trade & Peace Treaty. (aced the art of diplomacy)\n")


    # creating a oracle
    def create_oracle(self,on_qubits, oracle_name, gate):
        # create an oracle for 2-qubit system
        oracle = QuantumCircuit(len(on_qubits), name=oracle_name)


        # get the gate and apply to circuit using getattr() : flip phase of req scenario 
        gate_name = gate
        # ----oracle.cz-----------(0,1), since oracle:an obj, gate_name:a key, getattr(): return oracle.gate_name
        getattr(oracle, gate_name)(on_qubits[0],on_qubits[1])

        return oracle

    # querying oracle to mark the req scenario
    def query_oracle(self):
        '''mark the optimal sscenario (|11>) with -ive phase'''
        self.self_interests.barrier()

        print(f'Marking the optimal strategy using a -ive phase (no affect seen in Probablility yet)...')
        oracle = self.create_oracle([0,1], "Oracle", "cz")

        # => gate to add to circuit
        oracle_gate = oracle.to_gate()
        oracle_gate.name = "Oracle"

        # add to circiut on qubit 0&1
        self.self_interests.append(oracle_gate, [0,1])
        # draw updated circuit
        print(self.self_interests.draw())
        # get updated statevector
        ψ1 = Statevector(self.self_interests)
        print(ψ1.data)
        for scenario in ψ1.data:
            print(f"Probability of {scenario:.1f} = {np.pow(np.abs(scenario), 2)*100:.2f}%")

    
    def query_diffuser(self):
        '''Amplify marked state, destructively interference rest of the states'''
        self.self_interests.barrier()

        print('Amplifying the marked state....(Change in Probablility => interference happened)')

        # create a diffueser
        diffuser = QuantumCircuit(2, name="diffuser")

        # get avg of amplitudes in |00> using H-gate
        diffuser.h([0,1])
        # 00 => 11 to applly CZ
        diffuser.x([0,1])
        # flip avg state(11=>-11)
        diffuser.cz(0, 1)
        # -11 => -00
        diffuser.x([0,1])
        # H^2 = I => perform interference
        diffuser.h([0,1])

        diffuser_gate = diffuser.to_gate()
        diffuser_gate.name = "Diffuser/Amplifier"

        # add to circiut on qubit 0&1
        self.self_interests.append(diffuser_gate, [0,1])
        # draw updated circuit
        print(self.self_interests.draw())
        # get updated statevector
        ψ2 = Statevector(self.self_interests)
        print(ψ2.data)
        for scenario in ψ2.data:
            print(f"Probability of {scenario:.1f} = {np.pow(np.abs(scenario), 2)*100:.2f}%")


    def evaluate_results(self):
        '''Final Probablities'''
        print()
        print()
        print('\nOptimal Strategy')

        possible_scenarios = ["|00>", "|01>", "|10>", "|11>"]


        # get final state vector
        # draw updated circuit
        print(self.self_interests.draw())
        # get updated statevector
        ψ3 = Statevector(self.self_interests)
        print(ψ3.data)

        for scenario, amplitude in enumerate(ψ3.data):
            prob = np.pow(np.abs(amplitude), 2) * 100
            print(f"Probability of {possible_scenarios[scenario]} = {prob:.2f}%")

        print("\nQuantum Search Complete. Optimal path isolated.")


    def analyze(self):
        """initially brace for all 4 possible scenarios => put in superposn"""
        print(f"Evaluating the optimum strategy...")
        # apply h-gate
        self.self_interests.h([0, 1])
        # draw the circuit
        print(self.self_interests.draw())
        # get the state vector to understand results at this point
        ψ0 = Statevector(self.self_interests)
        # get data frm state vector
        print(ψ0.data)
        for scenario in ψ0.data:
            print(f"Probability of {scenario:.1f} = {np.pow(np.abs(scenario), 2)*100:.2f}%")


        # apply oracle to mark req scenario
        self.query_oracle()

        # apply diffuser, to perform interference
        self.query_diffuser()

        # get final results
        self.evaluate_results()




if __name__ == "__main__":
    war_room = OptimalStrategy("USA", "Iran")

    war_room.possible_scenarios()

    # start analyis
    war_room.analyze()

