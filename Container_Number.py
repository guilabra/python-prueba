class Container_Number:

    def __init__(self, number):
        self.number=number
    
    def container(self):
        if self.number==1:
            return "bottle";    
        else:
            return "bottles";
    
    def nomore(self):
        if self.number==0:
            return "no more";
        else:
            return self.number;
        
    def itone(self):
        if self.number==1:
            return "it";
        else:
            return "one";
