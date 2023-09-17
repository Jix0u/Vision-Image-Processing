# Image Classification Research

Compared **Deep Learning Neural Networks** to **Traditional Machine Learning Algorithms** to better understand the training process + advantages of both models

#### Traditional ML Algorithm used: SVM (Support Vector Machine)
#### Deep Learning Neural Networks used: CNN (Convolutional Neural Networks)
#### Image Dataset used: MNIST Handwritten Digits Dataset (Modified National Institute of Standards and Technology)

[Full Report Here](Full%20Report%20MNIST%20Classification.pdf)

# 1. SVM
Support Vector Machines (SVM) is a traditional classification algorithm for both non-linear and linear classification problems (Jain, 2019). The fundamental principle behind SVM is straightforward: find the most optimal boundary line/hyperplane that separates n-dimensional training data into two distinct classes (Gandhi, 2018). This line is then generalized on testing data for classification purposes.
<img width="578" alt="Screenshot 2023-09-16 at 10 28 01 PM" src="https://github.com/Jix0u/MNIST-Classification/assets/55889031/df8bf002-2186-4e80-9a5c-16ef3aad25b4">\
Although a linear SVM can be used for this experiment, for the purpose of increased accuracy a non-linear SVM will be used - a non-linear or wavy separator would categorize the MNIST data more accurately as a linear separator may incorrectly classify certain data points. To separate data that is not linearly separable, it must be transformed to a higher dimensional feature space where properties of the image are represented as singular points (Brown, 2021). To visualize this transformation, non-linearly separable 2-dimensional data will be shown below:\
<img width="468" alt="Screenshot 2023-09-16 at 10 29 28 PM" src="https://github.com/Jix0u/MNIST-Classification/assets/55889031/2d32bc35-8448-45d9-96b2-271dd65b51d3">\
Evidently, the data is nonlinear and a line can not be drawn to accurately classify the data, thus the data points must be plotted in a 3-dimensional space. The data is then linearly separable, and a boundary line can now be drawn to divide and classify the data.\
<img width="570" alt="Screenshot 2023-09-16 at 10 31 03 PM" src="https://github.com/Jix0u/MNIST-Classification/assets/55889031/2e6fb731-497a-49a5-becf-eee4ca2a5b64">



# 2. CNN
Convolutional Neural Networks or ConvNet is a deep learning algorithm that takes raw images, assigns importance to features of the object, and uses them to differentiate the image without much preprocessing necessary (Saha, 2018). To achieve this, a CNN model is composed of 3 principal layers: convolution, pooling, and fully-connected. Each of the layers and their properties will be explained below.\
<img width="515" alt="Screenshot 2023-09-16 at 10 41 23 PM" src="https://github.com/Jix0u/MNIST-Classification/assets/55889031/59b90924-9c71-4810-978c-971c4eb831e5">

A pooling layer is used for resolution reduction after the image is processed within the convolution layer (Brownlee, 2019). It is also used to prevent overfitting, which occurs when models fit exactly to the training data, and perform inaccurately for testing data that it was not explicitly trained on (IBM, 2021). Max Pooling which takes the max value of a certain part of an image under the kernel filter will be used because of its simplicity and popularity (Yalçın, 2018).\
<img width="553" alt="Screenshot 2023-09-16 at 10 45 02 PM" src="https://github.com/Jix0u/MNIST-Classification/assets/55889031/80237dd2-31b9-49b9-90a8-452bd52b1d73">\
The final layer is the Fully Connected Layer, it receives the transformed input data (after pooling and convolution). This layer is composed of neurons that receive input, perform an operation and pass on the results to the next neuron layer (Karpathy, n.d.)\
<img width="551" alt="Screenshot 2023-09-16 at 10 46 37 PM" src="https://github.com/Jix0u/MNIST-Classification/assets/55889031/75139fbe-a3f9-4553-a90c-b33ddb59dbd8">


# 3. MNIST Handwritten Digit Dataset
The dataset used is the Modified National Institute of Standards and Technology (MNIST) dataset, composed of 70 000 digits extensively used in both training and testing machine learning visual classification (Yann, 1998). Each image is bounded by a 28*28 pixel grid (784 pixels in total), and approximately 250 writers contributed handwritten digits to ensure the machine learning algorithm can quantify a variety of handwritten digits.\
<img width="420" alt="Screenshot 2023-09-16 at 10 42 48 PM" src="https://github.com/Jix0u/MNIST-Classification/assets/55889031/3ff20946-2589-467c-a2b0-2eaed4eebe13">

# 4. Results
The accuracy of the SVM model was generally higher than the accuracy of the CNN model when the training set size was smaller (1000-10000 images), and the opposite was true for larger training set sizes (10000-60000 images).In terms of accuracy, CNN models generally perform better (higher accuracy) when there is more data available. It is prone to overfitting on smaller sized training sets as a result of the numerous layers, kernels and parameters necessary to build a complete model.\
<img width="571" alt="Screenshot 2023-09-16 at 10 50 19 PM" src="https://github.com/Jix0u/MNIST-Classification/assets/55889031/f374ecee-df49-435f-ba3d-c0a3236ea24e">\
For training time, SVM was faster when the dataset size was smaller (1000- 30000 images) while CNN was faster when the dataset size was larger
(30000-60000 images). The trend line for the training time was generally steeper for the SVM model compared to the CNN model, meaning CNN scales much better with the size of the dataset. SVM time complexity scales superlinearly with the # of data points since it requires large amounts of memory to be stored in the kernel matrix. This makes it infeasible for larger datasets. CNN models generally scale linearly with the amount of visual data given, working well with larger datasets.
<img width="571" alt="Screenshot 2023-09-16 at 10 51 27 PM" src="https://github.com/Jix0u/MNIST-Classification/assets/55889031/a091e562-dffd-46bd-9f3d-cae4b89613a2">

