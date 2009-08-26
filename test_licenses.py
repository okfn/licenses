import licenses

def test_basic():
    ourlist = licenses.LicenseList.all_formatted
    okd = licenses.LicenseList.okd_compliant_formatted
    assert ourlist[1] == okd[0], ourlist[0]
    assert 'OKD Compliant::Other (Public Domain)' in okd, okd

