import pickle
from pathlib import Path

import cv2
import numpy as np

PACKAGE_DIR = Path(__file__).resolve().parent.parent
if not (PACKAGE_DIR / "pyproject.toml").exists():
    raise FileNotFoundError("This script must be run from the current package directory.")

RESOURCES_DIR = PACKAGE_DIR / "src" / "colormap_tools" / "resources"

if not RESOURCES_DIR.exists():
    raise FileNotFoundError("Resources directory does not exist.")

CV_COLORMAP_FILE = RESOURCES_DIR / "cv_colormaps.pickle"


def extract_cv_colormaps(cv_cmp: int, len_: int = 256):
    indices = np.arange(len_, dtype=np.uint8)

    colormap_arr_bgr = cv2.applyColorMap(indices, cv_cmp)
    colormap_arr_rgb = cv2.cvtColor(colormap_arr_bgr, cv2.COLOR_BGR2RGB)

    assert colormap_arr_rgb.shape == (len_, 1, 3)

    return colormap_arr_rgb


def main():
    _CV_CMPS = {
        loc.replace("COLORMAP_", "").lower(): getattr(cv2, loc) for loc in cv2.__dict__ if loc.startswith("COLORMAP_")
    }
    CV_CMPS = {}
    for cmp in _CV_CMPS:
        CV_CMPS[cmp] = extract_cv_colormaps(_CV_CMPS[cmp])

    with (RESOURCES_DIR / "cv_colormaps.pickle").open("wb") as f:
        pickle.dump(CV_CMPS, f)

    print(f"Colormaps extracted and saved to {RESOURCES_DIR}.")


if __name__ == "__main__":
    main()
