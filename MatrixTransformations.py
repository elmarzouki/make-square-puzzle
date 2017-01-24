"""
about:
This code was written by Mostafa El-Marzouki @iSuperMostafa
------------------------------------------------------------
summery:
this project contains these methods to manipulate a matrix:
- TransposeMatrix
- FlipHorizontally
- FlipVertically
- Rotate90Clockwise
- Rotate90CounterClockwise
- Rotate180Clockwise
- Rotate180CounterClockwise
input: Matrix
output: manipulated matrix
"""
class MatrixTranformations:
    def TransposeMatrix(self, Matrix):
        for i in range(len(Matrix)):
            for j in range(i+1, len(Matrix[0])):
                Matrix[i][j], Matrix[j][i] = Matrix[j][i], Matrix[i][j]
        return Matrix

    def FlipHorizontally(self, Matrix):
        for i in range(len(Matrix)//2):
            for j in range(len(Matrix[0])):
                Matrix[j][len(Matrix) - (i + 1)], Matrix[j][i] = Matrix[j][i], Matrix[j][len(Matrix) - (i + 1)]
        return Matrix

    def FlipVertically(self, Matrix):
        for i in range(len(Matrix)-1, 0, -1):
            for j in range(len(Matrix[0])):
                Matrix[i][j], Matrix[j][i] = Matrix[j][i], Matrix[i][j]
        return Matrix

    # rotate Matrix by +90
    def Rotate90Clockwise(self, Matrix):
        return self.FlipHorizontally(self.TransposeMatrix(Matrix))

    # rotate Matrix by -90
    def Rotate90CounterClockwise(self, Matrix):
        return self.FlipVertically(self.TransposeMatrix(Matrix))

    # rotate Matrix by +180
    def Rotate180Clockwise(self, Matrix):
        return self.Rotate90Clockwise(self.Rotate90Clockwise(Matrix))

    # rotate Matrix by -180
    def Rotate180CounterClockwise(self, Matrix):
        return self.Rotate180Clockwise(Matrix)


    def Rotate90ClockwiseThenFlipHorizontally(self, Matrix):
        return self.Rotate90Clockwise(self.FlipHorizontally(Matrix))

    def Rotate90ClockwiseThenFlipVertically(self, Matrix):
        return self.Rotate90Clockwise(self.FlipVertically(Matrix))