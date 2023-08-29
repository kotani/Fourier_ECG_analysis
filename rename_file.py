#import os
import pathlib

pwd = pathlib.Path().resolve()
data_path = pwd.parent/"CARTO_data"
"""
jisyo = {}
for data in data_path.glob("*"):
    base = data.stem
    base_1 = str(base).strip().split()
    base_2 = "_".join(base_1)
    data_2 = data_path/base_2
    data_1 = data_path/base
    jisyo[data_1] = data_2

for old, new in jisyo.items():
    old.rename(pathlib.Path(new))
"""
#data_path = pathlib.Path("/Users/furutanimotoki/Desktop/fourier_miyamoto/CARTO_data/20230216_587_FINDER/Patient_2023_02_16/Study_1/Export_Study-1-08_16_2023-11-49-01")
#data_path = pathlib.Path("/Users/furutanimotoki/Desktop/fourier_miyamoto/CARTO_data/20230407_741_FINDER/Patient_2023_04_07/af/Export_af-08_16_2023-11-43-07")
#data_path = pathlib.Path("/Users/furutanimotoki/Desktop/fourier_miyamoto/CARTO_data/20230629_654_FINDER/Patient_2023_06_29/Study_1/Export_Study-1-08_16_2023-11-31-16")
data_path = pathlib.Path("/Users/furutanimotoki/Desktop/fourier_miyamoto/CARTO_data/Patient_2023_06_29/Study_1/Export_Study-1-08_16_2023-11-31-16")

jisyo = {}
for data in data_path.glob("*"):
    base = data.name
    base_1 = str(base).strip().split()
    base_2 = "_".join(base_1)
    data_2 = data_path/base_2
    data_1 = data_path/base
    jisyo[data_1] = data_2

for old, new in jisyo.items():
    old.rename(pathlib.Path(new))
