from mnist import MNIST
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import time
import pandas as pd

print("Loading dataset...")
#loading the dataset
mndata = MNIST("/Users/leonachen/Downloads/")
images, labels = mndata.load_training()
img, lbl = mndata.load_testing()

#get training size
train_x = images[:45000]
train_y = labels[:45000]
#get testing size
test_x = img[:10000]
expected = lbl[:10000].tolist()

#test all c parameters
C_2d_range = [1e1, 1e2, 1e3, 1e4, 1e5]
# G_2d_range = [1e-2, 1e-1, 1,1e1, 1e2, 1e3, 1e4, 1e5]

m_a=0
m_c=0
m_g=0

#find best c and g parameter
for C in C_2d_range:
    clf = SVC(kernel = 'rbf', C=C, gamma='scale')
    print("Train model")
    start = time.time()
    clf.fit(train_x, train_y)
    stop = time.time()
    print(f"Training Time: {stop - start}s")
    print("Compute predictions")
    predicted = clf.predict(test_x)

    print("Accuracy: ", accuracy_score(expected, predicted))
    if m_a<accuracy_score(expected, predicted):
        m_a=accuracy_score(expected, predicted)
        m_c=C

# for x in range(5):
#     clf = SVC(kernel = 'rbf', C=m_a, gamma='scale')


print("Accuracy: ", m_a)
    

# Test on the next 1000 images:




