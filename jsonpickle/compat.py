try:
    set = set
except NameError:
    from sets import Set as set
    set = set

try:
    unicode = unicode
except NameError:
    unicode = str
