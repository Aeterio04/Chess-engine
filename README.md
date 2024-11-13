# Chess-engine
First attempt at devloping a project. used basic OOP to create classes for each chess piece, which were then stored in a dictionary. The GUI for the same was made by using a tkinter grid of buttons, with the pieces being displayed as text.

File 1:

Chess Logic:
each piece has a class namely rook, knight, bishop, queen, king, pawn. Each class has attributes stat(status(alive or dead)), color, number, name. It also has a method named move(), common to all classes, accepting previous and post positions.

Chess Gui:

The Gui is created by using tkinter to create buttons and there are methods to update the board and ask for moves on the basis of what two squares were pressed in succession. Theres also a Switchmove() method to switch the player after recieveing a valid input
