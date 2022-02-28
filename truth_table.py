from math import pow
import re
from boolean_operations import And, If, Not,  Or, Varible
BOOLEAN_TOKENS = {
    "¬": Not(), 
    "~": Not(), 
    "!": Not(),

    "^": And(), 
    "&": And(), 
    "∧": And(), 
    "·": And(), 

    "v": Or(),
    "V": Or(),
    "||": Or(),
    "+":  Or(),
    "∨": Or(),

    "=>":If(),  
    "⇒": If(), 
    "→":If(), 
    "⊃": If(), 
}
class SymbolicExpression:
    def __init__(self, expression) -> None:
        self.expression = expression
        self.variables = set(re.findall(r"[a-uA-UW-Zw-z]", expression)) #Find all alphabetic characters that aren't v and save it as a set for individualization
    def truth_table(self): 
        truth_values = variable_truth_values(self.variables)
        print(self.variables, truth_values)

def variable_truth_values(variables):
        truth_values = []
        l = 2**len(variables)
        for i in range(l): 
            truth_values.append({})
        for e, var in enumerate(variables): 
            truth = True
            n = 2**((len(variables))-(e+1))
            m = n
            for i, dic in enumerate(truth_values): 
                dic[var] = truth
                if n <= i+1:
                    n += m
                    truth = not truth
        return truth_values 

expression = SymbolicExpression("(P^Q)v(¬P^(P v Q)v(P^Q))v(P^¬Q)v(¬P^¬Q)")
expression.truth_table()