# Author: Amish Mishra
# Date: April 19, 2021
# README: This file is used to check run-time of both algorithms for analysis and making tables/graphs

import numpy as np
import time
import matplotlib.pyplot as plt

def dynamic_chain(p):
    n = len(p)-1
    m = np.zeros((n, n))
    s = np.zeros((n-1, n))
    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i+l-1
            m[i-1, j-1] = np.infty
            for k in range(i, j):
                q = m[i-1, k-1] + m[k, j-1] + p[i-1]*p[k]*p[j]
                if q < m[i-1, j-1]:
                    m[i-1, j-1] = q
                    s[i-1, j-1] = k-1
    return m, s


def brute_chain(p, i, j): # format: brute_chain(p, 0, num_matrices-1)
    if i == j:
        brute_cost_matrix[i, j] = 0
    else:
        brute_cost_matrix[i, j] = np.infty
        for k in range(i, j):
            number_of_multiplications = brute_chain(p, i, k) + brute_chain(p, k+1, j) + p[i]*p[k+1]*p[j+1]
            if number_of_multiplications < brute_cost_matrix[i, j]:
                brute_cost_matrix[i, j] = number_of_multiplications
                brute_parentheses_matrix[i, j] = k
    return brute_cost_matrix[i, j]


def print_optimal_parens(s, i, j):
    # print(i,j)
    if i == j:
        print("A_"+str(i+1), end='')
    else:
        print("(", end='')
        print_optimal_parens(s, int(i), int(s[i,j]))
        print_optimal_parens(s, int(s[i,j]+1), int(j))
        print(")", end='')


# Initialize variables
min_matrix_len = 3
max_matrix_len = 20
start_num_matrices = 3
end_num_matrices = 16
num_trials_for_each_dim = 5
brute_final_time_array = [0]*(end_num_matrices-start_num_matrices)
dynamic_final_time_array = [0]*(end_num_matrices-start_num_matrices)

# Create time vectors for increasing sizes of chain
for num_matrices in range(start_num_matrices, end_num_matrices):
    brute_average_time_array = [0]*num_trials_for_each_dim
    dynamic_average_time_array = [0]*num_trials_for_each_dim
    for i in range(num_trials_for_each_dim):
        p = list(np.random.randint(min_matrix_len, max_matrix_len, size=(1, num_matrices + 1)))[0]
        # print("Dimensions sequence:", p)

        global brute_cost_matrix, brute_parentheses_matrix
        brute_cost_matrix = np.zeros((num_matrices, num_matrices))
        brute_parentheses_matrix = np.zeros((num_matrices - 1, num_matrices))

        # Brute Chain
        tic = time.time()
        brute_chain(p, 0, num_matrices - 1)
        brute_optimal = brute_cost_matrix[0, num_matrices - 1]
        brute_run_time = time.time() - tic
        brute_average_time_array[i] = brute_run_time

        # Dynamic Chain
        tic = time.time()
        m, s = dynamic_chain(p)
        dynamic_optimal = m[0, num_matrices - 1]
        dynamic_run_time = time.time() - tic
        dynamic_average_time_array[i] = dynamic_run_time
    brute_final_time_array[num_matrices - start_num_matrices] = np.mean(brute_average_time_array)
    dynamic_final_time_array[num_matrices - start_num_matrices] = np.mean(dynamic_average_time_array)

number_of_matrices_array = np.arange(start_num_matrices-1, end_num_matrices-1, 1)

# Dump to csv
np.savetxt("empirical_brute_vs_dynamic.csv", np.transpose([number_of_matrices_array, brute_final_time_array, dynamic_final_time_array]), delimiter=",")

# Plot Empirical Brute vs Empirical Dynamic
fig1 = plt.figure(figsize=(8,4))
plt.plot(number_of_matrices_array, brute_final_time_array, color='b', label='Brute-Chain')
plt.plot(number_of_matrices_array, dynamic_final_time_array, color='r', label='Dynamic-Chain')

# Naming the x-axis, y-axis and the whole graph
plt.xlabel("Number of Matrices")
plt.ylabel("Time (seconds)")
plt.title("Empirical Run-time Comparison\nof Brute-Chain and Dynamic-Chain")
plt.xticks(np.arange(min(number_of_matrices_array), max(number_of_matrices_array)+1, 1))

# Adding legend, which helps us recognize the curve according to it's color
plt.legend()

# Plot Empirical Brute vs Predicted Brute
fig2 = plt.figure(figsize=(8,4))
c_brute = 0.00019458149327
brute_theoretical_complexity = np.power(2, number_of_matrices_array)
brute_predicted_rt = c_brute*brute_theoretical_complexity
plt.plot(number_of_matrices_array, brute_final_time_array, color='b', label='Empirical Brute')
plt.plot(number_of_matrices_array, brute_predicted_rt, '--', color='b', label='Predicted Brute')
plt.xlabel("Number of Matrices")
plt.ylabel("Time (seconds)")
plt.title("Brute-Chain Run-time Comparison\nEmpirical vs. Predicted")
plt.xticks(np.arange(min(number_of_matrices_array), max(number_of_matrices_array)+1, 1))
plt.legend()


# Plot Empirical Dynamic vs Predicted Dynamic
fig3 = plt.figure(figsize=(8,4))
c_dynamic = 2.38353169340492*10**-7
dynamic_theoretical_complexity = np.power(number_of_matrices_array, 3)
dynamic_predicted_rt = c_dynamic*dynamic_theoretical_complexity
plt.plot(number_of_matrices_array, dynamic_final_time_array, color='b', label='Empirical Dynamic')
plt.plot(number_of_matrices_array, dynamic_predicted_rt, '--', color='b', label='Predicted Dynamic')
plt.xlabel("Number of Matrices")
plt.ylabel("Time (seconds)")
plt.title("Dynamic-Chain Run-time Comparison\nEmpirical vs. Predicted")
plt.xticks(np.arange(min(number_of_matrices_array), max(number_of_matrices_array)+1, 1))
plt.legend()

# To load the display window
plt.show()

# # Print optimal parentheses and optimal solution for each
# print("Brute Force optimal parenthesization:")
# print_optimal_parens(brute_parentheses_matrix, 0, dim-1)
# print("\nBrute Force optimal value:", brute_optimal)
#
# print("Dynamic optimal parenthesization:")
# print_optimal_parens(s, 0, dim-1)
# print("\nDynamic optimal value:", dynamic_optimal)


