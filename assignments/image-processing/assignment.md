# Image Processing
- [Image Processing](#image-processing)
  - [Basic](#basic)
    - [Part 1: Image Processing Basics](#part-1-image-processing-basics)
  - [Advanced](#advanced)
    - [Part 2: Cat vs. Dog Image Classification](#part-2-cat-vs-dog-image-classification)
## Basic
### Part 1: Image Processing Basics

Use [`skimage`](http://scikit-image.org/) to practice basic image processing techniques.

1. Use `skimage.io.imread()` to read in the following images: 

   - `data/einstein.jpg`
   - `data/goodall.jpg`
   - `data/forest.jpg`
   - `data/beach.jpg`
   
   The images are read in as `numpy.ndarray`s. Examine the shape of images and resize the images to `300 x 300` pixels
   using `skimage.transform.resize()`.

2. Import `matplotlib` to show the images (`numpy.ndarray`) you have read in. Using the OO Artist interface, you'll want to use [ax.imshow](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.imshow.html) 
 

3. Say you were making a machine learning model to differentiate:

   i. `Albert Einstein` from `Jane Goodall`
   
   ii. `forest` from `beach`

   Which set of images would you grayscale (`i.` or `ii.`)? Explain your answer.
   
   Use `skimage.color.rgb2gray()` to grayscale the chosen set of images. Show the images to verify the transformation took
   place.  Note the `.shape` of the image.  From a computation and image storage perspective, single channel images (like gray-scale) offer advantages over 3 channel images.
   
4. Apply the Sobel (`skimage.filters.sobel()`) and Canny (`skimage.feature.canny()`) to the grayscaled images.
   Show the images to see the effect of the filters. Which one performs better in terms edge detection? Why might
   an edge detection filter be useful in an image classification problem?
   
   The Canny filter also takes a `sigma` argument which decides the level of denoising before the core edge detection 
   algorithm is executed. A higher `sigma` means more denoising and suppresses less prominent edges, and vice versa.
   Test out a few values of `sigma` in the range of `0` to `5` and settle on a value you think is appropriate for the 
   classification. (Do not spend more than a few minutes testing out `sigma`)

5. You might also be interested in applying some denoising after edge detection to smooth out some of the edges in order to
   achieve a better representation of the class of the image. Try out the following 2 algorithms:
   
   1. Bilateral (`skimage.restoration.denoise_bilateral`)
   2. Total Variation (`skimage.restoration.denoise_tv_chambolle`)
   
   **Hint :**
   - Total Variation denoise takes a `weight` argument where it weights the extent of denoising relative to retaining the
     details of the image, i.e. higher `weight` means more denoising. Try `weight` in the range of `0.3` to `3` and pick the
     number that would give the best signal:noise ratio. 
   
   - Bilateral denoise takes a `sigma_spatial` argument where a larger value results in averaging of pixels with larger spatial differences.
   
6. For the set of images you have not grayscaled (`Hint: scenery images`), color plays an important role in determining which
   class the image belongs to. In such cases, you are interested in extracting the dominant colors of the image.
   
   To extract the K most dominant colors of an image, one common practice is to cluster the RGB pixels using K-Means. This will group similarly colored pixels into some pre-chosen number of clusters. The centroids of the clusters can be seen as the dominant colors.
   
   Use the following code (or use `numpy.reshape`) to get a list of all the RGB pixels:
   
   ```python
   # Getting a list of all RBG pixels in an image
   nrow, ncol, depth = image_array.shape 
   lst_of_pixels = [image_array[irow][icol] for irow in range(nrow) for icol in range(ncol)]
   ```
   Review the documentation of [K-Means](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) and use it to divide each color image into three clusters and return the three dominant colors (centroids) of each image.

7. Write a function to featurize the `einstein` and `goodall` images. You will need to flatten the images and stack
   the flattened vectors by rows ([`numpy.r_`](http://docs.scipy.org/doc/numpy/reference/generated/numpy.r_.html))
   
   This is your feature matrix of the images. In a typical classification problem, you will have more samples.
   
<br>

## Advanced
### Part 2: Cat vs. Dog Image Classification

Now we have learned the basics of image processing, let's use the techniques on an actual image classification 
problem. We are going to classify dog from cat from images of dog/cat.
 
Remember the image processing pipeline is as follows:

- `Read`
- `Resize`
- `Transform`
- `Vectorize`


1. Decompress `data/cat_dog.zip`. Take a look at the `cat_dog` directory, it contains the sub-directories `cat` and `dog`.
   The `cat` sub-directory contains all the cat images and the `dog` sub-directory contains all the dog images.

2. To read and transform all the images in the sub-directories, you will need to loop through the sub-directories 
   and read in the images whilst keeping the images in 2 separate lists so you can still differentiate images of
   one class from the other. 
   
   A module has been implemented for you that will handle reading in and processing images in this directory structure.
   Examine the code in `src/pipeline.py` and make sure you understand the structure of the code on a high level.
   
3. Instantiate the `ImagePipeline` class by providing the path of the parent directory (`cat_dog`). Use the `read()`
   to read in all the images within the sub-directories of `cat_dog`. Provide the argument `sub_dirs` as a list of
   names of the sub-directories.
   
4. You can show any of the images you have read in by using `show()`, which takes 2 arguments (the sub-directory name
   as a string and the nth image in the sub-directory as an integer).
   
5. Resize all the images using `resize()`. Try a few sizes and show the effects of down-sampling (by using `show()` on
   a few images) and pick a size that yields a good compromise between the resolution and the size of the image.
    
6. Use `transform()` to apply various filters and denoising functions to the images. Remember to `show()` a few images
   along the way to guide the transformations you are going to perform. Make sure you are emphasizing the features of 
   the images that help differentiate images of one class from another. 
   
   The first argument of `transform()` is an `skimage` function and the second argument is a dictionary of additional
   arguments to the `skimage` function excluding the image array itself. 
   
   ```python
   pipe = ImagePipeline('cat_dog')
   pipe.read(sub_dirs=['cat', 'dog'])
   # Resize....
   pipe.transform(skimage.color.rgb2gray, {})
   pipe.show('cat', 10)
   ```

7. Now we are done with all the image transformations, compute the image feature matrix (`x`) and the 
   response labels (`y`). Call `vectorize()` and access the features and labels by `.features` and `.labels` respectively.

8. Train a `RandomForestClassifier()` on the image features and the labels. Find the best model using GridSearchCV.
.

