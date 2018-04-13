# MakeSquarePuzzle
## problem definition:
Make a square with size 4*4 by using 4 or 5 pieces. <br>
The pieces can be rotated or flipped and all pieces should be used to form a square.<br>
There may be more than one possible solution for a set of pieces,<br>
and not every arrangement will work even with a set for which a solution can be found.<br>
Ex: Rotate piece D 90 degree then flip horizontal {R 90 + F H}<br>
Input:<br>
Each piece is then specified by listing the first line contains piece number.<br>
Then a single line with two integers, the number of rows and columns in the piece,<br>
followed by one or more lines which specify the shape of the piece.<br>
The shape specification consists of 0 or 1characters, with the 1 character indicating<br>
the solid shape of the puzzle (the 0 characters are merely placeholders).<br>
For example, piece A above would be specified as follows:<br>
1<br>
2 3<br>
111<br>
101<br>
Output:<br>
Your program should report all solution, in the format shown by the examples below.<br>
A 4-row by 4-column square should be created, with each piece occupying<br>
its location in the solution. The solid portions of piece #1 should be replaced with<br>
`1' characters, of piece #2 with `2' characters. Last line displays the pieces which<br>
are changed in the original form. If the piece rotate with angle 90{R 90},<br>
and flip vertical or horizontal {F V or F H}.<br>
For cases which have no possible solution simply report "No solution possible".<br>
