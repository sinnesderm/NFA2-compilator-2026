# Formal Languages - Assignment 2: Subset Construction

## Student Information
- **Student Full Name:** Steven Granda Palencia - 1020110822
- **Class Number:** SI2002

## Environment & Requirements
- **Operating System:** Windows 11 / Linux
- **Programming Language:** Python 3.10+
- **Tools Used:** Standard Python Library (`sys`)

## Instructions for Running the Project

1. Make sure you have Python 3 installed on your system. You can verify it by running:
   ```bash
   python3 --version

   ## Sample Test Case

### TEST
```text
Input

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

Output

text
Initial state: 1
Final states: 2 3 4 5
State	a	b
1	2	3
2	4	5
3	6	7
4	4	3
5	4	5
6	6	6
```
## Algorithm Explanation

The program implements the Subset Construction algorithm described in Kozen (1997), Lecture 6. This algorithm converts a Non-Deterministic Finite Automaton (NFA) into an equivalent Deterministic Finite Automaton (DFA).

### Algorithm Steps:
1. Initial State: The initial state of the DFA is the set of initial states S of the NFA.
2. State Exploration: A queue is used to process reachable DFA states (where each DFA state is a set of NFA states).
3. Transition Function: For each set T of NFA states and each symbol in the alphabet, the new destination state in the DFA is the union of all reachable states from each state in T for that symbol.
4. New States: If the resulting set of states has not been seen before, it is added as a new DFA state and queued for processing.
5. Final States: A DFA state is marked as final if it contains at least one final state from the original NFA.
