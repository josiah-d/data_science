#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

class Circle():
    """A circular shape as defined by a center point and radius.
    This shape is designed to be drawn using SimpleGUI (see simplegui.py).

    Parameters
    ----------
    cx      : {int} x coordinate of the center point
    cy      : {int} y coordinate of the center point
    radius  : {int} radius of the circle
    color   : {tuple} of (r,g,b) coordinates
    """
    def __init__(self, cx, cy, radius, color):
        """Constructs a Circle instance
        centered around (cx,cy) with given radius and color.
        """
        self.cx = cx
        self.cy = cy
        self.radius = radius
        self.color = color

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
        t_dist = math.sqrt((x - self.cx)**2 + (y - self.cy)**2)
        return (t_dist < self.radius)


class Rectangle():
    """A rectangular shape as defined by two extreme pixels points
    (one upper-left, one lower-right).
    This shape is designed to be drawn using SimpleGUI (see simplegui.py).

    Parameters
    ----------
    x0      : {int} x coordinate of the top-left point
    y0      : {int} y coordinate of the top-left point
    x1      : {int} x coordinate of the bottom-right point
    y1      : {int} y coordinate of the bottom-right point
    color   : {tuple} of (r,g,b) coordinates
    """
    def __init__(self, x0, y0, x1, y1, color):
        """Constructs a Rectangle instance
        with top-left point (x0,y0), bottom-right (x1,y1) and color.
        """
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.color = color

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
        if (x < self.x0):
            return(False)
        if (x > self.x1):
            return(False)
        if (y < self.y0):
            return(False)
        if (y > self.y1):
            return(False)
        return(True)
