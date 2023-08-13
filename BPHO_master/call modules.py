import sys
import os
import matplotlib.pyplot as graphing
from openpyxl import load_workbook
import pandas
import turtle
import numpy
from tabulate import tabulate
import math
import matplotlib.pyplot as plt

path = os.path.abspath("Modules")
sys.path.append(path)

from C1 import Challenge1 #Challenge1()
from C2 import Challenge2 # Challenge2all()
from C3_IP import c3IP #c3IP()
from C3_OP import c3OP() #c3OP()
from C4_IP import c4IP() #c4IP()
from C4_OP import c4OP() #c4OP()
from C5 import Challenge5() #Challenge5()
from C6 import Challenge6() #Challenge6()
'''
RE: Challenge 7
For 2D versions call IP71(), OP71(), C71()
For 3D verisons call IP72(), OP72(), C72()
'''
from Modules import C7_IP #IP71()
from Modules import C7_OP #OP71()
from Modules import C7 #C71()
from Modules import C7_3D_IP #IP72()
from Modules import C7_3D_OP #OP72()
from Modules import C7_3D #C72()




