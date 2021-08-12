#!/usr/bin/env python
# -*- coding: utf-8 -*-

class UnionShape():
    """The union of two shapes (as objects defined in shapes.py).

    Parameters
    ----------
    shape_a   : {shape} shape object A.
    shape_b   : {shape} shape object B.

    Attributes
    ----------
    shape_a : {object} the shape A (in union A | B)
    shape_b : {object} the shape B (in union A | B)
    color   : {tuple} of (r,g,b) coordinates
    """
    def __init__(self, shape_a, shape_b):
        """Constructs a UnionShape as union of given shapes
        shape_a and shape_b.

        Note: color or union should be the average between
        colors of shape_a and shape_b.
        """
        self.shape_a = shape_a
        self.shape_b = shape_b
        self.color = ( (shape_a.color[0] + shape_b.color[0])/2,
                       (shape_a.color[1] + shape_b.color[1])/2,
                       (shape_a.color[2] + shape_b.color[2])/2 )

    def mu(self, x, y):
        """Characteristic function of the shape.
        Returns True if (x,y) is inside the shape, else False.

        Parameters
        ----------
        x : {int} x coordinate of a pixel
        y : {int} y coordinate of a pixel

        Returns
        -------
        bool : True or False whether (x,y) is within the shape.
        """
        return (self.shape_a.mu(x,y) or self.shape_b.mu(x,y))


class IntersectionShape():
    """The intersection of two shapes (as objects defined in shapes.py).

    Parameters
    ----------
    shape_a   : {shape} shape object A.
    shape_b   : {shape} shape object B.

    Attributes
    ----------
    shape_a : {object} the shape A (in intersection A & B)
    shape_b : {object} the shape B (in intersection A & B)
    color   : {tuple} of (r,g,b) coordinates
    """
    def __init__(self, shape_a, shape_b):
        """Constructs a IntersectionShape as intersection
        of given shapes shape_a and shape_b.

        Note: color or intersection should be the average between
        colors of shape_a and shape_b."""
        self.shape_a = shape_a
        self.shape_b = shape_b
        self.color = ( (shape_a.color[0] + shape_b.color[0])/2,
                       (shape_a.color[1] + shape_b.color[1])/2,
                       (shape_a.color[2] + shape_b.color[2])/2 )

    def mu(self, x, y):
        """Characteristic function of the shape.
        Returns True if (x,y) is inside the shape, else False.

        Parameters
        ----------
        x : {int} x coordinate of a pixel
        y : {int} y coordinate of a pixel

        Returns
        -------
        bool : True or False whether (x,y) is within the shape.
        """
        return (self.shape_a.mu(x,y) and self.shape_b.mu(x,y))


class DiffShape():
    """The difference of two shapes (as objects defined in shapes.py).

    Parameters
    ----------
    shape_a   : {shape} shape object A.
    shape_b   : {shape} shape object B.

    Attributes
    ----------
    shape_a : {object} the shape A (in difference A-B)
    shape_b : {object} the shape B (in difference A-B)
    color   : {tuple} of (r,g,b) coordinates
    """
    def __init__(self, shape_a, shape_b):
        """Constructs a DiffShape as difference between two given shapes
        shape_a and shape_b.

        Note: color or difference should be the color of shape_a."""
        self.shape_a = shape_a
        self.shape_b = shape_b
        self.color = shape_a.color

    def mu(self, x, y):
        """Characteristic function of the shape.
        Returns True if (x,y) is inside the shape, else False.

        Parameters
        ----------
        x : {int} x coordinate of a pixel
        y : {int} y coordinate of a pixel

        Returns
        -------
        bool : True or False whether (x,y) is within the shape.
        """
        return(self.shape_a.mu(x,y) and not self.shape_b.mu(x,y))
