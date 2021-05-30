# class parent:
#     parentAttr = 100
#     def __init__(self):
#         print('calling parent constructor')
#     def parentMethod (self):
#         print('calling parent method')
#     def setAttr(self, attr):
#         parent.parentAttr = attr
#     def getAttr(self):
#         print('parent attr =', parent.parentAttr)

# class child(parent):
#     def __init__(self):
#         print('calling child construktor') 
#     def childMethod(self):
#         print('calling child method')


# c = child()
# c.childMethod()
# c.parentMethod()
# c.setAttr(100)
# c.getAttr()

# # overading method

# # sebenernya gua belum pasti maksudnya apa, nanti gw cari tau oke
# class orangtua:
#     def apakke(self):
#         print('calling parent method')

# class anak(orangtua):
#     def apakke(self):
#         print('calling child method')

# c = anak()
# c.apakke()

# class vector:
#     def __init__(self, a, b): # konstruktor dengan beberapa argumen
#         self.a = a
#         self.b = b
#     def __str__(self):
#         return 'vector (%d, %d) '%(self.a, self.b) # untuk mencetak string
#     def __add__(self, other):
#         return vector(self.a + other.a, self.b + other.b)
    
# v1 = vector(2,10)
# v2 = vector(5,-2)
# print(v1+v2)

class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount +=1
        print(self.__secretCount)
counter = JustCounter()
counter.count()
counter.count()
print(counter.__secretCount)

    

