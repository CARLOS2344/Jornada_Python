from .moeda import aumento_porcentagem, diminuição_porcentagem, dobro_do_número, metade_do_número
from .moeda2 import resumo
import sys

import os 

caminho_absoluto = os.path.abspath(os.curdir)
sys.path.insert(0, caminho_absoluto)

print("Pacotes carregados!")