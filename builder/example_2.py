"""
Here we give more control to the builder.
Also using product properties instead creating separate classes for all parts.
"""

class Car:
    def __init__(self, wheels = None, engine = None, body = None):
        self.wheels = wheels
        self.engine = engine
        self.body = body

    def specification(self):
        print("body: %s" % self.body)
        print("engine horsepower: %s" % self.engine)
        print("tire size: %s\'" % ' '.join(self.wheels))

class JeepBuilder:
    def __init__(self):
        self.jeep = Car()

    def set_wheels(self, wheel):
        self.jeep.wheels = [str(wheel) for _ in range(4)]

    def set_body(self, body):
        self.jeep.body = body

    def set_engine(self, engine):
        self.jeep.engine = engine

class Director:
   builder = None

   def setBuilder(self, builder):
      self.builder = builder

   def getCar(self):
       self.builder.set_body("some body...")
       self.builder.set_engine("some engine...")
       self.builder.set_wheels(22)

       return self.builder.jeep



def main():
   jeepBuilder = JeepBuilder() # initializing the class

   director = Director()

   # Build Jeep
   print("Jeep")
   director.setBuilder(jeepBuilder)
   jeep = director.getCar()
   jeep.specification()
   print("")

if __name__ == "__main__":
   main()