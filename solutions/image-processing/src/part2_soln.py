from pipeline import ImagePipeline
from skimage.filters import sobel 
from skimage.feature._canny import canny
from skimage.restoration import denoise_bilateral, denoise_tv_chambolle
from skimage.color import rgb2gray
from skimage.transform import resize
from skimage.io import imread
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.model_selection import GridSearchCV

def read_images(): 
	'''
	Input: None
	Output: ImagePipline Object

    Please create the `cat_dog` folder using the zip file in the assignment repo.
    
	Initialize the ImagePipleine object and read through all of the images 
	to attach them to our ImagePipeline object. 
	'''
	ip = ImagePipeline('../data/cat_dog')
	ip.read(sub_dirs=('cat', 'dog'))

	return ip

def test_sizes(ip, init=False):
	'''
	Input: ImagePipeline Object
	Output: None

	Run through a number of different sizes of pictures and pick which one fits best -
	i.e. strikes a good compromise between the size and resolution of the image. 
	''' 

	if init: 
		shapes = [(200, 200, 3), (200, 250, 3), (250, 300, 3), (300, 300, 3), (400, 400, 3)]
	shapes = [(100, 100, 3), (150, 150, 3)]

	for shape in shapes: 

		ip.resize(shape=shape)
		ip.show('cat', 10)
		ip.show('cat', 50)
		ip.show('cat', 30)
		ip.show('dog', 10)
		ip.show('dog', 50)
		ip.show('dog', 30)

	'''
	I can still tell that the images are cats and dogs with 100 pixels, so I'm going to try 
	starting with that and seeing how that turns out. I don't think it will end up well, 
	but I'd like to try it. 
	'''

def test_transforms(ip): 
	'''
	Input: ImagePipeline Object
	Output: None

	Run through a couple of different transformations for our images and pick which one fits
	the best. 
	'''

	transformations = [rgb2gray, sobel, canny, denoise_tv_chambolle, denoise_bilateral]
	ip.resize((100, 100, 3))
	for transformation in transformations: 
		ip.transform(transformation, {})
		ip.show('cat', 10)
		ip.show('cat', 50)
		ip.show('cat', 30)
		ip.show('dog', 10)
		ip.show('dog', 50)
		ip.show('dog', 30)

	'''
	The grayscale transformation looks like it might help quite a bit. At least for the three cats 
	and three dogs that I looked at above, the cats all had some fractions of white, whereas the dogs
	didn't. Using the grayscale transformation makes this stand out a little bit more. 

	Using the sobel transformation also seemed to help a little. It highlighted the corners/sharp edges
	that were typically associated with a cats ears, which I think could be helpful in predicting
	whether its a cat or not. 

	The rest of the transformations look terrible - the canny, denoise_tv_chambolle, and denoise_bilateral
	transformations don't highlight any features (at least with the default parameters for those 
	transformations, which for right now is all I'm using). So from this I'm going to try 
	the grayscale transformation in my random forest and my sobel transformation in my random forest. 
	'''

def fit_rand_forest(image_size, transformation=None):
	'''
	Input: ImagePipeline Object, Tuple, List
	Output: List of floats. 

	Fit a random forest using the images in an ImagePipeline Object and a number of different
	transformations (holding the image size fixed), and output the accuracy score for identifying 
	the classes of images (dogs and cats). 
	''' 

	rf = RandomForestClassifier(random_state=1)
	ip = ImagePipeline('../data/cat_dog')
	ip.read(sub_dirs=('cat', 'dog'))
	ip.resize(shape = image_size)

	if transformation == rgb2gray: 
		ip.grayscale()
	elif transformation == sobel: 
		ip.grayscale()
		ip.transform(sobel, {})
	
	ip.vectorize()
	features = ip.features
	target = ip.labels

	X_train, X_test, y_train, y_test = train_test_split(features, target, random_state=1)

	rf.fit(X_train, y_train)
	rf_preds = rf.predict(X_test)
	rf_accuracy = accuracy_score(y_test, rf_preds)

	return rf_accuracy

def fit_best_model(parameters): 
	'''
	Input: None
	Output: Fitted Random Forest Model

	Return the best fitted Random Forest Model that we have used from above. 
	'''

	ip = ImagePipeline('../data/cat_dog')
	ip.read(sub_dirs=('cat', 'dog'))
	ip.resize(shape = (100, 100, 3))
	ip.grayscale()

	ip.vectorize()
	features = ip.features
	target = ip.labels
	
	rf = RandomForestClassifier()
	clf = GridSearchCV(rf, parameters, n_jobs=-1, cv=3, scoring='accuracy',
	                   verbose=True)
	clf.fit(features, target)
	return clf.best_estimator_, clf.best_params_, clf.best_score_	

def predict_img(model, filepath): 
	'''
	Input: Fitted model, Numpy Array
	Output: String

	Transform the image to fit the transformations we were using for our best random
	forest model (100, 100, 3), grayscale and then predict whether the given image is 
	a cat or a dog. 
	'''
	img = imread(filepath)
	img = img_transform(img)
	prediction = model.predict(img)

	output = 'dog' if prediction == 1 else 'cat'

	return output

def img_transform(img): 
	'''
	Input: Numpy Array
	Output: Numpy Array

	Transform an image by reshaping it and also applying a grayscale to it. 
	'''
	img = resize(img, (100, 100, 3))
	img = rgb2gray(img)
	img = np.ravel(img)

	return img

if __name__ == '__main__': 
	ip = read_images()
	#print('Testing image sizes')	
	#test_sizes(ip)
	#print('Test different transforms')
	#test_transforms(ip)

	'''
	for img_size in [(100, 100, 3), (200, 200, 3), (300, 300, 3), (400, 400, 3)]: 
		print 'Testing img size: %s' %str(img_size)
		accuracies = fit_rand_forest(image_size=img_size, transformation = rgb2gray)
		print 'Using rgb2gray: {0:.4f}'.format(accuracies)

	for img_size in [(100, 100, 3), (200, 200, 3), (300, 300, 3), (400, 400, 3)]: 
		print 'Testing img size: %s' %str(img_size)
		accuracies = fit_rand_forest(image_size=img_size, transformation = sobel)
		print 'Using both sobel and rgb2gray: {0:.4f}'.format(accuracies)

	for img_size in [(100, 100, 3), (200, 200, 3), (300, 300, 3), (400, 400, 3)]: 
		print 'Testing img size: %s' %str(img_size)
		accuracies = fit_rand_forest(image_size=img_size)
		print 'Using none: {0:.4f}'.format(accuracies)
	'''
	'''
	The best I got out of the above was 100, 100, just grayscaling it (63% accuracy). 
	I'm going to run through a couple of other different image sizes and see if I can't 
	get a little bit closer. 
	'''
	'''
	for img_size in [(80, 80, 3), (90, 90, 3), (100, 100, 3), (110, 110, 3), (120, 120, 3)]: 
		print 'Testing img size: %s' %str(img_size)
		accuracies = fit_rand_forest(image_size=img_size, transformation = rgb2gray)
		print 'Using rgb2gray: {0:.4f}'.format(accuracies)
	'''
	'''
	None of those worked very well either, so I'm going to try one last thing. I'm going to try 
	giving it a little room to not be square. 
	'''
	'''
	for img_size in [(100, 80, 3), (100, 90, 3), (90, 100, 3), (80, 100, 3)]: 
		print 'Testing img size: %s' %str(img_size)
		accuracies = fit_rand_forest(image_size=img_size, transformation = rgb2gray)
		print 'Using rgb2gray: {0:.4f}'.format(accuracies)
	'''
	''' 
	100 * 100 still seems to be the best. I find this very odd - the accuracy score seemed 
	to jump kind of all over the place when doing this, rather than moving more incrementally
	like I would have expected. 
	'''

	params = {'n_estimators': [10, 100, 1000],
	          'max_depth': [8, 12, 16]}
	best_rf, best_params, best_score = fit_best_model(params)

	print("\nBest parameters from the grid search:")
	print(best_params)
	print("\nCross validated score of best estimator:")
	print(best_score)
