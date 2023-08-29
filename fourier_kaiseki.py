import pathlib

pwd = pathlib.Path().resolve()
data_path = pwd.parent/"CARTO_data"



for paths in data_path.glob("*"):
    for path in paths.glob("*"):
        for path_1 in path.glob("*"):
            if path_1.stem[0] != ".":
                for path_2 in  path_1.glob("*"):
                    if path_2.stem[0] != ".":
                        for path_3 in path_2.glob("*.txt"):
                            print(path_3)
                            #with open(path_3) as f:
                            #    for lines in f:
                            #        columns = lines.strip().split()
                            #        print(*columns)
