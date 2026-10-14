import sys
import pandas as pd
import numpy as np
import sklearn
import econml

print("EconoCausal Environment Check")
print(f"Python: {sys.version.split()[0]}")
print(f"Pandas: {pd.__version__}")
print(f"NumPy: {np.__version__}")
print(f"Scikit-learn: {sklearn.__version__}")
print("EconML imported successfully")
print("Environment verification completed")