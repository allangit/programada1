import pandas as pd
from keras.layers import Dense
from keras.models import Sequential
import numpy as np


class Redes_neuronales:


	def __init__(self):
	
		self.model=0
		self.x=0
		self.y=0
	
	def build_NetWork(self):
	
		self.model=Sequential()
		self.model.add(Dense(12,input_dim=8,activation='relu'))
		self.model.add(Dense(8,activation='relu'))
		self.model.add(Dense(1,activation='sigmoid'))

	def compilar(self):

		self.compile()

		

	
		
