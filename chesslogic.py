def updatekey(old,new):
    chess_board_setup[new]=chess_board_setup.pop(old)
    chess_board_setup[old]='_'
    
class rook:
    def __init__(self,color,number):

        self.color=color
        self.num=number
        if self.color=='b':
            self.symbol='♜'
        elif self.color=='w':
            self.symbol='♖'
        self.stat=True
        self.name=f'{self.color} rook'
    
    def move(self,prev,post):
        print('moving rook',prev,post)
        global chess_board_setup
        if (prev[0]==post[0]) or (prev[1]==post[1]):
            
            for i in chess_board_setup.keys():
                if chess_board_setup[i]!='_':
                    if (prev[0]<i[0]<post[0] or prev[0]>i[0]>post[0]) and i[1]==prev[1]:
                        return False
                    elif (prev[1]<i[1]<post[1] or prev[1]>i[1]>post[1]) and i[0]==prev[0]:
                        return False
            #kill
            if chess_board_setup[post]!='_':
                if chess_board_setup[post].color==self.color:
                    print('cant kill same color')
                    return False
            updatekey(prev,post)
            return True

class bishop:
    
    def __init__(self,color,number):
        self.color=color
        self.num=number
        if self.color=='b':
            self.symbol='♝'
        elif self.color=='w':
            self.symbol='♗'
        self.stat=True
        self.name=f'{self.color} bishop'

    def move(self,prev,post):
        print('moving bishop',prev,post)
        global chess_board_setup
        if (prev[0]+prev[1]==post[0]+post[1]) or (prev[0]-prev[1]==post[0]-post[1]):
            
            for i in chess_board_setup.keys() :
                if chess_board_setup[i]!='_':
                    if ((prev[0]+prev[1]==i[0]+i[1]) ) and ((prev[0]>i[0]>post[0]) or (prev[0]<i[0]<post[0]))  :
                        print(i,'blocks')
                        return False
                    elif (prev[0]-prev[1]==i[0]-i[1]) and ((prev[0]>i[0]>post[0]) or (prev[0]<i[0]<post[0])) :
                        print(i,'blocks')
                        return False
                #kill
            if chess_board_setup[post]!='_':
                if chess_board_setup[post].color==self.color:
                    print('cant kill same color')
                    return False
                else:
                    chess_board_setup[post].stat=False
            
            
            updatekey(prev,post)
            return True
            

class knight:
            
    def __init__(self,color,number):
        self.color=color
        self.num=number
        if self.color=='b':
            self.symbol='♞'
        elif self.color=='w':
            self.symbol='♘'
        self.stat=True
        self.name=f'{self.color} knight'
    
    def move(self,prev,post):
        print('moving knight',prev,post)
        global chess_board_setup
        delx=abs(prev[0]-post[0])
        dely=abs(prev[1]-post[1])
        if delx==0 or dely==0:
            return False
        
        elif delx+dely==3:
            #kill
            if chess_board_setup[post]!='_':
                if chess_board_setup[post].color==self.color:
                    print('cant kill same color')
                    return False
                else:
                    chess_board_setup[post].stat=False
        else:
            return False
        print('this does',delx,dely)            
        updatekey(prev,post)
        return True


class queen:

    def __init__(self,color,num):

        self.color=color
        self.num=num
        if self.color=='b':
            self.symbol='♛'
        elif self.color=='w':
            self.symbol='♕'
        self.stat=True
        self.name=f'{self.color} queen'

    def move(self,prev,post):
        print('moving queen',prev,post)
        global chess_board_setup
        #like a rook
        if (prev[0]==post[0]) or (prev[1]==post[1]):
            
            for i in chess_board_setup.keys():
                if chess_board_setup[i]!='_':    
                    if (prev[0]<i[0]<post[0] or prev[0]>i[0]>post[0]) and i[1]==prev[1]:
                        return False
                    elif (prev[1]<i[1]<post[1] or prev[1]>i[1]>post[1]) and i[0]==prev[0]:
                        return False
            
        #like a bishop

        elif (prev[0]+prev[1]==post[0]+post[1]) or (prev[0]-prev[1]==post[0]-post[1]):
            
            for i in chess_board_setup.keys():
                if chess_board_setup[i]!='_': 
                    if ((prev[0]+prev[1]==i[0]+i[1]) ) and ((prev[0]>i[0]>post[0]) or (prev[0]<i[0]<post[0]))  :
                        return False
                    elif (prev[0]-prev[1]==i[0]-i[1]) and ((prev[0]>i[0]>post[0]) or (prev[0]<i[0]<post[0])) :
                        return False
        #kill
        if chess_board_setup[post]!='_':
                if chess_board_setup[post].color==self.color:
                    print('cant kill same color')
                    return False
                else:
                    chess_board_setup[post].stat=False
                    
        updatekey(prev,post)
        return True

class king:
        
    def __init__(self,color):

        self.color=color
        if self.color=='b':
            self.symbol='♚'
        elif self.color=='w':
            self.symbol='♔'
        self.stat=True
        self.name=f'{self.color} king'
        self.check=0

    def move(self,prev,post):
        print('moving king',prev,post)
        global chess_board_setup
        delx=abs(prev[0]-post[0])
        dely=abs(prev[1]-post[1])
        #kill
        if (delx==0 and dely==1) or (dely==0 and delx==1) or (delx==1 and dely==1):
            if chess_board_setup[post]!='_':
                if chess_board_setup[post].color==self.color:
                    print('cant kill same color')
                    return False
                else:
                    chess_board_setup[post].stat=False
                    
            updatekey(prev,post)
            return True
            
        else: 
            return False
            
        

class pawn:
    
    def __init__(self,color,number):
        self.color=color
        self.num=number
        self.moves=0
        if self.color=='b':
            self.symbol='♟'
        elif self.color=='w':
            self.symbol='♙'
        self.stat=True
        self.name=f'{self.color} pawn'
    
    def move(self,prev,post):
        global chess_board_setup
        print('moving pawn',prev,post)
        delx=prev[0]-post[0]
        dely=prev[1]-post[1]

        
        if chess_board_setup[post]!='_':
            print('kill')
            if self.color=='w' and self.color!=chess_board_setup[post].color:
                if (delx==1 or delx==-1) and dely==-1:
                    chess_board_setup[post].stat=False
            
                    updatekey(prev,post)
                    self.moves+=1
                    return True
                else:
                    return False
            elif self.color=='b'and self.color!=chess_board_setup[post].color:
                if (delx==1 or delx==-1) and dely==1:
                    chess_board_setup[post].stat=False
                    updatekey(prev,post)
                    self.moves+=1
                    return True
                else:
                    return False
            else:
                return False
            
        
        elif (self.moves==0 and prev[0]==post[0]) and (((post[1]-prev[1]==2) and self.color=='w') or ((prev[1]-post[1]==2) and self.color=='b')):
            print('move1')
            updatekey(prev,post)
            self.moves+=1
            return True
        
        elif (prev[0]==post[0]) and (((post[1]-prev[1]==1) and self.color=='w') or ((prev[1]-post[1]==1) and self.color=='b')):
            print('move2')
            updatekey(prev,post)
            self.moves+=1
            return True
        else:
            return False

        
        
        ...




rook_black_1 = rook("b", 1)
knight_black_1 = knight("b", 1)
bishop_black_1 = bishop("b", 1)
queen_black = queen("b",1)
king_black = king("b")
bishop_black_2 = bishop("b", 2)
knight_black_2 = knight("b", 2)
rook_black_2 = rook("b", 2)
pawn_black_1 = pawn("b", 1)
pawn_black_2 = pawn("b", 2)
pawn_black_3 = pawn("b", 3)
pawn_black_4 = pawn("b", 4)
pawn_black_5 = pawn("b", 5)
pawn_black_6 = pawn("b", 6)
pawn_black_7 = pawn("b", 7)
pawn_black_8 = pawn("b", 8)

# White pieces
rook_white_1 = rook("w", 1)
knight_white_1 = knight("w", 1)
bishop_white_1 = bishop("w", 1)
queen_white = queen("w",1)
king_white = king("w")
bishop_white_2 = bishop("w", 2)
knight_white_2 = knight("w", 2)
rook_white_2 = rook("w", 2)
pawn_white_1 = pawn("w", 1)
pawn_white_2 = pawn("w", 2)
pawn_white_3 = pawn("w", 3)
pawn_white_4 = pawn("w", 4)
pawn_white_5 = pawn("w", 5)
pawn_white_6 = pawn("w", 6)
pawn_white_7 = pawn("w", 7)
pawn_white_8 = pawn("w", 8)

# Initial positions with chess piece objects as values and coordinates as keys
chess_board_setup = {
    (0, 0): rook_white_1, (1, 0): knight_white_1, (2, 0): bishop_white_1, (3, 0): queen_white, 
    (4, 0): king_white, (5, 0): bishop_white_2, (6, 0): knight_white_2, (7, 0): rook_white_2,
    (0, 1): pawn_white_1, (1, 1): pawn_white_2, (2, 1): pawn_white_3, (3, 1): pawn_white_4,
    (4, 1): pawn_white_5, (5, 1): pawn_white_6, (6, 1): pawn_white_7, (7, 1): pawn_white_8,
    (0, 7): rook_black_1, (1, 7): knight_black_1, (2, 7): bishop_black_1, (3, 7): queen_black, 
    (4, 7): king_black, (5, 7): bishop_black_2, (6, 7): knight_black_2, (7, 7): rook_black_2,
    (0, 6): pawn_black_1, (1, 6): pawn_black_2, (2, 6): pawn_black_3, (3, 6): pawn_black_4,
    (4, 6): pawn_black_5, (5, 6): pawn_black_6, (6, 6): pawn_black_7, (7, 6): pawn_black_8,
    (0, 2): '_', (0, 3): '_', (0, 4): '_', (0, 5): '_', (1, 2): '_', (1, 3): '_', (1, 4): '_', 
    (1, 5): '_', (2, 2): '_', (2, 3): '_', (2, 4): '_', (2, 5): '_', (3, 2): '_', (3, 3): '_', 
    (3, 4): '_', (3, 5): '_', (4, 2): '_', (4, 3): '_', (4, 4): '_', (4, 5): '_', (5, 2): '_', 
    (5, 3): '_', (5, 4): '_', (5, 5): '_', (6, 2): '_', (6, 3): '_', (6, 4): '_', (6, 5): '_', 
    (7, 2): '_', (7, 3): '_', (7, 4): '_', (7, 5): '_'}

