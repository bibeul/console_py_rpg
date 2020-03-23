class Character:
    def __init__(self, hp, name, damage):
        self.hp = hp
        self.name = name
        self.damage = damage
        self.is_blocking = False

    def attack(self, target):
        if target.is_blocking:
            print("{} is blocking, no damage".format(target.name))
            target.is_blocking = False
        else:
            print("{} took {} damage from {}".format(target.name, self.damage, self.name))
            target.hp -= self.damage

    def defend(self):
        self.is_blocking = True

    def heal(self):
        self.hp += 5
