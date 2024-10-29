import numpy as np


def gaussian1d_kernel(k, sigma):
    """
    Creates 1-dimensional gaussian kernel with kernel size 'k' and a variance of 'sigma'
    """
    ax = np.linspace(-(k - 1) / 2.0, (k - 1) / 2.0, k)
    kernel = np.exp(-0.5 * np.square(ax) / np.square(sigma))
    return kernel / np.sum(kernel)


def gaussian2d_kernel(k, sigma):
    """
    Creates 2-dimensional gaussian kernel with kernel size 'k' and a variance of 'sigma'.

    NOTE: k MUST be odd.
    """
    if k % 2 == 0:
        print("Error: k MUST be odd.")
        return None

    ax = np.linspace(-(k - 1) / 2.0, (k - 1) / 2.0, k)
    gauss = np.exp(-0.5 * np.square(ax) / np.square(sigma))
    kernel = np.outer(gauss, gauss)
    return kernel / np.sum(kernel)


def motion_blur_kernel(k):
    """
    Creates motion blur kernel with kernel size 'k'
    """
    kernel_motion_blur = np.zeros((k, k))

    for i in range(k):
        kernel_motion_blur[i, k - i - 1] = 1

        if i > 0:
            kernel_motion_blur[i, k - i] = 0.5
        if i < k - 1:
            kernel_motion_blur[i, k - i - 2] = 0.5
    kernel_motion_blur = kernel_motion_blur / np.sum(kernel_motion_blur)
    return kernel_motion_blur


def gaussian_noise(y, noise_level):
    r"""
    Samples and returns a realization of Gaussian noise with the same shape of y, with norm equal to noise_level * || y ||_2.
    """
    # Sample noise
    e = np.random.normal(loc=0, scale=1, size=y.shape)

    # Normalize
    e = e / np.linalg.norm(e.flatten())

    # Scale
    e = noise_level * np.linalg.norm(y.flatten()) * e
    return e
