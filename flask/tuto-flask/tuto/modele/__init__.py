import sys
import os
print(sys.path)
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
print(" gia ga",ROOT)
sys.path.append(os.path.join(ROOT, 'src'))
print(sys)

#from modele import *
#
#__all__=["modele"]
#from . import modele
#from ft_package.modele import *