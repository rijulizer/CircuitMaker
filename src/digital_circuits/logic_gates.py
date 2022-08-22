from math import prod


class LogicGates:
    def __init__(self):
        pass
    
    def NOT(self, *inp):
        """
        Logically implements not gate without using the python not()
        """
        # Check if no arguments were provided
        if not inp:
            raise KeyError("input to NOT gate can not be Empty")

        # Check if multiple inputs were provided
        if len(inp) > 1:
            raise KeyError("NOT gate only accepts a single input")
        
        # Check if non-binary inputs were provided
        if inp[0] not in ([0,1]):
            raise KeyError("input to NOT gate should be 0 or 1")

        # Perform logical NOT operation
        return 1-inp[0]

        # Using universal gates
        # return self.ug.U_NAND(inp[0])
    
    def AND(self, *inp):
        """
        Logically implements and gate, without using the python and(), and by mimicking how AND works 
        """
        if not inp:
            raise KeyError("input to AND gate can not be Empty")
        
        # Check if non-binary inputs were provided
        for i in inp:
            if i not in ([0,1]):
                raise KeyError("input to AND gate should be 0 or 1")

        # Perform logical AND operation
        return prod(inp)

        # Using universal gates
        # return self.ug.U_NAND(self.ug.U_NAND(inp))

    def OR(self, *inp):
        """
        Logically implements or gate, without using the python or(), and by mimicking how OR works 
        """
        if not inp:
            raise KeyError("input to OR gate can not be Empty")
        
        # Check if non-binary inputs were provided
        for i in inp:
            if i not in ([0,1]):
                raise KeyError("input to OR gate should be 0 or 1")

        # Perform logical OR operation
        return (1 if sum(inp) > 0 else 0)

        # Using universal gates
        # return self.ug.U_NOR(self.ug.U_NOR(inp))

    def NAND(self, inp_a=None, inp_b=None):
        """
        Logically implements nand gate 
        """
        if None in ([inp_a, inp_b]):
            raise KeyError("input to NAND gate can not be None")
        if not(inp_a in ([0,1]) and inp_b in ([0,1])):
            raise KeyError("input to NAND gate should be 0 or 1")

        return self.NOT(self.AND(inp_a, inp_b))
    
    
    def NOR(self, inp_a=None, inp_b=None):
        """
        Logically implements nor gate 
        """
        if None in ([inp_a, inp_b]):
            raise KeyError("input to NOR gate can not be None")
        if not(inp_a in ([0,1]) and inp_b in ([0,1])):
            raise KeyError("input to NOR gate should be 0 or 1")

        return self.NOT(self.OR(inp_a, inp_b))
    
    def XOR(self, *inp):
        """
        Logically implements xor gate, by mimicking how XOR works 
        """
        if not inp:
            raise KeyError("input to XOR gate can not be Empty")
        
        # Check if non-binary inputs were provided
        for i in inp:
            if i not in ([0,1]):
                raise KeyError("input to XOR gate should be 0 or 1")

        # Perform logical XOR operation
        return sum(inp)%2
