# For Licenses SoS v2.0.

class Licenses(object):
    
    def __iter__(self):
        return iter(self.get_licenses().keys())

    def __getitem__(self, key):
        return self.get_licenses()[key]

    def keys(self):
        return self.get_licenses().keys()

    def values(self):
        return self.get_licenses().values()

    def get_licenses(self):
        return self.get_data()['licenses']

    def get_data(self):
        if not hasattr(self, '_data'):
            self._data = self.load_data()
        return self._data

    def load_data(self):
        import pkg_resources
        import simplejson
        import os
        try:
            path = pkg_resources.resource_filename(
                pkg_resources.Requirement.parse('licenses'),
                'licenses/licenses.db'
            )
        except Exception, inst:
            msg = "Couldn't make path for 'licenses.db' resource."
            raise Exception, msg
        if not os.path.exists(path):
            print "Couldn't find licenses data file: %s" % path
        return simplejson.loads(open(path).read())

    def get_group(self, group_name):
        if group_name == 'all':
            return self.keys()
        else:
            msg = "Group name '%s' is not supported." % group_name
            raise Exception, msg

# For Licenses SoS v1.0.

class LicenseList(object):
    okd_compliant = [
        u'Open Data Commons Public Domain Dedication and License (PDDL)',
        u'Open Data Commons Open Database License (ODbL)',
        u'Creative Commons CCZero',
        u'Creative Commons Attribution',
        u'Creative Commons Attribution-ShareAlike',
        u'GNU Free Documentation License (GFDL)',
        u'UK Click Use PSI',
        u'Other',
        u'Other (Public Domain)',
        u'Other (Attribution)',
        u'UK Crown Copyright with data.gov.uk rights',
        u'Higher Education Statistics Agency Copyright with data.gov.uk rights',
    ]

    okd_compliant_formatted = [ u'OKD Compliant::' + x for x in okd_compliant ]

    non_okd_compliant = [
        u'Creative Commons Non-Commercial (Any)',
        u'Crown Copyright',
        u'Non-Commercial Other',
        u'Other',
        ]

    non_okd_compliant_formatted = [ u'Non-OKD Compliant::' + x for x in non_okd_compliant]
    
    other = [
        u'License Not Specified'
        ]

    other_formatted = [ u'Other::' + x for x in other ]

    osi_approved = [
        # main ones
        u'New BSD license',
        u'GNU General Public License (GPL)',
        u'GNU General Public License v3 (GPLv3)',
        u'GNU Library or "Lesser" General Public License (LGPL)',
        u'MIT license',
        # rest are alphabetical
        u'Academic Free License',
        u'Adaptive Public License',
        u'Apache Software License',
        u'Apache License, 2.0',
        u'Apple Public Source License',
        u'Artistic license',
        u'Attribution Assurance Licenses',
        u'Computer Associates Trusted Open Source License 1.1',
        u'Common Development and Distribution License',
        u'Common Public License 1.0',
        u'CUA Office Public License Version 1.0',
        u'EU DataGrid Software License',
        u'Eclipse Public License',
        u'Educational Community License',
        u'Eiffel Forum License',
        u'Eiffel Forum License V2.0',
        u'Entessa Public License',
        u'Fair License',
        u'Frameworx License',
        u'IBM Public License',
        u'Intel Open Source License',
        u'Jabber Open Source License',
        u'Lucent Public License (Plan9)',
        u'Lucent Public License Version 1.02',
        u'MITRE Collaborative Virtual Workspace License (CVW License)',
        u'Motosoto License',
        u'Mozilla Public License 1.0 (MPL)',
        u'Mozilla Public License 1.1 (MPL)',
        u'NASA Open Source Agreement 1.3',
        u'Naumen Public License',
        u'Nethack General Public License',
        u'Nokia Open Source License',
        u'OCLC Research Public License 2.0',
        u'Open Group Test Suite License',
        u'Open Software License',
        u'PHP License',
        u'Python license (CNRI Python License)',
        u'Python Software Foundation License',
        u'Qt Public License (QPL)',
        u'RealNetworks Public Source License V1.0',
        u'Reciprocal Public License',
        u'Ricoh Source Code Public License',
        u'Sleepycat License',
        u'Sun Industry Standards Source License (SISSL)',
        u'Sun Public License',
        u'Sybase Open Watcom Public License 1.0',
        u'University of Illinois/NCSA Open Source License',
        u'Vovida Software License v. 1.0',
        u'W3C License',
        u'wxWindows Library License',
        u'X.Net License',
        u'Zope Public License',
        u'zlib/libpng license',
        ]

    osi_approved_formatted = [ u'OSI Approved::' + x for x in osi_approved]

    all_formatted = other_formatted + okd_compliant_formatted + \
        non_okd_compliant_formatted + osi_approved_formatted

