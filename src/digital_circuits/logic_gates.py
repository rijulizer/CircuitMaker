class LogicGates:
    def __init__(self):
        pass
    
    def NOT(self, inp= None):
        """
        Logically implements not gate without using the python not()
        """
        if inp in ([None]):
            raise KeyError("input to NOT gate can not be None")
        if inp == 0:
            return 1
        elif inp ==1:
            return 0
        else:
            raise KeyError("input to NOT gate should be 0 or 1")
    
    def AND(self, inp_a=None, inp_b=None):
        """
        Logically implements and gate, without using the python and(), and by mimicking how AND works 
        """
        if None in ([inp_a, inp_b]):
            raise KeyError("input to AND gate can not be None")
        if inp_a == 0:
            if inp_b == 0:
                return 0
            if inp_b == 1:
                return 0
            else:
                raise KeyError("input to AND gate should be 0 or 1")
        elif inp_a == 1:
            if inp_b == 0:
                return 0
            if inp_b == 1:
                return 1
            else:
                raise KeyError("input to AND gate should be 0 or 1")
        else:
            raise KeyError("input to AND gate should be 0 or 1")

    def OR(self, inp_a=None, inp_b=None):
        """
        Logically implements or gate, without using the python or(), and by mimicking how OR works 
        """
        if None in ([inp_a, inp_b]):
            raise KeyError("input to OR gate can not be None")
        if inp_a == 0:
            if inp_b == 0:
                return 0
            if inp_b == 1:
                return 1
            else:
                raise KeyError("input to OR gate should be 0 or 1")
        elif inp_a == 1:
            if inp_b == 0:
                return 1
            if inp_b == 1:
                return 1
            else:
                raise KeyError("input to OR gate should be 0 or 1")
        else:
            raise KeyError("input to OR gate should be 0 or 1")

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
    
    def XOR(self, inp_a=None, inp_b=None):
        """
        Logically implements xor gate, by mimicking how XOR works 
        """
        if None in ([inp_a, inp_b]):
            raise KeyError("input to XOR gate can not be None")
        if inp_a == 0:
            if inp_b == 0:
                return 0
            if inp_b == 1:
                return 1
            else:
                raise KeyError("input to XOR gate should be 0 or 1")
        elif inp_a == 1:
            if inp_b == 0:
                return 1
            if inp_b == 1:
                return 0
            else:
                raise KeyError("input to XOR gate should be 0 or 1")
        else:
            raise KeyError("input to XOR gate should be 0 or 1")