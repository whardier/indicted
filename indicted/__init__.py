
#!/usr/bin/env python
#
#  Copyright (c) 2012  Shane R. Spencer
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of
#  this software and associated documentation files (the "Software"), to deal in
#  the Software without restriction, including without limitation the rights to
#  use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
#  of the Software, and to permit persons to whom the Software is furnished to do
#  so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

"""indicted - Indexed Dictionary Class"""

__name__ = "indicted"
__author__ = 'Shane R. Spencer'
__email__ = "shane@bogomip.com"
__license__ = 'MIT'
__copyright__ = '2012 Shane R. Spencer'
__version__ = '0.0.1'
__status__ = "Prototype"
__description__ = "Indexed Dictionary Class"

from collections import OrderedDict

class InList(list):
    def __init__(self, iterable=[], indexclass=None, indexkey=None):
        self.__ids = {}
        list.__init__(self, iterable)

        for n, i in enumerate(self):
            if issubclass(type(i), dict):
                _id = i.get(indexkey)
                if issubclass(type(_id), indexclass):
                    self.__ids[_id] = int(n)

    def find(self, id):
        _n = self.__ids.get(id)
        if not isinstance(_n, None.__class__):
            return self[_n]
        else:
            return None

    def ids(self):
        return sorted(self.__ids.keys(), key=lambda k: self.__ids[k])

class _InDict(object):

    INDEXCLASS = int
    INDEXKEY = "_id"

    def __init__(self, *args, **kwargs):
        if issubclass(type(self), dict):
            self.__dict_class = dict
        if issubclass(type(self), OrderedDict):
            self.__dict_class = OrderedDict    
        self.__dict_class.__init__(self, *args, **kwargs)

    def __setitem__(self, key, val):
        if issubclass(type(val), list): val = InList(val, self.INDEXCLASS, self.INDEXKEY)
        self.__dict_class.__setitem__(self, key, val)


class InDict(_InDict, dict):
    pass

class OrderedInDict(_InDict, OrderedDict):
    pass      
