'''
Unit tests for Bernoulli Naive Bayes
Usage: from main nlp directory run: py.test test/unittest_bernoulli.py
'''

import unittest as unittest
import numpy as np
from src.bernoulli_naive_bayes import BernoulliNaiveBayes

def laplace(n, d):
    return (n + 1.) / (d + 1. * 2)

class TestNaiveBayes(unittest.TestCase):

    def setUp(self):
        X = ['a long fishing document about fishing',
             'a book on fishing',
             'a book on knot-tying']
        self.X = [x.split() for x in X]
        self.y = np.array(['fishing', 'fishing', 'knot-tying'])
        self.nb = BernoulliNaiveBayes()
        self.nb.fit(self.X, self.y)

    def tearDown(self):
        self.X = None
        self.y = None
        self.nb = None

    def test_class_counts(self):
        self.assertEqual(self.nb.class_counts['fishing'], 2)
        self.assertEqual(self.nb.class_counts['knot-tying'], 1)

    def test_p_is_number_features(self):
        self.assertEqual(self.nb.p, 8)

    def test_class_feature_counts(self):
        self.assertEqual(self.nb.class_feature_counts['knot-tying']['fishing'], 0)
        self.assertEqual(self.nb.class_feature_counts['fishing']['document'], 1)
        self.assertEqual(self.nb.class_feature_counts['fishing']['fishing'], 2)

    def test_predict(self):
        test_X = [["book"]]
        posts = self.nb.posteriors(test_X)
        preds = self.nb.predict(test_X)
        fishing_likelihood = -6.9314718
        knot_tying_likelihood = -6.421774665
        self.assertAlmostEqual(fishing_likelihood, posts[0]['fishing'])
        self.assertAlmostEqual(knot_tying_likelihood, posts[0]['knot-tying'])
        self.assertEqual(preds[0], 'knot-tying')
        self.assertNotEqual(preds[0], 'fishing')

    def test_score(self):
        self.assertEqual(self.nb.score(self.X, self.y), 1.)


if __name__ == '__main__':
    unittest.main()
