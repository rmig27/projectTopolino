import numpy as np

from .fourier import ft, ift, fs
from .propagation import propTF


def gaussian(x, mean, fwhm):
    """
    1D Gaussian parameterised by FWHM.

    Parameters
    ----------
    x : array_like
        Evaluation points (any units).
    mean : float
        Centre (same units as x).
    fwhm : float
        Full width at half maximum (same units as x).

    Returns
    -------
    ndarray
    """
    sigma = fwhm / (2 * np.sqrt(2 * np.log(2)))
    return np.exp(-((x - mean) / (np.sqrt(2) * sigma)) ** 2)


def rms_width(field, x):
    """
    RMS width of a 1D field distribution.

    Parameters
    ----------
    field : array_like
        Complex or real field (intensity is |field|²).
    x : array_like
        Spatial axis (same length as field).

    Returns
    -------
    float
        RMS width in the same units as x.
    """
    x = np.asarray(x)
    I = np.abs(field) ** 2
    I = I / I.sum()
    xc = np.sum(I * x)
    return np.sqrt(np.sum(I * (x - xc) ** 2))


def generate_speckle(dx_m, Dx_m, z_m, fwhm_m=500e-6, lambda_m=1e-6, fc_cpm=1e6, wfe_w=1 / 20):
    """
    Simulate a speckle intensity pattern after free-space propagation.

    Parameters
    ----------
    dx_m : float
        Pixel size in metres.
    Dx_m : float
        Field extent in metres.
    z_m : float
        Propagation distance in metres.
    fwhm_m : float
        Beam FWHM at the source plane (metres).
    lambda_m : float
        Wavelength (metres).
    fc_cpm : float
        Speckle spatial-frequency cutoff (cycles per metre).
    wfe_w : float
        Wavefront error amplitude in waves (peak-to-valley).

    Returns
    -------
    I : 2D ndarray
        Intensity at the output plane.
    """
    x_m = np.linspace(-Dx_m / 2, Dx_m / 2, int(np.ceil(Dx_m / dx_m)))
    N = len(x_m)
    X_m, Y_m = np.meshgrid(x_m, x_m)

    f_cpm = fs(x_m)
    Fx, Fy = np.meshgrid(f_cpm, f_cpm)

    GFILT = gaussian(Fx, 0, fc_cpm) * gaussian(Fy, 0, fc_cpm)

    noise = np.random.randn(N, N)
    noise_filt = np.abs(ift(ft(noise) * GFILT))
    noise_filt = noise_filt / np.std(noise_filt)

    E0 = gaussian(X_m, 0, fwhm_m) * gaussian(Y_m, 0, fwhm_m)
    E1 = E0 * np.exp(1j * 2 * np.pi * noise_filt * wfe_w)

    E2 = propTF(E1, Dx_m, lambda_m, z_m)
    return np.abs(E2) ** 2
