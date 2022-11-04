

class Buff:

    def __init__(self) -> None:
        # CALCULATE PERCENTAGE
        self._health_percent = 0
        self._mana_percent = 0
        self._atk_percent = 0
        self._dodge_percent = 0
        self._def_percent = 0
        self._light_percent = 0
        self._fire_percent = 0
        self._water_percent = 0
        self._stone_percent = 0
        self._wind_percent = 0

        # TURNS
        self._present_turn = 0
        self._max_turn = 0
        self._destructible = False

        # BEFORE EFFECT
        self._max_hp = 0
        self._max_mana = 0
        self._atk = 0
        self._dodge = 0
        self._def = 0
        self._light = 0
        self._fire = 0
        self._water = 0
        self._stone = 0
        self._wind = 0

    def set_percentage(self, percent: float, type: str) -> None:  # CALCULATE THE PERCENTAGE
        if type == 'FIRE':
            pass
        elif type == 'WATER':
            pass
        elif type == 'STONE':
            pass
        elif type == 'WIND':
            pass
        elif type == 'LIGHT':
            pass
        elif type == 'DEF':
            pass
        elif type == 'ATK':
            pass
        elif type == 'DODGE':
            pass
        elif type == 'HEALTH':
            pass
        elif type == 'MANA':
            pass

    def update_turn(self) -> None:  # UPDATE TURN
        if self._present_turn <= self._max_turn:
            self._present_turn += 1
        else:
            self._destructible = True

    def get_destruction(self) -> bool:
        return self._destructible
