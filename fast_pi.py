#!/bin/env python3

from numba import njit
import random

## njit is like jit(nopython=True) - forces it to try fast mode, not object mode
@njit(cache=True)
def fast_pi(npoints): 
  n_in_circle = 0 
  for i in range(npoints):
    x = random.random()
    y = random.random()
    if (x**2+y**2 < 1):
      n_in_circle += 1
  return 4*n_in_circle / npoints

print(fast_pi(100000))


