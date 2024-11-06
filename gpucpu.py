from numba import njit
import numpy as np
from timeit import default_timer as timer

def cpufunction(matrix):
    n = matrix.shape[0]
    for i in range(n):
        matrix[i] += np.tanh(np.sin(i * np.pi) * np.cos(i * np.pi))

@njit
def gpufunction(matrix):
    n = matrix.shape[0]
    for i in range(n):
        matrix[i] += np.tanh(np.sin(i * np.pi) * np.cos(i * np.pi))

if __name__ == '__main__':
    N = 10_000_000
    a = np.zeros(N, dtype=np.float64)

    print(f'Start programu.')

    start = timer()
    cpufunction(a)
    print(f'Czas wykonania na CPU: {(timer() - start):.2f} s')

    start = timer()
    gpufunction(a)
    print(f'Czas wykonania na GPU: {(timer() - start):.2f} s')
