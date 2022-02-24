from functools import reduce
import re
from boolean_operations import and_operation, not_operation, or_operation
def truth_table(expression):
    pattern = re.compile(r"[({[]([^(){}[\]]*?)[\]})]")
    return pattern.finditer(expression)

class SymbolicExpression:
    def __init__(self, expression) -> None:
        self.expression = expression
        self.variables = set(re.findall(r"[a-uw-zA-UW-Z]", expression)) #Find all alphabetic characters that aren't v and save it as a set for individualization
        self.connectors = {
            "¬": "not", 
            "~": "not", 
            "!": "not",

            "^": "and", 
            "·": "and",
            "∧": "and",
            "&": "and", 

            "v": "or", 
            "∨": "or",
            "V": "or", 
            "+": "or", 
            "||": "or", 
        }
    def truth_table(self): 
        truth_values = {key:True for key in self.variables}
        formula_list = re.findall(r"[({[](.+?)[(){}[\]]", self.expression) #Extract expressions between parentheses
        formula_symbols_list = [re.findall(r"\S", formula) for formula in formula_list]  #Individual symbols and variables
        parsed_formula_symbol_list = [list(map(lambda symbol: truth_values[symbol] if symbol in truth_values.keys() else self.connectors[symbol], formula)) for formula in formula_symbols_list]
        
                
  
expression = SymbolicExpression("(P^Q)v(¬P^(P v Q)v(P^Q))v(P^¬Q)v(¬P^¬Q)")
expression.truth_table()