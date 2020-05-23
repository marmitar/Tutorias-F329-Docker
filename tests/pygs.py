import pygments
from pygments import lexers, formatters

lxr = lexers.get_lexer_by_name('python')
fmt = formatters.get_formatter_by_name('latex')

res = pygments.highlight('import numpy', lxr, fmt)

assert res.find('\\') >= 0
assert res.find('{') >= 0
