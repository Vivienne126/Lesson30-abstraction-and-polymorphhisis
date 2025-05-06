class india():
    def capital(self):
        print("New delhi")
    def language(self):
        print("Hindi")
class USA():
    def capital(self):
        print("Washington")
    def language(self):
        print("English")
obj1=india()
obj2=USA()
for i in(obj1,obj2):
    i.capital()
    i.language()
