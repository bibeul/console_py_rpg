from Models import Character
from Games import Combat

if __name__ == '__main__':
    p1 = Character(100, "oui", 10)
    p2 = Character(100, "non", 10)
    Combat(p1, p2)
