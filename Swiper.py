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
class Swiper:
    # remove AllZeros row
    def __RemoveRow__(self, Matrix, Row):
        for i in range(Row, len(Matrix)):
            for j in range(len(Matrix[0])):
                if i + 1 < len(Matrix):
                    Matrix[i][j] = Matrix[i+1][j]
        for j in range(len(Matrix[0])):
            Matrix[len(Matrix[0]) - 1][j] = 0
        return Matrix

    # remove AllZeros column
    def __RemoveColumn__(self, Matrix, Row):
        for i in range(len(Matrix)):
            for j in range(len(Matrix[i])):
                if j+1 < len(Matrix[i]):
                    Matrix[i][j] = Matrix[i][j+1]
        for i in range(len(Matrix)):
            Matrix[i][len(Matrix[i])-1] = 0
        return Matrix

    # check if the first row in the matrix contains Ones
    def __FirstRowContainsOnes__(self, Matrix):
        for i in range(len(Matrix[0])):
            if Matrix[0][i] == 1:
                return True
        return False

    # check if the first column in the matrix contains Ones
    def __FirstColumnContainsOnes__(self, Matrix):
        for i in range(len(Matrix)):
            if Matrix[i][0] == 1:
                return True
        return False

    # check if the first row and column in the matrix contains Ones
    def __UpperEdgesContainsOnes__(self, Matrix):
        if self.__FirstRowContainsOnes__(Matrix):
            return self.__FirstColumnContainsOnes__(Matrix)
        return False

    # remove Dump Zeros from the matrix and append it to the end
    # of the matrix
    def RemoveDumpZeros(self, Matrix):
        if self.__UpperEdgesContainsOnes__(Matrix):
           return Matrix
        ColumnsZeros = {}
        for i in range(len(Matrix)):
            ColumnsZeros[i] = 0
        for i in range(len(Matrix)):
            RowZeroCounter = 0
            for j in range(len(Matrix[i])):
                if not self.__FirstRowContainsOnes__(Matrix):
                    if Matrix[i][j] == 0:
                        RowZeroCounter += 1
                    if RowZeroCounter == len(Matrix[i]):
                        Matrix = self.__RemoveRow__(Matrix, i)
                        return self.RemoveDumpZeros(Matrix)
                if not self.__FirstColumnContainsOnes__(Matrix):
                    if Matrix[i][j] == 0:
                        ColumnsZeros[j] += 1
                    if ColumnsZeros[j] == len(Matrix):
                        Matrix = self.__RemoveColumn__(Matrix, j)
                        return self.RemoveDumpZeros(Matrix)
