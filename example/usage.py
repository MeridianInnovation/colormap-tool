#!/usr/bin/env python
"""Example usage of the colormap-tools package.

This file contains examples from the README.md file, organized into functions
that can be run individually or imported and tested.
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

import colormap_tool


def example_accessing_colormaps_separate_params():
    """Example of accessing colormaps using separate namespace and name parameters."""
    # Get a matplotlib colormap
    cmap_cv = colormap_tool.get_cv_colormaps("viridis", "mpl")
    print(f"Got matplotlib 'viridis' colormap for OpenCV: shape={cmap_cv.shape}, dtype={cmap_cv.dtype}")

    # Get an OpenCV colormap
    cmap_mpl = colormap_tool.get_mpl_colormaps("viridis", "cv")
    print(f"Got OpenCV 'viridis' colormap for matplotlib: {type(cmap_mpl).__name__}")


def example_accessing_colormaps_dot_notation():
    """Example of accessing colormaps using dot notation."""
    # Get a matplotlib colormap
    cmap_cv = colormap_tool.get_cv_colormaps("mpl.viridis")
    print(f"Got matplotlib 'viridis' colormap for OpenCV: shape={cmap_cv.shape}, dtype={cmap_cv.dtype}")

    # Get an OpenCV colormap
    cmap_mpl = colormap_tool.get_mpl_colormaps("cv.viridis")
    print(f"Got OpenCV 'viridis' colormap for matplotlib: {type(cmap_mpl).__name__}")


def example_using_colormaps_with_opencv(display=True):
    """Example of using colormaps with OpenCV."""
    # Get a matplotlib colormap for use with OpenCV
    cmap = colormap_tool.get_cv_colormaps("viridis", "mpl")

    # Create a sample grayscale image
    gray_img = np.random.randint(0, 255, (100, 100), dtype=np.uint8)

    # Apply the colormap
    colored_img = cv2.applyColorMap(gray_img, cmap)

    if display:
        # Display the image (note: OpenCV uses BGR format)
        colored_img_rgb = cv2.cvtColor(colored_img, cv2.COLOR_BGR2RGB)  # Convert to RGB for display
        cv2.imshow("Colored Image", colored_img_rgb)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def example_using_colormaps_with_matplotlib(display=True):
    """Example of using colormaps with matplotlib."""
    # Get an OpenCV colormap for use with matplotlib
    cmap = colormap_tool.get_mpl_colormaps("viridis", "cv")

    # Create a sample grayscale image
    gray_img = np.random.randint(0, 255, (100, 100), dtype=np.uint8)

    # Display the image with the colormap
    plt.figure(figsize=(6, 6))
    plt.imshow(gray_img, cmap=cmap)
    plt.colorbar(label="Value")
    plt.title("Image with OpenCV VIRIDIS colormap")

    if display:
        plt.show()


def example_registering_colormaps_with_matplotlib(display=True):
    """Example of registering colormaps with matplotlib."""
    # Register all colormaps with matplotlib
    colormap_tool.register_all_cmps2mpl()

    # Now you can use any colormap directly with matplotlib by name
    plt.figure(figsize=(12, 4))

    # Create a sample data array
    data = np.random.rand(20, 20)

    # Plot with different colormaps
    plt.subplot(121)
    plt.imshow(data, cmap="cv.jet")  # do not use cv.JET
    plt.title("OpenCV JET")
    plt.colorbar()

    plt.subplot(122)
    plt.imshow(data, cmap="viridis")  # do not use mpl.viridis
    plt.title("Matplotlib Viridis")
    plt.colorbar()

    plt.tight_layout()

    if display:
        plt.show()


def example_converting_rgb_arrays_to_matplotlib_colormaps(display=True):
    """Example of converting RGB arrays to matplotlib colormaps."""
    # Create a custom RGB array (256x3 uint8 values)
    rgb_data = np.zeros((256, 3), dtype=np.uint8)
    # Fill with a gradient from blue to red
    rgb_data[:, 0] = np.linspace(0, 255, 256)  # Red channel
    rgb_data[:, 2] = np.linspace(255, 0, 256)  # Blue channel

    # Convert to a matplotlib colormap
    custom_cmap = colormap_tool.uint8_rgb_arr2mpl_cmp(rgb_data, name="custom_blue_red", alpha=1.0, mode="linear")

    if display:
        # Use the custom colormap
        plt.figure(figsize=(6, 6))
        data = np.random.rand(20, 20)
        plt.imshow(data, cmap=custom_cmap)
        plt.colorbar(label="Value")
        plt.title("Custom Blue-Red Colormap")
        plt.show()


def run_all_examples():
    """Run all examples."""
    print("Running all examples...\n")

    print("\n1. Accessing Colormaps (Separate Parameters)")
    example_accessing_colormaps_separate_params()

    print("\n2. Accessing Colormaps (Dot Notation)")
    example_accessing_colormaps_dot_notation()

    print("\n3. Using Colormaps with OpenCV")
    example_using_colormaps_with_opencv()

    print("\n4. Using Colormaps with Matplotlib")
    example_using_colormaps_with_matplotlib()

    print("\n5. Registering Colormaps with Matplotlib")
    example_registering_colormaps_with_matplotlib()

    print("\n6. Converting RGB Arrays to Matplotlib Colormaps")
    example_converting_rgb_arrays_to_matplotlib_colormaps()


if __name__ == "__main__":
    run_all_examples()
