
# By Mohamed Eraky
"""
In order to run this on your computer, you need to put the game.py and a folder contains all music tracks name sounds.
----->>> You need to pip install pygame <<<--- for music playing
Hello welcome to Mini-go-->Fish card game.
Rules are simple:
Example game:
The game asks you for the number of cards to be dealt for each player, we will choose for example 3
The game asks you for how many books for the game to be completed.
A book is simply two cards of the same rank, suit doesn't matter!

the player asks the second player to give him the card with a rank to complete a book, if the other player doesn't have
he simply say " Go fish"
so the player draws one card from the deck!!

Once a book is completed a music is played!

Background music is playing all the game and victory music runs once at the end

"""
# Some of the feature added to the game:
# 1- Game statistics display upon completion
# 2- music running, another music runs when a player completes a book
# Cards are hidden from the other player, the other player can only know how many cards the opponent has --> exactly as in real life.

import random
# pip install pygame
import pygame
import os
class Card:
    # class of card, each card is represented with suit and rank
    # List of suits and ranks
    suit_list = ["Clubs", "Diamond", "Hearts", "Spades"]
    rank_list = ["None", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        # initalize card with suit and rank, default is at suit 0 and rank 2.
        # suit and rank is defined by index according to the list.
        self.suit = suit
        self.rank = rank

    def __str__(self):
        # to overload print, basically it prints the rank and the suit, for example: 2 of clubs
        return self.rank_list[self.rank] + " of " + self.suit_list[self.suit]

    def __eq__(self, other):
        # overloading =
        return self.rank == other.rank

    def __gt__(self, other):
        # overloading >
        if self.suit > other.suit:
            # compare based on the suit first if they are eof equal suits they compare by rank.
            return True
        elif self.suit == other.suit:
            if self.rank > other.rank:
                return True
        return False


class Deck:
    def __init__(self):
        self.cards = []
        # make a deck of 52 cards by looping
        for i in range(4):  # Number of suits
            for j in range(1, 14):  # 13 cards
                self.cards.append(Card(i, j))

    def shuffle(self):  # shuffle cards
        # this is old code given in the lecture
        # n_cards = len(self.cards)
        # for i in range(n_cards):  #loop over cards and shuffle by swapping using random numbers
        #     j = random.randrange(0, 1,n_cards)
        #     self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
        random.shuffle(self.cards)

    def pop_card(self):
        # pop top card
        return self.cards.pop()

    def is_empty(self):
        #  deck is empty check
        return len(self.cards) == 0

    def deal(self, n_players, n_cards=3):
        # change n_cards to control how many cards handed to each player, for mini go fish
        # I choose only 3 cards
        # Deal n_cards to each player,

        for hand in n_players:
            for j in range(n_cards):
                if self.is_empty():
                    break
                # Get a card from the deck
                card = self.pop_card()
                hand.add_card(card)


class Hand:
    def __init__(self, name=""):
        # Init new hand for a player
        self.cards = []  # empty list to store the player's current hand of cards
        self.name = name  # the name of the player
        self.books = []  # empty list to store completed books
        self.books_completed = 0 # to keep track of completed books

    def add_card(self, card):
        self.cards.append(card)

    def remove_rank(self, rank):
        # collect the cards in matches list if they match what is asked for, using list comprehension
        matches = [i for i in self.cards if i.rank == rank]
        # update the cards in player's hand for example if there is any card given away this round, it has to be removed
        self.cards = [j for j in self.cards if j.rank != rank]
        return matches

    def check_books(self):
        ranks = {}  # keep track of how many times each rank appears
        for i in self.cards:
            # make dictionary of each rank and its count
            # for example {5: 2, 7: 1}
            ranks[i.rank] = ranks.get(i.rank, 0) + 1
        # split the dictionary into items
        for r, count in list(ranks.items()):
            # if the count of similar cards = 2 or greater store this in a book
            if count >= 2 and r not in self.books:
                self.books.append(r)
                self.books_completed += 1
                print(f"{self.name} completed a book of {Card.rank_list[r]}s")

                # this counter " removed" counts how many cards are removed
                removed = 0
                # new player hands
                new_hand = []
                for c in self.cards:
                    if c.rank == r and removed < 2:
                        removed += 1
                    else:
                        #  append cards that are not in the book
                        new_hand.append(c)
                self.cards = new_hand
                return True
        return False

    def has_rank(self, rank):
        # this function checks if the player  has the requested rank
        for c in self.cards:
            if c.rank == rank:
                return True
        return False

    def __str__(self, reveal=False):
        if reveal:
            if self.cards:
                hand_have = ", ".join(str(c) for c in self.cards)
                return f"Hand of {self.name}: [[ {hand_have} ]]"
            return f"Hand of {self.name} is empty"
        else:
            # hide the cards from the opponent
            return f"Hand of {self.name}: [[ {len(self.cards)} cards hidden ]]"


class MiniGoFish:
    def __init__(self):
        self.deck = Deck()  # creates a new deck of cards
        self.deck.shuffle()  # shuffle the cards
        # Initialize pygame mixer
        pygame.init()
        pygame.mixer.init()
        # exception handling

        try:
            # Load the Music
            current_path = os.path.dirname(__file__)
            pygame.mixer.music.load(os.path.join(current_path, "sounds/background.mp3"))
            self.book_sound = pygame.mixer.Sound(os.path.join(current_path, "sounds/book_completed.mp3"))
            self.victory_sound = pygame.mixer.Sound(os.path.join(current_path, "sounds/victory.mp3"))
            # background music
            pygame.mixer.music.play(-1)
        except Exception as e:
            print(f"Could not load sound files: {e}")

        # Enter player 1 and player 2
        n_cards_per_player = int(input("Enter the number of cards for each player: "))
        self.books_to_win = int(input("Enter the number of books to win: "))
        name1 = input("Enter Player 1's name: ")
        name2 = input("Enter Player 2's name: ")

        self.players = [Hand(name1), Hand(name2)]
        # deal only 3 cards for each player, you can change that, I kept it for only 3 to have kinda quick game
        self.deck.deal(self.players, n_cards_per_player)
        # set first player  to 0
        self.current = 0
        # statics
        self.total_draws = 0
        self.go_fish_attempts = 0
        self.successful_matches = 0

    def play_turn(self, player, opponent):
        print(20 * str('***'))  # just print using string multiplier
        print(f"------------------> {player.name} turn <--------------------")
        print(player.__str__(reveal=True))
        print(opponent.__str__(reveal=False))

        while True:
            try:
                # asked to borrow a card, capitalize capitalizes only the first letter.
                asked = input(f"{player.name} asks for a rank (2–10, Jack, Queen, King, Ace): ").capitalize()
                # this finds the index of the asked rank
                rank = Card.rank_list.index(asked)
                if player.has_rank(rank):
                    break
                print("You must ask for a rank you have.")
            except ValueError:
                print(f"Invalid request. Try again {player.name}")

        # taken removes the card from player's hand
        taken = opponent.remove_rank(rank)
        if taken:
            print(f"{opponent.name} gives you {len(taken)} card(s).")
            # extend players card by appending the taken cards
            player.cards.extend(taken)
            self.successful_matches += len(taken)

            # Check for completed books
            book_completed = player.check_books()
            if book_completed:
                try:
                    self.book_sound.play()
                except:
                    print("Could not play book completion sound")

            print(player.__str__(reveal=True))
            return True
        else:
            print("Go Fish!")
            # collect statistics
            self.go_fish_attempts += 1
            if not self.deck.is_empty():
                # pop card from the deck
                drawn = self.deck.pop_card()
                print(f"You drew {drawn}")
                # collect statistics
                self.total_draws += 1

                # add card to players hand
                player.add_card(drawn)
                # check if player completed any books
                book_completed = player.check_books()
                if book_completed:
                    try:
                        self.book_sound.play()
                    except:
                        print("Could not play book completion sound")

                print(player.__str__(reveal=True))
                # Go again if draw matches
                return drawn.rank == rank
            else:
                print("Deck is empty")
                return False

    def is_game_over(self):
        # end the game if n books reached target or deck is empty
        return any(len(pl.books) >= self.books_to_win for pl in self.players) or self.deck.is_empty()

    def display_statistics(self):
        print("\n===== Game Statistics =====")
        print(f"Total Cards Drawn from the Deck: {self.total_draws}")
        print(f"Total 'Go Fish' Attempts: {self.go_fish_attempts}")
        print(f"Total Successful Matches: {self.successful_matches}")
        for player in self.players:
            print(f"{player.name} completed {len(player.books)} books")
        print("=================================")

    def play(self):
        print(f"\nStarting MiniGo-->Fish (First to {self.books_to_win} books wins)\n")
        try:
            while not self.is_game_over():
                # current player index
                p = self.players[self.current]
                # if current player index is zero, opponent is one and vice versa
                o = self.players[1 - self.current]
                # check if the players get another go
                go_again = self.play_turn(p, o)
                # switch to another player if there is no another go
                if not go_again:
                    self.current = 1 - self.current

            print("********** Game Over **********")
            # stop background music
            pygame.mixer.music.stop()
            # loop through all players and display all the pairs
            for p in self.players:
                # convert rank numbers to rank name
                pairs = [Card.rank_list[r] for r in p.books]
                print(f"{p.name} has books: {pairs}")

            # who is the winner based on the number of books
            if len(self.players[0].books) > len(self.players[1].books):
                print(f"{self.players[0].name} wins!!!")
                try:
                    self.victory_sound.play()
                    pygame.time.delay(3000)  # Let victory sound play
                except:
                    print("Could not play victory sound")
            elif len(self.players[1].books) > len(self.players[0].books):
                print(f"{self.players[1].name} wins!!!")
                try:
                    self.victory_sound.play()
                    pygame.time.delay(3000)  # Let victory sound play
                except:
                    print("Could not play victory sound")
            else:
                print("It's a draw!")

            # Display statistics
            self.display_statistics()

        finally:
            #  quit pygame properly
            pygame.mixer.quit()
            pygame.quit()


if __name__ == "__main__":
    try:
        game = MiniGoFish()
        game.play()
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

