from machine import ADC, Pin, deepsleep
import time

# Configure the ADC pin for voltage measurement
adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)  # Configure attenuation to 11 dB for full range (0-3.3V)

# Define deep sleep duration (in milliseconds)
deep_sleep_duration = 5000  # 5 seconds (adjust as needed)

# Read voltage
voltage = adc.read() / 4095 * 3.3  # Convert ADC reading to voltage
print("Voltage:", voltage)

# Check voltage condition for deep sleep
if voltage > 2.0:
    print("Entering deep sleep mode for {} ms".format(deep_sleep_duration))
    deepsleep(deep_sleep_duration)  # Enter deep sleep