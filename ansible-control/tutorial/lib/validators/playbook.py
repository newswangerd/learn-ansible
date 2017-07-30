class PlaybookValidator():
    '''
    WIP Evaulates a task by running a playbook against the host in check
    mode to see if any setps are marked as "changed" or "failed"
    '''

    def __init__(self, args):
        self.args = args
    def validate(self):
        return True
    def get_message(self):
        return "winner winner chicken dinner"
