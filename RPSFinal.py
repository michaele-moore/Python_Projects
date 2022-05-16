import random


# validates player input


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print("Not a valid move, please try again.")


# valid game moves
move = ['rock', 'paper', 'scissors']


class Player:

    my_move = random.choice(move)
    their_move = random.choice(move)

    def move(self):
        return'rock'

    def learn(self, my_move, their_move):
        pass

# Human player input


class userPlayer(Player):

    def move(self):
        return valid_input("Rock, Paper, or Scissors?", move)

    def learn(self, my_move, their_move):
        pass


# Rock obsessed player subclass


class rockPlayer(Player):
    def move(self):
        return 'rock'

# Random player


class randomPlayer(Player):
    def move(self):
        return random.choice(move)

    def learn(self, my_move, their_move):
        pass
# Learning player


class learnPlayer(Player):
    def move(self):
        return self.their_move

    def learnMoves(self, my_move, their_move):
        self.their_move = their_move
        self.my_move = my_move
        

class cyclePlayer(Player):
    def __init__(self):
        self.my_next_move_index = random.randrange(3)

    def move(self):
        my_next_move = move[self.my_next_move_index]
        self.my_next_move_index = (self.my_next_move_index + 1) % 3
        return my_next_move


def beats(one, two):

    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    p1_score = 0
    p2_score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if move1 == move2:
            print("This round is a DRAW!\n"
                  f"Player 1 Score: {self.p1_score}\n"
                  f"Player 2 Score: {self.p2_score}")

        elif beats(move1, move2):
            self.p1_score += 1
            print("Player 1 Wins this round!\n"
                  f"Player 1 Score: {self.p1_score}\n"
                  f"Player 2 Score: {self.p2_score}")

        elif beats(move2, move1):
            self.p2_score += 1
            print("Player 2 wins this round!\n"
                  f"Player 1 Score: {self.p1_score}\n"
                  f"Player 2 Score: {self.p2_score}")

# gameplay
    def play_game(self):
        print("Let's play Rock, Paper, Scissors!")
        print("Best 2 out of 3 WINS!")
        for round in range(3):
            print(f"Round {round+1}:")
            self.play_round()
        print("Game over!")
# Winner
        if self.p1_score == self.p2_score:
            print("This game ends in a tie!\n"
                  f"Player 1 Score: {self.p1_score}\n"
                  f"Player 2 Score: {self.p2_score}")
        elif self.p1_score > self.p2_score:
            print(f"Player 1 wins the game!\nFinal Score: {self.p1_score}\n"
                  f"Play 2 Final Score: {self.p2_score}")
        if self.p1_score < self.p2_score:
            print(f"Player 2 wins the game!\nFinal Score: {self.p2_score}\n"
                  f"Player 1 Final Score: {self.p1_score}")


if __name__ == '__main__':
    randomGame = random.randint(0, 3)
    game = Game(userPlayer(), cyclePlayer())
    game.play_game()
