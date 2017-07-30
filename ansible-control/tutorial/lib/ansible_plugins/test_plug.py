from ansible.plugins.callback import CallbackBase
import os

class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'notification'
    CALLBACK_NAME = 'test_plug'

    _current_task=None

    def __init__(self, display=None):
        super(CallbackModule, self).__init__(display)
        self.results = []
        self.failed_tasks = None

    def v2_playbook_on_stats(self, result, **kwargs):
        self.failed_tasks.close()

    def runner_on_failed(self, host, res, ignore_errors=False):
        message = ""

        if not ignore_errors:
            error = ""
            for i in res:
                error += "[%s]=> %s" % (i, res[i]) + "\n"

            message += "############ FAILURE ############"
            message += "\n"
            message += "[" + self._current_task.get_name().strip() + "] \n"
            message += self._current_task.get_path()
            message += "\n\n"
            message += error
            message += "\n\n\n"


        # else:
        #     message += "############ IGNORED ############"
        #     message += "\n"
        #     message += "See %s if you think this is a problem \n\n\n" % self._current_task.get_path()

            self.failed_tasks.write(message)


    def v2_playbook_on_task_start(self, task, is_conditional):
        self._current_task = task

    def v2_playbook_on_play_start(self, play):
        log = os.environ['TASK_ERROR_DIR'] + "/" + str(play) + ".err"
        f = open(log, "w")
        f.write("")
        f.close()

        self.failed_tasks = open(log, "a")
