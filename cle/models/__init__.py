import ipdb
import theano

from collections import OrderedDict
from cle.cle.utils import (
    flatten,
    tolist,
    topological_sort,
    PickleMixin
)


class Model(object):
    """
    Abstract class for models

    Parameters
    ----------
    .. todo::
    """
    def __init__(self, inputs=None, nodes=None, params=None, updates=None):
        self.inputs = inputs
        self.nodes = nodes
        self.params = params
        self.updates = OrderedDict()
        if updates is not None:
            for update in updates:
                self.updates[update] = update

    def set_updates(self, updates):
        for update in updates:
            self.updates[update] = update
