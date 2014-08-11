#!/usr/bin/env python
import sys
import os
import fnmatch
import json
import shutil

license_dir = 'licenses'
groups_dir = os.path.join('licenses', 'groups')
jsonp_dir = os.path.join('licenses', 'jsonp')
jsonp_callback = 'license_callback'

class DeployCommand(object):
    def run(self):
        self.clean()
        self.write_group_files()
        self.write_jsonp_files()
    
    def clean(self):
        if os.path.exists(groups_dir):
            shutil.rmtree(groups_dir)
        if os.path.exists(jsonp_dir):
            shutil.rmtree(jsonp_dir)

    od_plus = [
        "notspecified", 
        "other-open", 
        "other-pd", 
        "other-at", 
        "CC-BY-NC-4.0", 
        "other-nc", 
        "other-closed"
        ]

    ckan = [
        "notspecified", 
        "ODC-PDDL-1.0", 
        "ODbL-1.0", 
        "ODC-BY-1.0",
        "CC0-1.0", 
        "CC-BY-4.0", 
        "CC-BY-SA-4.0", 
        "GFDL-1.3-no-cover-texts-no-invariant-sections", 
        "other-open", 
        "other-pd", 
        "other-at", 
        "OGL-UK-2.0", 
        "CC-BY-NC-4.0", 
        "other-nc", 
        "other-closed"
        ]

    def write_group_files(self):
        print('Writing group files...')
        os.makedirs(groups_dir)
        licenses = self.get_licenses()
        od = dict([
            (id_,data) for id_,data in licenses.items() if
            data['od_conformance'] == "approved"
        ])
        od_plus = dict(od)
        for id_ in self.od_plus:
            od_plus[id_] = licenses[id_]
        # NB: this set is *ordered* list not dict
        ckan = [ licenses[id_] for id_ in self.ckan ]
        osi = dict([
            (id_,data) for id_,data in licenses.items() if
            data['osd_conformance'] == "approved"
        ])
        for name, dict_ in [
                ('all', licenses),
                ('osi', osi),
                ('od', od),
                ('od_plus', od_plus),
                ('ckan', ckan)]:
            fo = open(os.path.join(license_dir, 'groups', name + '.json'), 'w')
            json.dump(dict_, fo, indent=2, sort_keys=True)
            fo.close()
        print('Writing group files: DONE')

    def write_jsonp_files(self):
        print('Writing jsonp files')
        os.makedirs(jsonp_dir)
        files = [ (fn, os.path.join(license_dir, fn)) for fn in
            os.listdir(license_dir) if fn.endswith('.json') ]
        files += [ (fn, os.path.join(groups_dir, fn)) for fn in
            os.listdir(groups_dir) ]
        for filename, path in files:
            newpath = os.path.join(jsonp_dir,  filename[:-5] +
                    '.js')
            content = open(path).read()
            content = '%s(%s);' % (jsonp_callback, content)
            outfo = open(newpath, 'w')
            outfo.write(content)
            outfo.close()
        print('Writing jsonp files: DONE')

    def get_licenses(self):
        all_ = {}
        for filename in os.listdir(license_dir):
            if fnmatch.fnmatch(filename, '*.json'):
                data = json.load(open(os.path.join('licenses', filename)))
                all_[data['id']] = data
        return all_ 


if __name__ == "__main__":
    usage = """Usage: deploy.py run | clean
    
Create license groups and JSONP versions."""
    if len(sys.argv) < 2:
        print usage
        sys.exit(1)
    action = sys.argv[1]
    if action == 'run':
        DeployCommand().run()
    elif action == 'clean':
        DeployCommand().clean()
    else:
        print usage

