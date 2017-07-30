# The idea here is to run the corret playbook against the hosts in check mode and validate that nothing has changed or fails
# loop through plays
#   loop through tasks
#   record task name
#      loop through hosts in task to verify none failed or changed

from subprocess import Popen, PIPE
import json
import os

def validate_with_playbook(book):
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


print validate_with_playbook('testbook.yaml')
