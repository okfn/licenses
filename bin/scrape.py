"""Script to scrape licenses and update the package records (licenses.db).
"""
import os
from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
import re
import sys
import json
import pprint
import datetime

opendefinition = {
    'fqdn': 'http://www.opendefinition.org',
    'list': '/licenses/',
    'rexp': '^/licenses/.+'
}
opensource = {
    'fqdn': 'http://www.opensource.org',
    'list': '/licenses/alphabetical',
    'rexp': '^/licenses/(?!(category|alphabetical|historical|do-not-use)).+(\\.php|\\.html|\\.txt)?'
}
od_licenses_url = "http://www.opendefinition.org/licenses"
os_licenses_url = "http://www.opensource.org/licenses/alphabetical"

def scrape(site):
    licenses = []
    url = site['fqdn']+site['list']
    print "Scraping: %s" % url
    soup = BeautifulSoup(urlopen(url).read())
    for a in soup.findAll('a', href=re.compile(site['rexp'])):
        license_url = a['href']
        if not 'http://' in license_url:
            license_url = site['fqdn'] + license_url
        license_id = a['href'].strip('/').split('/')[-1].lower()
        license_id = license_id.split('.html')[0]
        license_id = license_id.split('.php')[0]
        license_id = license_id.split('.txt')[0]
        license_title = a.contents[0]
        license = {
            'id': license_id,
            'title': license_title,
            'url': license_url,
        }
        license['is_okd_compliant'] = 'www.opendefinition' in site['fqdn']
        license['is_osi_compliant'] = 'www.opensource' in site['fqdn']
        license['status'] = 'active'
        license['family'] = ''
        license['maintainer'] = ''
        licenses.append(license)
    return licenses

def get_licenses():
    all_ = {}
    for filename in os.listdir('licenses'):
        if filename.endswith('.json'):
            data = json.load(open(os.path.join('licenses', filename)))
            all_[data['id']] = data
    return all_ 

def main(out_path='licenses'):
    all_licenses = get_licenses()
    od_licenses = scrape(opendefinition)
    os_licenses = scrape(opensource)
    for license in od_licenses + os_licenses:
        if license['id'] in all_licenses:
            existing = all_licenses[license['id']]
            for attr_name, value in license.items():
                if attr_name in existing:
                    if value != existing[attr_name] and value:
                        print "Updating attribute on %s: %s changed from %s to %s." % (
                            license['id'], attr_name, repr(existing[attr_name]), repr(value)
                        )
                        existing[attr_name] = value
                else:
                    print "Adding new attribute to %s: %s is now %s." % (
                        license['id'], attr_name, repr(value)
                    )
                    existing[attr_name] = value
        else:
            print 'Adding new license: %s "%s"' % (license['id'], license['url'])
            all_licenses[license['id']] = license

    if not os.path.exists(out_path):
        os.makedirs(out_path)
    for id_, data in all_licenses.items():
        fo = open(os.path.join(out_path, id_ + '.json'), 'w')
        json.dump(data, fo, indent=2, sort_keys=True)
        fo.close()

    print "There are now %d licenses in the records." % len(all_licenses)


if __name__ == '__main__':
    main()

