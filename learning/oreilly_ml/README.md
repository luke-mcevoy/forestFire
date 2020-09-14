## Chapter 1: Fundamentals of Machine Learning

### Supervised/Unsupervised Learning
ML systems can be classified according to the amount and type of supervision they get during training. 
There are four major categories:
- Supervised learning
    - In supervised learning, the training set you feed to the algorithm includes the dresired solutions called labels.
    - A typical supervised learning task is classification.
    - k-Nearest Neighbors
    - Linear Regression
    - Logistic Regression
    - Support Vector Machines (SVMs)
    - Decision Trees and Random Forests
    - Neural Networks
- Unsupervised learning
    - In unsupervised learning, the training data is unlabeled. The system tries to learn without a teacher.
    - Clustering
        - K-Means
        - DBSCAN
        - Hierarchical Cluster Analysis (HCA)
    - Anomaly detection and novelty detection
        - One-class SVM
        - Isolation Forest
    - Visualization and dimensionality reduction
        - Principal Component Analysis (PCA)
        - Kernel PCA
        - Locally Linear Embedding (LLE)
        - t-Distributed Stochastic Neighbor Embedding (t-SNE)
    - Association rule learning
        - Apriori
        - Eclat
- Semisupervised learning
    - Algorithms that work with partially labeled data.
- Reinforcement learning
    - The system observes the enviornment, selects and performs actions, and gets rewards or penalities for its choices.

#### Batch and Online Learning
- Batch Learning
    - The system is incapable of learning incrementally. It must be trained using all the avaliable data.
    - The system applies what it has learned offline while taking in no info which is called offline learning.
- Online Learning
    - Train system incrementally by feeding it data instances sequentially.
    - System can learn data as it arrives.

#### Instance-Based vs. Model-Based Learning
- Instance-Based
    - System learns examples by heart then generalizes to new cases by using a similarity measure to compare them to the learned examples.
- Model-Based
    - Build a model of examples and use that model to make predictions

#### Overfitting the Training Data
- Occurs when the model is too complex relative to the amount and noisiness of training data. Possible solutions are
    - Simplify the model by selecting one with fewer parameters (e.g., a linear model rather than a high-degree polynomial model), by reducing the number of attributes in the training data, or by constraining the model.
    - Gather more training data.
    - Reduce the noise in the training data (e.g., fix data errors and remove outliers).

#### Overfitting the Training Data
- Occurs when model is too simple to learn the underlying structure of the data. For example, a linear model of life satisfaction is prone to underfit. Reality is just more complex than the model, so its predictions are bound to be inaccurate, even on the training examples. To fix that:
    - Select a more powerful model, with more parameters
    - Feed better features to the learning algorithms (feature engineering)
    - Reduce teh constraints of the model (e.g., reduce the regularization hyperparameter)

#### Testing and Validation
- Split your data into two sets: the training set and the test set. The error rate on new cases is called the generalization error (or out-of-sampel error), and by evaluating your model on the test set, you get an estimate of this error. If the training error is low but the generalization error is high, your model is overfitting the training data.
    - It is common to use 80% of the data for training and hold out 20% for testing. However, this depends on the size of the dataset: if it containts 10 million instances, then holding out 1% means your test set will contain 100,000 instance which is probably more than need to get a good estimate of the generalization error.

#### Hyperparameter Tuning and Model Selection
- Measuring the generalization error multiple time on the same test set can mislead developers and adapt the model and hyperparameters to produce teh best model for that particular set only. This means that the model is unlikely to perform as well on new data.

- Holdout validation: hold out part of the training set to evaluate several candidate models and select the best one. THe held-out set is called the validation set. After this holdout validation process, you train the best model on the full training set to get an estimate of the generalization error.

- Cross Validation: uses small validation sets. Each model is evaluated once per validation set after it is trained on the rest of the data. By averaging out all the evaluations of a model, you get a much more accurate measure of its performance. There is a drawback, the training time is multiplied by the number of validation sets.

#### Data Mismatch
- It's easy to get a large amount of data for training, but this data most likely won't be a perfect representative of the data that will by used in production.
    - Suppose you want to create a mobile app to take pictures of flowers and automatically determine their species. **You can download millions of flowers on the web, by they won't perfectly represent the pictures taken using the app on a mobile device. Perhaps you only have 10,000 representative pictures (actually taken with the app). In this case, the most important rule to remember is that the validation set and the test set must be as representative as possible of the data you expect to use in production, so they should be composed exclusively of representative pictures: you can shuffle them and put half in the validation set and half in the test set (making sure that no duplicates or near-duplicates end up in both sets).** After training the model with the web photos if you observe that the performance of the model on the validation set is disappointing, you will not know whether this is because your model has overfit the training set or whether this is just due to the mistmatch between the web pictures and the mobile app pictures. **One solution is to hold out some of the training pictures (from the web) in yet another set that Andrew Ng calls the train-dev set**. If it performs well, then the model is not overfitting the training set. If it performs poorly on the validation set, the problem must be coming from the data mismatch. You can try to tackle this problem by preprocessing the web images to make them look more like pictures that will be taken by the mobile app, and then retraining the model. Conversely, if the model performs poorly on the train-dev set, then it must have overfit the training set so try to simplify or regularize the model, get more training data, and clean up the training data.