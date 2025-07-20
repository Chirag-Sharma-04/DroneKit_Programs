from dronekit import connect
import time

vehicle = connect('127.0.0.1:14550', baud=57600, wait_ready=False,timeout=60)

def set_servo(servo_number, pwm_value):
    print(f"Setting SERVO{servo_number} to PWM: {pwm_value}")
    vehicle._master.mav.command_long_send(
        vehicle._master.target_system,
        vehicle._master.target_component,
        183,                 # MAV_CMD_DO_SET_SERVO
        0,
        servo_number,        # Servo number (SERVO9 = 9)
        pwm_value,           # PWM value (1000 to 2000)
        0, 0, 0, 0, 0        # Unused parameters
    )


try:
    # while True:
    #     for i in range(1000,2000,10):
    #         set_servo(9,i)
    #         time.sleep(0.01)
    #     for i in range(200,1000,-10):
    #         set_servo(9,i)
    #         time.sleep(0.01)
    set_servo(9, 1000) 
except KeyboardInterrupt:
    print("Exiting...")
    vehicle.close()
