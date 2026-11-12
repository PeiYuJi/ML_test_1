from sklearn.datasets import load_iris
import pandas as pd

data = load_iris()
print(data)

pd.DataFrame(data.data, columns=data.feature_names).head()


