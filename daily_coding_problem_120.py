'''
This problem was asked by Microsoft.

Implement the singleton pattern with a twist. First, instead of storing one instance, 
store two instances. And in every even call of getInstance(), 
return the first instance and in every odd call of getInstance(), return the second instance.
'''

class DoubleSingleton():
    __instance_1 = None
    __instance_2 = None
    __count = 1

    @staticmethod 
    def getInstance():
        """ Static access method. """

        if DoubleSingleton.__instance_1 == None and DoubleSingleton.__instance_2 == None:
            DoubleSingleton()
            # on first, leave as 1
            
            return DoubleSingleton.__instance_1

        if DoubleSingleton.__count == 0:
            DoubleSingleton.__count = 1
            return DoubleSingleton.__instance_1
        else:
            DoubleSingleton.__count = 0
            return DoubleSingleton.__instance_2

    def getCount(self):
        return DoubleSingleton.__count

    def __init__(self):
        """ Virtually private constructor. """
        if DoubleSingleton.__instance_1 != None and DoubleSingleton.__instance_2 != None:
            raise Exception("This class is a singleton!")
        else:
            DoubleSingleton.__instance_1 = self
            DoubleSingleton.__instance_2 = self


# test

ds = DoubleSingleton.getInstance()
assert ds.getCount() == 1
ds = DoubleSingleton.getInstance()
assert ds.getCount() == 0

ds = DoubleSingleton.getInstance()
assert ds.getCount() == 1

ds = DoubleSingleton.getInstance()
assert ds.getCount() == 0

