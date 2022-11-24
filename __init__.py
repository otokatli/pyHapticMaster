
import socket
import time


def _hapticMaster_message(msg):
    hm_msg = [0, 0, 0, 0, 0, 0, 0, 0]
    
    # Convert msg to ascii dec
    decimal_msg = [ord(c) for c in msg]
    
    hm_msg[3] = len(decimal_msg)
    
    return hm_msg + decimal_msg

def _hapticMaster_response(msg):
    return str(msg).split('"')[1:2][0]

def send_message(s, msg):
    s.sendall(bytearray(_hapticMaster_message(msg)))

def send_recv_message(s, msg):
    s.sendall(bytearray(_hapticMaster_message(msg)))

    time.sleep(0.5)

    return _hapticMaster_response(s.recv(1024))

def recv_message(s):
    return _hapticMaster_response(s.recv(1024))

def set_state(s, device_state):
    """ Set the state of the HapticMaster 
    Args
    ----
    s            : Socket handle
    device_state : State for the HapticMaster

    Returns
    -------
    True if setting the state is successful, False o.w.
    """
    if device_state in ['init', 'off', 'force', 'position']:
        msg = 'set state ' + device_state
        send_message(s, msg)

        return True
    else:
        print('Wrong state name')

        return False

def create_spring(s, name: str, position: list, constant: float, direction: list, damp_factor: float, max_force: float):
    # First step, create the damper
    msg = 'create spring ' + name
    send_message(s, msg)

    # Second step, set the damping coefficient
    msg = 'set ' + name + ' pos ' + str(position).replace(' ', '')
    send_message(s, msg)

    # Third step, set spring constant
    msg = 'set ' + name + ' stiffness ' + str(constant)
    send_message(s, msg)

    # Fourth step, set spring direction
    msg = 'set ' + name + ' direction ' + str(direction).replace(' ', '')
    send_message(s, msg)

    # Fifth step, set spring dampfactor
    msg = 'set ' + name + ' dampfactor ' + str(damp_factor)
    send_message(s, msg)

    # Sixth step, set max spring force
    msg = 'set ' + name + ' maxforce ' + str(max_force)
    send_message(s, msg)

    # Seventh step, enable the spring
    msg = 'set ' + name + ' enable'
    send_message(s, msg)

def create_damper(s, name: str, coefficient: list) -> None:
    # First step, create the damper
    msg = 'create damper ' + name
    send_message(s, msg)

    # Second step, set the damping coefficient
    msg = 'set ' + name + ' dampcoef ' + str(coefficient).replace(' ', '')
    send_message(s, msg)

    # Third step, enable the damper
    msg = 'set ' + name + ' enable'
    send_message(s, msg)

def set_inertia(s, value):
    msg = 'set inertia ' + str(value)
    send_message(s, msg)

def calibrate_robot(s):
    # Check if the robot is calibrated
    msg = 'get position_calibrated'
    response = send_recv_message(s, msg)
    print(response)
    if response == 'false':
        print('Initialise the robot')
        set_state(s, 'init')
        
        time.sleep(1.0)

        print('Waiting for calibration to complete')
        print(response)
        while response == 'false':
            time.sleep(1.0)

            response = send_recv_message(s, 'get position_calibrated')
            print(response)
    else:
        print('Robot is already calibrated')

def clear_all_effects(s):
    msg = 'remove all'
    send_message(s, msg)

def move_spring(name, position):
    # Second step, set the damping coefficient
    msg = 'set ' + name + ' pos ' + str(position).replace(' ', '')
    send_message(s, msg)

if __name__ == '__main__':
    ip = '192.168.0.25'
    port = 7654

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))
        
        # Calibrate the robot
        calibrate_robot(s)
        
        # Wait for calibration to finish
        time.sleep(30.0)

        # Set end-effector inertia
        set_inertia(s, 3)
        
        # Set robot to force mode
        set_state(s, 'force')
        
        # Create a damper at the end-effector
        create_damper(s, 'myDamper', [10.6, 10.6, 10.6])
        
        # Create a spring at the end-effector
        create_spring(s, 'mySpring', [0, 0, 0], 50, [0, 0, 1], 0.0, 25.0)

        # Clear all haptic effects
        clear_all_effects(s)
        
        # Turn off the robot
        set_state(s, 'off')