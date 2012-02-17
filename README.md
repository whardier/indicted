MongoDict
=========

MongoDict - PyMongo Document Helper Classes

Usage
-----

Take for example the following data.  This structure is being used to reduce 
relationships between a parent object and sub objects.  This allows us to create 
indexes that help with relationships rather than making multiple calls to a 
database.  This is just an example structure of a document.

```javascript
{
    "_id" : ObjectId("4f3eb7cac4f804960a859467"),
    "subdata" : [
        {
            "_id" : ObjectId("4f3eb7cac4f804960a859468"),
            "bits" : 1234
        },
        {
            "_id" : ObjectId("4f3eb7cac4f804960a859469"),
            "bits" : 5678
        }
    ]
}
```

If we access the **subdata** key in the root of this document we will be given 
an array when using standard Dict/List types.

```python
[{u'_id': ObjectId('4f3eb7cac4f804960a859468'), u'bits': 1234.0},
 {u'_id': ObjectId('4f3eb7cac4f804960a859469'), u'bits': 5678.0}]
```

Ideally we would want to return the list element that matches a specific **_id** 
if the list contains dictionaries that have a key matching that ObjectId.  This 
is where MongoDict and MongoList comes in.  MongiDict is a simple Dict wrapper 
that uses MongoList for all list type values.  As MongoList is initialized and 
modified it keeps an internal dictionary of **_id** references relating to list 
positions.  An extra function called **MongoList.find_id** is used to pull out a 
referenced object if it finds one.  **None** is returned otherwise.
    
```python
import pprint
import pymongo

from mongodict import MongoDict

from pymongo.objectid import ObjectId

connection = pymongo.Connection(document_class=MongoDict)
database = connection.test

data = database.data.find_one()

pprint.pprint(data['subdata'].find_id(ObjectId('4f3eb7cac4f804960a859469')))
pprint.pprint(data['subdata'].find_id(ObjectId('000000000000000000000000')))
```

Yields

```python
{u'_id': ObjectId('4f3eb7cac4f804960a859469'), u'bits': 5678.0}
None
```

