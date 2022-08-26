from chapter14.Q6.minion import Minion


class Minions:
    def __init__(self):
        self.minions_list = []

    def add_minions_from_file(self, file_name):
        with open(file_name, "r") as file:
            for line in file:
                line = line.strip()
                m = Minion(line)
                self.minions_list.append(m)

    def save_minions_to_file(self, file_name):
        for minion in self.minions_list:
            json_string = Minion.create_json_string(minion)
            with open(file_name, "a") as file:
                file.write(json_string)
                file.write("\n")
        print("file named {}, was created successfully.".format(file_name))

    def list_minions(self):
        for minion in self.minions_list:
            print(minion)

    def assign_job(self):
        required_job = input("What is the job? ")
        required_eyes_amount = int(input("How many eyes are required? "))
        match_list = self.matching_minions(required_eyes_amount)
        if len(match_list) == 0:
            print("No matching minions were found.")
            return
        print("OK, the list of unemployed minions with {} eyes are:".format(required_eyes_amount))
        for minion in match_list:
            print(minion)
        while True:
            selected_minion = input("Type the minion name: ")
            for minion in match_list:
                if minion.name == selected_minion:
                    minion.assign_job(required_job)
                    print("OK, {} is now working on job {}".format(selected_minion, required_job))
                    return
            print("Please select a minion from the list above.")

    def matching_minions(self, required_eyes_amount):
        match_list = []
        for minion in self.minions_list:
            if minion.is_unemployed() and minion.is_eyes_amount(required_eyes_amount):
                match_list.append(minion)
        return match_list

    def report_job_complete(self):
        finisher_minion = input("Who completed his job? ")
        for minion in self.minions_list:
            if minion.name == finisher_minion:
                if minion.is_unemployed():
                    print("{} is already unemployed.".format(finisher_minion))
                    return
                minion.complete_job()
                print("OK, {} is now unemployed".format(finisher_minion))
        minions_names = []
        for minion in self.minions_list:
            minions_names.append(minion.name)
        if finisher_minion not in minions_names:
            print("{} doesn't exist in the minions list.".format(finisher_minion))
