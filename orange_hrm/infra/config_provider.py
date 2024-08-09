import json
import logging


class ConfigProvider:
    """
    This class loads config file.
    """

    @staticmethod
    def load_from_file(filename):
        """
        This method loads config file.
        :param: filename
        :return: json file.
        """
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logging.error(f"File {filename} not found.")
        except Exception as e:
            logging.error(f"Can not load config. {e}")

