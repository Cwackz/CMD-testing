import os
import subprocess

def pi():
    raspberry_pi_address = "pi@100.125.100.39"
    try:
        subprocess.call(['ssh', raspberry_pi_address])
    except Exception as e:
        print(f"Error connecting to Raspberry Pi: {e}")