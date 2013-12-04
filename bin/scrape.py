#!/usr/bin/env python
"""Script to scrape licenses and update the package records (licenses).
"""
import os
from BeautifulSoup import BeautifulSoup
from urllib import urlopen
import re
import json

opendefinition = {
    'fqdn': 'http://www.opendefinition.org',
    'list': '/licenses/',
    'rexp': '^/licenses/.+'
}
opensource = {
    'fqdn': 'http://www.opensource.org',
    'list': '/licenses/alphabetical',
    'rexp': '^/licenses/(?!(category|alphabetical|do-not-use)).+(\\.php|\\.html|\\.txt)?'
}
opensource_old = {
    'fqdn': 'http://www.opensource.org',
    'list': '/licenses/do-not-use',
    'rexp': '^/licenses/.+'
}

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
        
        """Fill in the license details"""
        lic = {
            'id': license_id,
            'title': license_title,
            'url': license_url,
            'domain_content': False,
            'domain_data': False,
        }
        lic['is_okd_compliant'] = 'www.opendefinition' in site['fqdn']
        if 'www.opensource' in site['fqdn']:
            lic['is_osi_compliant'] = True
            lic['domain_software'] = True
        if 'do-not-use' in site['list']:
            lic['status'] = 'retired'
        else:
            lic['status'] = 'active'
        lic['family'] = ''
        lic['maintainer'] = ''
        licenses.append(lic)
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
    os_retired_licenses = scrape(opensource_old)
    for lic in od_licenses + os_licenses + os_retired_licenses:
        if lic['id'] in all_licenses:
            existing = all_licenses[lic['id']]
            for attr_name, value in lic.items():
                if attr_name in existing:
                    if value != existing[attr_name] and value:
                        print "Updating attribute on %s: %s changed from %s to %s." % (
                            lic['id'], attr_name, repr(existing[attr_name]), repr(value)
                        )
                        existing[attr_name] = value
                else:
                    print "Adding new attribute to %s: %s is now %s." % (
                        lic['id'], attr_name, repr(value)
                    )
                    existing[attr_name] = value
        else:
            """Don't add retired if not already"""
            if lic['status'] == 'active':
                print 'Adding new license: %s "%s"' % (lic['id'], lic['url'])
                all_licenses[lic['id']] = lic

    if not os.path.exists(out_path):
        os.makedirs(out_path)
    for id_, data in all_licenses.items():
        fo = open(os.path.join(out_path, id_.lower() + '.json'), 'w')
        json.dump(data, fo, indent=2, sort_keys=True)
        fo.close()

    print "There are now %d licenses in the records." % len(all_licenses)


if __name__ == '__main__':
    main()

