## Supervised
## Definition 
Supervised learning (SL) is the machine learning task of learning a function that maps an input to an output based on example input-output pairs. It infers a function from labeled training data consisting of a set of training examples. In supervised learning, each example is a pair consisting of an input object (typically a vector) and a desired output value (also called the supervisory signal). A supervised learning algorithm analyzes the training data and produces an inferred function, which can be used for mapping new examples. (From Wikipedia)

When the target variable we are trying to predict is continuous, as in our house size-price example, such a learning problem is called a **Regression** problem. When y can only take a small number of discrete values (e.g., given the size of a house, we want to determine whether the house is a home or an apartment), such a learning problem is called a **Classification** problem.

* **Classification** -  Common classification algorithms are linear classifiers, decision trees, and k-nearest neighbors.
* **Regression** -  Linear regression and logistical regression are popular regression algorithms.

## Contents 
There are 8 Supervised Machine Learning algorithms in this file path, some from scratch, others import from sklearn. Descriptions of the algorithm projects are given below:

- Decision_Trees -- Importing a Classification Tree from sklearn on Diabetes data to predict health condition.
- Gradient_Descent -- Using Gradient Descent to apply linear regression on artificial random data and compare Batch Gradient Descent with Stochastic Gradient Descent 
- K_Nearest_Neighbors -- Using KNN from scratch on the Iris dataset, determining the optimal K for most accurate prediction 
- Linear_Regression -- Predicting nasal length from nasal width of a kangaroo using Linear Regression from scratch 
- Logistic_Regression -- Projecting a student's admission into grad school with Logistic Regression from scratch on Candidate data 
- Neural_Networks -- Using a Neural Network from scratch to predict labels on MNIST dataset 
- Perceptron -- Using the Perceptron Learning Algorithm from scratch to classify Iris data
- Random Forest -- Using the Perceptron  Algorithm from scratch on artifically generated data for classification 
