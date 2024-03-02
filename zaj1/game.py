from gameBoard import GameBoard
from player import Player

class Game:

    def __init__(self):
        self.gameBoard = GameBoard() # Utwórz słownik planszy KIK.
        self.currentPlayer, self.nextPlayer = Player(self.gameBoard.X), Player(self.gameBoard.O) # X wykonuje ruch jako pierwszy, O jako następny. 
    
    def restart(self):
        self.gameBoard.cleanBoard()

    def start(self):
        """Rozgrywka w kółko i krzyżyk."""
        print('Witaj w grze kółko i krzyżyk!')
        while True:
            print(self.gameBoard.getBoardStr())  # Wyświetl planszę na ekranie.

            # Zadawaj graczowi pytanie, aż wprowadzi prawidłową liczbę od 1 do 9:
            move = None
            while not self.gameBoard.isValidSpace(move):
                print(f'Jaki jest ruch gracza {self.currentPlayer}? (1-9)')
                move = input()
            self.gameBoard.updateBoard(move, self.currentPlayer)  # Wykonanie ruchu.
            # Sprawdzenie, czy gra jest zakończona:
            if self.gameBoard.isWinner(self.currentPlayer):  # Sprawdzenie, kto wygrał.
                print(self.gameBoard.getBoardStr())
                print(self.currentPlayer + ' wygrał grę!')
                break
            elif self.gameBoard.isBoardFull():  # Sprawdzenie remisu.
                print(self.gameBoard.getBoardStr())
                print('Gra zakończyła się remisem!')
                break
            self.currentPlayer, self.nextPlayer = self.nextPlayer, self.currentPlayer  # Zmiana gracza.
        print('Dziękuję za grę!')