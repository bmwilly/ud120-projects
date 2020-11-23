#!/usr/bin/python

from pathlib import Path
import pickle
import sys
import matplotlib.pyplot
import pandas as pd

sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

### read in data dictionary, convert to numpy array
with Path("../final_project/final_project_dataset.pkl").open("rb") as f:
    data_dict = pickle.load(f)

data_dict.pop("TOTAL", 0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

print("high salaries:", pd.DataFrame(data_dict).T['salary'].astype(float).sort_values().dropna().tail())
print("high bonuses:", pd.DataFrame(data_dict).T['bonus'].astype(float).sort_values().dropna().tail())

### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
