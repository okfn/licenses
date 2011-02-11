from licenses import Licenses

L = Licenses()

def test_total():
    ourlist = L.get_licenses()
    assert len(ourlist) == 102, len(ourlist)

def test_groups():
    ckan = L.get_group_licenses('ckan_original')
    assert len(ckan) == 78, len(ckan)
    assert ckan[0]['title'] == 'Other::License Not Specified', ckan[0]
    assert ckan[2]['url'] == 'http://www.opendefinition.org/licenses/odc-odbl', ckan[2]

    ukgov = L.get_group_licenses('ukgov')
    assert len(ukgov) == 2

