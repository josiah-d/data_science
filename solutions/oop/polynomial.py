from itertools import zip_longest


class Polynomial(object):

    def __init__(self, coefs):
        """Create a Polynomial object
        Parameters
        ----------
        coefs : list of numbers
            The coefficients of the polynomial, starting at the constant term,
            so the index of the coefficient corresponds to the power.
        """

        coefs = coefs[:]
        while len(coefs) > 0 and coefs[-1] == 0:
            coefs.pop()
        if len(coefs) == 0:
            coefs = [0]
        self.coefs = coefs

    def __add__(self, other):
        """Add to polynomial."""
        result = []
        for c1, c2 in zip_longest(self.coefs, other.coefs, fillvalue=0):
            result.append(c1 + c2)
        return Polynomial(result)

    def __sub__(self, other):
        """Subtract another polynomial."""
        return self + -other

    def __mul__(self, other):
        """Multipy by another polynomial."""
        result = [0] * (len(self.coefs) + len(other.coefs) + 1)
        for power_1, coef_1 in enumerate(self.coefs):
            for power_2, coef_2 in enumerate(other.coefs):
                result[power_1 + power_2] += coef_1 * coef_2
        return Polynomial(result)

    def __eq__(self, other):
        """Check if equal to another polynomial."""
        return self.coefs == other.coefs

    def _sign_string(self, coef, is_largest):
        """The sign part of the string representation of a term,
        used by __str__."""
        assert(coef != 0)
        if is_largest and coef > 0:
            return ""
        elif is_largest and coef < 0:
            return "-"
        elif coef > 0:
            return " + "
        else:
            return " - "

    def _coef_string(self, coef, index):
        """The coefficient part of the string representation of a term,
        used by __str__."""
        if abs(coef) == 1 and index != 0:
            return ''
        return str(abs(coef))

    def _var_string(self, index):
        """The variable part of the string representation of a term,
        used by __str__."""
        if index == 0:
            return ""
        elif index == 1:
            return "x"
        else:
            return "x^" + str(index)

    def _term_string(self, coef, index, is_largest):
        """The string representation of a single term,
        used by __str__."""
        if coef == 0:
            return ""
        return (self._sign_string(coef, is_largest) +
                self._coef_string(coef, index) +
                self._var_string(index))

    def __str__(self):
        """The string representation of the polynomial."""
        result = ""
        if len(self.coefs) == 1 and self.coefs[0] == 0:
            return "0"
        for i in range(len(self.coefs) - 1, -1, -1):
            result += self._term_string(self.coefs[i],
                                        i,
                                        i == len(self.coefs)-1)
        return result

    def __repr__(self):
        return "Polynomial({})".format(self.coefs)

    def __neg__(self):
        """The negative of the polynomial."""
        result = []
        for coef in self.coefs:
            result.append(-coef)
        return Polynomial(result)

    def degree(self):
        """The highest exponent in the polynomial."""
        return len(self.coefs) - 1

    def evaluate(self, x):
        """Evaluate the polynomial with for a specified value of the variable
        Parameters
        ----------
        x : number
            The number to set the variable to.

        Returns
        -------
        number
            The result of evaluating the polynomial.
        """

        result = 0
        for power, coef in enumerate(self.coefs):
            result += coef * x ** power
        return result

    def differentiate(self):
        """ The derivative of a polynomial.

        Returns
        -------
        Polynomial
            The derivative of the polynomial.
        """

        result = []
        for i in range(1, len(self.coefs)):
            result.append(i * self.coefs[i])
        return Polynomial(result)

    def integrate(self):
        """ The integral of a polynomial.

        Returns
        -------
        Polynomial
            The integral of the polynomial,
            with the constant term set to zero.
        """

        result = [0]
        for i in range(len(self.coefs)):
            result.append(self.coefs[i] / (i+1))
        return Polynomial(result)
