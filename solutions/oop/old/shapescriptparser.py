#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shapes import Circle, Rectangle
from operators import UnionShape, IntersectionShape, DiffShape
from collections import OrderedDict

class ShapeScriptParser():
    """A parser for a scripting language
    that would generate shapes (as objects defined in shapes.py)
    and display the result on screen (using SimpleGUI).

    Parameters
    ----------
    gui : {SimpleGUI} a gui object for drawing pixels.

    Attributes
    ----------
    gui     : {SimpleGUI} object for drawing shapes
    shape_register : {OrderedDict} of shapes to draw
    """
    def __init__(self, gui):
        """Instantiates the parser, gui is provided for drawing.
        """
        self.gui = gui
        self.shape_register = OrderedDict()


    def parse(self, filepath):
        """Parses a file line by line using parse_line().

        Parameters
        ----------
        filename : {str} the path to the file

        Returns
        -------
        None
        """
        self.shape_register = OrderedDict()
        with open(filepath, 'r') as sfile:
            for line in sfile:
                self.parse_line(line.strip())


    def parse_line(self, line):
        """Parses one line of the scripting language.
        Creates the corresponding object.

        Parameters
        ----------
        line    : {str} the line to parse

        Returns
        -------
        None
        """
        args = line.split(',')

        key = args[0]

        if args[1] == 'circle':
            x, y, rad, r, g, b = map(int,args[2:])
            self.shape_register[key] = Circle(x,y,rad,(r,g,b))
        elif args[1] == 'rectangle':
            x1, y1, x2, y2, r, g, b = map(int,args[2:])
            self.shape_register[key] = Rectangle(x1,y1,x2,y2,(r,g,b))
        elif args[1] in {'union', 'intersection', 'difference'}:
            keyA, keyB = args[2:]
            if not (keyA in self.shape_register and keyB in self.shape_register):
                print('error: shape {} or {} do not exist'.format(keyA,keyB))

            if args[1] == 'union':
                self.shape_register[key] = UnionShape(self.shape_register[keyA],
                                                      self.shape_register[keyB])
            if args[1] == 'intersection':
                self.shape_register[key] = IntersectionShape(self.shape_register[keyA],
                                                      self.shape_register[keyB])
            if args[1] == 'difference':
                self.shape_register[key] = DiffShape(self.shape_register[keyA],
                                                      self.shape_register[keyB])
        else:
            print('error: shape {} unknown'.format(args[1]))


    def draw(self):
        """Draws objects that have been created previously
        with parse() or parse_line().

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.gui.draw(self.shape_register.values())
