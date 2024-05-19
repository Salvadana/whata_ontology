
import xml.etree.ElementTree as ET
from rdflib import Graph, URIRef, Literal, Namespace, RDF
from rdflib.namespace import RDFS

# Parse the XML file
tree = ET.parse(r'C:\Users\lored\OneDrive\Desktop\whata_ontology\corpus\sample_corpus.xml')
root = tree.getroot()

# Create a graph
g = Graph()

# Define namespaces
NS = Namespace("http://example.org/annotations#")
g.bind("ex", NS)  # Bind the namespace with prefix 'ex' for easy reference

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

