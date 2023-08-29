import pandas as pd
import pathlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


pwd = pathlib.Path().resolve()
data_path = pwd.parent/"data"

for path in data_path.glob("*"):
    df_cathe = pd.read_table(path/"cathe_position/cathe.txt",sep ="\s+",skiprows =2,header = None)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    x = df_cathe.iloc[:,3]
    y = df_cathe.iloc[:,4]
    z = df_cathe.iloc[:,5]

    ax.scatter(x, y, z)
    plt.show()
