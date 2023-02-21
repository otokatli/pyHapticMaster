import socket
from typing import Tuple
from .communication import send_message
import logging


class HapticMaster:
    def __init__(self, ip: str, port: int, inertia_value: float = 0.0) -> None:
        self._ip = ip
        self._port = port
        self._inertia = inertia_value
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    @property
    def address(self) -> Tuple[str, int]:
        return (self._ip, self._port)

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
        logging.info(send_message(self._socket, msg))

        # Close connection
        self._socket.close()

    def get_inertia(self) -> float:
        msg = 'get inertia'

        return float(send_message(self._socket, msg))
    
    def set_inertia(self, value: float) -> bool:
        msg = 'set inertia ' + str(value)
        
        response = send_message(self._socket, msg)

        logging.info(response)

        return True 

    def set_state(self, device_state):
        if device_state in ['init', 'off', 'force', 'position', 'home']:
            msg = 'set state ' + device_state
            return send_message(self._socket, msg)
        else:
            raise ValueError('Wrong state name is given')
