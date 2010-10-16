from licenses.vocab import rdf_data

def test_01_rdf():
    for g in rdf_data():
        print g.identifier
        print g.serialize(format="n3")
