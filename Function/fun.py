# # Example of a simple Python function with parameters
# def pyFunction_example(param1, param2):
#     print(f"Parameter 1: {param1}")
#     print(f"Parameter 2: {param2}")
#     return param1 + param2
# print(pyFunction_example(5, 10))

# # Function with multiple arguments one variable number of arguments
# def pyFunction_multiArgs(*args):
#     for index, value in enumerate(args):
#         print(f"Argument {index}: {value}")
#     return sum(args)
# print(pyFunction_multiArgs(1, 2, 3, 4, 5))

# # Function with default parameter values
# def pyFunction_defaultParams(a, b=10):
#     print(f"a: {a}, b: {b}")
#     print(f"Result: {a * b}")
#     return a * b
# print(pyFunction_defaultParams(5))

# Decorator example
# def decorator_example(func):
#    def wrapper(*args):
#         print("Before calling the function")
#         print(f"Arguments: {args}")
#         result = func(*args)
#         print("After calling the function")
#         print(f"Result: {result}")
#         return result
#    return wrapper

# @decorator_example
# def pyFunction_decorator(a, b):
#     print(f"a: {a}, b: {b}")
#     return a + b
# print(pyFunction_decorator(5, 10))

# import functools

# def changecase(func):
#   @functools.wraps(func)
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Have a great day!"

# print(myfunction.__name__)
# print(myfunction())

# labada function

x = lambda a : a + 10                                                                               
print(x(5))

thislambda = lambda a, b : a * b

print(thislambda(5, 10))