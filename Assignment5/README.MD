Disclaimer - code is not entirely correct, though it does show a general trend.

With the world file given it iterates 42 times until the differences between gamma and gamma' are below our threshold.
The first output of the program is the map with arrows pointing in the recommended direction, and [] representing walls.
The second output of the program is the map with U values printed. These are rounded to 3 decimal points for readability.

There is no path as some of the nodes give contradictory instructions (where you would go back the way you came from endlessly).
However we can see a general path resulting from the data:
<br>
<br>
We should first go right 3 spaces, up 3, right 1, right 4, up 2, right 2.
Which is to say we go under the first snake, pass through the second snake, go through second barn, then up to the apple.

I cannot find where my bug is that causes only a general trend and not an exact path.


Usage:
  python Assignment5.py <World File>
ex:
  python Assignment5.py World1MDP.txt
  

