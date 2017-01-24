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


"""
known bugs:
there's a problem in determining the board position
The project will be updated later!
"""
import _thread as thread
import Helper, MatrixTransformations, Swiper
helper = Helper.Helper()
Transform = MatrixTransformations.MatrixTranformations()
swiper = Swiper.Swiper()


class MakeSquare:
    def __init__(self):
        self.Sets = []
        self.Board = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]

    # check if the Ones count in the pieces is 16
    def __Are16__(self):
        Pieces = helper.ReadPieces()
        AllOnes = 0
        for Piece in Pieces:
            for i in range(len(Piece['Values'])):
                for j in range(len(Piece['Values'][i])):
                    if Piece['Values'][i][j] == 1:
                        AllOnes += 1
        return AllOnes == 16

    # check if the values of the set of pieces is already exists!
    def __Exists__(self, NewSet):
        Found = []
        for Piece in NewSet['Pieces']:
            for Set in self.Sets:
                if Piece in Set['Pieces']:
                    Found.append(Set)
                else:
                    if Set in Found:
                        Found.remove(Set)
        if not Found:
            return True
        return False


    # Transform one piece at a time
    def __TransformOne__(self, Operation):
        Pieces = helper.ReadPieces()
        for i in range(len(Pieces)):
            Pieces = helper.ReadPieces()
            NewSet = {}
            Pieces[i]['Values'] = Operation(Pieces[i]['Values'])
            Pieces[i]['Values'] = swiper.RemoveDumpZeros(Pieces[i]['Values'])
            NewSet['Pieces'] = Pieces
            NewSet['State'] = "Piece#" + str(Pieces[i]['ShapeNumber']) + ": " + str(Operation)
            if not self.__Exists__(NewSet):
                self.Sets.append(NewSet)

    # Transform all the pieces
    def __TransformAll__(self, Operation):
        Pieces = helper.ReadPieces()
        NewSet = {}
        for i in range(len(Pieces)):
            Pieces[i]['Values'] = Operation(Pieces[i]['Values'])
            Pieces[i]['Values'] = swiper.RemoveDumpZeros(Pieces[i]['Values'])
        NewSet['Pieces'] = Pieces
        NewSet['State'] = "All: " + str(Operation)
        if not self.__Exists__(NewSet):
            self.Sets.append(NewSet)

    # apply all the Transformations to generate all the possible sets
    def __AllPossibleSets__(self):
        Set = {}
        Originals = helper.ReadPieces()
        Set['Pieces'] = Originals
        Set['State'] = "Originals"
        self.Sets.append(Set)
        Operations = [Transform.Rotate90Clockwise, Transform.FlipHorizontally, Transform.FlipVertically,
                      Transform.Rotate90ClockwiseThenFlipHorizontally, Transform.Rotate90ClockwiseThenFlipVertically]
        for Operation in Operations:
            thread.start_new_thread(self.__TransformOne__, (Operation,))
            thread.start_new_thread(self.__TransformAll__, (Operation,))

    def __IsFit__(self, CurrentTry, AllPieces):
        """
        this function is translated from 1995 ACM Mid-Central Programming Contest Problem #3 - A Puzzling Problem
        because of it's great performance and speed
        reference: http://www.cs.nthu.edu.tw/~progcont/ACM/ProblemSetArchive/B_US_MidCen/1995/index.html
        """
        for row in range(4):
            for column in range(4):
                self.Board[row][column] = 0

        for Piece in range(len(AllPieces)):
            BoardPosition = int(int(CurrentTry % int(pow(16, Piece + 1))) / int(pow(16, Piece)))
            BoardRow = BoardPosition // 4
            BoardColumn = BoardPosition % 4

            for row in range(AllPieces[Piece]['Rows']):
                for column in range(AllPieces[Piece]['Columns']):
                    if (BoardRow + row < 4) and (BoardColumn + column < 4):
                        self.Board[BoardRow + row][BoardColumn + column] += AllPieces[Piece]['Values'][row][column]

        for row in range(4):
            for column in range(4):
                return self.Board[row][column] == 1

    def Solve(self):
        PossibleSolutions = []
        if self.__Are16__():
            self.__AllPossibleSets__()
            for THIS in range(len(self.Sets)):
                solved = False
                NumberOfTries = 1
                for x in range(len(self.Sets[THIS]['Pieces'])):
                    NumberOfTries *= 16
                CurrentTry = 0
                while True:
                    if (CurrentTry < NumberOfTries) and (solved == False):
                        if self.__IsFit__(CurrentTry, self.Sets[THIS]['Pieces']):
                            solved = True
                        CurrentTry += 1
                    else:
                        break
                answer = CurrentTry - 1

                if solved:
                    PossibleSolution = {}
                    board = [[0, 0, 0, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0]]
                    for Piece in range(len(self.Sets[THIS]['Pieces'])):
                        Position = int(int(answer % int(pow(16, Piece + 1))) / int(pow(16, Piece)))
                        Row = Position // 4
                        Column = Position % 4
                        for row in range(self.Sets[THIS]['Pieces'][Piece]['Rows']):
                            for column in range(self.Sets[THIS]['Pieces'][Piece]['Columns']):
                                if self.Sets[THIS]['Pieces'][Piece]['Values'][row][column] == 1:
                                    board[Row + row][Column + column] = 1 + Piece
                    PossibleSolution['Board'] = board
                    PossibleSolution['State'] = self.Sets[THIS]['State']
                    PossibleSolutions.append(PossibleSolution)
        return PossibleSolutions

