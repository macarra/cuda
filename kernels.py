#!/bin/env python3


from numba import cuda

@cuda.jit
def my_kernel1(io_array):
    """
    Code for kernel.
    """
    # code here
    
@cuda.jit
def my_kernel2(io_array):
    # Thread id in a 1D block
    tx = cuda.threadIdx.x
    # Block id in a 1D grid
    ty = cuda.blockIdx.x
    # Block width, i.e. number of threads per block
    bw = cuda.blockDim.x
    # Compute flattened index inside the array
    pos = tx + ty * bw
    if pos < io_array.size:  # Check array boundaries
        io_array[pos] *= 2 # do the computation

@cuda.jit
def my_kernel3(io_array):
    pos = cuda.grid(1)
    if pos < io_array.size:
        io_array[pos] = pos # do the computation


import numpy

# Create the data array - usually initialized some other way
data = numpy.ones(32)

# Set the number of threads in a block
threadsperblock = 8 

# Calculate the number of thread blocks in the grid
blockspergrid = (data.size + (threadsperblock - 1)) // threadsperblock

# Now start kernel 1
my_kernel1[blockspergrid, threadsperblock](data)
print(data)

# Now start kernel 2
my_kernel2[blockspergrid, threadsperblock](data)
print(data)

# Now start kernel 3
my_kernel3[blockspergrid, threadsperblock](data)
print(data)


