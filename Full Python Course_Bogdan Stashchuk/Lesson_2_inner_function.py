# Some of the function:
# print() -> Can write to terminal some data
# type()
# id()
# len()
# sum()
# input() -> Enter some date from terminal -> push ENTER (input data all the time is String)
name = input('Enter your name: ')
print(name)


# round()
# min()
# max()
# int()
# str()
# bool()

# all functions:
# 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']


def my_fn(a, b):
    a = a + 1
    c = a + b
    return c


result = my_fn(2, 3)

print(result)
