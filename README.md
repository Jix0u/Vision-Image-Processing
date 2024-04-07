# Comparative Vision Processing with CNN and SVM

Compared **Deep Learning Neural Networks** to **Traditional Machine Learning Algorithms** to better understand the training process + advantages of both models

**Model Definition**:
Within the notebook, you'll find the architecture definition for CNN and SVM models:

**CNN Architecture:** The Convolutional Neural Network (CNN) architecture begins by convolving input images with learnable filters, followed by pooling layers to reduce spatial dimensions. This hierarchical feature extraction process enables the network to discern patterns and representations directly from pixel values.

**SVM Definition**: Support Vector Machines (SVM) operate by identifying the hyperplane that best separates different classes in the feature space. By mapping input data into a higher-dimensional feature space, SVM determines the optimal separating hyperplane that maximizes the margin between classes.

**Training and Evaluation:**
Training CNN involves backpropagation with gradient descent optimization algorithms like Adam or SGD, where the network adjusts its parameters based on minimizing a predefined loss function.

Training SVM entails maximizing the margin between classes while minimizing classification errors through solving a convex optimization problem using techniques such as Sequential Minimal Optimization (SMO) or gradient descent.

**Evaluation Metrics:**
Both CNN and SVM models can be evaluated using standard metrics including accuracy, precision, recall, and F1-score, offering insights into their performance in correctly classifying MNIST digits.

**Deployment and Usage:**
Post-training, CNN and SVM models find utility in MNIST digit classification tasks, either integrated into production systems or for batch processing of image data.

**Code Examples and Resources:**
For implementation, tutorials, textbooks, and open-source libraries such as TensorFlow or scikit-learn offer invaluable resources. They often provide code examples, datasets, and pre-trained models to facilitate experimentation and implementation processes.
[Full Report Here](Full%20Report%20MNIST%20Classification.pdf)
