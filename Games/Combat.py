class Combat:
    def __init__(self, player, foe, two_player=False):
        self.is_two_player = two_player
        self.foe = foe
        self.player = player
        self.round = 0
        self.current_player = player
        self.other_player = foe
        self.start_combat()

    def start_combat(self):
        print("Combat start")
        round = 0
        while self.player.hp > 0 and self.foe.hp > 0:
            if round % 2 == 0 or self.is_two_player:
                print("player turn, type attack, defend, heal or quit")
                action = input()
                self.handle_action(action)
                self.current_player = self.foe
                self.other_player = self.player
            else:
                self.handle_action("attack")
                self.current_player = self.player
                self.other_player = self.foe
            round += 1

    def handle_action(self, action):
        if action == "attack":
            self.current_player.attack(self.other_player)
            self.round += 1
        elif action == "defend":
            self.current_player.defend()
            self.round += 1
        elif action == "heal":
            self.current_player.heal()
            self.round += 1
        elif action == "quit":
            exit(0)
        elif action == "help":
            self.display_info()
        else:
            print("no such command")

    def display_info(self):
        print("To play an action, type attack, defend or heal.")
        print("If you want to quit during your turn type quit.")
        print("You have {}hp and doing {} damage".format(self.current_player.hp, self.current_player.damage))
        print("Your opponent have {}hp and do {} damage".format(self.other_player.hp, self.other_player.damage))
