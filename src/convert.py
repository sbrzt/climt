from rdflib import Graph, URIRef, Literal, Namespace, BNode
from rdflib.namespace import RDF, RDFS, XSD

# CONVERSIONENGINE
# document -> InformationObject
# text -> LinguisticObject
# character -> SymbolicObject
# syllable -> SymbolicObject
# word -> InformationObject
# sentence -> InformationObject
# paragraph -> InformationObject
# results -> PropositionalObject
# AttributeAssignment
# attributeAssignment --assigned--> Dimension --hasValue--> number (es. number of X)
# type -> Type
# person, software -> Actor

# word -> symbolicObject
# attributeAssignment --assigned--> Dimension --hasValue--> number
# type -> Type
# sense 

# word -> symbolicObject
# attributeAssignment --assigned--> Dimension --hasValue--> number
# type -> Type

# document -> informationObject
# attributeAssignment --assigned--> Dimension --hasValue--> number
# type -> Type

# paragraph -> informationObject
# attributeAssignment --assigned--> Dimension --hasValue--> number
# type -> Type


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