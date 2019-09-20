from unittest import TestCase
from com.kuma.conta import Conta

class test_conta (TestCase):
	def setUp (self):
		self.conta = Conta()
		
	def test_debito(self):
		self.assertEqual (self.conta.debito (500), 505, "should be 505")