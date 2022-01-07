# Problem
Given a sequence (chain) of matrices with compatible dimensions <A_1,A_2, ..., A_{n}>to be multiplied, in what order should we parenthesize the matrices to minimize the total number of scalar multiplications needed to yield the result? Since matrix multiplication is associative, we can place parentheses anywhere. However, some ways of parenthesizing the sequence of matrices yield the product faster than other ways.
\newline
\newline
\textbf{Input:} $p$, an array of length $n+1$ where $n$ is the number of matrices. $p$ has the dimensions of the matrices to be multiplied. So, $p[0]$ and $p[1]$ are the number of rows and columns of matrix $A_1$ respectively. Then, $p[1]$ and $p[2]$ are the number of rows and columns of matrix $A_2$, respectively. And so on and so forth.
\newline
\textbf{Output:} $m$ and $s$ where $m$ is the minimum number of scalar multiplications done for an optimal solution and $s$ contains the parenthesization of the matrices $\langle A_1,A_2, \dots, A_n\rangle$.

\section{Application}
A matrix can also be viewed as a linear transformation from one vector space, say $\R^n$ to another vector space $\R^k$. In finite dimensions, a linear transformation can be written as a matrix \cite{Chen}. Thus, when considering a sequence of linear transformations
    $$T_1T_2\dots T_n.$$
We may write them as a product of their associated matrices
    $$A_1A_2\dots A_n.$$
Computing such a product is a matrix chain multiplication problem.


\section{Algorithms}
In this project, I implemented and analyzed two algorithms:
\begin{enumerate}
    \item Brute-Chain (Brute-Force)
        \subitem This algorithm exhaustively checks all possible parenthesizations. It then returns the minimum number of multiplications done over all possible parenthesizations. This algorithm has a worst-case run-time of $\Omega(2^n)$ \cite{CLRS}. The pseudo-code in this report is adapted from R. Muhammad \cite{muhammad}.
    \item Dynamic-Chain (Dynamic Programming)
        \subitem This algorithm makes use of the type of problem we have, which has the optimal solution determined by finding optimal solutions of subproblems and many subproblems overlap. Thus, we use dynamic programming which stores the results of expensive computations for use again when the same computation needs to be run. In our case, as we look to find an optimal parenthesization, we will end up multiplying the same dimension matrices over and over. Thus, using a look-up table saves much computation time and brings the run-time down to $\Omega(n^3)$. This pseudo-code in this report is adapted from the CLRS book \cite{CLRS}.
\end{enumerate}