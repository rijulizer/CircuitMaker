from logic_gates import LogicGates

class ALU:
    def __init__(self):
        self.lg = LogicGates()
    
    def half_adder(self, inp_a=None, inp_b=None):
        """
        Logically implements half_adder circuit 
        """
        if None in ([inp_a, inp_b]):
            raise KeyError("input to AND gate can not be None")
        if not(inp_a in ([0,1]) and inp_b in ([0,1])):
            raise KeyError("input to half_adder should be 0 or 1")
        sum = self.lg.XOR(inp_a, inp_b)
        carry = self.lg.AND(inp_a, inp_b)
        return (sum, carry)

if __name__=="__main__":
    alu = ALU()
    print(alu.half_adder(0,1), alu.half_adder(1,1))