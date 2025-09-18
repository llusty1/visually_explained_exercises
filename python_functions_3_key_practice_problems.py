# Problem 1
# It's important to assign return values to variables if you'd like to use them later in your program
# What will be the output of the following code?


def greet(name):
    return "Hello " + name

greeting = greet("Alice")
greeting = greet("Bob")
print(greeting)

# Problem 2
# The return value of on function call can be used as an argument to another function call.
# What will this code output?

def add(a, b):
    return a + b

result = add(5, 10)
print(result)
print(add (result, 20))

# Problem 3 
# Python allows us to use multiple return statements inside a function.
# What will this code output?

def compute(a, b):
    result = a * b
    if result > 10:
        return result - 3
    return result + 4
    
print(compute(3, 2))
print(compute(5, 3))