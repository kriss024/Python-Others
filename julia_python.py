import julia
julia.install()

from julia.api import Julia
jl = Julia(compiled_modules=False)

mass = 80

julia_code = f"""
mass = {mass}
G = 6.67
c = 2.99  
R =  (2 * G * mass) / (c^2)
"""

result = jl.eval(julia_code)
print(type(result))
print(f'result = {result:.6f}')
