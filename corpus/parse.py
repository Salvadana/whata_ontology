
'''
import xml.etree.ElementTree as ET
from rdflib import Graph, URIRef, Literal, Namespace, RDF
from rdflib.namespace import RDFS

# Parse the XML file
tree = ET.parse(r'C:\Users\lored\OneDrive\Desktop\whata_ontology\corpus\sample_corpus.xml')
root = tree.getroot()

# Create a graph
g = Graph()

# Define namespaces
NS = Namespace("https://raw.githubusercontent.com/Salvadana/whata_ontology/main/ontology/whataboutism_ontology.owl#")
g.bind("whata", NS)  # Bind the namespace with prefix 'ex' for easy reference

# Extract annotations and add to graph
for annotation in root.findall('.//{http://www.tei-c.org/ns/1.0}Annotation'):
    entity = annotation.find('{http://www.tei-c.org/ns/1.0}Entity').text
    concept = annotation.find('{http://www.tei-c.org/ns/1.0}Class').text
    
    entity_uri = URIRef(NS[entity.replace(" ", "_")])  # Create a unique URI for the entity
    concept_uri = URIRef(NS[concept])  # Create a unique URI for the concept
    
    # Add triples to the graph
    g.add((entity_uri, RDF.type, concept_uri))
    g.add((entity_uri, RDFS.label, Literal(entity)))
    g.add((concept_uri, RDFS.label, Literal(concept)))

# Save graph to a file in Turtle format (optional)
g.serialize(destination='C:\\Users\\lored\\OneDrive\\Desktop\\whata_ontology\\corpus\\annotations.ttl', format='turtle')

# Query the graph using SPARQL
query = """
PREFIX ex: <http://example.org/annotations#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?entity ?conceptLabel
WHERE {
    ?entity a ?concept .
    ?entity rdfs:label ?entityLabel .
    ?concept rdfs:label ?conceptLabel .
}
"""

# Execute the query and print results
for row in g.query(query):
    print(f"Entity: {row.entity}, Concept: {row.conceptLabel}")

'''
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, XSD

# Definisci i namespace
ear = Namespace("http://www.essepuntato.it/2008/12/earmark#")
whata = Namespace("https://raw.githubusercontent.com/Salvadana/whata_ontology/main/ontology/whataboutism_ontology.owl#")

# Crea il grafo RDF
g = Graph()

# Aggiungi i prefissi
g.bind("ear", ear)
g.bind("whata", whata)
g.bind("xsd", XSD)

# Definisci il documento
doc = URIRef("http://example.org/doc1")
g.add((doc, RDF.type, ear.StringDocuverse))
g.add((doc, ear.hasContent, Literal("The West has no right to criticize our record on human rights, look at US actions in Central America, the history of slavery and of lynchings, not to mention apartheid in South Africa…", datatype=XSD.string)))

# Definisci le annotazioni
annotations = [
    (URIRef("http://example.org/annotation1"), "WhataboutistPerspectivisation", 0, 53),
    (URIRef("http://example.org/annotation2"), "actsAgainst", 63, 92),
    (URIRef("http://example.org/annotation3"), "BlamableEventuality", 98, 136),
    (URIRef("http://example.org/annotation4"), "BlamableEventuality", 150, 184)
]

# Aggiungi le annotazioni al grafo
for ann, typ, start, end in annotations:
    g.add((ann, RDF.type, ear.PointerRange))
    g.add((ann, ear.refersTo, doc))
    g.add((ann, ear.begins, Literal(start, datatype=XSD.nonNegativeInteger)))
    g.add((ann, ear.ends, Literal(end, datatype=XSD.nonNegativeInteger)))
    g.add((ann, RDF.type, whata[typ]))

# Salva il grafo in un file Turtle
with open("annotated_document.ttl", "wb") as f:
    f.write(g.serialize(format="turtle"))
