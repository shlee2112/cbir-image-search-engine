import numpy as np
import csv

class Measure:

	def __init__(self, indexPath):
		self.indexPath = indexPath # path to the index.csv



	# search the 5 most relevant images from the dataset based on the query image
	def similarity(self, queryFeatures, limit = 5):
		results = {}

		# By comparing the distance between the two feature vectors, it pulls the most relevant images.
		with open(self.indexPath) as f:
			reader = csv.reader(f)

			for row in reader:
				features = [float(x) for x in row[1:]]
				d = self.chi2_distance(features, queryFeatures)

				results[row[0]] = d

			f.close()

		# 5 images with the smallest chi-squared similarity value will be shown.
		results = sorted([(v, k) for (k, v) in results.items()])

		return results[:limit]



	def chi2_distance(self, histA, histB, eps = 1e-10):

			d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
				for (a, b) in zip(histA, histB)])

			return d
