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
