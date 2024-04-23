1) Prototype:
- Description: This pattern allows you to create new objects using an existing prototype object instead of creating a new object from scratch.
- Issues: Efficient copying of objects, which can reduce the load on the system when creating objects.

2) Factory Method:
- Description: A pattern that uses the factory method to create objects without specifying the specific class of that object.
- Issues: Ensuring flexibility when creating objects and separating the object creation code from the main business logic.

3) Strategy:
- Description: This pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable.
- Issues: Support for different algorithms or ways of performing actions depending on the context without having to change the main code.

4) Command (micro):
- Description: The command pattern allows encapsulating requests or operations in command objects, which allows you to pass requests as arguments, store the history of executed commands, and support reversal of operations.
- Issues: Ensuring interaction between objects that initiate requests and objects that execute them, as well as support for cancellation of operations and creation of composition of operations.
