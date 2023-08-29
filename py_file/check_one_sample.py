import pandas as pd
import pathlib

pwd = pathlib.Path().resolve()
data_path = pwd.parent/"CARTO_data"

#txt一つのみ取り出す
one_sample = []
for path in data_path.glob("**/*.txt"):
    one_sample.append(path)
    break

#症例のIDを取得する
sample_name = []
for i in one_sample:
    sample_name.append(i.parent.parent.parent.stem)

#取得した症例のIDを使って保存ファイルを作る
for i in sample_name:
    pathlib.Path(f"{pwd.parent}/data/{i}/ECG").mkdir(exist_ok =True, parents = True)
    pathlib.Path(f"{pwd.parent}/data/{i}/cathe_position").mkdir(exist_ok =True, parents = True)
    pathlib.Path(f"{pwd.parent}/data/{i}/algorhitm_result").mkdir(exist_ok =True, parents = True)
"""
keyword 
Catheter Position:
Algorithm result:
ECG:
"""

#行を上手く取り出す方法がわからないので1行ずつ読んでkeywordにあたったらその行番号をまず取得するようにする
count = 0
for i in one_sample:
    with open(i) as f:
        for lines in f:
            columns = lines.strip().split()
            if len(columns) >0:
               if columns[0] == "Catheter":
                   cathe_num = count
               if columns[0] == "ECG:":
                   ecg_num = count 
               if columns[0] == "Algorithm":
                   algo_num = count
               count += 1

#取得した行番号を元にテキストを作る
count_1 = 0
for i in one_sample:
    with open(i) as f,open(f"{pwd.parent}/data/{i.parent.parent.parent.stem}/ECG/ecg.txt","w") as out, open(f"{pwd.parent}/data/{i.parent.parent.parent.stem}/cathe_position/cathe.txt","w") as out1, open(f"{pwd.parent}/data/{i.parent.parent.parent.stem}/algorhitm_result/algo.txt","w") as out2:
        for lines in f:
            columns = lines.strip().split()
            if len(columns) >0:
                if count_1 in range(ecg_num,count):
                    print(*columns,file = out)
                if count_1 in range(cathe_num, algo_num):
                    print(*columns,file = out1)
                if count_1 in range(algo_num,ecg_num -1):
                    print(*columns,file = out2)
                count_1 += 1
