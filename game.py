import random
class Player:
    def __init__(self,name):
        self.name = name
        self.health = 100
        self.attack = 10
        self.experience = 0
        self.level = 1
        self.inventory = []
    def perform_attack(self):
       damage = random.randint(5,15)
       return damage
    def take_damage(self,damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
    def level_up(self):

        if self.experience >= 100:
                self.level += 1
                self.experience = 0
                self.health += 20
                self.attack += 5
                print(f"{self.name} leveled up to level {self.level}!")
    def add_item(self,item):
        self.inventory.append(item)

    def use_item(self, item):
        if item in self.inventory:
                self.inventory.remove(item)
                self.health += 10
                print(f"Used {item}! Health: {self.health}")
        else:
                print(f"You don't have {item}!")

    def is_alive(self):
        return self.health > 0
    def display_stats(self):
        print("Health:",self.health)
        print("Experience:",self.experience)
        print("Level:",self.level)
        print("Inventory:",self.inventory)

player1 = Player("John")
player1.display_stats()
damage = player1.perform_attack()
print(f"Attack damage: {damage}")
player1.take_damage(20)
player1.display_stats()


class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def perform_attack(self):
        damage = random.randint(5,15)
        return damage
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
    def is_alive(self):
        return self.health > 0
    def display_stats(self):
        print("Health:",self.health)
        print("is_alive:",self.is_alive())

goblin = Enemy("Goblin", 30, 5)
goblin.display_stats()

damage = goblin.perform_attack()
print(f"Goblin attacks! Damage: {damage}")

goblin.take_damage(10)
goblin.display_stats()

print(f"Is goblin alive? {goblin.is_alive()}")


class Game:
    def __init__(self, player):
        self.player = player
        self.enemies = [
            Enemy("Goblin", 30, 5),
            Enemy("Orc", 50, 10),
            Enemy("Troll", 70, 15),
            Enemy("Dragon", 200, 25)
        ]

    def create_random_enemy(self):
        return random.choice(self.enemies)
    def battle(self, enemy):
        print(f"\n===== Battle: {enemy.name} =====")
        while self.player.is_alive() and enemy.is_alive():
            choice = input("\n1. Attack  2. Use Item  3. Run\nChoice: ")
            print(f"\nYour Health: {self.player.health}")
            print(f"{enemy.name} Health: {enemy.health}")


            if choice == "1":
                damage = self.player.perform_attack()
                enemy.take_damage(damage)
                print(f"You attack! Damage: {damage}")

            elif choice == "2":
                 item = input("Which item to use? ")
                 self.player.use_item(item)

            elif choice == "3":
                 print("You ran away!")
                 return

            if enemy.is_alive():
               damage = enemy.perform_attack()
               self.player.take_damage(damage)
               print(f"{enemy.name} attacks! Damage: {damage}")
            if self.player.is_alive():
               print(f"\n You defeated {enemy.name}!")
               self.player.experience += 50
               self.player.level_up()
            else:
                print("\n❌ You died! Game Over!")

    def run_game(self):
        print(f"Welcome {self.player.name}!")

        while self.player.is_alive():
            print("\n===== Main Menu =====")
            print("1. Fight")
            print("2. View Stats")
            print("3. Quit")

            choice = input("Choice: ")

            if choice == "1":
                enemy = self.create_random_enemy()
                self.battle(enemy)

            elif choice == "2":
                self.player.display_stats()

            elif choice == "3":
                print("Thanks for playing!")
                break

        print("Game Over!")
player = Player("Hero")
game = Game(player)
game.run_game()



