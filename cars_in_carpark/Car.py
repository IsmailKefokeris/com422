
class Car:

    def __init__(self, reg_num):
        self.reg_num = reg_num

    def __repr__(self):
        return f"Reg Num: {self.reg_num}"