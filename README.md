# Formal Languages - Assignment 2: Subset Construction

## Student Information
- **Student Full Name:** Steven Granda Palencia - 1020110822
- **Class Number:** SI2002

## Environment & Requirements
- **Operating System:** Windows 11 / Linux
- **Programming Language:** Python 3.10+
- **Tools Used:** Standard Python Library (`sys`)

## Instructions for Running the Project

1. make sure you have Python 3 installed on your system. You can verify it by running:
   ```bash
   python3 --version

   ## Sample Test Case

### Input (`input.txt`)
```text
  1
  5
  3 5
  a b
  1 4
  1 {1 5} 0
  2 {1} 0
  3 {2 4} 0
  4 0 {5}
  5 {1 5} {4}
  
##Output 

Initial state: 1
Final states: 2 3 4 5
State	a	b
1	2	3
2	4	5
3	6	7
4	4	3
5	4	5
6	6	6

Algorithm ExplanationThe program implements the Subset Construction algorithm as described in Kozen (1997), Lecture 6. This algorithm translates a Non-Deterministic Finite Automaton (NFA) $N = (Q, \Sigma, \Delta, S, F)$ into an equivalent Deterministic Finite Automaton (DFA) $M = (Q', \Sigma, \delta', q_0', F')$.
