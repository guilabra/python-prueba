from Container_Number import Container_Number

class Bottles:

    def song(self):
        return self.verses(99,0)

    def verses(self, last, first):
        o = self.verse(last)
        for i in range (last-1, first-1, -1):
            o += "\n" + self.verse (i) 
        return o

    def verse(self, number = None):
        numero_actual= Container_Number(number)
        numero_anterior= Container_Number(number-1)
        if number == 0:
            return """No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.
"""
        else:
           return """{0} {3} of beer on the wall, {0} {3} of beer.
Take {4} down and pass it around, {1} {2} of beer on the wall.
""".format(number, numero_anterior.nomore(), numero_anterior.container(), numero_actual.container(), numero_actual.itone())


            
    
    
        
