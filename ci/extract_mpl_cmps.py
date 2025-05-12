import pickle
from pathlib import Path

import matplotlib.cm as cm
import numpy as np
from matplotlib import colormaps

PACKAGE_DIR = Path(__file__).resolve().parent.parent
if not (PACKAGE_DIR / "pyproject.toml").exists():
    raise FileNotFoundError("This script must be run from the current package directory.")

RESOURCES_DIR = PACKAGE_DIR / "src" / "colormap_tools" / "resources"

if not RESOURCES_DIR.exists():
    raise FileNotFoundError("Resources directory does not exist.")

MPL_COLORMAP_FILE = RESOURCES_DIR / "mpl_colormaps.pickle"

MPL_CMPS = list(colormaps)


def extract_mpl_colormaps(cmp: str, len_: int = 256):
    colormap = cm.get_cmap(cmp)
    indices = np.arange(len_)
    # shape (len, 4), range [0, 1], dtype float
    colormap_arr = colormap(indices)

    assert colormap_arr.shape == (len_, 4)

    # shape (len, 4), range [0, 255], dtype uint8
    colormap_arr = (colormap_arr * 255).astype(np.uint8)

    # shape (len, 3)
    colormap_arr = colormap_arr[:, :3]

    # expand to (len, 1, 3)
    colormap_arr = np.expand_dims(colormap_arr, axis=1)

    assert colormap_arr.shape == (len_, 1, 3)

    return colormap_arr


def main():
    mpl_colormaps = {}

    for cmp in MPL_CMPS:
        mpl_colormaps[cmp] = extract_mpl_colormaps(cmp)
        print(f"Extracted: {cmp}")

    with (RESOURCES_DIR / "mpl_colormaps.pickle").open("wb") as f:
        pickle.dump(mpl_colormaps, f)

    print(f"Colormaps extracted and saved to {RESOURCES_DIR}.")


if __name__ == "__main__":
    main()
