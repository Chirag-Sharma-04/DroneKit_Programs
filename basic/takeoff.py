from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

# Connect to the vehicle
vehicle = connect('udp:127.0.0.1:14550', wait_ready=True)

def arm_and_takeoff(target_altitude):
    print("Arming motors...")
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)
    
    print("Taking off!")
    vehicle.simple_takeoff(target_altitude)

    # Wait until the vehicle reaches a safe height
    while True:
        print(f" Altitude: {vehicle.location.global_relative_frame.alt:.2f}m")
        if vehicle.location.global_relative_frame.alt >= target_altitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)

# Arm and take off to 5 meters
arm_and_takeoff(5)

# Hover for 5 seconds
time.sleep(5)

# Land the drone
print("Landing...")
vehicle.mode = VehicleMode("LAND")

# Wait for landing to complete
while vehicle.armed:
    print(f" Altitude: {vehicle.location.global_relative_frame.alt:.2f}m")
    time.sleep(1)

print("Landed and disarmed.")
vehicle.close()
