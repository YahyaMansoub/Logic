from typing import List

def evaluate_expression(expression: str, variables: List[str], values: List[bool]) -> bool:
    """Evaluates the logical expression with given variable values."""
    local_dict = dict(zip(variables, values))
    return eval(expression, {"__builtins__": None}, local_dict)

def generate_truthh_table(A: List[str], s: str):
    """
    Generates and prints a truth table for the given logical expression.
    
    Args:
    A: List of variable names.
    s: Logical expression (Python-compatible).
    
    Returns:
    A list representing the truth table.
    """
    n = len(A)
    table = []

    print("Truth Table for:", s)
    print()

    
    for var in A:
        print(var, end=" ")
    print("|", s)  
    print("-" * (2 * n + len(s) + 3)) 

    
    for i in range(2**n):
        row = []
        for j in range(n):
            row.append((i >> (n - 1 - j)) % 2)  
        
        
        bool_values = [bool(val) for val in row]
        result = evaluate_expression(s, A, bool_values)

        
        table.append(row + [result])

        
        for j in row:
            print("T" if j else "F", end=" ")
        print("|", "T" if result else "F")

    return table

# Example Usage:
variables = ["A", "B"]
expression = "(A and not B) or (B and A)"

generate_truthh_table(variables, expression)


