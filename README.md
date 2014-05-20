Dataset Creator for Cuda Convnet
==============

Create datasets for cuda-convnet (http://code.google.com/p/cuda-convnet/).

Input: Folder with images.

Output: Batch files that can be loaded with the Data Providers in cuda-convnet.

Usage:
```python
    from ConvnetDataset import *
    
    ConvnetDataset.CreateConvNetDataset(SourceFolder = sourceFolder, 
                                        TargetFolder = saveFolder,
                                        ExpectedDistribution = expectedDistribution)
```

Options:

* **SourceFolder**: Folder where the input images are located
* **TargetFolder**: Folder to store the batch files
* **ExpectedDistribution**: Tuple with 3 values: expected distribution among Train, Validation, Test
* **Classes**: Which class numbers should be used to build the dataset
* **ClassNames**: Name of the classes (for visualization using convnet's "shownet.py" only)
* **GetLabelsFrom** (default: LabelFromFirstChars(2)): A function to obtain the label from the filename of the image
* **Grayscale** (default: False): Loads the images in grayscale instead of color
* **InvertColor** (default: False): Inverts the image when loading them
* **ResizeBy** (default: None): A function to resize each image when loading them
* **Preprocessor** (default: None): A function to be applied before splitting the dataset (e.g. to extract patches)
* **SplitFunction** (default: ClassBalancingSplit()): A function that splits a dataset into train, valid and test
* **NumTrainBatches** (default: 3): Number of training batch files to be created 
* **Log** (default: True): Logs the image loading process in the screen


Bultin function to get labels from the filenames:

* **LabelFromFirstChars(n)**: Gets the label from the first n chars from the filenames
* **LabelFromList(names, separator)**: Gets the label finding the class name in a list. The class name if everything in the filename before the separator.
    
Builtin functions to resize images:
* **ResizeByPercent(percent)**: Resizes each each to *percent* of original size
* **ResizeToSquare(newSize)**: Resizes the image to square of size *newSize x newSize*, without distortion

Builtin functions to split the dataset:
* **ClassBalancingSplit()**: Splits the dataset into Train, Valid and Test mainting the classes balanced in each split.
* **GroupingSplit(GetSampleNumberFunction)**: Splits the dataset ensuring all images from a given sample are grouped (e.g. all images of a given group belong to the same split). The function to get the sample number from the filename should be provided. The default behavior is to parse a filename like this: \<class\>\_\<sample\>\_*.\<ext\>


Example:
```python
    from ConvnetDataset import *
  
    sourceFolder = '/home/data/images/genre_images'
    saveFolder = '/home/data/genre_convnet'
    expectedDistribution = [0.5, 0.2, 0.3] #Train: 50%, Valid: 20%, Test: 30%


    classNames = ["axe", "bachata", "bolero", "forro", "gaucha", 
                  "merengue", "pagode", "salsa", "sertaneja", "tango"]
    classNumbers = range(10) #Use all classes


    ConvnetDataset.CreateConvNetDataset(SourceFolder = sourceFolder, 
                                            TargetFolder = saveFolder,
                                            ExpectedDistribution = expectedDistribution,
                                            ResizeBy = ResizeByPercent(0.6),
                                            Classes = classNumbers,
                                            ClassNames = classNames,
                                            Grayscale = True)
```
