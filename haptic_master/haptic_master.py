import socket
from typing import Tuple
import re
import logging
from string import printable
from dataclasses import dataclass, field


@dataclass(frozen=True)
class HapticMaster:
    ip: str
    port: int
    sock: socket = field(default_factory=lambda: socket.socket(socket.AF_INET, socket.SOCK_STREAM))

    def connect(self):
        try:
            # Connect to the robot
            self.sock.connect((self.ip, self.port))

        except socket.error:
            logging.error('Connection error')

    def disconnect(self):
        # Clear all haptic effects
        msg = 'remove all'
        logging.info(self.send_message(msg))

        # Close connection
        self.sock.close()

    def get_inertia(self) -> float:
        msg = 'get inertia'

        return float(self.send_message(msg))

    def set_inertia(self, value: float) -> bool:
        msg = 'set inertia ' + str(value)

        response = self.send_message(msg)

        logging.info(response)

        return True

    def get_state(self) -> str:
        msg = 'get state'

        return self.send_message(msg)

    def set_state(self, device_state):
        if device_state in ['init', 'off', 'force', 'position', 'home']:
            msg = 'set state ' + device_state
            return self.send_message(msg)
        raise ValueError('Wrong state name is given')

    def get_coulombfriction(self) -> float:
        msg = 'get coulombfriction'

        return float(self.send_message(msg))

    def set_coulombfriction(self, value: float) -> bool:
        msg = 'set coulombfriction ' + str(value)

        return 'Coulomb friction set' in self.send_message(msg

    def get_measpos(self) -> list:
        msg = 'get measpos'

        return self.string_to_list(self.send_message(msg))

    def get_measforce(self) -> list:
        msg = 'get measforce'

        return self.string_to_list(self.send_message(msg))

    def get_modelpos(self) -> list:
        msg = 'get modelpos'

        return self.string_to_list(self.send_message(msg))

    def get_modelvel(self) -> list:
        msg = 'get modelvel'

        return self.string_to_list(self.send_message(msg))

    def get_modelacc(self) -> list:
        msg = 'get modelacc'

        return self.string_to_list(self.send_message(msg))

    def get_measposjoint(self) -> list:
        msg = 'get measposjoint'

        return self.string_to_list(self.send_message(msg))

    def get_measforcejoint(self) -> list:
        msg = 'get measforcejoint'

        return self.string_to_list(self.send_message(msg))

    def get_modelposjoint(self) -> list:
        msg = 'get modelposjoint'

        return self.string_to_list(self.send_message(msg))

    def get_modelveljoint(self) -> list:
        msg = 'get modelveljoint'

        return self.string_to_list(self.send_message(msg))

    def get_modelaccjoint(self) -> list:
        msg = 'get modelaccjoint'

        return self.string_to_list(self.send_message(msg))

    def get_force_calibrated(self) -> bool:
        msg = 'get force_calibrated'

        return self.string_to_bool(self.send_message(msg))

    def get_position_calibrated(self) -> bool:
        msg = 'get position_calibrated'

        return self.string_to_bool(self.send_message(msg))

    def get_workspace_r(self) -> list:
        msg = 'get workspace_r'

        return self.string_to_list(self.send_message(msg))

    def get_workspace_phi(self) -> list:
        msg = 'get workspace_phi'

        return self.string_to_list(self.send_message(msg))

    def get_workspace_z(self) -> list:
        msg = 'get workspace_z'

        return self.string_to_list(self.send_message(msg))

    def calibrateforcesensor(self) -> bool:
        return 'Force sensor calibrated' in self.send_message('calibrateforcesensor')

    def _haptic_master_message(self, msg):
        hm_msg = [0, 0, 0, 0, 0, 0, 0, 0]

        # Convert msg to ascii dec
        decimal_msg = [ord(c) for c in msg]

        hm_msg[3] = len(decimal_msg)

        return hm_msg + decimal_msg

    def _haptic_master_response(self, msg):
        msg_str = ''.join(c for c in msg.decode('ascii') if c in printable)

        if re.search('[a-zA-Z]', msg_str):
            return msg_str.replace('"', '').replace('\n', '')

        return msg_str

    def send_message(self, msg: str) -> str:
        self.sock.sendall(bytearray(self._haptic_master_message(msg)))

        try:
            return self._haptic_master_response(self.sock.recv(1024))
        except Exception as e:
            raise e

    def string_to_list(self, s: str):
        return [float(si) for si in s[s.find('[')+1:s.find(']')].split(',')]

    def string_to_bool(self, s: str):
        return True if 'true' in s else False
