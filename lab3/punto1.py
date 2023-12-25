import bluetooth
import ubinascii
import utime

# Generate a random address type (0x01 for random static address)
address_type = bytes([0x01])

# Get the ESP32's MAC address
mac_address = ubinascii.hexlify(bluetooth.get_mac()).decode('utf-8')

# Combine the address type and MAC address to create a random BLE address
ble_address = address_type + bytes.fromhex(mac_address[-6:])  # Use the last 6 digits of the MAC address

ble_name = "BLE_Energy_Meter"

# Create a BLE server
ble = bluetooth.BLE()
ble.active(True)

# Create a custom service and characteristic UUID
service_uuid = bluetooth.UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")
char_uuid = bluetooth.UUID("6E400002-B5A3-F393-E0A9-E50E24DCCA9E")

# Create the custom service
ble_service = bluetooth.Service(service_uuid)

# Create the custom characteristic
ble_characteristic = bluetooth.Characteristic(char_uuid, properties=bluetooth.Characteristic.WRITE | bluetooth.Characteristic.NOTIFY)
ble_service.add_characteristic(ble_characteristic)

# Add the service to the server
ble.add_service(ble_service)

# Define the accumulated energy variable
accumulated_energy = 0.0

while True:
    # Simulate energy consumption (replace with actual sensor data)
    current_reading = 0.5  # Example: 0.5 A
    period_seconds = 1    # 1 second

    # Calculate consumed energy in kWh
    consumed_energy = (current_reading * period_seconds) / 3600000  # kWh

    # Accumulate energy
    accumulated_energy += consumed_energy

    # Update the characteristic with the accumulated energy
    ble_characteristic.value(str(accumulated_energy))

    # Advertise the BLE service and characteristic
    ble.gap_advertise(100, bytearray(ble_name, 'utf-8'))

    utime.sleep(period_seconds)

