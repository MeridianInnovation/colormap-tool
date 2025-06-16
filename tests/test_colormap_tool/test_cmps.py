"""Tests for the _cmps module."""

import numpy as np
import pytest

from colormap_tool import CV_COLORMAPS, MPL_COLORMAPS, get_colormaps, resample_lut


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


def test_get_colormaps():
    """Test getting colormaps in RGB format."""
    # Test getting a matplotlib colormap with default length
    cmap = get_colormaps("viridis", "mpl")
    assert isinstance(cmap, np.ndarray)
    assert cmap.shape == (256, 3)
    assert cmap.dtype == np.uint8

    # Test getting an OpenCV colormap with custom length
    cmap = get_colormaps("jet", "cv", n=128)
    assert isinstance(cmap, np.ndarray)
    assert cmap.shape == (128, 3)
    assert cmap.dtype == np.uint8

    # Test dot notation
    cmap1 = get_colormaps("mpl.viridis")
    cmap2 = get_colormaps("viridis", "mpl")
    np.testing.assert_array_equal(cmap1, cmap2)

    # Test resampling
    cmap = get_colormaps("viridis", "mpl", n=64)
    assert cmap.shape == (64, 3)

    # Test error cases
    with pytest.raises(ValueError, match="Colormap nonexistent is not found in namespace mpl"):
        get_colormaps("nonexistent", "mpl")

    with pytest.raises(ValueError, match="Namespace nonexistent is not recognized"):
        get_colormaps("viridis", "nonexistent")

    with pytest.raises(ValueError, match="Namespace mpl is provided, so name mpl.viridis should not include a dot"):
        get_colormaps("mpl.viridis", "mpl")


def test_resample_lut():
    """Test LUT resampling functionality."""
    # Test with 2D input
    lut_2d = np.array([[0, 0, 0], [255, 255, 255]], dtype=np.uint8)
    resampled = resample_lut(lut_2d, 5)
    assert resampled.shape == (5, 3)
    assert resampled.dtype == np.uint8
    assert resampled[0].tolist() == [0, 0, 0]
    assert resampled[-1].tolist() == [255, 255, 255]

    # Test with 3D input
    lut_3d = lut_2d.reshape(-1, 1, 3)
    resampled = resample_lut(lut_3d, 5)
    assert resampled.shape == (5, 1, 3)
    assert resampled.dtype == np.uint8
    assert resampled[0, 0].tolist() == [0, 0, 0]
    assert resampled[-1, 0].tolist() == [255, 255, 255]

    # Test same length returns copy
    out = resample_lut(lut_2d, 2)
    assert out.shape == (2, 3)
    assert np.all(out == lut_2d)
    assert out is not lut_2d
    out3d = resample_lut(lut_3d, 2)
    assert out3d.shape == (2, 1, 3)
    assert np.all(out3d == lut_3d)
    assert out3d is not lut_3d

    # Test error cases

    with pytest.raises(ValueError):  # noqa: PT011
        resample_lut(np.zeros((5, 2), dtype=np.uint8), 5)  # Wrong number of channels
    with pytest.raises(ValueError):  # noqa: PT011
        resample_lut(np.zeros((5, 2, 3), dtype=np.uint8), 5)  # Wrong middle dimension
    with pytest.raises(ValueError):  # noqa: PT011
        resample_lut(np.zeros((5, 3, 1), dtype=np.uint8), 5)  # Wrong 3D shape
    with pytest.raises(ValueError):  # noqa: PT011
        resample_lut(np.zeros((5,), dtype=np.uint8), 5)  # 1D array
