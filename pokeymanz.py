class Pokeyman(object):
    def  __init__(self, poketype, HP, Attack, Defense, SAttack, SDefense, Speed, Luck):
        self.poketype = poketype
        self.HP = HP
        self.Attack = Attack
        self.Defense = Defense
        self.SAttack = SAttack
        self.SDefense = SDefense
        self.Speed = Speed
        self.Luck = Luck


class Squirtle(Pokeyman):
    def __init__(self):
        super().__init__("Water", 10, 5, 5, 5, 5, 5, 5)


class Charmander(Pokeyman):
    def __init__(self):
        super().__init__("Fire", 10, 5, 5, 5, 5, 5, 5)


class Bulbasaur(Pokeyman):
    def __init__(self):
        super().__init__("Grass", 10, 5, 5, 5, 5, 5, 5)


class Ratatta(Pokeyman):
    def __init__(self):
        super().__init__("Normal", 8, 4, 4, 4, 4, 7, 6)
