import numpy as np
from timeit import timeit


def np_concat():
    # Method 1:
    # Join a sequence of arrays along an existing axis.
    a = np.arange(10).reshape(2, -1)
    b = np.repeat(1, 10).reshape(2, -1)
    np.concatenate([a, b], axis=1)


def np_hstack():
    # Method 2:
    # Stack arrays in sequence horizontally (column wise).
    a = np.arange(10).reshape(2, -1)
    b = np.repeat(1, 10).reshape(2, -1)
    np.hstack([a, b])


def np_c():
    # Method 3:
    # Translates slice objects to concatenation along the second axis.
    a = np.arange(10).reshape(2, -1)
    b = np.repeat(1, 10).reshape(2, -1)
    np.c_[a, b]


if __name__ == "__main__":
    setup_method1 = "from __main__ import np_concat"
    setup_method2 = "from __main__ import np_hstack"
    setup_method3 = "from __main__ import np_c"
    print(timeit("np_concat()", setup=setup_method1))
    print(timeit("np_hstack()", setup=setup_method2))
    print(timeit("np_c()", setup=setup_method3))
