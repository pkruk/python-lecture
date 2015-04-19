__author__ = 'Piotr Kruk'

from sklearn.datasets import load_svmlight_file
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import normalize
from matplotlib import pyplot as plt
import numpy as np
import warnings
import pickle

warnings.filterwarnings('ignore')

class FacesClassifier(object):

    def __init__(self, model='Kruk.model'):
        self.model = pickle.load( open( model, "rb" ) )

    def predict(self, X):
        X = normalize(X)
        return self.model.predict(X)
