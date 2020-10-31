print("Welcome to the Tic Tac Toe game \n Hope you enjoy !!")
class InvalidInputError(Exception):
    pass

def GetPlayerCode():
    while True:
        symbol = input("Please select your symbol: X or O : ")
        if symbol.lower() == 'x' or symbol.lower() == 'o':
            return symbol.upper()
        print("The option you selected is Invalid. Could you please try again?")

def GetGridSize():
    while True:
        try:
            print("The grid sizes are in the form of a square, for example 3*3, 4*4 etc")
            size = int(input("Please enter the grid size : "))
            if(size>=3):
                break;
            else:
                print("Sorry, but the grid size has to be greater than or equal to 3");
        except:
            print("Please enter a valid integer value")
    return size;
    
def BeginGame():
    while True:
        choice = input("Please enter your choice : ").lower()
        if choice  == "quit":
            print("\n See you later. Bye!.")
            break;
        elif choice == "begin":
            print("\n Let's begin. \n Good luck !")
            return True;
        else:
            print("Sorry, but the input you entered is invalid.")
            raise InvalidInputError("SOrry")
    return False;
   
class Board:
    def __init__(self,board,grid):
        self.board = board
        self.grid = grid
    def display_board(self):
        for i in self.board:
            line = "";
            line2 ="";
            for j in i:
                line += f" {j} | "
                line2+="---| "
            print(line)
            print(line2)
    def check_board(self,symbol):
        res = True
        #checking rows for winning
        for i in self.board:
            if i.count(symbol) == self.grid:
                print(f"{symbol} row Wins");
                res= False;
        #checking columns for winning
        dia1 =0
        dia2 =0
        for i in range(0,grid):
            count =0
            for j in range(0,grid):
                if self.board[j][i] == symbol:
                    count+=1
                if i==j and self.board[i][j] == symbol:
                    dia1+=1
                if i+j == grid -1 and self.board[i][j] == symbol:
                    dia2 +=1
            if( count == self.grid):
                print(f"{symbol} col Wins");
                res= False
        #checking diagonal
        if(dia1 == grid or dia2 == grid):
            print(f"{symbol} diagonal Wins");
            res= False
        
        return res
        
class Player:
    def __init__(self,symbol,grid):
        self.symbol = symbol
        self.grid = grid
        self.currentRow = 0
        self.currentCol = 0
    def interaction(self):
        while True:
            try:
                pos = int(input(f"Enter a row position [1 - {grid}]: "))
                if(pos>=1 and pos<=grid):
                    self.currentRow = pos -1
                    break;
                else:
                    print("Not a valid Position")
            except:
                print("Enter a valid Number")
        while True:
            try:
                pos = int(input(f"Enter a column position [1 - {grid}]: "))
                if(pos>=1 and pos<=grid):
                    self.currentCol = pos -1
                    break;
                else:
                    print("Not a valid Position")
            except:
                print("Enter a valid Number")

    def update_board(self,board):
        while True:
            if board.board[self.currentRow][self.currentCol] ==" ":
                board.board[self.currentRow][self.currentCol] = self.symbol
                break;
            else:
                print("That position is already taken! Try again\n")
                self.interaction()

class GameState:
    def __init__(self, p1,p2,board):
        self.p1 = p1
        self.p2 = p2
        self.playerTurn = True
        self.board = board
    def turn(self):
        if(self.playerTurn):
            print(f"\n{p1.symbol} Turn :")
            self.p1.interaction()
        else:
            print(f"\n{p2.symbol} Turn :")
            self.p2.interaction()
            

    def place(self):
        if(self.playerTurn):
            self.p1.update_board(self.board)
            print("\n")
            self.board.display_board()
            print("\n")
        else:
            self.p2.update_board(self.board)
            print("\n")
            self.board.display_board()
            print("\n")

    def game_loop(self):
        print("")
        while self.board.check_board(self.p1.symbol):
            self.turn()
            self.place()
            if(self.playerTurn):
                self.playerTurn = False
            else:
                self.playerTurn = True

print("Commands\n")
print("Begin => To start the game\n")
print("Quit => To close the game\n")

while BeginGame():
    
    grid = GetGridSize();
    list = [[" " for i in range(0,grid)] for i in range(0,grid)]
    board = Board(list,grid)
    p1Symbol = GetPlayerCode()
    if p1Symbol == 'X':
        p2Symbol = 'O'
    else :
        p2Symbol = "X"
        
    p1= Player(p1Symbol,grid)
    p2 =Player(p2Symbol,grid)
    game = GameState(p1,p2,board)
    game.game_loop()
    

 
    
    
    
    
    
    
    
    
    
