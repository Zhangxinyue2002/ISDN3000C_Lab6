# ISDN3000C Lab 06: GPIO Programming on RDK X-5

This repository contains Python scripts for controlling GPIO pins on the RDK X-5 development board, including LED control, button input, PWM, and camera integration.

## 📋 Table of Contents
- [Hardware Setup](#hardware-setup)
- [Software Setup](#software-setup)
- [Project Files](#project-files)
- [Running the Scripts](#running-the-scripts)
- [Exercises](#exercises)
- [Circuit Diagrams](#circuit-diagrams)

## 🔧 Hardware Setup

### Components Required
- RDK X-5 Development Board
- Breadboard
- LED (any color)
- 220Ω resistor
- Push button
- USB Camera (for Exercise 2)
- Jumper wires

### Safety Precautions
⚠️ **Important:**
- RDK X-5 GPIO pins operate at **3.3V** (NOT 5V!)
- Always use a current-limiting resistor with LEDs
- Discharge static electricity before handling components
- Double-check wiring before running code

## 💻 Software Setup

### 1. Create Virtual Environment
```bash
cd ~/
mkdir LAB06
cd LAB06
sudo apt-get install virtualenv
virtualenv lab06_venv --system-site-packages
source lab06_venv/local/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure PWM (for PWM exercises)
```bash
sudo srpi-config
```
Navigate to: `3 Interface Options` → `I3 Peripheral bus config`
- Enable **PWM4** on Physical Pin 32
- Enable **PWM0** on Physical Pin 33

Reboot is required.

## 📁 Project Files

### Basic Examples
- **`blink.py`** - Simple LED blinking (Pin 31)
- **`button_read.py`** - Read button state (Pin 13)
- **`button_led.py`** - Button controls LED
- **`led_fade.py`** - PWM LED fading effect (Pin 32)
- **`clean.py`** - Manually clean GPIO pins

### Exercises
- **`exercise1_pwm_button.py`** - PWM brightness control with button
- **`exercise2_camera.py`** - Camera capture with Canny edge detection

## 🚀 Running the Scripts

### Activate Virtual Environment
```bash
cd ~/LAB06
source lab06_venv/local/bin/activate
```

### Run Basic Examples
```bash
# Blink LED
python3 lab06_venv/blink.py

# Read button
python3 lab06_venv/button_read.py

# Button controls LED
python3 lab06_venv/button_led.py

# PWM LED fade
python3 lab06_venv/led_fade.py
```

### Run Exercises
```bash
# Exercise 1: PWM Button Control
python3 lab06_venv/exercise1_pwm_button.py

# Exercise 2: Camera Capture
python3 lab06_venv/exercise2_camera.py
```

### Clean GPIO (if ports are in use)
```bash
python3 lab06_venv/clean.py
```

## 🎯 Exercises

### Exercise 1: PWM Button Control
**Features:**
- **Short press:** Cycles through brightness levels (Off → 25% → 50% → 75% → 100% → Off)
- **Long press (2s):** Switches to blinking mode
- LED connected to **Pin 32** (PWM-enabled)
- Button connected to **Pin 13**

**Wiring:**
- LED: Pin 32 → Resistor → LED Anode → LED Cathode → GND
- Button: 3.3V → Button → Pin 13

### Exercise 2: Camera Capture with Edge Detection
**Features:**
- Press button to capture image
- Applies Canny edge detection
- LED lights for 0.5s to confirm capture
- Saves both original and edge-detected images

**Wiring:**
- LED: Pin 31 → Resistor → LED Anode → LED Cathode → GND
- Button: 3.3V → Button → Pin 13
- Camera: USB port

**Output:**
- Images saved in `captured_images/` directory
- Filenames include timestamp for uniqueness

## 📸 Circuit Diagrams

### Circuit Photos
<!-- Add your circuit photos here -->

**Example 1: Basic LED Blink**
![Blink Circuit](./media/blink.png)

**Example 2: Button Input**
![Button Circuit](./media/button.png)

**Example 3: Combined Circuit**
![Combined Circuit](./media/combine.png)

### Pin Reference

| Physical Pin | Function | Usage |
|--------------|----------|-------|
| Pin 1 | 3.3V Power | Button power |
| Pin 6 | Ground | LED ground |
| Pin 13 | GPIO | Button input |
| Pin 31 | GPIO | LED output |
| Pin 32 | PWM4 | PWM LED control |
| Pin 33 | PWM0 | Alternative PWM |

## 🔍 Pin Numbering

This project uses **BOARD** numbering (physical pin numbers 1-40), not BCM numbering.

```python
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbers
```

## 🐛 Troubleshooting

### GPIO Pins "In Use" Error
```bash
python3 lab06_venv/clean.py
```

### Camera Not Opening
- Check USB connection
- Try `cap = cv2.VideoCapture(0)` or `cv2.VideoCapture(1)`
- Ensure camera has permissions

### PWM Not Working
- Verify PWM is enabled via `sudo srpi-config`
- Check correct pin (32 or 33)
- Reboot after configuration changes

### LED Not Lighting
- Check resistor is connected (220Ω)
- Verify LED polarity (long leg = anode = +)
- Check ground connection

## 📚 Resources

- [RDK X-5 Official Documentation](https://developer.d-robotics.cc/rdk_doc/en/)
- [RDK 40-Pin GPIO Guide](https://developer.d-robotics.cc/rdk_doc/en/Basic_Application/03_40pin_user_guide/40pin_define/)
- [OpenCV Documentation](https://docs.opencv.org/)

## 👥 Team Members
<!-- Add your team member names here -->
- Member 1: [Name]
- Member 2: [Name]
- Member 3: [Name]

## 📝 License
This project is for educational purposes as part of ISDN3000C.

---

**Course:** ISDN3000C  
**Lab:** Lab 06 - GPIO Programming  
**Date:** October 2025
