"""Tests for the _mpl module."""

import matplotlib.pyplot as plt
import numpy as np
import pytest
from matplotlib.colors import Colormap

from colormap_tool import get_mpl_colormaps, register_all_cmps2mpl, uint8_rgb_arr2mpl_cmp
from colormap_tool._cv import get_cv_colormaps


@pytest.fixture
def no_show_plots(monkeypatch):
    """Prevent plots from being displayed during tests."""
    # Replace plt.show with a no-op function
    monkeypatch.setattr(plt, "show", lambda: None)
    yield
    # Close all figures to avoid memory leaks
    plt.close("all")


def test_get_mpl_colormaps_mpl():
    """Test getting a matplotlib colormap."""
    # Get a matplotlib colormap
    cmap = get_mpl_colormaps("viridis", "mpl")

    # Check that it's a matplotlib colormap
    assert isinstance(cmap, Colormap)
    assert cmap.name == "viridis"


def test_get_mpl_colormaps_cv():
    """Test getting an OpenCV colormap for matplotlib."""
    # Get an OpenCV colormap
    cmap = get_mpl_colormaps("jet", "cv")

    # Check that it's a matplotlib colormap
    assert isinstance(cmap, Colormap)
    assert "cv.jet" in cmap.name


def test_get_mpl_colormaps_dot_notation():
    """Test getting colormaps using dot notation."""
    # Get an OpenCV colormap
    cmap = get_mpl_colormaps("cv.jet")

    # Check that it's a matplotlib colormap
    assert isinstance(cmap, Colormap)
    assert "cv.jet" in cmap.name


def test_register_all_cmps2mpl():
    """Test registering all colormaps with matplotlib."""
    # Register all colormaps
    register_all_cmps2mpl()

    # Check that OpenCV colormaps are available in matplotlib
    assert "cv.jet" in plt.colormaps()

    # Test using a registered colormap
    cmap = plt.get_cmap("cv.jet")
    assert isinstance(cmap, Colormap)


@pytest.fixture
def test_image():
    """Create a linear gradient test image."""
    # Create a 1D linear gradient from 0 to 255
    gradient = np.linspace(0, 255, 256, dtype=np.uint8)
    # Expand to 2D image (256x256)
    return np.tile(gradient, (256, 1))


def test_uint8_rgb_arr2mpl_cmp_listed(test_image):
    """Test converting a uint8 RGB array to a matplotlib colormap (listed mode)."""
    arr_cmp = get_cv_colormaps("viridis", "mpl")
    arr_cmp = arr_cmp[:, :, ::-1]

    mpl_cmp = uint8_rgb_arr2mpl_cmp(arr_cmp, "test_cmap", alpha=1.0, mode="listed")

    ori_cmp = plt.get_cmap("viridis")

    assert isinstance(mpl_cmp, Colormap)
    assert isinstance(ori_cmp, Colormap)

    mpl_result = mpl_cmp(test_image)
    ori_result = ori_cmp(test_image)

    mpl_result = (mpl_result[:, :, :3] * 255).astype(np.uint8)
    ori_result = (ori_result[:, :, :3] * 255).astype(np.uint8)

    assert np.allclose(mpl_result, ori_result, atol=1)
