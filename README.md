# Problem
Given a sequence (chain) of matrices with compatible dimensions A_1,A_2, ..., A_n to be multiplied, in what order should we parenthesize the matrices to minimize the total number of scalar multiplications needed to yield the result? Since matrix multiplication is associative, we can place parentheses anywhere. However, some ways of parenthesizing the sequence of matrices yield the product faster than other ways.

# Overview of project
In this project, I implemented in python two algorithms and analyzed their theoretical and empirical runtimes.
- Brute-Chain (Brute-Force)
- - This algorithm exhaustively checks all possible parenthesizations. It then returns the minimum number of multiplications done over all possible parenthesizations.

- Dynamic-Chain (Dynamic Programming)
- - This algorithm makes use of the type of problem we have, which has the optimal solution determined by finding optimal solutions of subproblems and many subproblems overlap. Thus, we use dynamic programming which stores the results of expensive computations for use again when the same computation needs to be run. In our case, as we look to find an optimal parenthesization, we will end up multiplying the same dimension matrices over and over.
\end{enumerate}