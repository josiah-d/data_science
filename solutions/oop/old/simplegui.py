#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

class SimpleGUI():
    """A Graphical User Interface using matploblib to display
    shapes using their characteristic function.

    Each shape is represented by a class with a color and a characteristic
    function (method) mu(). For displaying shapes, this class

    Parameters
    ----------
    None

    Attributes
    ----------
    width  : {int} the width of the image generated
        and the maximum value for x coordinates of pixels.
    height : {int} the height of the image generated
        and the maximum value for y coordinates of pixels.
    pixels : the matrix of colors for each pixel (to generate img)
    img    : {PIL.Image} the image generated for display.
    """
    def __init__(self):
        self.width = 640
        self.height = 480
        self.img = None
        self.pixels = None
        self.clear()

    def show(self):
        """Shows the current image on display (uses matplotlib).
        Uses attribute img, transforms it into an array
        and use plt.imshow() to display it.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        plt.imshow(np.asarray(self.img), aspect='equal')
        plt.axis('off')
        plt.show()

    def clear(self):
        """ Resets the image to white, draw a black border around.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.img = Image.new( 'RGB', (self.width, self.height), "white" )
        self.pixels = self.img.load()
        # horizontal borders
        for i in range(self.width):
            self.pixels[i,0] = (0, 0, 0)
            self.pixels[i,self.height-1] = (0, 0, 0)
        # vertical borders
        for j in range(self.height):
            self.pixels[0,j] = (0, 0, 0)
            self.pixels[self.width-1,j] = (0, 0, 0)

    def test(self):
        """Displays a test image.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.clear()
        for i in range(self.width):
            for j in range(self.height):
                self.pixels[i,j] = (i % 255, j % 255, 128)
        self.show()

    def draw(self, shape_list):
        """Draw a list of shapes as defined in module shapes.py
        and show() the result.

        Parameters
        ----------
        shape_list : a {list} of shapes

        Returns
        -------
        None
        """
        # clears the image
        self.clear()

        # checks for every pixel in the image
        for i in range(self.width):
            for j in range(self.height):
                # if we are in one of the areas in the list
                for o in shape_list:
                    if o.mu(i,j):
                        # drop a pixel in there, using color of the area
                        self.pixels[i,j] = (int(o.color[0]),
                                            int(o.color[1]),
                                            int(o.color[2]))

        # systematically show the resulting image
        self.show()
