"""
Exercise 2: Camera Capture with Canny Edge Detection
- Press button to capture image
- Applies Canny edge detection
- LED lights up for 0.5 seconds to confirm capture
- Saves both original and edge-detected images
"""

import Hobot.GPIO as GPIO
import cv2
import time
import os

# Pin Definitions
LED_PIN = 31      # Regular GPIO pin for LED
BUTTON_PIN = 13   # Button input pin

# Create output directory for images
OUTPUT_DIR = "captured_images"

def setup_gpio():
    """Initialize GPIO pins"""
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.setup(BUTTON_PIN, GPIO.IN)  # Hobot.GPIO 不支持内部上拉/下拉
    GPIO.output(LED_PIN, GPIO.LOW)  # Ensure LED starts off

def setup_output_directory():
    """Create directory for saving images"""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created directory: {OUTPUT_DIR}")

def capture_and_process(cap):
    """Capture frame, apply Canny edge detection, and save both images"""
    # Capture frame
    ret, frame = cap.read()
    
    if not ret:
        print("ERROR: Failed to capture frame!")
        return False
    
    print("Frame captured successfully!")
    
    # Convert to grayscale
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print("Converted to grayscale")
    
    # Apply Canny edge detection
    edges = cv2.Canny(gray_image, 100, 200)
    print("Applied Canny edge detection")
    
    # Generate unique filenames using timestamp
    timestamp = int(time.time() * 1000)  # milliseconds for uniqueness
    original_filename = os.path.join(OUTPUT_DIR, f"original_{timestamp}.jpg")
    edges_filename = os.path.join(OUTPUT_DIR, f"edges_{timestamp}.jpg")
    
    # Save images
    cv2.imwrite(original_filename, frame)
    cv2.imwrite(edges_filename, edges)
    
    print(f"Saved: {original_filename}")
    print(f"Saved: {edges_filename}")
    
    return True

def wait_for_button_release():
    """Wait until button is released to prevent multiple captures"""
    while GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        time.sleep(0.01)
    print("Button released\n")

def main():
    print("=" * 60)
    print("Camera Capture with Canny Edge Detection")
    print("=" * 60)
    
    # Setup
    setup_output_directory()
    setup_gpio()
    
    # Initialize camera
    print("\nInitializing camera...")
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("ERROR: Cannot open camera!")
        GPIO.cleanup()
        return
    
    print("Camera initialized successfully!")
    
    # Warm up camera (sometimes first few frames are dark)
    print("Warming up camera...")
    for _ in range(5):
        cap.read()
        time.sleep(0.1)
    
    print("\n" + "=" * 60)
    print("Ready! Press the button to capture an image.")
    print("Press Ctrl+C to exit.")
    print("=" * 60 + "\n")
    
    image_count = 0
    
    try:
        while True:
            button_state = GPIO.input(BUTTON_PIN)
            
            if button_state == GPIO.HIGH:
                print(f"\n>>> BUTTON PRESSED! Capturing image #{image_count + 1}...")
                
                # Turn LED ON
                GPIO.output(LED_PIN, GPIO.HIGH)
                
                # Capture and process image
                success = capture_and_process(cap)
                
                if success:
                    image_count += 1
                    print(f"Total images captured: {image_count}")
                
                # Keep LED on for 0.5 seconds
                time.sleep(0.5)
                
                # Turn LED OFF
                GPIO.output(LED_PIN, GPIO.LOW)
                print("LED OFF")
                
                # Wait for button release to prevent multiple captures
                wait_for_button_release()
            
            time.sleep(0.02)  # Small delay to reduce CPU usage
    
    except KeyboardInterrupt:
        print("\n\nExiting...")
    
    finally:
        print("\nCleaning up...")
        GPIO.output(LED_PIN, GPIO.LOW)  # Ensure LED is off
        cap.release()  # Release camera
        GPIO.cleanup()  # Clean up GPIO
        print(f"Done! Captured {image_count} images.")
        print(f"Images saved in: {OUTPUT_DIR}/")

if __name__ == '__main__':
    main()
