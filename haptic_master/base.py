from .communication import send_message
import socket


class Base:
    def __init__(self) -> None:
        pass
    
    def get_pos(self, s: socket) -> list:
        msg = 'get ' + self.name + ' pos'

        return send_message(s, msg)

    def get_vel(self) -> str:
        return 'get ' + self.name + ' vel'
    
    def get_att(self) -> str:
        return 'get ' + self.name + ' att'
    
    def get_enable(self) -> str:
        return 'get ' + self.name + ' enabled'
    
    def set_pos(self, value: list) -> str:
        return 'set ' + self.name + ' pos ' + str(value).replace(' ', '')
    
    def set_vel(self, value: list) -> str:
        return 'set ' + self.name + ' vel ' + str(value).replace(' ', '')
    
    def set_att(self, value: list) -> str:
        'set ' + self.name + ' att ' + str(value).replace(' ', '')

    def set_enable(self) -> str:
        return 'set ' + self.name + ' enable'
    
    def set_disable(self) -> str:
        return 'set ' + self.name + ' disable'