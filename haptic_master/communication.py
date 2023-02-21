import socket
import re
from string import printable


def haptic_master_message(msg):
    hm_msg = [0, 0, 0, 0, 0, 0, 0, 0]
    
    # Convert msg to ascii dec
    decimal_msg = [ord(c) for c in msg]
    
    hm_msg[3] = len(decimal_msg)
    
    return hm_msg + decimal_msg

def haptic_master_response2(msg):
    # Decode the response from the server
    msg_str = msg.decode('utf-8')

    # Check if the response conveys error message
    if 'ERROR' in msg_str:
        raise Exception(msg_str)
    else:
        # Check if the response is a vector
        if '[' in msg_str and ']' in msg_str:
            return [float(s) for s in msg_str[msg_str.find('[')+1:msg_str.find(']')].split(',')]
        elif 'true' in msg_str:
            return True
        elif 'false' in msg_str:
            return False
        else:
            return "INFO: " + msg_str.replace('"', '')
            
def haptic_master_response(msg):
    msg_str = ''.join(c for c in msg.decode('ascii') if c in printable)
    # msg_str = msg.decode('ascii')
    
    if re.search('[a-zA-Z]', msg_str):
        return msg_str.replace('"', '')
    else:
        return msg_str

def send_message(s: socket, msg: str) -> str:
    s.sendall(bytearray(haptic_master_message(msg)))

    try:
        return haptic_master_response(s.recv(1024))
    except Exception as e:
        raise e