from ui import *
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

def display_graph():
    height = np.arange(1, 500, 1) # display as X
    weight = np.arange(1, 500, 1) # display as Y

    bmi = weight / (height/100)**2
    print(len(height), len(weight), len(bmi))
    type_class = {"underweight": [], "helthy": [], "overweight": [], "obesity": []}
    for h in height:
        underweight_w = np.zeros(len(weight) + 1)
        helthy_w = np.zeros(len(weight) + 1)
        overweight_w = np.zeros(len(weight) + 1)
        obesity_w = np.zeros(len(weight) + 1)

        for w in weight:
            bmi = w / (h/100)**2
            if (bmi < 18.5):
                underweight_w[w] = w
            elif (bmi >= 18.5 and bmi < 25):
                helthy_w[w] = w
            elif (bmi >= 25 and bmi < 30):
                overweight_w[w] = w
            elif (bmi >= 30):
                obesity_w[w] = w

        type_class["underweight"].append(np.max(underweight_w))
        type_class["helthy"].append(np.max(helthy_w))
        type_class["overweight"].append(np.max(overweight_w))
        type_class["obesity"].append(np.max(obesity_w))
        
    print(type_class)
    fig, ax = plt.subplots()
    ax.stackplot(height, type_class["underweight"], type_class["helthy"], type_class["overweight"], type_class["obesity"], labels=['Underweight', 'Helthy', 'Overweight', 'Obesity'])

    ax.set_title('BMI Calculator')
    ax.set_xlabel('Height')
    ax.set_ylabel('Weight')
    ax.set_xlim(50, 300)
    ax.set_ylim(20, 250)

    plt.show()

display_graph()


# emptydf = pd.DataFrame(columns=["name", "height", "weight", "bmi", "timestamp"])
# try:
#     emptydf.to_csv("data.csv", mode="x", index=False)
# except:
#     pass

# root = ui("BMI Calculator")
# root.mainloop()