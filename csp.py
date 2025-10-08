from typing import Dict, List 
from itertools import product 
from copy import deepcopy
class CSP: 
    def __init__(self, variables: List[str], domains: Dict[str, List[str]], constraints): 
        self.variables = variables 
        self.domains = domains 
        self.constraints = constraints 
         
    def solve(self): 
        assignments = {} 
        return self.backtrack(assignments) 
     
    def backtrack(self, assignments): 
        if len(assignments) == len(self.variables): 
            return assignments 
         
        var = self.select_unassigned_variable(assignments) 
        for value in self.order_domain_values(var, assignments): 
            new_assignments = deepcopy(assignments) 
            new_assignments[var] = value 
            if self.is_consistent(new_assignments): 
                result = self.backtrack(new_assignments) 
                if result is not None: 
                    return result 
         
        return None 
     
    def select_unassigned_variable(self, assignments): 
        for var in self.variables: 
