from dronekit import connect
from pymavlink import mavutil
import time

# Connect to Pixhawk via serial
vehicle = connect('127.0.0.1:14550', baud=57600, wait_ready=False)

# Request RC_CHANNELS at 10Hz
vehicle._master.mav.request_data_stream_send(
    vehicle._master.target_system,
    vehicle._master.target_component,
    mavutil.mavlink.MAV_DATA_STREAM_RC_CHANNELS,
    10,  # frequency in Hz
    1    # start stream
)

def print_rc_channels():
    msg = vehicle._master.recv_match(type='RC_CHANNELS', blocking=True, timeout=2)
    if msg:
        print(f"CH1: {msg.chan1_raw} | CH2: {msg.chan2_raw} | CH3: {msg.chan3_raw} | CH4: {msg.chan4_raw}")
        print(f"CH5: {msg.chan5_raw} | CH6: {msg.chan6_raw} | CH7: {msg.chan7_raw} | CH8: {msg.chan8_raw}")
        print(f"CH9: {msg.chan9_raw} | CH10: {msg.chan10_raw} | CH11: {msg.chan11_raw}")
    else:
        print("No RC_CHANNELS message received!")

while True:
    try:
        print_rc_channels()
        time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nExiting...")
        vehicle.close()
        break
