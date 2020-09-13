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

