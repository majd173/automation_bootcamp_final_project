import json


class ConfigProvider:
    # No constructor because this class only submits actions.

    @staticmethod
    def load_from_file():
        try:  # With opening files always we use -try-.
            with open(r'C:\Users\Admin\Desktop\automation_bootcamp_final_project\orange_hrm\orange_hrm.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File not found. Starting with an empty library.")
