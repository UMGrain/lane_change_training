import os
import pathlib
import torch

from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms
from typing import Tuple, Dict, List

if __name__ == '__main__':


    # Setup path for target directory
    target_directory = train_dir
    print(f"Target directory: {target_directory}")

    # Get the class names from the target directory
    class_names_found = sorted([entry.name for entry in list(os.scandir(image_path / "train"))])
    print(f"Class names found: {class_names_found}")


