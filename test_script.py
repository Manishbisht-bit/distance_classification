import numpy as np
import pandas as pd

try:
    df = pd.DataFrame({'Feature1': [1, 2], 'Feature2': [3, 4]})
    print("Test Passed: DataFrame loaded successfully!")
except Exception as e:
    print(f"Test Failed: {e}")
