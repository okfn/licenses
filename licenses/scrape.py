"""Script to scrape licenses and update the package records (licenses.db).
"""

od = {
    'fqdn': 'http://www.opendefinition.org',
    'list': '/licenses/',
    'rexp': '^/licenses/.+'
}
os = {
    'fqdn': 'http://www.opensource.org',
    'list': '/licenses/alphabetical',
    'rexp': '^/licenses/(?!(category|alphabetical|historical|do-not-use)).+(\\.php|\\.html|\\.txt)?'
}
od_licenses_url = "http://www.opendefinition.org/licenses"
os_licenses_url = "http://www.opensource.org/licenses/alphabetical"

licenses_db_path = './licenses/licenses.db'

from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
import re
import sys
from licenses import json
import pprint
import datetime

def scrape(site):
    licenses = []
    url = site['fqdn']+site['list']
    print "Scraping: %s" % url
    soup = BeautifulSoup(urlopen(url).read())
    for a in soup.findAll('a', href=re.compile(site['rexp'])):
        license_url = a['href']
        if not 'http://' in license_url:
            license_url = site['fqdn'] + license_url
        license_id = a['href'].strip('/').split('/')[-1]
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
        license['date_created'] = datetime.datetime.utcnow().isoformat()
        license['tags'] = []
        license['family'] = ''
        license['maintainer'] = ''
        licenses.append(license)
    return licenses


def main():
    try:
        licenses_db = open(licenses_db_path, 'r')
    except Exception, inst:
        msg = "Couldn't open existing licenses records: %s" % inst
        print "Error: %s" % msg
        sys.exit(1)

    try:
        all_data = json.loads(licenses_db.read())
        groups_register = all_data['groups']
        licenses_register = all_data['licenses']
        all_licenses = licenses_register
        if type(all_licenses) != dict:
            msg = "Loaded licenses data type not 'dict': %s" % type(all_licenses)
            raise Exception, msg
    except Exception, inst:
        msg = "Couldn't read existing licenses records: %s" % inst
        print "Error: %s" % msg
        sys.exit(1)

    licenses_db.close()
        
    print "There are %d licenses in the records." % len(all_licenses)

    od_licenses = scrape(od)
    os_licenses = scrape(os)

    for license in od_licenses + os_licenses:
        if license['id'] in all_licenses:
            existing = all_licenses[license['id']]
            for attr_name, value in license.items():
                if attr_name in existing:
                    if attr_name == 'date_created' and existing[attr_name]:
                        pass
                    elif value != existing[attr_name]:
                        print "Updating attribute on %s: %s changed from %s to %s." % (
                            license['id'], attr_name, repr(existing[attr_name]), repr(value)
                        )
                        existing[attr_name] = value
                else:
                    print "Adding new attribute to %s: %s is now %s." % (
                        license['id'], attr_name, repr(value)
                    )
                    existing[attr_name] = value
     
            pass #print 'Skipping license: %s"' % (license['id'])
        else:
            print 'Adding new license: %s "%s"' % (license['id'], license['url'])
            all_licenses[license['id']] = license

    try:
        licenses_db = open(licenses_db_path, 'w')
    except Exception, inst:
        msg = "Couldn't open existing licenses records for writing: %s" % inst
        print "Error: %s" % msg
        sys.exit(1)

    licenses_db.write(json.dumps(all_data, indent=2, sort_keys=True))

    print "There are now %d licenses in the records." % len(all_licenses)


if __name__ == '__main__':
    main()

