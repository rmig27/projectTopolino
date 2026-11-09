import numpy as np


def ft(t):
    """Centered 2D FFT: ifftshift → fft2 → fftshift."""
    return np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(t)))


def ift(t):
    """Centered 2D IFFT: ifftshift → ifft2 → fftshift."""
    return np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(t)))


def fs(t):
    """Frequency axis (cycles per unit) matching a centered spatial axis t."""
    N = len(t)
    df = 1 / (t[-1] - t[0])
    return np.fft.fftshift(
        np.array([df * n if n < N / 2 else df * (n - N) for n in range(N)])
    )


def setfreq(px_size_m, img_size_m):
    """
    Build spatial and frequency axes for a square image.

    Parameters
    ----------
    px_size_m : float
        Pixel size in metres.
    img_size_m : float
        Full image extent in metres.

    Returns
    -------
    dx_m, Dx_m, f_cpm, px_size_m, x_m, Nfft, df_cpm, Df_cpm
    """
    dx_m = px_size_m
    Dx_m = img_size_m
    x_m = np.linspace(-Dx_m / 2, Dx_m / 2, int(Dx_m / dx_m) + 1)
    f_sample = 1 / (x_m[1] - x_m[0])
    Nfft = len(x_m)
    df_cpm = f_sample / Nfft
    f_cpm = np.linspace(0, f_sample - df_cpm, Nfft) - (
        f_sample - np.mod(Nfft, 2) * df_cpm
    ) / 2
    df_cpm = f_cpm[1] - f_cpm[0]
    Df_cpm = f_cpm[-1] - f_cpm[0]
    return dx_m, Dx_m, f_cpm, px_size_m, x_m, Nfft, df_cpm, Df_cpm
