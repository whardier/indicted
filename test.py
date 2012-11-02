from indicted import InDict, OrderedInDict

class TestInDict(InDict):
    INDEXCLASS = str
    INDEXKEY = 'testid'

a = TestInDict()

a['subdata'] = [{'testid': '1'},{'testid': '2'}]

print a['subdata'].find('1')
print a['subdata'].find('2')

class TestOrderedInDict(OrderedInDict):
    INDEXCLASS = int
    INDEXKEY = '_id'

b = TestOrderedInDict()

b['subdata'] = [{'_id': 1},{'_id': 2}]

print b['subdata'].find(1)
print b['subdata'].find(2)
