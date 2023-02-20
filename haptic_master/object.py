class Object:
    def __init__(self, name: str, position: list, velocity: list,
                 attitute: list, stiffness: float, dampfactor: float,
                 no_pull: bool, tangential_damping: float,
                 damping_forcemax: float, friction: float,
                 ejection_velmax: float, ejection_damping: float,
                 outward_forcemax: float, powermax: float) -> None:
        self._name = name
        self._pos = position
        self._vel = velocity
        self._att = attitute
        self._stiffness = stiffness
        self._dampfactor = dampfactor
        self._no_pull = no_pull
        self._tang_damping = tangential_damping
        self._damping_forcemax = damping_forcemax
        self._friction = friction
        self._ejection_velmax = ejection_velmax
        self._ejection_damping = ejection_damping
        self._outward_forcemax = outward_forcemax
        self._powermax = powermax

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
        self.att = new_attitude
    
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
    def no_pull(self) -> bool:
        return self._no_pull
    
    @no_pull.setter
    def no_pull(self, new_condition: bool) -> None:
        self._no_pull = new_condition

    @property
    def tang_damping(self) -> float:
        return self._tang_damping
    
    @tang_damping.setter
    def tang_damping(self, new_damping: float) -> None:
        self._tang_damping = new_damping

    @property
    def damping_forcemax(self) -> float:
        return self._damping_forcemax
    
    @damping_forcemax.setter
    def damping_forcemax(self, new_max_force: float) -> None:
        self._damping_forcemax = new_max_force

    @property
    def friction(self) -> float:
        return self._friction
    
    @friction.setter
    def friction(self, new_friction: float) -> None:
        self._friction = new_friction

    @property
    def ejection_velmax(self) -> float:
        return self._ejection_velmax
    
    @ejection_velmax.setter
    def ejection_velmax(self, new_max_vel: float) -> None:
        self._ejection_velmax = new_max_vel

    @property
    def ejection_damping(self) -> float:
        return self._ejection_damping
    
    @ejection_damping.setter
    def ejection_damping(self, new_damping: float) -> None:
        self._ejection_damping = new_damping

    @property
    def outward_forcemax(self) -> float:
        return self._outward_forcemax
    
    @outward_forcemax.setter
    def outward_forcemax(self, new_force: float) -> None:
        self._outward_forcemax = new_force

    @property
    def powermax(self) -> float:
        return self._powermax
    
    @powermax.setter
    def powermax(self, new_power: float) -> None:
        self._powermax = new_power


class Block(Object):
    def __init__(self, name: str, position: list, velocity: list,
                 attitute: list, stiffness: float, dampfactor: float,
                 no_pull: bool, tangential_damping: float,
                 damping_forcemax: float, friction: float,
                 ejection_velmax: float, ejection_damping: float,
                 outward_forcemax: float, powermax: float,
                 size: list) -> None:
        super().__init__(name, position, velocity, attitute, stiffness,
                         dampfactor, no_pull, tangential_damping,
                         damping_forcemax, friction, ejection_velmax,
                         ejection_damping, outward_forcemax, powermax)
        self._size = size

        @property
        def size(self) -> list:
            return self._size
        
        @size.setter
        def size(self, new_size: list) -> None:
            self._size = new_size


class Sphere(Object):
    def __init__(self, name: str, position: list, velocity: list,
                 attitute: list, stiffness: float, dampfactor: float,
                 no_pull: bool, tangential_damping: float,
                 damping_forcemax: float, friction: float,
                 ejection_velmax: float, ejection_damping: float,
                 outward_forcemax: float, powermax: float,
                 radius: float) -> None:
        super().__init__(name, position, velocity, attitute, stiffness,
                         dampfactor, no_pull, tangential_damping,
                         damping_forcemax, friction, ejection_velmax,
                         ejection_damping, outward_forcemax, powermax)
        self._radius = radius

    @property
    def radius(self) -> float:
        return self._radius
    
    @radius.setter
    def radius(self, new_radius: float) -> None:
        self._radius = new_radius


class FlatPlane(Object):
    def __init__(self, name: str, position: list, velocity: list,
                 attitute: list, stiffness: float, dampfactor: float,
                 no_pull: bool, tangential_damping: float,
                 damping_forcemax: float, friction: float,
                 ejection_velmax: float, ejection_damping: float,
                 outward_forcemax: float, powermax: float,
                 normal: list) -> None:
        super().__init__(name, position, velocity, attitute, stiffness,
                         dampfactor, no_pull, tangential_damping,
                         damping_forcemax, friction, ejection_velmax,
                         ejection_damping, outward_forcemax, powermax)
        self._normal = normal

    @property
    def normal(self) -> list:
        return self._normal
    
    @normal.setter
    def normal(self, new_normal: list) -> None:
        self._normal = new_normal


class Cylinder(Object):
    def __init__(self, name: str, position: list, velocity: list,
                 attitute: list, stiffness: float, dampfactor: float,
                 no_pull: bool, tangential_damping: float,
                 damping_forcemax: float, friction: float,
                 ejection_velmax: float, ejection_damping: float,
                 outward_forcemax: float, powermax: float,
                 radius: float, length: float) -> None:
        super().__init__(name, position, velocity, attitute, stiffness,
                         dampfactor, no_pull, tangential_damping,
                         damping_forcemax, friction, ejection_velmax,
                         ejection_damping, outward_forcemax, powermax)
        self._radius = radius
        self._length = length

    @property
    def radius(self) -> float:
        return self._radius
    
    @radius.setter
    def radius(self, new_radius: float) -> None:
        self._radius = new_radius
    
    @property
    def length(self) -> float:
        return self._length
    
    @radius.setter
    def length(self, new_length: float) -> None:
        self._length = new_length


class Torus(Object):
    def __init__(self, name: str, position: list, velocity: list,
                 attitute: list, stiffness: float, dampfactor: float,
                 no_pull: bool, tangential_damping: float,
                 damping_forcemax: float, friction: float,
                 ejection_velmax: float, ejection_damping: float,
                 outward_forcemax: float, powermax: float,
                 ring_radius: float, tube_radius: float) -> None:
        super().__init__(name, position, velocity, attitute, stiffness,
                         dampfactor, no_pull, tangential_damping,
                         damping_forcemax, friction, ejection_velmax,
                         ejection_damping, outward_forcemax, powermax)
        self._ring_radius = ring_radius
        self._tube_radius = tube_radius
    
    @property
    def ring_radius(self) -> float:
        return self._ring_radius
    
    @ring_radius.setter
    def ring_radius(self, new_radius: float) -> None:
        self._ring_radius = new_radius
    
    @property
    def tube_radius(self) -> float:
        return self._tube_radius
    
    @tube_radius.setter
    def tube_radius(self, new_radius: float) -> None:
        self._tube_radius = new_radius
