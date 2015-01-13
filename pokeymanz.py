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
