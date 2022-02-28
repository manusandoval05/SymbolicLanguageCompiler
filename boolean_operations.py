class And: 
    def __init__(self) -> None:
        self.left = None
        self.right = None
    def compile(self): 
        return self.left and self.right
class Or:
    def __init__(self) -> None:
        self.left = None
        self.right = None
    def compile(self): 
        return self.left or self.right
class If:
    def __init__(self) -> None:
        self.left = None
        self.right = None
    def compile(self): 
        return False if self.left and not self.right else True

class Not: 
    def __init__(self) -> None:
        self.right = None
    def compile(self): 
        return not self.right
class Varible:
    def __init__(self, value) -> None:
        self.value = value
        