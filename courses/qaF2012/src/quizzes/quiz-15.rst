Quiz 15 
#######

:date: 2012-10-23
:category: quizzes
:tags: C.18, C.19, C.20

1. You have three employees, whose salaries are 8, 10, and 15 dollars per hour.  Working alone, they can bake and decorate cakes at rates of 3, 7, and 12 cakes per hour (respectively).  An order comes in for 184 cakes, to be delivered tomorrow (in 24 hours), and you will only be able to pay your employees 268 dollars total.

   a. Construct the system of equations that represents your bakery
   b. Construct the matrix representation of the system of equations
   c. Use that matrix to determine the best allocation of hours between the three employees 
   d. Find the inverse of the matrix
   e. Use the inverse of the matrix to determine the best allocation of hours for an order of 580 cakes in 60 hours of work with 780 dollars
 
Solution: 
a. $$
\\begin{eqnarray}
8x + 10y + 15z &=& 268\\\\
3x + 7y + 12z &=& 184\\\\
x+y+z &=& 24
\\end{eqnarray}
$$
b. $$
\\begin{bmatrix}
8 & 10 & 15 & 268\\\\
3 & 7 & 12 & 184\\\\
1 & 1 & 1 & 24
\\end{bmatrix}
$$
c. 6 hours, 10 hours, 8 hours

d. $$
\\begin{bmatrix}
0.5 & -0.5 & -1.5\\\\
-0.9 &  0.7 &  5.1\\\\
0.4 & -0.2 & -2.6
\\end{bmatrix}
$$

e. 10 hours, 10 hours, 40 hours
 
