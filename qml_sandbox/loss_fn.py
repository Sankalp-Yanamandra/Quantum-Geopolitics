import numpy as np

def loss_score(model_guess, real_ans):
    '''Formula :mean squared error(MSE) for single guess'''

    # MSE
    score = np.pow(model_guess - real_ans, 2)

    return score

# testing grader
if __name__ == "__main__":
    # eg 1 : ai guess = 0.8 i.e. 80 % conflict, but real ans 1.0 (100% coflict happened)
    score_1 = loss_score(0.8, 1.0)
    print(f'Eg 1 : Loss (small mistake => small score => lesser punishment): {score_1:.3f}')

    # eg 2 : ai guess 0.1 (10% conflict) but real ans 1.0
    score_2 = loss_score(0.1, 1.0)
    print(f'Eg 2 : Loss (big mistake => big score => more punishment): {score_2:.3f}')
    