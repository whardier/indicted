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

import pymongo

from pymongo.objectid import ObjectId

from collections import OrderedDict

class MongoList(list):
    def __init__(self, iterable=[]):
        list.__init__(self, iterable)
        self.__ids = {}

        for n, i in enumerate(self):
            if issubclass(type(i), dict):
                _id = i.get('_id')
                if issubclass(type(_id), ObjectId):
                    self.__ids[_id] = int(n)            

    def find_id(self, id):
        _n = self.__ids.get(id)
        if not isinstance(_n, None.__class__):
            return self[_n]
        else:
            return None


class _MongoDict(object):
    def __init__(self, *args, **kwargs):
        if issubclass(type(self), dict):
            self.__dict_class = dict
        if issubclass(type(self), OrderedDict):
            self.__dict_class = OrderedDict    
        self.__dict_class.__init__(self, *args, **kwargs)

    def __setitem__(self, key, val):
        if issubclass(type(val), list): val = MongoList(val)
        self.__dict_class.__setitem__(self, key, val)


class MongoDict(_MongoDict, dict):
    pass


class MongoOrderedDict(_MongoDict, OrderedDict):
    pass      
