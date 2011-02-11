__all__ = ["LicensesService1", "LicensesService2"]

import urllib2
from licenses import json

class LicensesService1(object):

    default_url = 'http://licenses.opendefinition.org/1.0/all_formatted'

    def get_names(self):
        from pylons import config
        url = config.get('licenses_service_url', self.default_url)
        try:
            response = urllib2.urlopen(url)
            response_body = response.read()
        except Exception, inst:
            msg = "Couldn't connect to licenses service %r: %s" % (url, inst)
            raise Exception, msg
        try:
            license_names = json.loads(response_body)
        except Exception, inst:
            msg = "Couldn't read response from licenses service %r: %s" % (response_body, inst)
            raise Exception, inst
        return [unicode(l) for l in license_names]


## For Licenses SoS v2.0.
class LicensesService2(object):

    default_group_url = 'http://licenses.opendefinition.org/2.0/all'

    def __init__(self, group_url=''):
        self.group_url = group_url or self.default_group_url

    def get_licenses(self):
        try:
            response = urllib2.urlopen(self.group_url)
            response_body = response.read()
        except Exception, inst:
            msg = "Couldn't connect to licenses service %r: %s" % (self.group_url, inst)
            raise Exception, msg
        try:
            licenses = json.loads(response_body)
        except Exception, inst:
            msg = "Couldn't read response from licenses service %r: %s" % (response_body, inst)
            raise Exception, inst
        return licenses

