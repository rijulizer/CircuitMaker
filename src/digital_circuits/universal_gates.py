from math import prod

class UniversalGates:

    def __init__(self):
        pass

    def U_NAND(self, *inp):

        # Check if no arguments were provided
        if not inp:
            raise KeyError("input to NAND gate can not be Empty")
        
        # Check if non-binary inputs were provided
        else:
            for i in inp:
                if i not in ([0,1]):
                    raise KeyError("input to OR gate should be 0 or 1")
        
        # Perform logical NAND operation
        return 1-prod(inp)

    def U_NOR(self, *inp):

        # Check if no arguments were provided
        if not inp:
            raise KeyError("input to NOR gate can not be Empty")
        
        # Check if non-binary inputs were provided
        else:
            for i in inp:
                if i not in ([0,1]):
                    raise KeyError("input to NOR gate should be 0 or 1")
        
        # Perform logical NOR operation
        return (0 if sum(inp) > 0 else 1)
