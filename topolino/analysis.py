import numpy as np
from skimage.transform import warp_polar


def azimuthal_avg(data_2d):
    """
    Azimuthal average of a 2D square image.

    Parameters
    ----------
    data_2d : 2D ndarray
        Square array (intensity or amplitude).

    Returns
    -------
    1D ndarray
        Radial profile from centre to edge (length = floor((N+1)/2) - 1).
    """
    Np = int(np.floor((len(data_2d) + 1) / 2))
    return np.sum(warp_polar(data_2d), axis=0)[: Np - 1]


def circsum(field):
    """
    Radial power spectrum via azimuthal sum of |field|².

    Parameters
    ----------
    field : 2D ndarray
        Complex or real field.

    Returns
    -------
    1D ndarray
    """
    return np.sum(warp_polar(np.abs(field) ** 2), axis=0)
