"""Test the format of the colormap pickle files."""

import numpy as np

from colormap_tool._cmps import CV_COLORMAPS, MPL_COLORMAPS


def test_mpl_colormaps_format():
    """Test that matplotlib colormaps have the correct format."""
    assert isinstance(MPL_COLORMAPS, dict), "MPL_COLORMAPS should be a dictionary"

    # Check at least one colormap exists
    assert len(MPL_COLORMAPS) > 0, "MPL_COLORMAPS should not be empty"

    # Check format of each colormap
    for name, cmap_array in MPL_COLORMAPS.items():
        assert isinstance(name, str), f"Colormap key should be a string, got {type(name)}"
        assert isinstance(cmap_array, np.ndarray), f"Colormap value should be a numpy array, got {type(cmap_array)}"
        assert cmap_array.shape[0] == 256, f"Colormap should have 256 entries, got {cmap_array.shape[0]}"
        assert cmap_array.ndim == 3, f"Colormap should be 3-dimensional, got {cmap_array.ndim}"
        assert cmap_array.shape[1] == 1, f"Second dimension should be 1, got {cmap_array.shape[1]}"
        assert cmap_array.shape[2] == 3, f"Third dimension should be 3 (RGB), got {cmap_array.shape[2]}"
        assert cmap_array.dtype == np.uint8, f"Colormap dtype should be uint8, got {cmap_array.dtype}"


def test_cv_colormaps_format():
    """Test that OpenCV colormaps have the correct format."""
    assert isinstance(CV_COLORMAPS, dict), "CV_COLORMAPS should be a dictionary"

    # Check at least one colormap exists
    assert len(CV_COLORMAPS) > 0, "CV_COLORMAPS should not be empty"

    # Check format of each colormap
    for name, cmap_array in CV_COLORMAPS.items():
        assert isinstance(name, str), f"Colormap key should be a string, got {type(name)}"
        assert isinstance(cmap_array, np.ndarray), f"Colormap value should be a numpy array, got {type(cmap_array)}"
        assert cmap_array.shape[0] == 256, f"Colormap should have 256 entries, got {cmap_array.shape[0]}"
        assert cmap_array.ndim == 3, f"Colormap should be 3-dimensional, got {cmap_array.ndim}"
        assert cmap_array.shape[1] == 1, f"Second dimension should be 1, got {cmap_array.shape[1]}"
        assert cmap_array.shape[2] == 3, f"Third dimension should be 3 (RGB), got {cmap_array.shape[2]}"
        assert cmap_array.dtype == np.uint8, f"Colormap dtype should be uint8, got {cmap_array.dtype}"
