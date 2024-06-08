# 1) Prototype:
- Description: This pattern allows you to create new objects using an existing prototype object instead of creating a new object from scratch.
- Issues: Efficient copying of objects, which can reduce the load on the system when creating objects.

--------------------------------

# 2) Factory Method:
- Description: A pattern that uses the factory method to create objects without specifying the specific class of that object.
- Issues: Ensuring flexibility when creating objects and separating the object creation code from the main business logic.

--------------------------------

# 3) Strategy:
- Description: This pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable.
- Issues: Support for different algorithms or ways of performing actions depending on the context without having to change the main code.

--------------------------------

# 4) Command (micro):
- Description: The command pattern allows encapsulating requests or operations in command objects, which allows you to pass requests as arguments, store the history of executed commands, and support reversal of operations.
- Issues: Ensuring interaction between objects that initiate requests and objects that execute them, as well as support for cancellation of operations and creation of composition of operations.

--------------------------------

# 5. Iterator
- Description: The Iterator pattern provides a way to sequentially access the elements of a collection without revealing its internal implementation. An iterator allows you to traverse a collection without depending on its structure (e.g., array, list, tree).
- Problems: Complicated lifecycle management: Iterators can hold references to objects, which affects memory management and potentially leads to memory leaks.

--------------------------------

# 6. Interpreter
- Description: The Interpreter pattern defines a grammar for a language and implements an interpreter for that language. It is used to evaluate expressions constructed from that grammar and is often used to create scripting languages or to process formal languages.
- Problems: The pattern is not suitable for complex grammars because each grammar rule requires its own class, which makes it difficult to maintain and extend.

--------------------------------

# 7. Memento
- Description: The Keeper pattern allows you to save and restore the previous state of an object without revealing its internal details. This is useful for implementing undo functionality.
- Problems: Saving large or frequently changed states can require a significant amount of memory.

--------------------------------

# 8. Adapter
- Description: The Adapter template allows objects with incompatible interfaces to work together. It acts as a bridge between two incompatible interfaces, allowing one object to use the functionality of the other. The adapter wraps the object and translates method calls from one interface to the other.
- Problems: Using an adapter adds another layer of abstraction, which can make it difficult to understand and maintain the code.
