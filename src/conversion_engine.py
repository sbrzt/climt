import uuid
from rdflib import Graph, URIRef, Literal, Namespace, BNode
from rdflib.namespace import RDF, RDFS, XSD, PROV, FOAF


class ConversionEngine:
    """
    """

    def __init__(self, analysis):
        self.analysis = analysis

    def convert_data(self):
        """
        """
        g = Graph()
        g.bind("foaf", FOAF)
        g.bind("prov", PROV)
        g.bind("rdf", RDF)
        BASE = "http://example.org"

        document = URIRef(f"{BASE}/document")
        g.add((document, RDF.type, FOAF.Document))
        agent = URIRef(f"{BASE}/lodot")
        g.add((agent, RDF.type, PROV.Agent))

        for analysis, results in self.analysis.items():
            activity = URIRef(f"{document}/activity/{analysis}")
            g.add((activity, PROV.used, document))
            g.add((activity, PROV.wasAssociatedWith, agent))
            for key, value in results.items():
                dimension = URIRef(f"{document}/dimension/{key}")
                g.add((activity, RDF.type, PROV.Activity))
                g.add((activity, PROV.generated, dimension))
                g.add((dimension, PROV.value, Literal(value)))

        return g.serialize(format="turtle")


# CONVERSIONENGINE
# document -> InformationObject -- Document
# text -> LinguisticObject      -- ?
# character -> SymbolicObject   -- Entity
# syllable -> SymbolicObject    -- Entity
# word -> InformationObject     -- Entity
# sentence -> InformationObject -- Entity
# paragraph -> InformationObject - Entity
# results -> PropositionalObject - Entity
# AttributeAssignment           -- Activity
# attributeAssignment --assigned--> Dimension --hasValue--> number (es. number of X)
# type -> Type
# person, software -> Actor     -- Agent

# word -> symbolicObject
# attributeAssignment --assigned--> Dimension --hasValue--> number
# type -> Type

# word -> symbolicObject
# attributeAssignment --assigned--> Dimension --hasValue--> number
# type -> Type

# document -> informationObject
# attributeAssignment --assigned--> Dimension --hasValue--> number
# type -> Type

# paragraph -> informationObject
# attributeAssignment --assigned--> Dimension --hasValue--> number
# type -> Type
