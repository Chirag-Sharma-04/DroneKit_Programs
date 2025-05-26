from dronekit import connect, VehicleMode

connection_string = '127.0.0.1:14550'

vehicle = connect(connection_string, wait_ready=True, timeout=60)

print("Vehicle connected successfully!")
print("\n--- Vehicle Information ---")
print(f" Type: {vehicle._vehicle_type}")
print(f" Is Armable: {vehicle.is_armable}")
print(f" Armed: {vehicle.armed}")
print(f" Mode: {vehicle.mode.name}")
print(f" System Status: {vehicle.system_status.state}")
print(f" GPS: {vehicle.gps_0}")
print(f" Battery: {vehicle.battery}")
print(f" Last Heartbeat: {vehicle.last_heartbeat}")


