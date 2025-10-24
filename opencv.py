import time
import cv2
import Hobot.GPIO as GPIO

LED_PIN = 31
BUTTON_PIN = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN)

def take_and_process(cap):
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame from camera")
        return False

    ts = int(time.time())
    orig_name = f"image_{ts}.jpg"
    edges_name = f"edges_{ts}.jpg"

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)

    cv2.imwrite(orig_name, frame)
    cv2.imwrite(edges_name, edges)

    print(f"Saved {orig_name} and {edges_name}")
    return True

def wait_for_release(pin):
    while GPIO.input(pin) == GPIO.HIGH:
        time.sleep(0.01)

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        return

    print("Ready. Press the button to take a picture.")

    try:
        while True:
            if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
                print("Button Pressed! Capturing...")
                success = take_and_process(cap)
                # flash LED for 0.5s to confirm
                if success:
                    GPIO.output(LED_PIN, GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(LED_PIN, GPIO.LOW)

                # wait for release to avoid multiple captures
                wait_for_release(BUTTON_PIN)

            time.sleep(0.02)

    except KeyboardInterrupt:
        print("Interrupted by user")

    finally:
        print("Cleaning up...")
        cap.release()
        GPIO.cleanup()

if __name__ == '__main__':
    main()
