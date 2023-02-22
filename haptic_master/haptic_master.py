import socket
from typing import Tuple
import re
import logging
from string import printable



class HapticMaster:
    def __init__(self, ip: str, port: int, inertia_value: float = 0.0) -> None:
        self._ip = ip
        self._port = port
        self._inertia = inertia_value
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    @property
    def address(self) -> Tuple[str, int]:
        return (self._ip, self._port)

    @property
    def sock(self):
        return self._socket
    
    # @property
    # def inertia(self) -> float:
    #     return self._inertia

    # @inertia.setter
    # def inertia(self, new_inertia: float):
    #     self._inertia = new_inertia
    #     msg = 'set inertia ' + str(new_inertia)
    #     print(send_message(self._socket, msg))

    def connect(self):
        try:
            # Connect to the robot
            self._socket.connect((self._ip, self._port))

        except socket.error:
            logging.error('Connection error')

    def disconnect(self):
        # Clear all haptic effects
        msg = 'remove all'
        logging.info(self.send_message(msg))

        # Close connection
        self._socket.close()

    def get_inertia(self) -> float:
        msg = 'get inertia'

        return float(self.send_message(msg))
    
    def set_inertia(self, value: float) -> bool:
        msg = 'set inertia ' + str(value)
        
        response = self.send_message(msg)

        logging.info(response)

        return True 

    def set_state(self, device_state):
        if device_state in ['init', 'off', 'force', 'position', 'home']:
            msg = 'set state ' + device_state
            return self.send_message(msg)
        else:
            raise ValueError('Wrong state name is given')
        
    def _haptic_master_message(self, msg):
        hm_msg = [0, 0, 0, 0, 0, 0, 0, 0]
        
        # Convert msg to ascii dec
        decimal_msg = [ord(c) for c in msg]
        
        hm_msg[3] = len(decimal_msg)
        
        return hm_msg + decimal_msg
    
    def _haptic_master_response(self, msg):
        msg_str = ''.join(c for c in msg.decode('ascii') if c in printable)
        
        if re.search('[a-zA-Z]', msg_str):
            return msg_str.replace('"', '')
        else:
            return msg_str

    def send_message(self, msg: str) -> str:
        self._socket.sendall(bytearray(self._haptic_master_message(msg)))

        try:
            return self._haptic_master_response(self._socket.recv(1024))
        except Exception as e:
            raise e
