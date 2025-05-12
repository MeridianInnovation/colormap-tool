"""Test colormap conversion between different libraries."""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import pytest

from colormap_tool import apply_colormap_with_numpy, get_cv_colormaps, get_mpl_colormaps


@pytest.fixture
def test_image():
    """Create a linear gradient test image."""
    # Create a 1D linear gradient from 0 to 255
    gradient = np.linspace(0, 255, 256, dtype=np.uint8)
    # Expand to 2D image (256x256)
    return np.tile(gradient, (256, 1))


def test_mpl_to_cv_conversion(test_image):
    """Test that matplotlib colormaps converted to OpenCV format produce correct results."""
    # Select a common colormap available in both libraries
    cmap_name = "viridis"

    # Get the matplotlib colormap in OpenCV format
    cv_cmap = get_cv_colormaps(cmap_name, "mpl")

    # Apply the colormap using OpenCV
    cv_result = cv2.applyColorMap(test_image, cv_cmap)
    cv_result = cv2.cvtColor(cv_result, cv2.COLOR_BGR2RGB)

    # Get the same colormap directly from matplotlib
    mpl_cmap = plt.get_cmap(cmap_name)

    mpl_result = mpl_cmap(test_image)
    mpl_result = mpl_result[:, :, :3]
    mpl_result = (mpl_result * 255).astype(np.uint8)

    # The results should be very close (allowing for small rounding differences)
    # Using a small tolerance for floating point and conversion differences
    assert np.allclose(cv_result, mpl_result, atol=1)


def test_cv_to_mpl_conversion(test_image):
    """Test that OpenCV colormaps converted to matplotlib format produce correct results."""
    # Select a common colormap available in both libraries
    cmap_name = "jet"

    # Get the OpenCV colormap in matplotlib format
    mpl_cmap = get_mpl_colormaps(cmap_name, "cv")

    mpl_result = mpl_cmap(test_image)

    # Convert matplotlib result to uint8 RGB for comparison with OpenCV result
    mpl_result = (mpl_result[:, :, :3] * 255).astype(np.uint8)

    # Get the same colormap directly from OpenCV
    cv_cmap = cv2.COLORMAP_JET

    # Apply the colormap using OpenCV
    cv_result = cv2.applyColorMap(test_image, cv_cmap)
    cv_result = cv2.cvtColor(cv_result, cv2.COLOR_BGR2RGB)

    # The results should be very close (allowing for small rounding differences)
    # Using a small tolerance for floating point and conversion differences
    assert np.allclose(cv_result, mpl_result, atol=1)


def test_apply_colormap_with_numpy(test_image):
    """Test applying a colormap using numpy."""

    # Get a colormap
    cmap = get_cv_colormaps("viridis", "cv", return_arr=True)

    cv_result = cv2.applyColorMap(test_image, cmap)

    np_result = apply_colormap_with_numpy(test_image, cmap)

    assert isinstance(cmap, np.ndarray)
    assert cmap.shape == (256, 1, 3)
    assert cmap.dtype == np.uint8

    assert np_result.shape == (256, 256, 3)
    assert np_result.dtype == np.uint8

    assert cv_result.shape == np_result.shape
    # The results should be the same
    assert np.allclose(cv_result, np_result, atol=1)
