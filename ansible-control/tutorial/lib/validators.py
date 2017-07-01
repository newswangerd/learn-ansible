from subprocess import Popen, PIPE
import json
import os

def validate_with_playbook(book):
    '''
    Run a playbook in check mode to ensure that the hosts are in the target state. If a task indicates failed or changed, return the list of tasks which cause problems.
    '''
    os.environ['ANSIBLE_STDOUT_CALLBACK'] = "json"
    os.environ['ANSIBLE_RETRY_FILES_ENABLED']= "False"
    p = Popen(['ansible-playbook','--check' , book], stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    rc = p.returncode

    data = json.loads(output)

    failures = []

    for play in data['plays']:
        for task in play['tasks']:
            for host in task['hosts']:
                host_data = task['hosts'][host]
                if host_data['changed'] or host_data['failed']:
                    failures.append(task['task']['name'])

    return failures

class intro:
    def test1(self):
        print "validation failed"
        return False

    def test2(self):
        print "validation succeeded!"
        return True
