# Image Processing

Images and video are a growing source of data for data scientists and machine-learning algorithms.  Python has image processing libraries that making working with images easy.  These libraries treat images as numpy arrays, so that operations you already know to slice and index arrays work similarly for images.

* [scikit-image](http://scikit-image.org/) is included in the Anaconda distribution of Python. It's developed by the SciPy community and has good [documentation](http://scikit-image.org/docs/dev/index.html) and a large gallery of [examples](http://scikit-image.org/docs/dev/auto_examples/index.html).  

* [OpenCV-Python](https://pypi.python.org/pypi/opencv-python) is a Python wrapper for [OpenCV](https://opencv.org/), an open source C++ computer vision library that is used academically and commercially.  Though not installed as part of a standard Python distribution, OpenCV should be consided when your image processing pipeline includes taking images using hardware.

* [PIL](http://effbot.org/imagingbook/), the Python Imaging Library, comes with Python but documentation and development are lacking.  [Pillow](https://pillow.readthedocs.io/en/5.1.x/) claims to be a "user-friendly" fork of PIL.

As scikit-image (skimage) comes installed with Anaconda's distribution of Python and has arguably the best Python documentation of the libraries above, it's recommended for the assignment.  However, skimage, OpenCV, PIL and Pillow have all been used successfully in student projects.


The goal of this repo is to give you experience in a typical image processing pipeline:

  1. `Read`
  2. `Resize`
  3. `Transform`
  4. `Featurize`

You'll be using this pipeline in an image classification problem in the [assignment](assignment.md).

