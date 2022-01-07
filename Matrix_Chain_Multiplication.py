# Author: Amish Mishra
# Date: April 19, 2021
# README: This file implements both algorithms, Brute Force and Dynamic programming, to solve the
# chain matrix multiplication problem

import numpy as np


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


if __name__ == '__main__':
    # Initialize variables
    num_matrices = 10
    p = list(np.random.randint(3, 10, size=(1, num_matrices+1)))[0]
    print(p)

    global brute_cost_matrix, brute_parentheses_matrix
    brute_cost_matrix = np.zeros((num_matrices, num_matrices))
    brute_parentheses_matrix = np.zeros((num_matrices-1, num_matrices))

    # Brute Chain
    brute_chain(p, 0, num_matrices-1)
    brute_optimal = brute_cost_matrix[0, num_matrices-1]

    # Dynamic Chain
    m, s = dynamic_chain(p)
    dynamic_optimal = m[0, num_matrices-1]

    # Print optimal parentheses and optimal solution for each
    print("Brute Force optimal parenthesization:")
    print_optimal_parens(brute_parentheses_matrix, 0, num_matrices-1)
    print("\nBrute Force optimal value:", brute_optimal)

    print("Dynamic optimal parenthesization:")
    print_optimal_parens(s, 0, num_matrices-1)
    print("\nDynamic optimal value:", dynamic_optimal)


