import tkinter as tk
from chesslogic import rook,bishop,knight,queen,king,pawn,chess_board_setup
from chesslogic import (
    rook_black_1, rook_black_2, knight_black_1, knight_black_2, bishop_black_1, bishop_black_2, queen_black,
    king_black, pawn_black_1, pawn_black_2, pawn_black_3, pawn_black_4, pawn_black_5, pawn_black_6,
    pawn_black_7, pawn_black_8, rook_white_1, rook_white_2, knight_white_1, knight_white_2,
    bishop_white_1, bishop_white_2, queen_white, king_white, pawn_white_1, pawn_white_2,
    pawn_white_3, pawn_white_4, pawn_white_5, pawn_white_6, pawn_white_7, pawn_white_8
)

# Initialize root window
root = tk.Tk()
root.title("Chess Board GUI")

kingobjs=[chess_board_setup[(4,0)],chess_board_setup[(4,7)]]
print(kingobjs)


#ouch
moves=0

player='w'


turn_label = tk.Label(root, text="white's Turn", font=("Arial", 16))
turn_label.grid(row=0, column=0, columnspan=9)  # Place it above the boar
def switch_turn():
    global player
    if player=='w':
        player='b'
    elif player=='b':
        player='w'
    turn_label.config(text=f"{player}'s Turn")

def popup(title,string):
    # Create the popup window
    popup = tk.Toplevel(root)
    popup.title(title)
    
    # Set popup window size
    popup.geometry("300x200")
    
    # Label in the popup window
    label = tk.Label(popup, text=string, font=("Arial", 12))
    label.pack(pady=20)
    
    # Close button in the popup window
    close_button = tk.Button(popup, text="Close", command=popup.destroy)
    close_button.pack(pady=10)


#defining invalidity and first play

    
# Define board size, tile coordinates list, and piece symbols
board_size = 8
coordinates = []
# Function to update the board display based on the pieces dictionary
def update_board(prev,post):

    
    prevpiece = chess_board_setup[prev].symbol 
    buttons[(prev[0], prev[1])].config(text='')
    buttons[(post[0], post[1])].config(text=prevpiece)

# Function to handle button click, which appends coordinates to the list
def tile_click(row, col):
    global coordinates
    global moves
    coordinates.append((col,row))
    
    if chess_board_setup[(col,row)]!='_':
        print(chess_board_setup[(col,row)].name)
    else:
        print('_')
    
    if len(coordinates) == 2:
        # Pass the coordinates to the backend's askmove functio
        
        askmove(coordinates[0],coordinates[1])
        print(moves)
        # Clear the coordinates for the next move
        coordinates.clear()

# Placeholder for askmove function (to be replaced with actual backend logic)
def askmove(prev,post):
    global player
    global moves 
    piece=chess_board_setup[prev].symbol if chess_board_setup[prev]!='_' else ''
    piece2=chess_board_setup[post].symbol if chess_board_setup[post]!='_' else ''
    if prev!=post:
        
        if player=='w' and chess_board_setup[prev]!='_':
            
            if  chess_board_setup[prev].color=='w':
                update_board(prev,post)
                if chess_board_setup[prev].move(prev,post):
                    print('move valid')
                    print(chess_board_setup)
                    switch_turn()
                else:
                    buttons[(prev[0], prev[1])].config(text=piece)
                    buttons[(post[0], post[1])].config(text=piece2)
                moves+=1
                
            
        elif player=='b' and chess_board_setup[prev]!='_':
            
            if chess_board_setup[prev].color=='b':
                update_board(prev,post)
                if chess_board_setup[prev].move(prev,post):
                    print('move valid')
                    print(chess_board_setup)
                    switch_turn()
                else:
                    buttons[(prev[0], prev[1])].config(text=piece)
                    buttons[(post[0], post[1])].config(text=piece2)
                moves+=1

    if (kingobjs[0].stat and kingobjs[1].stat)==False:
        winner=kingobjs[0].color if kingobjs[0].stat==True else kingobjs[1].color
        popup("Game Over",f"{winner} won by killing the king")
        root.quit()



# Create frame for the chessboard
frame = tk.Frame(root)
frame.grid(row=1, column=0, columnspan=9)

# Add column labels
for col in range(board_size):
    label = tk.Label(frame, text=chr(97 + col))  # Convert to 'a' to 'h'
    label.grid(row=0, column=col + 1)


# Add row labels and create tiles as buttons
buttons = {}
for row in range(board_size - 1, -1, -1):  # Start from 7 to 0 to get 7,0 at top
    # Row label (1-8)
    label = tk.Label(frame, text=str(board_size - row))  # '8' at top, '1' at bottom
    label.grid(row=1+ row, column=0)

    # Create each button for the board
    for col in range(board_size):
        # Set background color
        color = "white" if (row + col) % 2 == 0 else "gray"
        
        # Determine piece symbol if any
        if chess_board_setup[(col,row)]!= '_':
            piece = chess_board_setup[(col,row)].symbol
        elif chess_board_setup[(col,row)]=='_':
            piece=''
        # Create a button with piece symbol, assign click event
        button = tk.Button(frame, bg=color, text=piece, font=("Arial", 20),
                           width=4, height=2,
                           command=lambda r=row, c=col: tile_click(r, c))
        button.grid(row=board_size - row, column=col + 1)
        buttons[(col,row)] = button  # Store button for easy access



# Run the Tkinter main loop
root.mainloop()