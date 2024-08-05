import random
import string
import time


class Utilities:
    # This class manages strings and numbers generating functions.
    # This class in infra because it can be used all around the world
    # not only for a specific website or app.

    #------------------------------------------------------------------------------------------------------------
    # This function generate automatically a random string built
    # from letters, digits and punctuations.
    # It requires a"length" as an input.
    @staticmethod
    def generate_random_string_with_punctuation(length) -> str:
        letters = string.ascii_letters + string.digits + string.punctuation
        return ''.join((random.choice(letters) for _ in range(length)))

    #------------------------------------------------------------------------------------------------------------
    # This function generates automatically a random number
    # It requires a "length" as an input.
    @staticmethod
    def generate_random_number_by_length(length) -> str:
        digits = string.digits
        return ''.join((random.choice(digits) for _ in range(length)))

    #------------------------------------------------------------------------------------------------------------
    # This function generate automatically a random number from 1 to 100.
    @staticmethod
    def generate_random_number():
        return random.randint(1, 100)

    #------------------------------------------------------------------------------------------------------------
    # This function generate automatically a random string built
    # from letters only, it requires a "length" as an input.

    @staticmethod
    def generate_random_string_only_letters(length) -> str:
        letters = string.ascii_letters
        return ''.join((random.choice(letters) for _ in range(length)))

    #------------------------------------------------------------------------------------------------------------
    # This function can bea added in any test step as a time waiting
    # together with retries to submit a specific action.
    @staticmethod
    def wait_for_action(action, sleep_time, retries):
        result = action
        while retries > 0:
            if result:
                return True
            result = action
            time.sleep(sleep_time)
            retries -= retries
        return False
    #------------------------------------------------------------------------------------------------------------




