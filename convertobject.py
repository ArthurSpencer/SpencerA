class binaryconverterholderthing():
    binaryarray = [0,0,0,0,0,0,0,0]
    denary = 0
    def __init__(self):
        pass

    def denarysetter(self, inputdenary):
        check = int(inputdenary)
        if check < -128 or check > 127:
            return False 
        self.denary = check
        self.denarytobinary()
        return True

    def denarytobinary(self):
        num = int(self.denary)
        i = 0
        if num < 0:
            num = 256 - abs(num) # or just do + num since will subtract anyway
        while num != 0:
            rem = num % 2
            num = num // 2
            self.binaryarray[i] = rem
            i = i + 1

mytwostatevariableobject = binaryconverterholderthing()

done = False
while not done:
    x = mytwostatevariableobject.denarysetter(input())
    if x:
        print(mytwostatevariableobject.binaryarray[::-1])
