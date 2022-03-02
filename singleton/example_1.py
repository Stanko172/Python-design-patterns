class Singleton:
    __instance = None

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

    @staticmethod
    def getInstance():
        """ If the instance is None create a new one, else return the created instance """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

singleton = Singleton()
print("Call 1: ", singleton)
try:
    singleton2 = Singleton()
except Exception as exception:
    print(exception)
print("Call 2:", singleton.getInstance())