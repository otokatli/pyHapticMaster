from dataclasses import dataclass
from .effect import Effect


@dataclass(frozen=True, slots=True)
class Shaker(Effect):
    def create(self):
        msg = 'create shaker ' + self.name

        return f'Effect shaker with name {self.name} created' in self.robot.send_message(msg)
    

    def get_frequency1(self) -> float:
        msg =  'get ' + self.name + ' frequency1'
    
        return float(self.robot.send_message(msg))

    def set_frequency1(self, value: float) -> bool:
        msg =  'set ' + self.name + ' frequency1 ' + str(value)

        return 'Shaker\'s frequency1 set' in self.robot.send_message(msg)
    
    def get_frequency2(self) -> float:
        msg =  'get ' + self.name + ' frequency2'
    
        return float(self.robot.send_message(msg))

    def set_frequency2(self, value: float) -> bool:
        msg =  'set ' + self.name + ' frequency2 ' + str(value)
    
        return 'Shaker\'s frequency2 set' in self.robot.send_message(msg)
    
    def get_direction(self) -> list:
        msg =  'get ' + self.name + ' direction'
    
        return self.robot._string_to_list(self.robot.send_message(msg))

    def set_direction(self, value: list) -> bool:
        msg =  'set ' + self.name + ' direction ' + str(value).replace(' ', '')
    
        return 'Shaker\'s direction set' in self.robot.send_message(msg)
    
    def get_posmax(self) -> float:
        msg =  'get ' + self.name + ' posmax'
    
        return float(self.robot.send_message(msg))

    def set_posmax(self, value: float) -> bool:
        msg =  'set ' + self.name + ' posmax ' + str(value)
    
        return 'Shaker\'s maximum position set' in self.robot.send_message(msg)
    
    def get_velmax(self) -> float:
        msg =  'get ' + self.name + ' velmax'
    
        return float(self.robot.send_message(msg))

    def set_velmax(self, value: float) -> bool:
        msg =  'set ' + self.name + ' velmax ' + str(value)
    
        return 'Shaker\'s maximum velocity set' in self.robot.send_message(msg)
    
    def get_accmax(self) -> float:
        msg =  'get ' + self.name + ' accmax'
    
        return float(self.robot.send_message(msg))

    def set_accmax(self, value: float) -> bool:
        msg =  'set ' + self.name + ' accmax ' + str(value)
    
        return 'Shaker\'s maximum acceleration set' in self.robot.send_message(msg)
    
    def get_stiffness(self) -> float:
        msg =  'get ' + self.name + ' stiffness'
    
        return float(self.robot.send_message(msg))

    def set_stiffness(self, value: float) -> bool:
        msg =  'set ' + self.name + ' stiffness ' + str(value)
    
        return 'Shaker\'s stiffness set' in self.robot.send_message(msg)
    
    def get_dampfactor(self) -> float:
        msg =  'get ' + self.name + ' dampfactor'
    
        return float(self.robot.send_message(msg))

    def set_dampfactor(self, value: float) -> bool:
        msg =  'set ' + self.name + ' dampfactor ' + str(value)
    
        return 'Shaker\'s damp factor set' in self.robot.send_message(msg)
    
    def get_deadband(self) -> float:
        msg =  'get ' + self.name + ' deadband'
    
        return float(self.robot.send_message(msg))

    def set_deadband(self, value: float) -> bool:
        msg =  'set ' + self.name + ' deadband ' + str(value)
    
        return 'Shaker\'s deadband set' in self.robot.send_message(msg)
    
    def get_maxforce(self) -> float:
        msg =  'get ' + self.name + ' maxforce'
    
        return float(self.robot.send_message(msg))

    def set_maxforce(self, value: float) -> bool:
        msg =  'set ' + self.name + ' maxforce ' + str(value)

        return 'Shaker\'s maximum force set' in self.robot.send_message(msg)
