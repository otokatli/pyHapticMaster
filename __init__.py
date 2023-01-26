
import socket


def _hapticMaster_message(msg):
    hm_msg = [0, 0, 0, 0, 0, 0, 0, 0]
    
    # Convert msg to ascii dec
    decimal_msg = [ord(c) for c in msg]
    
    hm_msg[3] = len(decimal_msg)
    
    return hm_msg + decimal_msg

def _hapticMaster_response(msg):
    # Message as a string
    msg_str = str(msg)

    # Check if there is error in the message
    error_ind = msg_str.find('ERROR')
    
    if error_ind > 0:
        # The message returns an error
        raise ValueError(msg_str[error_ind:-1])
    else:
        # The message does not contain error
        return str(msg).split('"')[1:2][0].replace('\\', '')
        

def send_message(s, msg: str):
    s.sendall(bytearray(_hapticMaster_message(msg)))

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
    if device_state in ['init', 'off', 'force', 'position', 'home']:
        msg = 'set state ' + device_state
        return send_message(s, msg)
    else:
        raise ValueError('Wrong state name is given')

def create_spring(s, name: str, position: list, constant: float, direction: list, damp_factor: float, max_force: float):
    # First step, create the damper
    msg = 'create spring ' + name
    print(send_message(s, msg))

    # Second step, set the damping coefficient
    msg = 'set ' + name + ' pos ' + str(list(position)).replace(' ', '')
    print(send_message(s, msg))

    # Third step, set spring constant
    msg = 'set ' + name + ' stiffness ' + str(constant)
    print(send_message(s, msg))

    # Fourth step, set spring direction
    msg = 'set ' + name + ' direction ' + str(list(direction)).replace(' ', '')
    print(send_message(s, msg))

    # Fifth step, set spring dampfactor
    msg = 'set ' + name + ' dampfactor ' + str(damp_factor)
    print(send_message(s, msg))

    # Sixth step, set max spring force
    msg = 'set ' + name + ' maxforce ' + str(max_force)
    print(send_message(s, msg))

    # Seventh step, enable the spring
    msg = 'set ' + name + ' enable'
    print(send_message(s, msg))

def create_damper(s, name: str, coefficient: list):
    # First step, create the damper
    msg = 'create damper ' + name
    print(send_message(s, msg))

    # Second step, set the damping coefficient
    msg = 'set ' + name + ' dampcoef ' + str(list(coefficient)).replace(' ', '')
    print(send_message(s, msg))

    # Third step, enable the damper
    msg = 'set ' + name + ' enable'
    print(send_message(s, msg))

def set_inertia(s, value):
    msg = 'set inertia ' + str(value)
    print(send_message(s, msg))

def clear_all_effects(s):
    msg = 'remove all'
    print(send_message(s, msg))

def move_spring(s, name, position):
    # Second step, set the damping coefficient
    msg = 'set ' + name + ' pos ' + str(list(position)).replace(' ', '')
    print(send_message(s, msg))

if __name__ == '__main__':
    ip = '192.168.0.25'
    port = 7654

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))
        
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