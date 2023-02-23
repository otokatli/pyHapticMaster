from .haptic_master import HapticMaster
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Base:
    name: str
    robot: HapticMaster

    def get_pos(self) -> list:
        msg = 'get ' + self.name + ' pos'

        return self.robot._string_to_list(self.robot.send_message(msg))

    def set_pos(self, value: list) -> bool:
        msg = 'set ' + self.name + ' pos ' + str(value).replace(' ', '')

        return 'Effect\'s position set' in self.robot.send_message(msg)

    def get_vel(self) -> list:
        msg = 'get ' + self.name + ' vel'

        return self.robot._string_to_list(self.robot.send_message(msg))

    def set_vel(self, value: list) -> bool:
        msg = 'set ' + self.name + ' vel ' + str(value).replace(' ', '')

        return 'Effect\'s velocity set' in self.robot.send_message(msg)

    def get_att(self) -> list:
        msg = 'get ' + self.name + ' att'

        return self.robot._string_to_list(self.robot.send_message(msg))

    def set_att(self, value: list) -> bool:
        msg = 'set ' + self.name + ' att ' + str(value).replace(' ', '')

        return 'Effect\'s attitude set' in self.robot.send_message(msg)

    def set_enable(self) -> bool:
        msg = 'set ' + self.name + ' enable'

        return 'enabled' in self.robot.send_message(msg)

    def set_disable(self) -> bool:
        msg = 'set ' + self.name + ' disable'

        return 'disabled' in self.robot.send_message(msg)

    def get_enabled(self) -> bool:
        msg = 'get ' + self.name + ' enabled'

        return self.robot._string_to_bool(self.robot.send_message(msg))

    def remove(self) -> bool:
        return 'Removed' in self.robot.send_message(f'remove {self.name}')
