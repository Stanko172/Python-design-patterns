"""
Factory is a creational design pattern used to create concrete implementation of a common interface.
It separates the process of creating an object from the code that depends on the interface of the object.

For example, an application requires an object with a specific interface to perform its tasks.
The concrete implementation of the interface is identified by some parameter in a separate method / function

We can imagine this as a client - creator - product process. Client requests a concrete implementation
of a common interface(product) by passing some decision parameter to the creator. Creator creates a concrete
product based on that parameter and returns it to the client.
"""