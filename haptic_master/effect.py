class Effect:
    def __init__(self, name:str, position: list = [0.0, 0.0, 0.0],
                 velocity: list = [0.0, 0.0, 0.0],
                 attitude: list = [0.0, 0.0, 0.0, 1.0]) -> None:
        self._name = name
        self._pos = position
        self._vel = velocity
        self._att = attitude
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def pos(self) -> list:
        return self._pos
    
    @pos.setter
    def pos(self, new_position: list) -> None:
        self._pos = new_position

    @property
    def vel(self) -> list:
        return self._vel
    
    @vel.setter
    def vel(self, new_velocity: list) -> None:
        self._vel = new_velocity

    @property
    def att(self) -> list:
        return self._att
    
    @att.setter
    def att(self, new_attitude: list) -> None:
        self._att = new_attitude

    
class Spring(Effect):
    def __init__(self, name: str, position: list, velocity: list, attitude: list,
                 stiffness: float, dampfactor: float, deadband: float,
                 direction: list, maxforce: float, dampglobal: bool) -> None:
        super().__init__(name, position, velocity, attitude)
        self._stiffness = stiffness
        self._dampfactor = dampfactor
        self._deadband = deadband
        self._direction = direction
        self._maxforce = maxforce
        self._dampglobal = dampglobal
    
    @property
    def stiffness(self) -> float:
        return self._stiffness
    
    @stiffness.setter
    def stiffness(self, new_stiffness: float) -> None:
        self._stiffness = new_stiffness

    @property
    def dampfactor(self) -> float:
        return self._dampfactor
    
    @dampfactor.setter
    def dampfactor(self, new_dampfactor: float) -> None:
        self._dampfactor = new_dampfactor
    
    @property
    def deadband(self) -> float:
        return self._dampfactor
    
    @deadband.setter
    def deadband(self, new_length: float) -> None:
        self._deadband = new_length
    
    @property
    def direction(self) -> list:
        return self._direction
    
    @direction.setter
    def direction(self, new_direction: list) -> None:
        self._direction = new_direction
    
    @property
    def maxforce(self) -> float:
        return self._maxforce
    
    @maxforce.setter
    def maxforce(self, new_maxforce: float) -> None:
        self._maxforce = new_maxforce

    @property
    def dampglobal(self) -> float:
        return self._dampglobal
    
    @dampglobal.setter
    def dampglobal(self, new_dampglobal: bool) -> None:
        self._dampglobal = new_dampglobal


class Damper(Effect):
    def __init__(self, name: str, position: list, velocity: list, attitude: list,
                 dampcoef: list) -> None:
        super().__init__(name, position, velocity, attitude)
        self._dampcoef = dampcoef

    @property
    def dampcoef(self) -> list:
        return self._dampcoef
    
    @dampcoef.setter
    def dampcoef(self, new_dampcoef: list) -> None:
        self._dampcoef = new_dampcoef


class BiasForce(Effect):
    def __init__(self, name: str, position: list, velocity: list, attitude: list,
                 force: list) -> None:
        super().__init__(name, position, velocity, attitude)
        self._force = force

    @property
    def force(self) -> list:
        return self._force
    
    @force.setter
    def force(self, new_force: list) -> None:
        self._force = new_force
