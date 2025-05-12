"""Tests for the _cv module."""

import cv2
import numpy as np

from colormap_tool import get_cv_colormaps


def test_get_cv_colormaps_mpl():
    """Test getting a matplotlib colormap for OpenCV."""
    # Get a matplotlib colormap
    cmap = get_cv_colormaps("viridis", "mpl")

    # Check that it has the correct format
    assert isinstance(cmap, np.ndarray)
    assert cmap.shape[0] == 256
    assert cmap.shape[1] == 1
    assert cmap.shape[2] == 3
    assert cmap.dtype == np.uint8


def test_get_cv_colormaps_cv():
    """Test getting an OpenCV colormap."""
    # Get an OpenCV colormap
    cmap = get_cv_colormaps("jet", "cv")

    # For OpenCV colormaps, we should get an integer constant
    if isinstance(cmap, int):
        # This is the case when cv2 is available
        assert cmap == cv2.COLORMAP_JET
    else:
        # If cv2 is not available, we should get a numpy array
        assert isinstance(cmap, np.ndarray)
        assert cmap.shape[0] == 256
        assert cmap.shape[1] == 1
        assert cmap.shape[2] == 3
        assert cmap.dtype == np.uint8


def test_get_cv_colormaps_dot_notation():
    """Test getting colormaps using dot notation."""
    # Get a matplotlib colormap
    cmap = get_cv_colormaps("mpl.viridis")

    # Check that it has the correct format
    assert isinstance(cmap, np.ndarray)
    assert cmap.shape[0] == 256
    assert cmap.shape[1] == 1
    assert cmap.shape[2] == 3
    assert cmap.dtype == np.uint8
