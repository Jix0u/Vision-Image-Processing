# MNIST Classification with SVM and CNN

Using SVM (Support Vector Machine) and CNN (Convolutional Neural Networks) algorithms to classify MNIST images 
Compare their performance based on varied dataset sizes

[Full Report Here](Full%20Report%20MNIST%20Classification.pdf)

# Comparing the performance of a traditional classification algorithm and a deep learning classification algorithm based on the size of the training set

How does the volume of training data affect the classification accuracy and training time of a Support Vector Machine (traditional) compared to Convolutional Neural Network (deep learning)?

Subject: Computer Science Word count: 3981

# 1. Introduction
Image classification is a core function in computer vision, and a necessary feature in automated medical diagnosis, vehicles, and security systems (Golemanova, 2018).

For a computer to classify an image, visual/training data must be fed into a classifier algorithm. Traditional classification algorithms are based on statistical analysis: the process of collecting/interpreting data to find underlying patterns/trends (Brooks, 2020). These algorithms are often simple in structure and require pre-processed labelled data. Comparatively, deep learning classification is based on an Artificial Neural Network: a machine imitation of a real, biological neural network composed of artificial neurons/brain cells. Deep learning models require hardly any user intervention as parameters are set automatically and data is pre-processed within the network (IBM, 2020).
Both types of classification algorithms are used extensively in bioinformatics to categorize genes among other biological issues (Chauhaun, 2019). However, the amount of available training data varies depending on the grandeur of the institution involved, forcing researchers to undergo an iterative selection process to find the most suitable algorithm.

This raises the question “How does the volume of training data affect the classification accuracy and training time of a traditional classification algorithm, Support Vector Machine (SVM), compared to a deep learning classification algorithm, Convolutional Neural Network (CNN)?”. In this paper, the performance of each algorithm on different dataset sizes will be analyzed, making it easier to pinpoint a suitable algorithm for a given dataset and reduce the selection process.

This investigation will use two models, an SVM model imported from sklearn and the CNN model built using Keras. The dataset used is the Modified National Institute of Standards and Technology (MNIST)
dataset of handwritten digits. The training set size (ranging from 1000 - 60000 training images) is altered after each rerun, and the average accuracy and training time after ten trials are recorded. Patterns and logical-mathematical conclusions will be then discussed.

# 2. Research Question
How does the volume of training data affect the classification accuracy and training time of a Support Vector Machine (traditional) compared to Convolutional Neural Network (deep learning)?

# 3. SVM
<img width="677" alt="Screen Shot 2023-01-10 at 10 12 49 AM" src="https://user-images.githubusercontent.com/55889031/211588740-d84323c1-cb13-494b-8ead-478a971a172f.png">

<img width="958" alt="Screen Shot 2023-01-10 at 10 12 25 AM" src="https://user-images.githubusercontent.com/55889031/211588655-0ee9a376-63ac-4c01-9b7e-41f4cf9eb0bb.png">

# 4. CNN
<img width="631" alt="Screen Shot 2023-01-10 at 10 12 58 AM" src="https://user-images.githubusercontent.com/55889031/211588782-b0e1a595-0cc4-4674-b6c5-5c2e58738d74.png">
<img width="649" alt="Screen Shot 2023-01-10 at 10 13 57 AM" src="https://user-images.githubusercontent.com/55889031/211588995-3b6f0f13-79b7-4e13-8dc3-63c4a59497d1.png">

# 5. Methodology
This investigation involves two models that were programmed and fed a specified number of images from the MNIST dataset, accuracy and training time were then recorded.

The SVM model was imported from Sklearn, set with the RBF kernel, and balance between C and Gamma parameters were tested (code in Appendix A, heavily adapted from Kothari). The average accuracy and training time of 10 trials were recorded (set with C & Gamma parameters that resulted in the highest training accuracy).

The CNN model was imported from Keras and the sequential model (a model built layer by layer) was used (code in Appendix B, heavily adapted from Brownlee). A convolutional layer composed of 32 (3x3) kernel filters was added first, then a max-pooling layer and a final fully connected/neural network layer. The accuracy and training time was recorded as the average of the 10 trial evaluations.

# 6. Tabulated Results
The tabulated results for both classifiers in relation to training set size can be found below. The results from every 10 trials were averaged and recorded.
<img width="640" alt="Screen Shot 2023-01-10 at 10 15 22 AM" src="https://user-images.githubusercontent.com/55889031/211589317-6849700c-580c-4d52-8603-9fe51a019c83.png">

<img width="652" alt="Screen Shot 2023-01-10 at 10 15 30 AM" src="https://user-images.githubusercontent.com/55889031/211589347-a3563d93-f304-4697-9fd9-78e6aa77d989.png">
