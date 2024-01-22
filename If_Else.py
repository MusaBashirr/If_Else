#!/bin/python3

import math
import os
import random
import re
import sys



user_input=int(input("Enter An Integer:"))
results=(user_input%2)
if results == 1:
    print("Weird")
elif results == 0 and 2 <= user_input <= 5:
    print("Not weird")
elif results == 0 and 6 <= user_input <= 20:
    print("Weird")
else:
    print("Not Weird")


