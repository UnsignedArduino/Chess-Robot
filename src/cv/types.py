from typing import Any

from cv2 import UMat
from numpy import dtype, generic, ndarray

CV2NumpyImage = UMat | ndarray[Any, dtype[generic]] | ndarray
