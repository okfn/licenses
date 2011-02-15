import sys
import os
from licenses import json
import shutil

class DeployCommand(object):
    usage = """Create a series of flat files from the licenses database that
    can directly served by a web server.

Usage:
    %s <path>

Deploys license files to <path>
    """ % sys.argv[0]

    service_version = '2.0'
    group_names = ['all_alphabetical', 'ckan_original', 'ckan_canada', 'ukgov']

    def run(self):
        if len(sys.argv) != 2:
            print "Usage: %s" % self.usage
            sys.exit(1)
        self.base_path = os.path.abspath(sys.argv[1])
        self.path = os.path.abspath(os.path.join(sys.argv[1],
            self.service_version))
        if os.path.exists(self.path):
            print "Error: Path already exists: %s" % self.path
            sys.exit(2)
        print ""
        print "Creating licenses service v%s in: %s" % (self.service_version, self.path)
        os.makedirs(self.path) # Will except if there isn't permission.
        self.write_group_files()
        indexhtml = os.path.abspath(os.path.join('.', 'licenses', 'www',
            'index.html'))
        indexdest = os.path.join(self.base_path, 'index.html')
        print "Copying index.html to %s" % indexdest
        shutil.copy(indexhtml, indexdest)
        self.print_further_instructions()

    def write_group_files(self):
        print ""
        print "Writing JSON licenses group files..."
        from licenses import Licenses
        licenses = Licenses()
        for group_name in self.group_names:
            group_licenses = licenses.get_group_licenses(group_name)
            group_json = json.dumps(group_licenses, indent=2)
            file_path = os.path.join(self.path, group_name)
            file = open(file_path, 'w')
            file.write(group_json)
            file.close()
            print "'%s' has %s licenses: %s" % (group_name, len(group_licenses), file_path)
           
    def print_further_instructions(self):
        print ""
        print "You now should configure your web server to serve the files at"
        print ""
        print "     %s" % self.base_path

if __name__ == "__main__":
    DeployCommand().run()

