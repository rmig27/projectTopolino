import numpy as np


def propTF(uin_V_m, L_m, lambda_m, z_m):
    """
    1D Fresnel propagation using the transfer function (TF) method.

    Propagates a 1D complex field a distance ``z_m`` via the paraxial
    transfer function

    .. math::

        H(f_x) = \\exp(-i \\pi \\lambda z f_x^2)

    applied in the spatial-frequency domain.

    Parameters
    ----------
    uin_V_m : numpy.ndarray, shape (M,)
        Complex input field amplitude [V/m].
    L_m : float
        Physical length of the sampling window [m].
    lambda_m : float
        Optical wavelength [m].
    z_m : float
        Propagation distance [m].

    Returns
    -------
    uout_V_m : numpy.ndarray, shape (M,)
        Complex output field amplitude at distance ``z_m`` [V/m].

    Notes
    -----
    The TF method assumes the Fresnel approximation is valid and that the
    output window size equals the input window size (``L_m``).  It is
    accurate when the sampling criterion
    ``|z_m| >= L_m^2 / (M * lambda_m)`` is satisfied.
    """
    M = uin_V_m.size
    dx_m = L_m / M

    fx_1_m = np.linspace(-1 / (2 * dx_m), 1 / (2 * dx_m) - (1 / L_m), M)

    H = np.exp(-1j * np.pi * lambda_m * z_m * (fx_1_m**2))
    H = np.fft.fftshift(H)

    Uin_V_m = np.fft.fft(np.fft.fftshift(uin_V_m))
    Uout_V_m = H * Uin_V_m
    uout_V_m = np.fft.ifftshift(np.fft.ifft(Uout_V_m))
    return uout_V_m


def propTF2(uin_V_m, Lx_m, Ly_m, lambda_m, z_m):
    """
    2D Fresnel propagation using the transfer function (TF) method.

    Propagates a 2D complex field a distance ``z_m`` via the paraxial
    transfer function

    .. math::

        H(f_x, f_y) = \\exp(-i \\pi \\lambda z (f_x^2 + f_y^2))

    applied in the spatial-frequency domain.

    Parameters
    ----------
    uin_V_m : numpy.ndarray, shape (Ny, Nx)
        Complex input field amplitude [V/m].
    Lx_m : float
        Physical width of the sampling window along x [m].
    Ly_m : float
        Physical height of the sampling window along y [m].
    lambda_m : float
        Optical wavelength [m].
    z_m : float
        Propagation distance [m].

    Returns
    -------
    uout : numpy.ndarray, shape (Ny, Nx)
        Complex output field amplitude at distance ``z_m`` [V/m].

    Notes
    -----
    The TF method assumes the Fresnel approximation is valid and that the
    output window size equals the input window size (``Lx_m`` × ``Ly_m``).
    It is accurate when the sampling criterion
    ``|z_m| >= max(Lx_m, Ly_m)^2 / (min(Nx, Ny) * lambda_m)`` is satisfied.
    """
    Ny, Nx = uin_V_m.shape
    dx = Lx_m / Nx
    dy = Ly_m / Ny

    fx = np.fft.fftshift(np.fft.fftfreq(Nx, d=dx))
    fy = np.fft.fftshift(np.fft.fftfreq(Ny, d=dy))
    FX, FY = np.meshgrid(fx, fy)

    H = np.exp(-1j * np.pi * lambda_m * z_m * (FX**2 + FY**2))

    Uin = np.fft.fft2(np.fft.fftshift(uin_V_m))
    Uout = H * Uin
    uout = np.fft.ifftshift(np.fft.ifft2(Uout))
    return uout
