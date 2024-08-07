import json
import logging


class ConfigProvider:
    """
    This class manages config file.
    """

    @staticmethod
    def load_from_file():
        try:  # With opening files always we use -try-.
            with open(r'C:\Users\Admin\Desktop\automation_bootcamp_final_project\orange_hrm\orange_hrm.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logging.error(f"File not found. Starting with an empty library.")
        except json.decoder.JSONDecodeError:
            logging.error(f"File is empty. Starting with an empty library.")
        except Exception as e:
            logging.error(f"An error has occurred: {e}")
