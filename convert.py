from rdflib import Graph, URIRef, Literal, Namespace, BNode
from rdflib.namespace import RDF, RDFS, XSD

# Namespaces
LEXINFO = Namespace("http://www.lexinfo.net/ontology/2.0/lexinfo#")
ONTOLEX = Namespace("http://www.w3.org/ns/lemon/ontolex#")
EX = Namespace("http://example.org/")

g = Graph()
g.bind("ontolex", ONTOLEX)
g.bind("lexinfo", LEXINFO)
g.bind("ex", EX)

def convert_text(word_details):
    for detail in word_details:
        word_uri = URIRef(EX[detail['word']])
        g.add((word_uri, RDF.type, ONTOLEX.LexicalEntry))

        g.add((URIRef(EX[f"{detail['word']}-form"]), RDF.type, ONTOLEX.Form))
        
        g.add((word_uri, ONTOLEX.lexicalForm, URIRef(EX[f"{detail['word']}-form"])))
        g.add((EX[f"{detail['word']}-form"], ONTOLEX.writtenRep, Literal(detail['word'], lang="en")))

        g.add((word_uri, LEXINFO.partOfSpeech, Literal(detail['pos_tag'], datatype=XSD.string)))

        for i, sense in enumerate(detail['senses']):
            sense_uri = URIRef(EX[f"{detail['word']}-sense-{i}"])
            context_uri = URIRef(EX[f"{detail['word']}-context-{i}"])
            g.add((sense_uri, RDF.type, ONTOLEX.LexicalSense))
            g.add((word_uri, ONTOLEX.sense, sense_uri))
            g.add((sense_uri, ONTOLEX.context, context_uri))
            g.add((context_uri, RDF.value, Literal(sense, lang='en')))

    rdf_output = g.serialize(format='turtle')
    return rdf_output