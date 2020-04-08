from lib.character import Character

class Superhero(Character):
    def super_strike(self, target):
        target.receive_damage(self.power * 10)
