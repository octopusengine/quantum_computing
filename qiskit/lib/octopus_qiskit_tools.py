"""
OctopusLAB simple tools
(c) 2023-24

usage:
from lib.octopus_qiskit_tools import create_noise_dict, sum_noise_res_dict, print_histogram
...
"""

import random
import math

__version__ = "0.1"


# general "fake" noise
def create_noise_dict(bits=2, err=0.1, shots=512): # 0.1 = 10%
     nb = bits
     err = 0.1
     max_noise = int(shots/2**nb*err)
     n_bit_noise_dict = {format(i, '0{}b'.format(nb)): random.randint(0, max_noise) for i in range(2**nb)}
     return n_bit_noise_dict


# adding dict.
def sum_noise_res_dict(noise_dict, res_sim_dict):
     result_dict = {} #OrderedDict() # {}
     for key in set(noise_dict.keys()) | set(res_sim_dict.keys()):

          value = noise_dict.get(key, 0) + res_sim_dict.get(key, 0)
          result_dict[key] = value
          data_dict = dict(sorted(result_dict.items()))
     return data_dict


def print_histogram(data_dict, height = 80, log10=False):
     max_value = max(data_dict.values())         

     if log10:
          max_value = math.log10(max(data_dict.values())) 

     for key, value in sorted(data_dict.items()):
          if log10:
               normalized_value = int(float(math.log10(value)) / max_value) * height
          else:
               normalized_value = int(value / max_value * height)

          print(key + ': ' + "#" * normalized_value, value) # , normalized_value / chr(219)
