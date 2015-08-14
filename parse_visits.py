import glob, os
from lxml import etree
from pprint import pprint as pp

def xpath_ns(tree, expr):
    "Parse a simple expression and prepend namespace wildcards where unspecified."
    qual = lambda n: n if not n or ':' in n else '*[local-name() = "%s"]' % n
    expr = '/'.join(qual(n) for n in expr.split('/'))
    nsmap = dict((k, v) for k, v in tree.nsmap.items() if k)
    return tree.xpath(expr, namespaces=nsmap)

for filename in glob.glob("visits/*.xml"):
	with open(filename, "rb") as f: txt = f.read()
	root = etree.fromstring(txt)
	date = xpath_ns(root, 'componentOf/encompassingEncounter/effectiveTime/low')[0].get('value')
	x = {vital.text: vital.getnext().text for vital in root.xpath("//*[starts-with(@ID, 'vital')]")}
	print(filename, date)
	pp(x)
	print("------------------------")