import json


class DataManager:
    def __init__(self):
        with open("settings.json", mode="r") as settings_file:
            self.settings = json.load(settings_file)
            self._study_seconds = self.settings["study_seconds"]
            self._break_seconds = self.settings["break_seconds"]

    @property
    def study_seconds(self):
        return self._study_seconds

    @property
    def break_seconds(self):
        return self._break_seconds

    @staticmethod
    def save_data(data: dict) -> None:
        with open("settings.json", mode="w") as settings_file:
            json.dump(data, settings_file)
