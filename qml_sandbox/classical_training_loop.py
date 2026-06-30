
import numpy as np

def classical_training_loop():
    '''a simple training loop to predict hostility based on tanks.'''

    # dataset : i/p : tanks, ans : hostility

    # let 2 tanks historically showed 80% hostility i.e 0.8 ans
    data = 2
    real_ans = 0.8

    # initializing weight randomly
    weight = 0.1

    # distance covered by 1 step to go downhill => learning rate => smaller the  better
    learning_rate = 0.05

    print(f'Started Training, Initial Wt. = {weight}, Real Answer : {real_ans}')

    # training loop => twisting  and turning of knobs(weights and bias) based on loss score until loss score =0
    # epoch : 1 pass in process of training a model=> lets take 20 epochs
    for epoch in range(1,21):
        # model make a guess
        ai_guess = weight * data

        # loss score using MEan Squared Error(MSE)
        loss_score = np.pow((ai_guess - real_ans), 2)

        # slope calculation for loss score
        slope = 2 * (ai_guess - real_ans) * data

        # updated weight
        weight = weight - (slope * learning_rate)
        print(f'Epoch : {epoch} | Model\'s guess : {ai_guess} | Loss_Score : {loss_score:.5f} | New Weight : {weight}')


if __name__ == "__main__":
    classical_training_loop()