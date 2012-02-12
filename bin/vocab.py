import pkg_resources, os

from ordf.namespace import Namespace, register_ns
register_ns("cc", Namespace("http://creativecommons.org/ns#"))
register_ns("licenses", Namespace("http://purl.org/okfn/licenses/"))
register_ns("opendef", Namespace("http://purl.org/okfn/opendefinition#"))
register_ns("xhv", Namespace("http://www.w3.org/1999/xhtml/vocab#"))

from ordf.graph import Graph
from ordf.namespace import RDF, RDFS, CC, LICENSES, XHV, SKOS, OWL, ORDF
from ordf.term import Literal, URIRef
from ordf.vocab.owl import Class, Property, predicate

from licenses.service import LicensesService2

__all__ = ['rdf_data', 'License']

class License(Class):
    def __init__(self, *av, **kw):
        kwa = kw.copy()
        kwa.setdefault("skipOWLClassMembership", True)
        super(License, self).__init__(*av, **kwa)
        self.type = CC.License
    license = predicate(CC.license)
    prefLabel = predicate(SKOS.prefLabel)
    notation = predicate(SKOS.notation)
    lens = predicate(ORDF.lens)
    
def rdf_data():
    s = LicensesService2()

    g = Graph(identifier=CC[""])
    g.parse("http://creativecommons.org/schema.rdf")
    yield g
    
    fp = pkg_resources.resource_stream("licenses", os.path.join("n3", "license.n3"))
    g = Graph(identifier=LICENSES["lens"])
    g.parse(fp, format="n3")
    fp.close()
    yield g
    
    for ld in s.get_licenses():
        ident = LICENSES[ld["id"]]
        g = Graph(identifier=ident)
        l = License(ident, graph=g)
        l.label = Literal(ld["title"])
        l.prefLabel = Literal(ld["title"])
        l.notation = Literal(ld["id"])
        l.lens = LICENSES.lens
        
        if ld.get("url"):
            url = URIRef(ld["url"])
            sa = Graph()
            try:
                sa.parse(url)
            except:
                pass
            try:
                sa.parse(url, format="rdfa")
            except:
                pass

            sa.remove((url, XHV.icon, None))
            sa.remove((url, XHV.alternate, None))
            sa.remove((url, XHV.stylesheet, None))
            for ll in sa.distinct_objects(url, XHV.license):
                l.license = ll
            sa.remove((url, XHV.license, None))

            if sa.bnc((url, None, None)):
                [g.add((ident, p, o)) for s,p,o in sa.bnc((url, None, None))]
                l.sameAs = url
            else:
                l.seeAlso = URIRef(ld["url"])
        yield g
