
import random
import time

# Different Role
class Role():
    def __init__(self, name = "role_name"):
        self.name = name
        self.life = random.randint(100, 150)
        self.attack = random.randint(30, 50)

class Knight(Role):
    def __init__(self, name = "Knight"):
        Role.__init__(self, name)
        self.life = self.life * 5
        self.attack = self.attack * 3

    def fight_buff(self, opponent):
        if opponent.name == "Assassin":
            self.attack = int(self.attack * 1.5)

class Assassin(Role):
    def __init__(self, name = "Assassin"):
        Role.__init__(self, name)
        self.life = self.life * 3
        self.attack = self.attack * 5

    def fight_buff(self, opponent):
        if opponent.name == "Bowman":
            self.attack = int(self.attack * 1.5)

class Bowman(Role):
    def __init__(self, name = "Bowman"):
        Role.__init__(self, name)
        self.life = self.life * 4
        self.attack = self.attack * 4

    def fight_buff(self, opponent):
        if opponent.name ==  "Knight":
            self.attack = int(self.attack * 1.5)


class Game:
    def __init__(self):
        # attribute
        self.players = []
        self.enemies = []
        self.score = 0
        # function
        self.game_start()
        self.born_role()
        self.show_role()
        self.order_role()
        self.pk_role()
        self.show_result()

    # welcome
    def game_start(self):
        print('------------ Welcome to the pk game ------------')
        print('player role and NPC generating')
        input('press enter to continue')

    # 6 roles
    def born_role(self):
        for i in range(3):
            roles_player = [Knight(), Assassin(), Bowman()]
            self.players.append(random.choice(roles_player))
            roles_enemy = [Knight(), Assassin(), Bowman()]
            self.enemies.append(random.choice(roles_enemy))

    # Show the order
    def order_role(self):
        order_dict = {}
        for i in range(3):
            order = int(input('Which place do you want to put %s on battle？(enter 1~3)'% self.players[i].name))
            order_dict[order] = self.players[i]
        self.players = []
        for i in range(1,4):
            self.players.append(order_dict[i])
        print('\nYour order is ：%s、%s、%s'
        %(self.players[0].name,self.players[1].name,self.players[2].name))
        print('NPC order is：%s、%s、%s'
        %(self.enemies[0].name,self.enemies[1].name,self.enemies[2].name))

    # Show the role
    def show_role(self):
        print('----------------- Role information -----------------')
        print('Your team：')
        for i in range(3):
            print('『Player』%s Life：%s  Attack：%s' %
                  (self.players[i].name, self.players[i].life, self.players[i].attack))
        print('--------------------------------------------')

        print('Team of NPC：')
        for i in range(3):
            print('『NPC』%s Life：%s  Attack：%s' %
                  (self.enemies[i].name, self.enemies[i].life, self.enemies[i].attack))
        print('--------------------------------------------')

    def pk_role(self):
        for i in range(3):
            print('\n----------------- 【Round %s】 -----------------' % (i + 1))
            # buff
            self.players[i].fight_buff(self.enemies[i])
            self.enemies[i].fight_buff(self.players[i])
            input('\nAll is ready, press enter to continue')
            print('--------------------------------------------')

            while self.players[i].life > 0 and self.enemies[i].life > 0:
                self.enemies[i].life -= self.players[i].attack
                self.players[i].life -= self.enemies[i].attack
                print('Your %s is attacking，NPC %s life: %s' %
                      (self.players[i].name, self.enemies[i].name, self.enemies[i].life))
                print('NPC %s is attacking，Your %s life: %s' %
                      (self.enemies[i].name, self.players[i].name, self.players[i].life))
                print('--------------------------------------------')
                time.sleep(1)
            if self.players[i].life <= 0 and self.enemies[i].life > 0:
                print('\nYour %s lose！' % (self.players[i].name))
                self.score -= 1
            elif self.players[i].life > 0 and self.enemies[i].life <= 0:
                print('\ncongrats，your %s win!' % (self.players[i].name))
                self.score += 1
            else:
                print('\nDraw')

    # Show the final result
    def show_result(self):
        input('\nPress enter to see the final result\n')
        if self.score > 0:
            print('【Final Result】\n You win!')
        elif self.score == 0:
            print('【Final Result】\n No win and no lose!')
        else:
            print('【Final Result】\nYou lose。')



gp = Game()  # Run the game