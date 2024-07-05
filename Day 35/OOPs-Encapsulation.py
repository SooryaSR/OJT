class myClass(object):
    def __init__(self):
        self.a = 123  # Public variable
        self._b = 123  # Protected variable (convention only)
        self.__c = 123  # Private variable

obj = myClass()

# Accessing public and protected variables is straightforward
print(obj.a)  # Output: 123
print(obj._b)  # Output: 123

# Accessing a private variable directly causes an error
# print(obj.__c)  # This would raise an AttributeError

# Correct way to access private variables using name mangling
class myClass(object):
    def __init__(self):
        self.__version = 22  # Private variable

    def getVersion(self):
        print(self.__version)

    def setVersion(self, version):
        self.__version = version

obj = myClass()
obj.getVersion()  # Output: 22
obj.setVersion(23)
obj.getVersion()  # Output: 23

# Accessing __version using name mangling
print(obj._myClass__version)  # Output: 23
