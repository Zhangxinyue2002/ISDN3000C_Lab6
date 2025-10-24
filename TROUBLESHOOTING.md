# Troubleshooting Guide - Lab06 GPIO

## Common Issues and Solutions

### 1. "This channel is in use" Error

**Problem:**
```
RuntimeError: This channel is in use
```

**Cause:** GPIO pin is still in use from a previous run that wasn't cleanedproperly.

**Solutions:**

#### Quick Fix:
```bash
cd ~/LAB06
python3 lab06_venv/cleanup_advanced.py
```

#### If that doesn't work:
```bash
# Try the basic cleanup
python3 lab06_venv/clean.py

# Then run the advanced cleanup
python3 lab06_venv/cleanup_advanced.py
```

#### Last Resort:
```bash
# Reboot the system
sudo reboot
```

### 2. PWM "Channel already exported" Warning

**Problem:**
```
RuntimeWarning: This channel(32) has been exported before this operation
```

**Cause:** PWM hardware channel is stuck at a lower level.

**Solutions:**

#### Option 1: Use Pin 33 instead of Pin 32
```python
led_pin = 33  # PWM0 instead of PWM4
```

#### Option 2: Full PWM Reset
```bash
# Run advanced cleanup
python3 lab06_venv/cleanup_advanced.py

# Check PWM configuration
sudo srpi-config
# Navigate to: 3 Interface Options → I3 Peripheral bus config
# Disable and re-enable PWM

# Reboot
sudo reboot
```

#### Option 3: Try the alternative script
```bash
python3 lab06_venv/led_fade_alt.py  # Uses Pin 33
```

### 3. PWM Not Working

**Problem:** LED doesn't fade, just turns on/off or doesn't light at all.

**Checklist:**

1. **Enable PWM in srpi-config:**
   ```bash
   sudo srpi-config
   ```
   - Go to: `3 Interface Options` → `I3 Peripheral bus config`
   - Enable PWM0 on Pin 33 OR PWM4 on Pin 32
   - Reboot

2. **Check Pin Assignment:**
   - Pin 32 = PWM4
   - Pin 33 = PWM0
   - Make sure your code matches your srpi-config setting

3. **Verify Wiring:**
   ```
   Pin 32/33 → 220Ω Resistor → LED Anode (+) → LED Cathode (-) → GND
   ```

4. **Test with alternative pin:**
   Edit your script:
   ```python
   led_pin = 33  # Try Pin 33 if Pin 32 doesn't work
   ```

### 4. Button Not Responding

**Problem:** Button presses aren't detected.

**Solutions:**

1. **Check Wiring:**
   ```
   3.3V (Pin 1) → Button → Pin 13 (GPIO)
   ```
   
2. **Verify Button Works:**
   ```bash
   python3 lab06_venv/button_read.py
   ```

3. **Check Pull-up/Pull-down:**
   The code uses `GPIO.IN` (without explicit pull-up/down).
   Try adding:
   ```python
   GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
   ```

### 5. Camera Not Opening

**Problem:**
```
ERROR: Cannot open camera!
```

**Solutions:**

1. **Check USB Connection:**
   ```bash
   ls /dev/video*
   ```
   Should show: `/dev/video0` or `/dev/video1`

2. **Try Different Camera Index:**
   ```python
   cap = cv2.VideoCapture(1)  # Try 1 instead of 0
   ```

3. **Check Permissions:**
   ```bash
   sudo usermod -a -G video $USER
   # Logout and login again
   ```

4. **Test Camera:**
   ```bash
   python3 -c "import cv2; cap = cv2.VideoCapture(0); print('OK' if cap.isOpened() else 'FAIL')"
   ```

### 6. LED Not Lighting Up

**Problem:** LED doesn't light at all.

**Checklist:**

1. **Check LED Polarity:**
   - Long leg = Anode (+) → connects to GPIO pin (via resistor)
   - Short leg = Cathode (-) → connects to GND

2. **Verify Resistor:**
   - Must use 220Ω resistor
   - Resistor can be on either side of LED

3. **Test with Simple Script:**
   ```bash
   python3 lab06_venv/blink.py
   ```

4. **Check Pin Number:**
   - Using BOARD numbering (physical pin numbers)
   - Pin 31, 32, or 33 depending on your script

5. **Test LED:**
   Carefully test LED directly with 3.3V and GND (with resistor!)

### 7. Import Errors

**Problem:**
```
ModuleNotFoundError: No module named 'cv2'
```

**Solutions:**

1. **Activate Virtual Environment:**
   ```bash
   cd ~/LAB06
   source lab06_venv/local/bin/activate
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify Installation:**
   ```bash
   python3 lab06_venv/test_setup.py
   ```

### 8. Hobot.GPIO Not Found

**Problem:**
```
ModuleNotFoundError: No module named 'Hobot'
```

**Cause:** Hobot.GPIO is a system package, needs --system-site-packages

**Solution:**

Check your virtual environment was created correctly:
```bash
virtualenv lab06_venv --system-site-packages
source lab06_venv/local/bin/activate
python3 -c "import Hobot.GPIO; print('OK')"
```

If still failing, install it:
```bash
sudo apt-get update
sudo apt-get install python3-hobot-gpio
```

### 9. Permission Denied Errors

**Problem:**
```
PermissionError: [Errno 13] Permission denied
```

**Solutions:**

1. **For GPIO:**
   ```bash
   sudo usermod -a -G gpio $USER
   # Logout and login
   ```

2. **For PWM:**
   ```bash
   sudo chmod 666 /sys/class/pwm/pwmchip*/export
   sudo chmod 666 /sys/class/pwm/pwmchip*/unexport
   ```

3. **Run with sudo (not recommended for development):**
   ```bash
   sudo python3 lab06_venv/led_fade.py
   ```

### 10. Script Won't Stop (Ctrl+C not working)

**Problem:** Script hangs and Ctrl+C doesn't work.

**Solutions:**

1. **Try Ctrl+Z then kill:**
   ```bash
   # Press Ctrl+Z
   bg  # Send to background
   jobs  # List jobs
   kill %1  # Kill job 1
   ```

2. **Find and kill process:**
   ```bash
   ps aux | grep python
   sudo kill -9 <PID>
   ```

3. **Run cleanup after killing:**
   ```bash
   python3 lab06_venv/cleanup_advanced.py
   ```

## Quick Reference Commands

```bash
# Cleanup
python3 lab06_venv/cleanup_advanced.py

# Test environment
python3 lab06_venv/test_setup.py

# Configure PWM
sudo srpi-config

# Check GPIO exports
ls -la /sys/class/gpio/

# Check PWM exports
ls -la /sys/class/pwm/

# Check camera
ls /dev/video*

# Activate environment
cd ~/LAB06
source lab06_venv/local/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Still Having Issues?

1. Check the main README.md
2. Check USAGE_GUIDE.md
3. Run test_setup.py
4. Try running basic examples before exercises
5. Reboot and try again
6. Contact instructor via WhatsApp

## Useful Debug Commands

```bash
# Show GPIO status
cat /sys/kernel/debug/gpio

# Show PWM status
cat /sys/kernel/debug/pwm

# Check Python packages
pip list | grep -i opencv
pip list | grep -i numpy

# Test Hobot.GPIO
python3 -c "import Hobot.GPIO as GPIO; print(GPIO.VERSION)"
```
