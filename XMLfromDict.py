from collections import OrderedDict
dictionary = OrderedDict([
    ('key', 'val'),
    ('key2', {'subkey': "subval"})
])


for key, val in dictionary.items():
    print("<{0}>{1}</{0}>".format(key, val))
