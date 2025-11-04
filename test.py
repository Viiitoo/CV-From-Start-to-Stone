import cv2
import numpy as np
import os

path = "datasets/StereoMIS/rgbd_monomis/depth_png/5985.png"
depth = cv2.imread(path, cv2.IMREAD_UNCHANGED)
print("Depth dtype:", None if depth is None else depth.dtype)
print("Depth shape:", None if depth is None else depth.shape)
print("Min/Max:", None if depth is None else (np.min(depth), np.max(depth)))
