# to perform math operations wherever req
import numpy as np

# quantum circuit clas to build quantum circuit
from qiskit import QuantumCircuit 

# state vector to store/get details from the circuit
from qiskit.quantum_info import Statevector

# class to handle diplomatic relation btwn 2 countries based on
# various parameters : eg. degree of tension(total peace/total conflict) etc

# btwn any 2 countries, 3 variables in the class : names of both countries and a quantum circuit that handles and calculates 
# updated state vector/relations status quo : SATE VECTOR (n-dimension for n qubits each representing a parameter/relation type)
# (eg. for trade relation, military relation, diaspora relation, conlict relation etc)
class DiplomaticRelations:
    # custom constructor to assign values : no need to now manually give amplitudes, Qiskit handles it
    def __init__(self, country_A, country_B):
        self.country_A = country_A
        self.country_B = country_B

        # creating a quantum circuit of 1 qubit that will apply events(matrices) on relations(qubit) to update relations
        # initially |0> i.e absolute peace
        self.relations_timeline = QuantumCircuit(1)

    # end of constructor


    # escalate_tension()
    def escalate_tension(self):
        '''Applies a EVENT : X-gate to the relations_timeline'''
        print(f'EVENT : X - gate')
        print(f'Diplomatic Event occurs btwn : {self.country_A} & {self.country_B}')
        # apply event
        self.relations_timeline.x(0) # since 1st qubit begins at index-0

    # high stakes meeting
    def delegation_lvl_meet(self):
        '''Apply a EVENT : H-gate => either causes superposn(randomness) or interference(if already H-gate applied before)'''
        print(f'EVENT : H-gate')
        print(f'High-stakes Meeting underway btwn : {self.country_A} & {self.country_B}')
        # apply event/gate/matrix
        self.relations_timeline.h(0) 


    # helper method, if not req, will remove later
    def check_status_quo(self):
        # get the state vector to store/get details of relations up until this moment
        state_till_now = Statevector(self.relations_timeline)
        # DRAW UPDATED CIRCUIT
        print(self.relations_timeline.draw())
        # draw updated state
        print(f'State : {state_till_now.data}')

        # return this state
        return state_till_now



    def get_hostility_status(self, state_vector):
        """calculate and return probabilities of given state vector"""

        # as a check 
        # find the norm
        vector_norm = np.sqrt( ( np.pow( np.abs(state_vector.data[0]) , 2) ) + np.pow( np.abs(state_vector.data[1]) , 2) ) 
        # normalize the amplitudes
        normalized_state_vector = np.array( (state_vector.data[0]/vector_norm , state_vector.data[1]/vector_norm) )

        # get probabilities
        prob_peace = np.pow(np.abs(normalized_state_vector[0]), 2) * 100
        
        prob_conflict = np.pow(np.abs(normalized_state_vector[1]), 2) * 100
        
        return prob_peace, prob_conflict

    # end of mtd

    def display_status_quo(self):
        """display a dashboard of current status of diplomacy"""
        # get the stats(prob) for : HOSTILITY STATUS
        p_peace, p_conflict = self.get_hostility_status(self.check_status_quo())
        
        # display
        print(f"Diplomatic Ties Status btwn : {self.country_A} & {self.country_B} : ")
        print(f"Probability of Peace : {p_peace:.3f}%")
        print(f"Probability of Conflict : {p_conflict:.3f}%")

    # end of mtd


# end of class

if __name__ == "__main__":
    print("Initializing Geopolitical Straategy Engine...\n")

    #  create an obj, relation btwn countries
    alliance = DiplomaticRelations("USA", "Iran")

    # introduce an event
    alliance.escalate_tension()
    # check relations status after this event
    alliance.display_status_quo()
    # again intro an event
    alliance.escalate_tension()
    alliance.display_status_quo()

    # event : meeting underway
    alliance.delegation_lvl_meet()
    # check relations status after meet
    alliance.display_status_quo()

    # event : meeting underway : INTERFERENCE
    alliance.delegation_lvl_meet()
    # check relations status after meet
    alliance.display_status_quo()

    # becomes 100% conflict
    alliance.escalate_tension()
    alliance.display_status_quo()

    # meeting to avoid conflict -> reduced to 50% conflict (relative phase introduced)
    alliance.delegation_lvl_meet()
    alliance.display_status_quo()

    # another meet to resolve differences, FAILS => again 100% conflict (interference)
    alliance.delegation_lvl_meet()
    alliance.display_status_quo()
