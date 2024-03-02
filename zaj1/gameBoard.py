
class GameBoard:
    ALL_SPACES = list('123456789')  # Klucze słownika planszy KIK.
    X, O, BLANK = 'X', 'O', ' '  # Stałe reprezentujące wartości tekstowe.

    def __init__(self):
        self.cleanBoard()

    def cleanBoard(self):
        """Tworzy pustą planszę gry w kółko i krzyżyk."""
        self.board = {}  # Plansza jest reprezentowana przez słownik Pythona.
        for space in self.ALL_SPACES:
            self.board[space] = self.BLANK  # Wszystkie pola na początku są puste.
        return self.board

    def isBoardFull(self):
        """Zwraca True, jeśli wszystkie pola na planszy są zajęte."""
        for space in self.ALL_SPACES:
            if self.board[space] == self.BLANK:
                return False # Jeśli nawet jedno pole jest puste, zwracaj False.
        return True # Nie ma wolnych pól, zatem zwróć True.
   
    def updateBoard(self, space, mark):
        """Ustawia pole na planszy na podany znak."""
        self.board[space] = mark

    def getBoardStr(self):
        """Zwraca tekstową reprezentację planszy."""
        return f'''
                {self.board['1']}|{self.board['2']}|{self.board['3']} 1 2 3 
                -+-+- 
                {self.board['4']}|{self.board['5']}|{self.board['6']} 4 5 6 
                -+-+- 
                {self.board['7']}|{self.board['8']}|{self.board['9']} 7 8 9'''

    def isValidSpace(self, space):
        """Zwraca True, jeśli pole na planszy ma prawidłowy numer i pole jest puste."""
        if space is None:
            return False
        return space in self.ALL_SPACES or self.board[space] == self.BLANK

    def isWinner(self, player):
        """Zwraca True, jeśli gracz jest zwycięzcą tej planszy KIK."""
        b, p = self.board, player # Krótsze nazwy jako "składniowy cukier".
        # Sprawdzenie, czy trzy takie same znaki występują w wierszach, kolumnach i po przekątnych.
        return ((b['1'] == b['2'] == b['3'] == p) or # poziomo na górze
                (b['4'] == b['5'] == b['6'] == p) or # poziomo w środku
                (b['7'] == b['8'] == b['9'] == p) or # poziomo u dołu
                (b['1'] == b['4'] == b['7'] == p) or # pionowo z lewej
                (b['2'] == b['5'] == b['8'] == p) or # pionowo w środku
                (b['3'] == b['6'] == b['9'] == p) or # pionowo z prawej
                (b['3'] == b['5'] == b['7'] == p) or # przekątna 1
                (b['1'] == b['5'] == b['9'] == p)) # przekątna 2