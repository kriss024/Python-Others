import julia
julia.install()

from julia.api import Julia
jl = Julia(compiled_modules=False)

sin_90 = jl.eval("sin(90)")
print(f'sin(90) = {sin_90:.5f}')