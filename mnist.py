import theano.tensor as T
from data import *


class MNIST(DesignMatrix):

    def theano_vars(self):
        return [T.fmatrix('inp'), T.lvector('out')]
