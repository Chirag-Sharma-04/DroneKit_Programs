from dronekit import connect, VehicleMode
import time

vehicle_address = '127.0.0.1:14550'

print("Connecting to vehicle...")
vehicle = connect(vehicle_address, wait_ready=False)


vehicle.wait_ready('gps_0', 'battery', 'system_status', timeout=10) #wait for these values to be set

while True:
    print("\n--- Vehicle Info ---")
    print(f" Armable: {vehicle.is_armable}")
    print(f" Armed: {vehicle.armed}")
    print(f" Mode: {vehicle.mode.name}")
    print(f" GPS: {vehicle.gps_0}")
    print(f" Battery: {vehicle.battery}")
    print(f" System Status: {vehicle.system_status.state}")
    time.sleep(1)
