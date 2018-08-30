import pickle
import numpy as np
from datmo.logger import Logger
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Set random seed
np.random.seed(0)

logger = Logger()

############# SAVING MY CONFIGURATIONS #############
config = { "solver": "newton-cg", "penalty": "l2" } 
# config = { "solver": "liblinear", "penalty": "l1" }

# LOG CONFIG
logger.log_config(config)

############# TRAINING MY MODEL ######################
iris_dataset = datasets.load_iris()
X, y = iris_dataset.data, iris_dataset.target
X_train, X_test, y_train, y_test = train_test_split(X, y)
model = LogisticRegression(**config).fit(X_train, y_train)
# SAVE MODEL TO FILE
pickle.dump(model, open('model.pkl', 'wb'))

############# SAVING MY STATISTICS/METRICS #########
train_acc = model.score(X_train, y_train)
test_acc = model.score(X_test, y_test)
results = {"train_accuracy": train_acc, "test_accuracy": test_acc}
print(results)

# LOG RESULTS
logger.log_result(results)
