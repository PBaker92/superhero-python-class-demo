from lib.character import Character

# Villain is a subclass of Character
# Villain inherits from Character
# Character is the super class of Villain
class Villain(Character):
    def receive_damage(self, how_much):
        self.health -= how_much
        if self.health <= 0:
            self.health = 5
