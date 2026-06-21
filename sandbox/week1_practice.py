import numpy as np

# define the amplitudes : eg. take alpha = 1/root2 = beta
# alpha = 1 / np.sqrt(2)
# beta = 1 / np.sqrt(2)

alpha = 3/5
beta = 4/5

# state vector/qubit
qubit = np.array([alpha, beta])

# print(qubit)

# modulus squares i.e. |alpha|^2
prob_peace = pow(np.abs(qubit[0]),2)
prob_conflict = pow(np.abs(qubit[1]),2)

# printing the results

print(f'Probability of peace : {prob_peace * 100:.2f}%')
print(f'Probability of conflict : {prob_conflict * 100:.2f}%')

# verifying the basic principle of prob : sum of all prob = 1
prob_total = prob_peace + prob_conflict
print(f'Total Probablity of occurence : {prob_total*100:.2f}%')
