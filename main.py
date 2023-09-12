from ui import *
import pandas as pd

emptydf = pd.DataFrame(columns=["name", "height", "weight", "bmi", "timestamp"])
try:
    emptydf.to_csv("data.csv", mode="x", index=False)
except:
    pass

root = ui("BMI Calculator")
root.mainloop()