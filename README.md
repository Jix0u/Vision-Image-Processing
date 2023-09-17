# Image Classification with SVM and CNN

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
Evidently, the data is nonlinear and a line can not be drawn to accurately classify the data, thus the data points must be plotted in a 3-dimensional space.\
<img width="570" alt="Screenshot 2023-09-16 at 10 31 03 PM" src="https://github.com/Jix0u/MNIST-Classification/assets/55889031/2e6fb731-497a-49a5-becf-eee4ca2a5b64">



# 2. CNN
<img width="788" alt="Screenshot 2023-09-16 at 10 23 44 PM" src="https://github.com/Jix0u/MNIST-Classification/assets/55889031/d9748a34-116a-42ac-8f5d-22fa23de6ee7">
<img width="610" alt="Screenshot 2023-09-16 at 10 23 59 PM" src="https://github.com/Jix0u/MNIST-Classification/assets/55889031/8656a5c1-502a-47a5-ba54-fc8e9ebaa2cd">


# 3. MNIST Handwritten Digit Dataset
<img width="668" alt="Screenshot 2023-09-16 at 10 24 38 PM" src="https://github.com/Jix0u/MNIST-Classification/assets/55889031/4e00195e-6e84-4c57-ab63-14e05e47e02d">

# 4. Results
<img width="809" alt="Screenshot 2023-09-16 at 10 24 58 PM" src="https://github.com/Jix0u/MNIST-Classification/assets/55889031/af9af00e-7ab9-48bd-a649-6a7fd5a50f76">
<img width="858" alt="Screenshot 2023-09-16 at 10 25 07 PM" src="https://github.com/Jix0u/MNIST-Classification/assets/55889031/ffde30a1-50be-4fe0-a698-d509d758ab5e">

