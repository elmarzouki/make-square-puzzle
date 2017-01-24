"""
about:
This code was written by Mostafa El-Marzouki @iSuperMostafa
------------------------------------------------------------
summery:
Make a square with size 4*4 by using 4 or 5 pieces. The pieces
can be rotated or flipped and all pieces should be used to form a square.
There may be more than one possible solution for a set of pieces,
and not every arrangement will work even with a set for which a solution can be found.
Ex: Rotate piece D 90 degree then flip horizontal {R 90 + F H}
Input:
Each piece is then specified by listing
The first line contains piece number.
Then a single line with two integers, the number of rows and columns in the piece,
followed by one or more lines which specify the shape of the piece.
The shape specification consists of 0 or 1characters, with the 1 character indicating
the solid shape of the puzzle (the 0 characters are merely placeholders).
For example, piece A above would be specified as follows:
1
2 3
111
101
Output:
Your program should report all solution, in the format shown by the examples below.
A 4-row by 4-column square should be created, with each piece occupying
its location in the solution. The solid portions of piece #1 should be replaced with
`1' characters, of piece #2 with `2' characters. Last line displays the pieces which
are changed in the original form. If the piece rotate with angle 90{R 90},
and flip vertical or horizontal {F V or F H}.
For cases which have no possible solution simply report "No solution possible".
"""
class Helper:
    # check if the pieces number is correct     >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     not used till now
    def IsVaild(self, Input, Limit):
        Digits = []
        for Char in Input:
            Digits.append(Char)
        if len(Digits) is not Limit:
            return False
        return True

    # get a string of numbers and convert it to digits
    def GetDigits(self, Input):
        Row = (Char for Char in Input if Char.isdigit())
        Digits = []
        for Char in Row:
            Digits.append(int(Char))
        return Digits

    # write the pieces in pieces.in     >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     not used till now
    def WritePieces(self, Pieces):
        open("data/pieces.in", 'w').close()
        with open("data/pieces.in", "w") as handle:
            for i in range(len(Pieces)):
                print(Pieces[i]['ShapeNumber'], file=handle)
                print(Pieces[i]['Rows'] + " " + Pieces[i]['Columns'], file=handle)
                for row in range(len(Pieces[i]['Values'])):
                    print(row, file=handle)

    # read the pieces from pieces.in
    def ReadPieces(self):
        Pieces = []
        with open("data/pieces.in") as Reader:
            Lines = Reader.readlines()
            for i in range(0, len(Lines), 6):
                Piece = {}
                Piece['ShapeNumber'] = int(Lines[i])
                RowColumn = Lines[i + 1].split()
                Piece['Rows'] = int(RowColumn[0])
                Piece['Columns'] = int(RowColumn[1])
                Piece['Values'] = [[None]*4]*4
                for j in range(len(Piece['Values'])):
                    Piece['Values'][j] = self.GetDigits(Lines[i + 2 + j])
                Pieces.append(Piece)
        return Pieces
