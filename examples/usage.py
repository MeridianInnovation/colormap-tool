"""The script demonstrates the core features of the colormap-tool library.

Each function shows a specific use case, from basic colormap conversion
to more advanced features like registration and custom LUT generation.
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

import colormap_tool


def recipe_1_mpl_in_cv():
    """Recipe 1: Use a Matplotlib Colormap in OpenCV."""
    print("--- Running Recipe 1: Matplotlib in OpenCV ---")

    # Get the 'viridis' colormap in a format suitable for OpenCV
    lut = colormap_tool.get_cv_colormaps("mpl.viridis")

    # Create a sample grayscale image
    gray_img = np.arange(256, dtype=np.uint8).reshape(1, 256)
    gray_img = cv2.resize(gray_img, (512, 100), interpolation=cv2.INTER_NEAREST)

    # Apply the colormap
    colored_img = cv2.applyColorMap(gray_img, lut)

    # Display the result
    cv2.imshow("Matplotlib's Viridis in OpenCV", colored_img)
    print("Displaying Matplotlib's 'viridis' in an OpenCV window. Press any key to close.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("-------------------------------------------\n")


def recipe_2_cv_in_mpl():
    """Recipe 2: Use an OpenCV Colormap in Matplotlib."""
    print("--- Running Recipe 2: OpenCV in Matplotlib ---")

    # Get the OpenCV 'jet' colormap as a Matplotlib Colormap object
    cmap = colormap_tool.get_mpl_colormaps("cv.jet")

    # Create sample data
    data = np.random.rand(20, 20)

    # Use it in a plot
    plt.figure()
    plt.imshow(data, cmap=cmap)
    plt.title("OpenCV's Jet in Matplotlib")
    plt.colorbar()
    print("Displaying OpenCV's 'jet' in a Matplotlib plot.")
    plt.show()
    print("------------------------------------------\n")


def recipe_3_get_raw_rgb_data():
    """Recipe 3: Get Raw Colormap Data (RGB)."""
    print("--- Running Recipe 3: Get Raw RGB Data ---")

    # Get the 'viridis' colormap as a 128-entry RGB array
    rgb_lut = colormap_tool.get_colormaps("mpl.viridis", n=128)

    # rgb_lut is a (128, 3) numpy array with dtype=uint8
    print(f"Shape of the fetched RGB LUT: {rgb_lut.shape}")
    print(f"Data type of the fetched RGB LUT: {rgb_lut.dtype}")
    print("----------------------------------------\n")


def advanced_usage_register_all():
    """Advanced Usage: Registering All Colormaps with Matplotlib."""
    print("--- Running Advanced Usage: Registering All Colormaps ---")

    # Register all colormaps
    colormap_tool.register_all_cmps2mpl()
    print("All colormaps registered with Matplotlib.")

    # Now, you can use OpenCV colormaps directly by name
    data = np.random.rand(20, 20)
    plt.figure()
    plt.imshow(data, cmap="cv.jet")
    plt.title("Using a Registered OpenCV Colormap ('cv.jet')")
    plt.colorbar()
    print("Displaying registered 'cv.jet' in a Matplotlib plot.")
    plt.show()
    print("-------------------------------------------------------\n")


def advanced_usage_resample_lut():
    """Advanced Usage: Custom LUT Resampling."""
    print("--- Running Advanced Usage: Custom LUT Resampling ---")

    # Create a simple 2-color LUT (black to white)
    my_lut = np.array([[0, 0, 0], [255, 255, 255]], dtype=np.uint8)
    print(f"Original LUT shape: {my_lut.shape}")

    # Resample it to 10 entries
    resampled_lut = colormap_tool.resample_lut(my_lut, 10)
    print(f"Resampled LUT shape: {resampled_lut.shape}")
    print("--------------------------------------------------\n")


def advanced_usage_custom_cmap():
    """Advanced Usage: Converting a Custom RGB Array to a Matplotlib Colormap."""
    print("--- Running Advanced Usage: Custom Colormap ---")
    data = np.random.rand(20, 20)

    # Create a custom gradient from blue to yellow
    custom_rgb = np.zeros((256, 3), dtype=np.uint8)
    custom_rgb[:, 0] = np.linspace(0, 255, 256)  # R
    custom_rgb[:, 1] = np.linspace(0, 255, 256)  # G
    custom_rgb[:, 2] = np.linspace(255, 0, 256)  # B
    print("Created a custom blue-to-yellow gradient.")

    # Convert it to a Matplotlib Colormap object
    custom_cmap = colormap_tool.uint8_rgb_arr2mpl_cmp(custom_rgb, name="blue_yellow")

    # Use it in a plot
    plt.figure()
    plt.imshow(data, cmap=custom_cmap)
    plt.title("Custom Blue-Yellow Colormap")
    plt.colorbar()
    print("Displaying custom colormap in a Matplotlib plot.")
    plt.show()
    print("----------------------------------------------\n")


if __name__ == "__main__":
    recipe_1_mpl_in_cv()
    recipe_2_cv_in_mpl()
    recipe_3_get_raw_rgb_data()
    advanced_usage_register_all()
    advanced_usage_resample_lut()
    advanced_usage_custom_cmap()
    print("All examples finished.")
