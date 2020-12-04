import numpy as np


a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)

# Method 1:
# Join a sequence of arrays along an existing axis.
np.concatenate([a, b], axis=1)

# Method 2:
# Stack arrays in sequence horizontally (column wise).
np.hstack([a, b])

# Method 3:
# Translates slice objects to concatenation along the second axis.
np.c_[a, b]
