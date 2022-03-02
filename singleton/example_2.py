"""
Creating singleton with __new__ dunder method
"""

class SingletonClass:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls

print(SingletonClass)
print(SingletonClass)
SingletonClass.test = "Hello World!"
print(SingletonClass.test)