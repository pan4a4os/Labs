import re

class Expression:
    def interpret(self, context):
        pass

class Variable(Expression):
    def __init__(self, name):
        self.name = name

    def interpret(self, context):
        return context[self.name]

class And(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) and self.right.interpret(context)

class Or(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) or self.right.interpret(context)

class Not(Expression):
    def __init__(self, expression):
        self.expression = expression

    def interpret(self, context):
        return not self.expression.interpret(context)

class Parser:
    def parse(self, expression):
        tokens = re.findall(r'\w+|[&|!()]', expression)
        return self._parse_expression(tokens)

    def _parse_expression(self, tokens):
        if not tokens:
            raise ValueError("Empty expression")
        
        token = tokens.pop(0)
        
        if token.isalpha():
            left = Variable(token)
        elif token == '!':
            expression = self._parse_expression(tokens)
            left = Not(expression)
        elif token == '(':
            left = self._parse_expression(tokens)
            tokens.pop(0)
        else:
            raise ValueError(f"Unexpected token: {token}")
        
        if not tokens:
            return left
        
        token = tokens[0]
        
        if token in '&|':
            operator = tokens.pop(0)
            right = self._parse_expression(tokens)
            if operator == '&':
                return And(left, right)
            elif operator == '|':
                return Or(left, right)
        
        return left


context = {
    'A': True,
    'B': False,
    'C': True
}

expression = "A & (B | !C)"
parser = Parser()
parsed_expression = parser.parse(expression)
result = parsed_expression.interpret(context)
print(f"Result of expression '{expression}' is {result}")
