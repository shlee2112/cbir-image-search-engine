from colordescriptor import ColorDescriptor   # from colordescriptor.py
from measure_distance import Measure # from search.py
import argparse   # for parsing command line arguments
import cv2   # OpenCV



# Construct the argument parser and parse the arguments
### --index: the output CSV file containing the image filename and the features associated with each image
### --query: the path to the query image
### --result-path: the path to the dog photos dataset
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())




# Initialzie the color descriptor - Extract the features of the query image
cd = ColorDescriptor((8, 12, 3)) # (Hue, Saturation, Value)

# load the query image and extract color features
query = cv2.imread(args['query'])
features = cd.describe(query)

# Compare the distance of the feature vectors to find 5 most relevant images.
measure = Measure(args['index'])
results = measure.similarity(features)

# Show the query image on the screen
cv2.imshow("Query", query)


# Show the 5 relevant images on the screen
for (score, resultID) in results:
	result = cv2.imread(args["result_path"] + "/" + resultID)
	cv2.imshow("Result", result)
	cv2.waitKey(0)








