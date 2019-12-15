from colordescriptor import ColorDescriptor   # from colordescriptor.py
import argparse   # for parsing command line arguments
import glob   # for grabbing the file paths to our images
import cv2   # OpenCV


# Construct the argument parser and parse the arguments
### --dataset: the path to our dog images directory
### --index: the output CSV file containing the image filename and the features associated with each image
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
	help = "Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
args = vars(ap.parse_args())




# Initialzie the color descriptor - Extract the features
cd = ColorDescriptor((8, 12, 3)) # (Hue, Saturation, Value)



# Write the extracted features into a CSV file
csv = open(args["index"], "w")

for imagePath in glob.glob(args["dataset"] + "/*.png"):

	# Assign a unique ID to the extracted images
	imageID = imagePath[imagePath.rfind("/") + 1:]
	image = cv2.imread(imagePath)

	features = cd.describe(image)

	features = [str(f) for f in features]
	csv.write("%s,%s\n" % (imageID, ",".join(features)))

csv.close()