"""
Singleton is an object which can be created only once during program lifetime
He has a static method which return the same cached object
"""


class Singleton:
    __instance = None
    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This is a singleton!")
        else:
            Singleton.__instance = self
    @staticmethod
    def get_instance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance


singleton = Singleton()
print("Call 1: ", singleton)
try:
    singleton2 = Singleton()
except Exception as exception:
    print(exception)
print("Call 2:", singleton.get_instance())