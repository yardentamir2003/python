import json


class Minion:
    def __init__(self, line):
        json_data = json.loads(line)
        self.name = json_data['name']
        self.eyes_amount = json_data['eyes_amount']
        self.job = json_data['job']

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def is_eyes_amount(self, number):
        if self.eyes_amount == number:
            return True
        return False

    def is_unemployed(self):
        if self.job == "none":
            return True
        return False

    def assign_job(self, job_name):
        self.job = job_name

    def complete_job(self):
        self.job = "none"

    def create_json_string(self):
        name = self.name
        eyes_amount = self.eyes_amount
        job = self.job
        json_data = {"name": name, "eyes_amount": eyes_amount, "job": job}
        line = json.dumps(json_data)
        return line
