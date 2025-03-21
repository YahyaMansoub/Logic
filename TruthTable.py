from typing import List




def generate_truthh_table(A : List[str], s:str):
    # A is a list of variable names
    # s is a string representing a logical expression
    # returns a truth table for the logical expression
    
    n = len(A)
    table = []

    for i in range(2**n):
        row = []
        for j in range(n):
            row.append((i>>j)%2)
        table.append(row)
    
    print("Truth Table for", s)
    print()
    for i in A:
        print(i, end = " ")
    print()
    for i in range(n):
        print("-", end = " ")
    print()
    for row in table:
        for j in row:
            if (j == 0):
                print("F", end = " ")
            else:
                print("T", end = " ")
        print()
    
generate_truthh_table(["A", "B", "C"], "A and B or C")



