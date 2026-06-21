import numpy as np

# class to handle diplomatic relation btwn 2 countries based on
# various parameters : eg. degree of tension(total peace/total conflict) etc


# btwn any 2 countries, 3 variables in the class : names of both countries and list
# of parameters/state_vectors
# (eg. for trade relation, military relation, diaspora relation, conlict relation etc)
class DiplomaticRelations:
    # custom constructor to assign values
    def __init__(self, country_A, country_B, alpha, beta):
        self.country_A = country_A
        self.country_B = country_B

        # now based on values of alpha, beta:
        # NORMALIZATION to ensure Probability sum = 1
        norm_of_vector = np.sqrt(pow(abs(alpha), 2) + pow(abs(beta), 2))

        normalized_alpha = alpha / norm_of_vector
        normalized_beta = beta / norm_of_vector

        # state vector
        self.degree_of_tension = np.array([normalized_alpha, normalized_beta])

    # end of constructor

    def get_probability(self):
        """calculate and return probabilities of state vectors"""
        prob_peace = pow(abs(self.degree_of_tension[0]), 2) * 100
        prob_conflict = pow(abs(self.degree_of_tension[1]), 2) * 100
        return prob_peace, prob_conflict

    # end of mtd

    def display_status_quo(self):
        """display a dashboard of current status of diplomacy"""
        # get the stats(prob)
        p_peace, p_conflict = self.get_probability()
        # display
        print(f"Diplomatic Status btwn : {self.country_A} & {self.country_B} : ")
        print(
            f"Quantum state vector : [{self.degree_of_tension[0]:.3f}, {self.degree_of_tension[1]:.3f}]"
        )
        print(f"Probability of Peace : {p_peace:.3f}%")
        print(f"Probability of Conflict : {p_conflict:.3f}%")

    # end of mtd


# end of class

if __name__ == "__main__":
    print("Initializing Geopolitical Straategy Engine...\n")

    #  create an obj, relation btwn countries = highly unstable i.e. conflict chance > peace(alpha <<< beta)
    alliance = DiplomaticRelations("USA", "Iran", alpha=0.54, beta=0.99)

    alliance.display_status_quo()
