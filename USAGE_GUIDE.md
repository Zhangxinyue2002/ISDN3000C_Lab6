# Lab06 Project Structure and Usage Guide

## 📂 Project Structure

```
LAB06/
├── README.md                          # Main documentation
├── requirements.txt                   # Python dependencies
├── .gitignore                        # Git ignore file
├── media/                            # Circuit photos directory
│   └── README.md                     # Instructions for photos
└── lab06_venv/                       # Virtual environment with code
    ├── blink.py                      # Basic: LED blinking
    ├── button_read.py                # Basic: Button reading
    ├── button_led.py                 # Basic: Button controls LED
    ├── led_fade.py                   # Basic: PWM LED fading
    ├── clean.py                      # Utility: GPIO cleanup
    ├── test_setup.py                 # Utility: Test environment
    ├── exercise1_pwm_button.py       # Exercise 1: PWM control
    └── exercise2_camera.py           # Exercise 2: Camera capture
```

## 🎯 What's Been Created

### Exercise Files (NEW!)

#### 1. **exercise1_pwm_button.py** - PWM Brightness Control
Controls LED brightness with button presses:
- **Short press**: Cycles through brightness (0% → 25% → 50% → 75% → 100%)
- **Long press (2s)**: Toggles blinking mode
- Uses Pin 32 (PWM) for LED, Pin 13 for button

#### 2. **exercise2_camera.py** - Camera with Edge Detection
Captures images on button press:
- Takes photo with USB camera
- Applies Canny edge detection
- LED blinks for 0.5s to confirm
- Saves both original and processed images
- Creates `captured_images/` directory automatically

### Supporting Files

- **README.md**: Complete documentation with setup instructions
- **requirements.txt**: Python dependencies (opencv-python, numpy)
- **.gitignore**: Excludes virtual environments, cache, images
- **test_setup.py**: Validates your environment setup
- **media/README.md**: Instructions for adding circuit photos

## 🚀 Quick Start Guide

### Step 1: Activate Virtual Environment
```bash
cd ~/LAB06
source lab06_venv/local/bin/activate
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Test Setup
```bash
python3 lab06_venv/test_setup.py
```

### Step 4: Configure PWM (for Exercise 1)
```bash
sudo srpi-config
# Enable PWM4 on Pin 32
# Reboot if needed
```

### Step 5: Run Exercises

**Exercise 1: PWM Button Control**
```bash
python3 lab06_venv/exercise1_pwm_button.py
```
- Wire LED to Pin 32 (with resistor) → GND
- Wire Button: 3.3V → Button → Pin 13
- Short press: cycle brightness
- Long press: toggle blinking

**Exercise 2: Camera Capture**
```bash
python3 lab06_venv/exercise2_camera.py
```
- Wire LED to Pin 31 (with resistor) → GND
- Wire Button: 3.3V → Button → Pin 13
- Connect USB camera
- Press button to capture and process images
- Check `captured_images/` directory for results

## 📋 Pin Configuration Reference

| Component | Physical Pin | Function | Notes |
|-----------|-------------|----------|-------|
| LED (PWM) | 32 | GPIO PWM4 | Exercise 1 |
| LED (Regular) | 31 | GPIO6 | Exercise 2, basic examples |
| Button | 13 | GPIO27 | All exercises |
| Button Power | 1 | 3.3V | Don't use 5V! |
| Ground | 6, 9, 14, etc. | GND | Any ground pin |

## 🔧 Hardware Wiring

### Exercise 1 Circuit (PWM Control)
```
3.3V (Pin 1) → Button → Pin 13
Pin 32 → 220Ω Resistor → LED Anode(+) → LED Cathode(-) → GND (Pin 6)
```

### Exercise 2 Circuit (Camera)
```
3.3V (Pin 1) → Button → Pin 13
Pin 31 → 220Ω Resistor → LED Anode(+) → LED Cathode(-) → GND (Pin 6)
USB Port → Camera
```

## 🎨 Features Overview

### Exercise 1 Features
✓ PWM brightness control (5 levels)
✓ Button debouncing
✓ Long press detection (2 seconds)
✓ Blinking mode toggle
✓ Clear console feedback
✓ Proper cleanup on exit

### Exercise 2 Features
✓ Camera initialization and warm-up
✓ Real-time button monitoring
✓ Image capture on button press
✓ Grayscale conversion
✓ Canny edge detection (threshold: 100, 200)
✓ Unique timestamped filenames
✓ LED confirmation (0.5s)
✓ Button release detection (prevents multiple captures)
✓ Automatic directory creation
✓ Proper camera and GPIO cleanup

## 📸 Output Examples

### Exercise 1 Console Output
```
==================================================
PWM Button Control
==================================================
Short press: Cycle brightness (Off -> 25% -> 50% -> 75% -> 100%)
Long press (2s): Toggle blinking mode
Press Ctrl+C to exit
==================================================
LED: OFF
Button pressed...
LED Brightness: 25%
Button pressed...
LED Brightness: 50%
...
```

### Exercise 2 Console Output
```
============================================================
Camera Capture with Canny Edge Detection
============================================================
...
Ready! Press the button to capture an image.
Press Ctrl+C to exit.
============================================================

>>> BUTTON PRESSED! Capturing image #1...
Frame captured successfully!
Converted to grayscale
Applied Canny edge detection
Saved: captured_images/original_1729682345123.jpg
Saved: captured_images/edges_1729682345123.jpg
Total images captured: 1
...
```

## 🐛 Troubleshooting

### GPIO "Channel already in use"
```bash
python3 lab06_venv/clean.py
```

### PWM not working
1. Run `sudo srpi-config`
2. Enable PWM4 on Pin 32
3. Reboot system
4. Check pin connection

### Camera not opening
1. Check USB connection
2. Verify permissions
3. Try different VideoCapture index (0 or 1)
4. Check camera with: `ls /dev/video*`

### Import errors
```bash
# Make sure virtual environment uses system packages
source lab06_venv/local/bin/activate
pip install -r requirements.txt
python3 lab06_venv/test_setup.py
```

## 📤 Submission Checklist

Before submitting to GitHub:

- [ ] All Python scripts run without errors
- [ ] Circuit photos added to `media/` directory
- [ ] README.md includes team member names
- [ ] Tested Exercise 1 (PWM control works)
- [ ] Tested Exercise 2 (camera captures and processes)
- [ ] requirements.txt is complete
- [ ] .gitignore is in place
- [ ] Repository is public
- [ ] Repository named: `ISDN3000C_Lab06`

### Git Commands
```bash
cd ~/LAB06
git init
git add .
git commit -m "Initial commit - Lab06 GPIO exercises"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ISDN3000C_Lab06.git
git push -u origin main
```

## 💡 Tips

1. **Always test basic examples first** before running exercises
2. **Double-check wiring** - especially LED polarity and resistor
3. **Use clean.py** if you get "port in use" errors
4. **Press Ctrl+C** to exit any running script
5. **Keep LED on time short** to avoid overheating
6. **Camera warm-up** is included - first few frames may be dark
7. **Button debouncing** is handled in the code

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section
2. Run `test_setup.py` to verify environment
3. Review pin connections
4. Check RDK X-5 documentation
5. Contact instructor via WhatsApp group

---

**Ready to submit?** Make sure all checklist items are complete!
