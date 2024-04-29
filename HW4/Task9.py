# Напишите функцию для транспонирования матрицы

# Использование библиотек NumPy
"""
import numpy as np 

a = np.array([[1,2,3,],[4,5,6]])
b = a.transpose()
print(a)
print(b)
"""
# библиотеки SymPy
"""
import sympy

a = sympy.Matrix([[1,2,3,],[4,5,6]])
b = a.T
print(a)
print(b)
"""

# вложенные циклы
"""
Matrix = [[1,2], [3,4], [5,6]]
# print(Matrix)

trans_Matrix = [[0 for j in range(len(Matrix))] for i in range(len(Matrix[0]))]
# print(trans_Matrix)
for i in range(len(Matrix)):
    for j in range(len(Matrix[0])):
        trans_Matrix[j][i] = Matrix[i][j]
print(Matrix)   
print(trans_Matrix)
"""

# Zip 
"""
matrixZip = [[1,2], [3,4], [5,6]]
zipped_rows = zip(*matrixZip)
# print(matrixZip)
transpose_matrix = [list(row) for row in zipped_rows]
print(transpose_matrix)
"""
# Pymatrix
import pymatrix

matrix=pymatrix.matrix([[1,2,3], [4,5,6]])    
pymatrix_tranpose = matrix.trans()
print(matrix)
print(pymatrix_tranpose)
