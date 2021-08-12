## Calculus helper for the polynomial assignment

A polynomial is an expression containing two or more algebraic terms.  In this
assignment, the polynomial is comprised of a variable `x` raised to a power
multiplied by a coefficient.

For example, in the polynomial:

    3 + x + 4x^2

    the first term is  3      (coefficient = 3, power of x is 0, so 3 * x^0 = 3)
    the second term is x      (coefficient = 1, power of x is 1, so 1 * x^1 = x)
    the third term is  4x^2   (coefficient = 4, power of x is 2, so 4 * x^2 = 4x^2)

In the last part of the assignment, you will be asked to differentiate and integrate
the polynomial (using calculus).

The polynomial defines the values a function can take.

### Derivative

A derivative defines the rate of change of the values in the function.  [Here is a 7 minute video](https://www.khanacademy.org/math/ap-calculus-ab/ab-differentiation-1-new/ab-2-1/v/derivative-as-a-concept)
on Khan Academy describing the concept.

The derivate of a polynomial is the sum of the derivate of each of its terms.  Algorithmically,
you can determine it like this:


<img src="http://hyperphysics.phy-astr.gsu.edu/hbase/math/immath/dpol.gif" width="300">

Source: [Hyperphysics](http://hyperphysics.phy-astr.gsu.edu/hbase/deriv.html)

Or for a specific example.

<img src="https://www.wikihow.com/images/thumb/b/bb/Differentiate-Polynomials-Step-4-Version-2.jpg/550px-nowatermark-Differentiate-Polynomials-Step-4-Version-2.jpg" width="400">

Source: [WikiHow](https://www.wikihow.com/Differentiate-Polynomials)

Taking the derivative of the polynomial above using this algorithm:

    1st term:  3       1st term derivative: 0 (derivative of a constant with respect to x is 0)
    2nd term:  x       2nd term derivative: 1 * 1 * x^(1-1) = 1 * x^0 = 1 * 1 = 1
    3rd term:  4x^2    3rd term derivative: 4 * 2 * x^(2-1) = 8 * x^1 = 8x

    the derivate of 3 + x + 4x^2 with respect to x is 1 + 8x

### Integral

An integral is the sum of the values of the function. [Here is a 5 minute video](https://www.khanacademy.org/math/ap-calculus-ab/ab-integration-new/ab-6-1/v/introduction-to-integral-calculus)
on Khan Academy descibing the concept.

The indefinite integral of a polynomial is the sum of the integrals of each of its terms.
Algorithmically, you can determine it like this:

<img src="http://hyperphysics.phy-astr.gsu.edu/hbase/imgmth/ipol2.gif" width="300">

Source: [Hyperphysics](http://hyperphysics.phy-astr.gsu.edu/hbase/intpol.html)

For a specific example:
<img src="https://revisionworld.com/sites/revisionworld.com/files/imce/int2.gif" width="400">

Source: [Revised Math](https://revisionmaths.com/advanced-level-maths-revision/pure-maths/calculus/integration)

Taking the indefinite integral of the example polynomial using this algorithm:

    1st term: 3        1st term integral  = 3 / (0+1) * x^(0+1)  =  3 * x^1 + C1 (C1 is a constant)
    2nd term: x        2nd term integral  = 1 / (1+1) * x^(1+1) = 1/2 * x^2 + C2 (C2 is a constant)
    3rd term: 4x^2     3rd term integral  = 4 / (1+2) * x^(2+1) = 4/3 * x^3 + C3 (C3 is a constant)

    the integral of 3 + x + 4x^2 with respect to x is C + 3x + (1/2)x^2 + (4/3)x^3 
    (it's convention to add the constants together, so C1 + C2 + C3 = C)

If you take the integral of a derivate of a polynomial, you should get the original polynomial except
for the constant:

    original polynomial: 3 + x + 4x^2
    its derivative:          1 + 8x

    integral of derivative
    1st term: 1         1st term integral: 1 / (0+1) * x^(0+1) = 1 * x = x + C1
    2nd term: 8x        2nd term integral: 8 / (1+1) * x^(1+1) = 4 * x^2 = 4x^2 + C2

    the integral of the derivative is : C + x + 4x^2 
    this is almost the original polynomial - it just differs by a constant. For the assignment, please set the constant to 0.

For these to match exactly you would need to use definite integrals with limits to the
integration (not key to this assignment).
