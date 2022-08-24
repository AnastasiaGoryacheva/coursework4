from dataclasses import dataclass

from skills import Skill, FuryPunch, HardShot


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass = UnitClass(
    name="Воин",
    max_health=100.0,
    max_stamina=30.0,
    attack=1.8,
    stamina=0.7,
    armor=1.2,
    skill=FuryPunch(),
)

ThiefClass = UnitClass(
    name="Вор",
    max_health=80.0,
    max_stamina=15.0,
    attack=0.9,
    stamina=1.4,
    armor=0.3,
    skill=HardShot(),
)

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}
