# Newton's-method

This program implements Newton’s method to compute and display the square root of a number entered by the user. 

The algorithm for Newton’s method follows:
1) Setupped a variable, in out case - 'x'
2) Initialized 'guess' variable to x/2
3) While 'guess' is not acceptable enough it is necessaty to perform:
      - Updating 'guess' to be the average of guess and 𝑥/guess
      
When this algorithm completes, 'guess' contains an approximation of the square root. The quality of the approximation depends on how we define 'acceptable'. In the author’s solution, 'guess' was considered 'acceptable' when the absolute value of the difference between guess * guess (=𝑔𝑢𝑒𝑠𝑠2) and x was less than or equal to  10^−12
