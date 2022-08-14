import json
import pathlib


class Minion:
    def __init__(self, line):
        json_data = json.loads(line)
        self.name = json_data['name']
        self.eyes_amount = json_data['eyes_amount']
        self.job = json_data['job']

    def is_eyes_amount(self, number):
        if self.eyes_amount == number:
            return True
        return False

    def is_unemployed(self):
        if self.job is None:
            return True
        return False

    def assign_job(self, job_name):
    def complete_job(self):
    def get_json_string(self):