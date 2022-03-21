# Para o Cython tem que ter esse arquivo para 
# mostrar quais módulos você quer compilar

from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(['computa.pyx'])
)

# apaga o __pycache__ que é onde fica os 
# arquivos compilados do python

# executa: python setup.py build_ext --inplace