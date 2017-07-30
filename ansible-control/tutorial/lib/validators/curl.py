# Validates that the user successfully
import urllib2

class CurlValidator():
    """
    Validates that a task has been successfully completed by loading the HTTP
    result from the target hosts and verifying that the response contains one
    or more strings

    Sample Args:

    Required:
    targets: list of hosts to check
    contains: list of patterns to check on the targets

    Optional:
    port: port to ping (defaults to 80)
    protocol: protocol to use (defaults to http://)
    """

    def __init__(self, args):
        self.args = args
        self.passed = True
        self.message = None

    def validate(self):
        self.passed = True

        if 'protocol' in self.args:
            protocol = self.args['protocol']
        else: protocol = "http://"
        for host in self.args['targets']:
            if 'port' in self.args:
                port = self.args['port']
            else: port = 80

            try:
                response = urllib2.urlopen(protocol + host + ":" + str(port))
                html = response.read()
            except urllib2.URLError:
                self.message = "Could not connect to one or more hosts."
                self.passed = False
                break

            for pattern in self.args['contains']:
                if pattern not in html:
                    self.passed = False
                    break

        return self.passed

    def get_message(self):
        if self.message:
            return self.message

        if not self.passed:
            message = "The pattern " + str(self.args['contains']) + " was not found on one or more of the following hosts: \n"
            message += str(self.args['targets'])

            return message
        else:
            return "Test passed."
