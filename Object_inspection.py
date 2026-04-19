def python_function(a, b=10, *args, c="default", **kwargs):
    """
    Perform a custom operation with a variety of parameter types.
    """
    pass

# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

help(python_function)

import inspect

sig = inspect.signature(python_function)

for name, param in sig.parameters.items():
    print(f"Name: {name}, Default: {param.default}")

# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

class PythonClass:
    def __dir__(self):
        return ["custom_attr1", "custom_attr2"]


obj = PythonClass()

for x in dir(obj):
  print(x)

print(type(obj))
