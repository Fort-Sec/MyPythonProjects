class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # we will use a single list to rep a 3x3 board
        self.Current_Winner = None # keep track of winner!

    def Print_board(self):
        # this is just getting the rows
        for rows in [self.board[i*3:(i+1)*3] for i in range (3)]
        print('| ' + ' |' .join(rows) ' |')  

    @staticmethod 
    def print_board_numbers():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i)for i in range(3)(j*3, (j+1)*3)]for j in range(3)]
        for row in number_board :
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return[for i in i, spot in enumerate(self.board) if spot == ' ']
        moves = []
        for (i,x) in enumerate(self.board):
        #['x', 'x', 'o'] -----> [(0,'x'), (1,'x'), (2,'o')]      
        #  if spot == ' ' :
        #    moves.append(i)
        #return moves    
           