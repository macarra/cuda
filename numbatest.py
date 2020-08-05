#!/bin/env python
import numba
from numba import cuda

import time
import numpy as np
print("Numba Version:",numba.__version__)
print("Checking for gpus:",cuda.gpus)

@cuda.jit
def create(data):
    data[cuda.blockIdx.x, cuda.threadIdx.x] = cuda.blockIdx.x

numBlocks = 4
threadsPerBlock = 6

data = np.ones((numBlocks, threadsPerBlock), dtype=np.uint8)
create[numBlocks, threadsPerBlock](data)
print(data)
