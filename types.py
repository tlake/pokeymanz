<<<<<<< HEAD
type_chart = {
    "Fire": {
        "Str": ["Grass"],
        "Wea": ["Water"]
        }
    "Grass": {
        "Str": ["Water"],
        "Wea": ["Fire"]
        }
    "Water": {
        "Str": ["Fire"],
        "Wea": ["Grass"]
        }
}
=======
class PokeType(object):
    pass



class Fire(PokeType):

    poke_type = ["Fire"]
    strengths = ["Grass"]
    weaknesses = ["Water"]



class Grass(PokeType):

    poke_type = ["Grass"]
    strengths = ["Water"]
    weaknessess = ["Fire"]



class Water(PokeType):

    poke_type = ["Water"]




>>>>>>> fe7b44c177bd679fe0c545b73244997704148aef
