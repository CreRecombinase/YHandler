import xml.etree.cElementTree as ET
from BaseSelector import BaseSelector

class DefaultSelector(BaseSelector):

	def __init__(self, root=None):
		super(DefaultSelector, self).__init__()
		self.root = root
		self.text = root.text if root else ''

	def parse(self, content):
		self.root = ET.fromstring(content)
		return DefaultSelector(self.root)

	def select(self, query, ns=None):
		els = []
		for el in self.root.findall(query, ns):
			selector = DefaultSelector(el)
			els.append(selector)
		return els

	def select_one(self, query, ns=None):
		el = self.root.findall(query, ns)
		if not el:
			return DefaultSelector()
		else:
			return DefaultSelector(el)		

	def iter_select(self, query, ns=None):
		for el in self.root.iterfind(query, ns):
			selector = DefaultSelector(el)
			yield selector
