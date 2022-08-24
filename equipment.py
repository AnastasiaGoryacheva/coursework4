from dataclasses import dataclass
from typing import List, Optional
from random import uniform
import marshmallow_dataclass
import marshmallow
import json


@dataclass
class Armor:
    id: int
    name: str
    defence: float
    stamina_per_turn: float


@dataclass
class Weapon:
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    @property
    def damage(self):
        return round(uniform(self.min_damage, self.max_damage), 1)


@dataclass
class EquipmentData:
    armors: List[Armor]
    weapons: List[Weapon]


class Equipment:

    def __init__(self):
        self.equipment = self._get_equipment_data()

    def get_weapon(self, weapon_name) -> Optional[Weapon]:
        """
        возвращает объект оружия по имени
        """
        for weapon in self.equipment.weapons:
            if weapon_name == weapon.name:
                return weapon

    def get_armor(self, armor_name) -> Optional[Armor]:
        """
        возвращает объект брони по имени
        """
        for armor in self.equipment.armors:
            if armor_name == armor.name:
                return armor

    def get_weapons_names(self) -> list:
        """
        возвращаем список с оружием
        """
        return [weapons.name for weapons in self.equipment.weapons]

    def get_armors_names(self) -> list:
        """
        возвращаем список с броней
        """
        return [armors.name for armors in self.equipment.armors]

    @staticmethod
    def _get_equipment_data() -> EquipmentData:
        """
        этот метод загружает json в переменную EquipmentData
        """
        with open("./data/equipment.json", encoding='utf-8') as equipment_file:
            data = json.load(equipment_file)
            equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)
        try:
            return equipment_schema().load(data)
        except marshmallow.exceptions.ValidationError:
            raise ValueError
