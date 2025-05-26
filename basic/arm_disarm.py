from dronekit import connect, VehicleMode
import time

# Connect to the vehicle (adjust the connection string as needed)
# Example: '/dev/ttyAMA0' for serial, 'udp:127.0.0.1:14550' for SITL
vehicle = connect('udp:127.0.0.1:14550', wait_ready=True)

# Function to arm the drone
def arm_drone():
    print("Arming drone...")
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    # Wait until the drone is armed
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)
    print("Drone is armed.")

# Function to disarm the drone
def disarm_drone():
    print("Disarming drone...")
    vehicle.armed = False

    # Wait until the drone is disarmed
    while vehicle.armed:
        print(" Waiting for disarming...")
        time.sleep(1)
    print("Drone is disarmed.")

# Main script
arm_drone()
time.sleep(5)  # Hold armed state for 5 seconds
disarm_drone()

# Close vehicle object
vehicle.close()
print("Script completed.")