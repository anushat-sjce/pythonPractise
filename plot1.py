import pandas as pd
import matplotlib.pyplot as plt

dict1 = {"a":[11,21,31], "b":[12,22,32]}
df = pd.DataFrame(dict1)
type(df)
print("DataFrame df head: ", df.head(),"\n")
print("DataFrame mean :", df.mean())
