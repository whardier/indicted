indicted
=========

indicted - Indexed Document Class

Summary
-------

Find an list element, which is a dict, by a keys value

Usage
-----

Take for example the following data.  This structure is being used to reduce 
relationships between a parent object and sub objects.  This allows us to create 
indexes that help with relationships rather than making multiple calls to a 
database.  This is just an example structure of a document.  This specific 
structure will benifit heavily from a multi-value index on **subdata._id**.

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
is where indicted and Inist comes in.  InDict is a simple Dict wrapper 
that uses InList for all list type values.  As InList is initialized and 
modified it keeps an internal dictionary of **_id** references relating to list 
positions.  An extra function called **InList.find** is used to pull out a 
referenced object if it finds one.  **None** is returned otherwise.
    
```python
import pprint
import pymongo

from bson import ObjectId

from indicted import InDict

class MongoInDict(InDict):
    INDEXCLASS = ObjectId
    INDEXKEY = '_id'

connection = pymongo.Connection(document_class=MongoInDict)
database = connection.test

data = database.data.find_one()

pprint.pprint(data['subdata'].find(ObjectId('4f3eb7cac4f804960a859469')))
pprint.pprint(data['subdata'].find(ObjectId('000000000000000000000000')))
```

Yields

```python
{u'_id': ObjectId('4f3eb7cac4f804960a859469'), u'bits': 5678.0}
None
```

There is also **indicted.OrderedInDict** that inherits 
**collections.OrderedDict**.  This is incredibly useful for maintaining the 
document key ordering of your documents.

Status
------

Currently this module only creates references during the initialization of the 
list.  This will be addressed soon.
    
Todo
----

* Dot notation
* JSON encoding/decoding/pretty printing helpers
