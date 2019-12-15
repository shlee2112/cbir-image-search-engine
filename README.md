# Content-Based Image Retrieval (CBIR) Search Engine
## Sanghyun Lee


## Project Description
I developed an image search engine that returns the most relevant image based on the query image by utilizing Content-Based Image Retrieval (CBIR) system. It uses Python and OpenCV, which is an open-source BSD-licensed computer vision library and includes several hundreds of computer vision algorithms. This system quantifies the dataset by utilizing an image descriptor to extract HSV color histogram features from each image. Then, when a query image is submitted, it finds similar images by comparing the chi^2 distance similarity.

![Image of CBIR Process](https://github.com/shlee2112/cbir-image-search-engine/blob/master/img/cbir_process.png)



## Dataset
I used [Stanford Dog Dataset](http://vision.stanford.edu/aditya86/ImageNetDogs/) to extract HSV color features and compare similarities with a query image. To get a faster result, I reduced the number of images from 20K to 1.5K. ALso, the dataset includes images of African Hunting Dogs, Toy Poodles, Pembroke Welsh Corgis, Eskimo Dogs, German Shepherds, Border Collies, Golden Retrievers, Beagles and Boston Bulls.
<!-- 
![Image of Stanford Dog Dataset](https://github.com/shlee2112/cbir-image-search-engine/blob/master/img/stanford_dogs.png)
 -->

## Script Description
### colordescriptor.py
This script stores `ColorDescriptor` class, which extracts the HSV color histrogram features for each image in the dataset.

### index.py
This script initializes `ColorDescriptor` from `colordescriptor.py` and indexes the features of the stored dog photos.

### measure_distance.py
It compares distance between two features vectors of the queried image and dog photos in the dataset. Then, it produces 5 images of the smalled chi-squared similarity value.

### search.py
Lastly, this script will show the 5 most relevant dog photos based on the query image.



## Installation
Please install following packages to run:
```
$ sudo pip install opencv-contrib-python
$ sudo pip install opencv-python
$ pip install imutils
```


## How to run the image search engine
1. Run `	
$ python index.py --dataset dataset --index index.csv` on the terminal to index the extracted features from the dataset
2. Run `$ wc -l index.csv` to check if 1471 dog photos are successfully indexed.
3. Run `$ python search.py --index index.csv --query queries/pembroke.png --result-path dataset` to discover the most relevant dog photos! Press Enter to view the next photos. 
- For #3 you can also try following query images:
	- african_hunting.png
	- beagle.png
	- border_collie.png
	- boston_bull.png
	- eskimo.png
	- german_shepherd.png
	- golden_retriever.png
	- pembroke.png
	- toy_poodle.png





## Code Reference
The code in this project was modified and was originally demostrated in an article called, [The complete guide to building an image search with Python and OpenCV](https://www.pyimagesearch.com/2014/12/01/complete-guide-building-image-search-engine-python-opencv/)