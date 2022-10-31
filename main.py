import bar_image_labels as bcr
import pandas as pd

df = pd.read_csv("data.csv", index_col="Date")
df.fillna(0.0, inplace=True)
