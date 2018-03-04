# ml2017hd
Will contain the code for our project in "Fundamentals of Machine Learning"

# Versions
|Nr.|Main Changes|
|---|---|
|v0|Basic architecture. CPU. MAE. Input: 224x224. "rater-first-attempt.ipynb".|
|v1|Same architecture. GPU. Categorical crossentopy, 6 classes. Input: 100x100. L2 regularizer, lr=0.0001.|
|v2|Tried training model generated by Hyperparameter Search (`opt_classifierv0`). Input: 200x200. Bad results.|
|v3|Data augmentation & streaming. Round ratings to integers (stars). Input: 200x200.|
|v3.1|Same architecture as v3, includes prediction output for human supervision (like v4.1).|
|v3.2|Same architecture as v3, no dropout after feature extraction. WORKS: val_loss: 0.56766, val_acc: 0.8145.|
|v4|Expanding on regression approach of v0. Data augmentation. No Dropout after feature extraction.|
|v4.1|Uses clipped ReLU to get results between 0 and 5. Predictions tend to extremes. No Dropout after feature extraction.|
|v4.2|Wider (512) first fc-layer, narrower (8) last fc-layer. Clipped ReLU. No Dropout after feature extraction.|
