# Write a program to print the documents (syntax, description etc) of Python built-in function(s)
# A docstring is a strign literal that occurs as the first statement in a module, function, class or method
# '__doc__' is a special attribute of that object
def get_docstring(built_in):
    return f'{built_in.__doc__}'


print(get_docstring(abs))