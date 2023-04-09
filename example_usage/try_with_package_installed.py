import numpy as np
from numpy.linalg import norm
from numpy.matrixlib import asmatrix
from verbose_chainsaw.nonnegdef import get_n_by_n

size = 20
dodeca = get_n_by_n(size)
true_matrix = asmatrix(dodeca)
epsilon = true_matrix - true_matrix.H
print(f'Frobenius norm of M - M^H : {norm(epsilon)}')


nonzeros = np.count_nonzero(true_matrix)

low_tri = np.tril(true_matrix)
nonzeros_in_lt = np.count_nonzero(low_tri)

delta_low_tri = np.tril(epsilon)
nonzeros_in_epsilon_lt = np.count_nonzero(delta_low_tri)

print(f'There are {nonzeros} non-zero elements in the generated matrix')
print(f'There are {nonzeros_in_lt} non-zero elements in the lower triangular-masked matrix')
print(f'There are {nonzeros_in_epsilon_lt} non-zero elements in lower triangular-masked epsilon (= M - M^H)')

# there is an excess of modulus if we only care about elements are unique.
#  many elements which by definition may have unique values in full generality are counted in the Frobenius norm of M

# To be precise, $\matr{M}_{\epsilon} = \matr{M}-\matr{M}^H$
print(f'Frobenius norm of the lower triangle of M - M^H : {norm(delta_low_tri)}')
print(f'Note that the ratio is the additive inverse of the calculated value for the upper triangular, namely {nonzeros_in_lt}/{nonzeros} = 1 - 19/40')