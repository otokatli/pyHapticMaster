from haptic_master.base import Base
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Effect(Base):
    pass


@dataclass(frozen=True, slots=True)
class Spring(Effect):
    def create(self) -> bool:
        msg = 'create spring ' + self.name

        return f'Effect spring with name {self.name} created' in self.robot.send_message(msg)

    def get_stiffness(self) -> float:
        msg = 'get ' + self.name + ' stiffness'

        return float(self.robot.send_message(msg))

    def set_stiffness(self, value: float) -> bool:
        msg = 'set ' + self.name + ' stiffness ' + str(value)

        return 'Spring\'s stiffness set' in self.robot.send_message(msg)

    def get_dampfactor(self) -> float:
        msg = 'get ' + self.name + ' dampfactor'

        return float(self.robot.send_message(msg))

    def set_dampfactor(self, value: float) -> bool:
        msg = 'set ' + self.name + ' dampfactor ' + str(value)

        return 'Spring\'s damp factor set' in self.robot.send_message(msg)

    def get_deadband(self) -> float:
        msg = 'get ' + self.name + ' deadband'

        return float(self.robot.send_message(msg))

    def set_deadband(self, value: float) -> bool:
        msg = 'set ' + self.name + ' deadband ' + str(value)

        return 'Spring\'s deadband set' in self.robot.send_message(msg)

    def get_direction(self) -> list:
        msg = 'get ' + self.name + ' direction'

        return self.robot.string_to_list(self.robot.send_message(msg))

    def set_direction(self, value: list) -> bool:
        msg = 'set ' + self.name + ' direction ' + str(value).replace(' ', '')

        return 'Spring\'s direction set' in self.robot.send_message(msg)

    def get_maxforce(self) -> float:
        msg = 'get ' + self.name + ' maxforce'

        return float(self.robot.send_message(msg))

    def set_maxforce(self, value: float) -> bool:
        msg = 'set ' + self.name + ' maxforce ' + str(value)

        return 'Spring\'s maximum force set' in self.robot.send_message(msg)

    def get_dampglobal(self) -> bool:
        msg = 'get ' + self.name + ' dampglobal'

        return self.robot.string_to_bool(self.robot.send_message(msg))

    def set_dampglobal(self, value: bool) -> bool:
        msg = 'set ' + self.name + ' dampglobal ' + str(value).lower()

        return 'Spring\'s damping global set' in self.robot.send_message(msg)


@dataclass(frozen=True, slots=True)
class Damper(Effect):
    def create(self) -> bool:
        msg = 'create damper ' + self.name

        return f'Effect damper with name {self.name} created' in self.robot.send_message(msg)

    def get_dampcoef(self) -> list:
        msg = 'get ' + self.name + ' dampcoef'

        return self.robot.string_to_list(self.robot.send_message(msg))

    def set_dampcoef(self, value: list) -> bool:
        msg = 'set ' + self.name + ' dampcoef ' + str(value).replace(' ', '')

        return 'Damper\'s damp coefficient set' in self.robot.send_message(msg)


@dataclass(frozen=True, slots=True)
class BiasForce(Effect):
    def create(self) -> bool:
        msg = 'create biasforce ' + self.name

        return f'Effect biasforce with name {self.name} created' in self.robot.send_message(msg)

    def get_force(self) -> list:
        msg = 'get ' + self.name + ' force'

        return self.robot.string_to_list(self.robot.send_message(msg))

    def set_force(self, value: list) -> bool:
        msg = 'set ' + self.name + ' force ' + str(value).replace(' ', '')

        return 'Bias force\'s force set' in self.robot.send_message(msg)

