import pickle
import numpy as np
import pandas as pd
from IPython.display import display

# Object to serialize
data = pd.read_excel('iris.xls', engine='xlrd')
display(data)

# Serialize to bytes
serialized = pickle.dumps(data)  # Returns bytes
print(type(serialized))  # <class 'bytes'>

# Save to file
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

# Deserialize
loaded = pickle.loads(serialized)  # From bytes
display(loaded)

# From file
with open('data.pkl', 'rb') as f:
    loaded = pickle.load(f)
