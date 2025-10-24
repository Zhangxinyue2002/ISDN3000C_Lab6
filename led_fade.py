import Hobot.GPIO as GPIO
import time

# Pin Definitions
led_pin = 32 # make sure that this pin is not in use when you doing PWM.

def main():
    # Clean up any previous GPIO state first
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.cleanup()
        print("Cleaned up previous GPIO state")
    except:
        pass
    
    # Now set up the pin
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led_pin, GPIO.OUT)

    # Create a PWM instance:
    # PWM(pin, frequency_in_Hz)
    pwm = GPIO.PWM(led_pin, 100)  # Use 100 Hz frequency

    # Start PWM with 0% duty cycle (off)
    pwm.start(0)

    print("Fading LED. Press Ctrl+C to exit.")

    try:
        while True:
            # Fade in (from 0% to 100% duty cycle)
            for duty_cycle in range(0, 101, 5):
                pwm.ChangeDutyCycle(duty_cycle)
                time.sleep(0.05)
            
            # Fade out (from 100% to 0% duty cycle)
            for duty_cycle in range(100, -1, -5):
                pwm.ChangeDutyCycle(duty_cycle)
                time.sleep(0.05)

    finally:
        print("\nStopping PWM and cleaning up...")
        pwm.stop()      # Stop the PWM
        GPIO.cleanup()  # Reset the GPIO pins

if __name__ == '__main__':
    main()