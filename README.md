# raspberry-pi-lcd-display

Raspberry Pi Pi Day LCD Display
This project uses a Raspberry Pi 3 Model B and a 20x4 I2C LCD display to scroll digits of π while displaying the current digit index and animated messages. The project was created for the PeopleTec Pi Day Competition.

Hardware Used
- Raspberry Pi 3 Model B
- 20x4 LCD display with I2C backpack
- Dupont jumper wires
- 3D printed case

Features
- Scrolls digits of π across the LCD
- Displays current digit index
- Animated pointer for current digit
- Automatic startup using systemd
- I2C communication between Raspberry Pi and LCD

Technologies Used
- Python
- Raspberry Pi OS
- I2C Protocol
- systemd
- smbus2
- RPLCD

Challenges
- LCD flickering issues
- I2C detection problems
- wiring stability fixes
