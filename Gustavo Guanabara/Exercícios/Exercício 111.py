import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Utilities.Utilidades_CV import moeda2

moeda2.resumo(500, 10, 18)