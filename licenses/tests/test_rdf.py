from licenses.vocab import rdf_data

def _test_01_rdf():
    for g in rdf_data():
        print g.identifier
        print g.serialize(format="n3")
