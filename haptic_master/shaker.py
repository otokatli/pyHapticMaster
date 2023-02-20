class Shaker:
    def __init__(self, frequency1: float, frequency2: float,
                 direction: list, posmax: float, velmax: float,
                 accmax: float, stiffness: float, dampfactor: float,
                 deadband: float, maxforce: float) -> None:
        self._frequency1 = frequency1
        self._frequency2 = frequency2
        self._direction = direction
        self._posmax = posmax
        self._velmax = velmax
        self._accmax = accmax
        self._stiffness = stiffness
        self._dampfactor = dampfactor
        self._deadband = deadband
        self._maxforce = maxforce