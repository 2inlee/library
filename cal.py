def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed!"
    return x / y

def evaluate_expression(expression):
    # Split the expression based on the four operators and capture the operators as well
    tokens = []
    start = 0
    for i, char in enumerate(expression):
        if char in "+-*/":
            tokens.append(expression[start:i])
            tokens.append(char)
            start = i + 1
    tokens.append(expression[start:])
    
    # First, handle multiplication and division
    i = 0
    while i < len(tokens):
        if tokens[i] == '*':
            tokens[i-1:i+2] = [multiply(float(tokens[i-1]), float(tokens[i+1]))]
            i -= 1
        elif tokens[i] == '/':
            result = divide(float(tokens[i-1]), float(tokens[i+1]))
            if isinstance(result, str):  # If there's an error message
                return result
            tokens[i-1:i+2] = [result]
            i -= 1
        i += 1
    
    # Then, handle addition and subtraction
    i = 0
    while i < len(tokens):
        if tokens[i] == '+':
            tokens[i-1:i+2] = [add(float(tokens[i-1]), float(tokens[i+1]))]
            i -= 1
        elif tokens[i] == '-':
            tokens[i-1:i+2] = [subtract(float(tokens[i-1]), float(tokens[i+1]))]
            i -= 1
        i += 1
    
    return tokens[0]

expression_input = "8*3+2/2+2"
result = evaluate_expression(expression_input)
print(result)
