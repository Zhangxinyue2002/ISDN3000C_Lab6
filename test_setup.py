"""
Quick test script to verify GPIO and OpenCV setup
Run this to check if your environment is properly configured
"""

import sys

print("=" * 60)
print("Testing Lab06 Environment Setup")
print("=" * 60)

# Test 1: Import Hobot.GPIO
print("\n[1] Testing Hobot.GPIO import...")
try:
    import Hobot.GPIO as GPIO
    print(f"✓ Hobot.GPIO imported successfully")
    print(f"  Version: {GPIO.VERSION}")
    print(f"  Model: {GPIO.model}")
except ImportError as e:
    print(f"✗ Failed to import Hobot.GPIO: {e}")
    print("  Make sure you're using --system-site-packages in your venv")

# Test 2: Import OpenCV
print("\n[2] Testing OpenCV import...")
try:
    import cv2
    print(f"✓ OpenCV imported successfully")
    print(f"  Version: {cv2.__version__}")
except ImportError as e:
    print(f"✗ Failed to import OpenCV: {e}")
    print("  Run: pip install opencv-python")

# Test 3: Import NumPy
print("\n[3] Testing NumPy import...")
try:
    import numpy as np
    print(f"✓ NumPy imported successfully")
    print(f"  Version: {np.__version__}")
except ImportError as e:
    print(f"✗ Failed to import NumPy: {e}")
    print("  Run: pip install numpy")

# Test 4: Test time module
print("\n[4] Testing time module...")
try:
    import time
    print(f"✓ time module available")
except ImportError as e:
    print(f"✗ Failed to import time: {e}")

print("\n" + "=" * 60)
print("Setup Check Complete!")
print("=" * 60)

# Check if all imports succeeded
all_good = True
try:
    import Hobot.GPIO as GPIO
    import cv2
    import numpy
    import time
    print("\n✓ All required modules are available!")
    print("  You're ready to run the lab exercises.")
except ImportError:
    print("\n✗ Some modules are missing. Please install them.")
    all_good = False

print("=" * 60)

sys.exit(0 if all_good else 1)
