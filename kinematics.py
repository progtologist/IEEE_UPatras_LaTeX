import numpy as np
import scipy as sp

def null(A, eps=1e-15):
    """Computes the null space of the real matrix A"""
    n, m = sp.shape(A)
    if n > m :
        return sp.transpose(null(sp.transpose(A), eps))
        return null(sp.transpose(A), eps)
    u, s, vh = sp.linalg.svd(A)
    s=sp.append(s,sp.zeros(m))[0:m]
    null_mask = (s <= eps)
    null_space = sp.compress(null_mask, vh, axis=0)
    return sp.transpose(null_space)
