from chapter14.Q5.minion import Minion


def get_file_name(file_name):
    with open(file_name, "r") as file:
        minions_list = []
        for line in file:
            line = line.strip()
            m = Minion(line)
            minions_list.append(m)
    print(minions_list)
    return minions_list


get_file_name("file1.txt")
