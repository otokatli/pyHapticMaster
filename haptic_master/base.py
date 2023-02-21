from dataclasses import dataclass, field


@dataclass
class Base:
    name: str
    pos: list = field(default_factory=lambda: [0.0, 0.0, 0.0])
    vel: list = field(default_factory=lambda: [0.0, 0.0, 0.0])
    att: list = field(default_factory=lambda: [0.0, 0.0, 0.0, 1.0])

    def get_pos_msg(self) -> str:
        return 'get ' + self.name + ' pos'
    
    def get_vel_msg(self) -> str:
        return 'get ' + self.name + ' vel'
    
    def get_att_msg(self) -> str:
        return 'get ' + self.name + ' att'
    
    def get_enable_msg(self) -> str:
        return 'get ' + self.name + ' enabled'
    
    def set_pos_msg(self, value: list) -> str:
        return 'set ' + self.name + ' pos ' + str(value).replace(' ', '')
    
    def set_vel_msg(self, value: list) -> str:
        return 'set ' + self.name + ' vel ' + str(value).replace(' ', '')
    
    def set_att_msg(self, value: list) -> str:
        'set ' + self.name + ' att ' + str(value).replace(' ', '')

    def set_enable_msg(self) -> str:
        return 'set ' + self.name + ' enable'
    
    def set_disable_msg(self) -> str:
        return 'set ' + self.name + ' disable'