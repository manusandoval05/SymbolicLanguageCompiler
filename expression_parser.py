import re

def solve_negations(expression):
    pattern = re.compile(
            r"([¬~!])([A-Ua-uW-Zw-z])"
    )