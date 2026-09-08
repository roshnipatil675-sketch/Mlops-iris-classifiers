# scripts/generate_data.py 
from sklearn.datasets import load_iris
import pandas as pd
 
iris = load_iris(as_frame=True)
df = iris.frame 

df.to_csv("data/raw/iris_v1.csv", index=False)
 
print(f"Saved {len(df)} rows of Iris data to data/raw/iris_v1.csv")
                                                     
 
