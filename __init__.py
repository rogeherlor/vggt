import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

# Recursively add all subdirectories to the Python path
for root, dirs, files in os.walk(current_dir):
    if root not in sys.path:
        sys.path.append(root)