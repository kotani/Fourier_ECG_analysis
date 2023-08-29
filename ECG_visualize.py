import pandas as pd
import pathlib
import numpy as np
import matplotlib.pyplot as plt


pwd = pathlib.Path().resolve()
data_path = pwd.parent/"data"

leads = ["V1","V2","V3","V4","V5","V6","I","II","III","aVL","aVR","aVF"]
for path in data_path.glob("*"):
    df_cathe = pd.read_table(path/"ECG/ecg.txt",sep ="\s+",skiprows =3,header = None)
    #df_V1 = df_cathe[df_cathe.iloc[:,1] =="V1"]
    #print(df_V1)
    df_cathe["lead"] = df_cathe.iloc[:,1]
    df_cathe = df_cathe.set_index("lead")
    df_cathe = df_cathe.drop([0,1],axis = 1)
    df_lead = df_cathe.loc[leads,:]
    fig, axes = plt.subplots()
    axes.plot(df_lead.T)
    plt.show()
