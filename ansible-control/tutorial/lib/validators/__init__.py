# Validators are called by

class BaseValidator:
    def __init__(self, args):
        self.args = args

    def validate(self):
        pass

    def get_message(self):
        pass
