import unittest

import maclasse

class TestClasse(unittest.TestCase):


	def test_life_objet(self):
	    self.assertIsInstance(bird.gettingolder(),int)

	def test_life(self) :
	    res=True
	    if bird.age>5:
	        res=False
	    self.assertIs(self.life, res)

	def life_object2(self):
	    self.assertIsInstance(bird.life,bool)

	def test_weight(self): #vérifie que weight est positif
		res=True
		if self.weight<1:
			res=False
		self.assertTrue(res)

	def test_age(self):
		self.assertNotEqual(self.age, 0)

	def test_paws(self): #vérifie que le nombre de pattes est 2, 4, 6 ou 8
		a=[2, 4, 6, 8]
		self.assertIn(self.paws, b)

