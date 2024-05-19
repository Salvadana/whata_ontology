# %% [markdown]
# ## Test and fix.
# 'An ontology module developed for addressing a certain user story associated to a certain competency question, is tested e.g.
# 
# - (i) by encoding in the ontology for a sample set of facts based on the user
# story, 
# - (ii) defining one or a set of SPARQL queries that formally encode
# the competency question, 
# - (iii) associating each SPARQL query with the expected result, 
# - and (i) running the SPARQL queries against the ontology and compare actual with expected results.' 
# 
# ### Task description
# 
# 'The goal of this task is to validate the resulting module
# with respect to the CQ just modeled. To this aim, the task is executed through
# the following steps: 
# - (i) the CQ is elaborated in order to derive a unit test e.g.,
# SPARQL query;
# - (ii) the instance module is fed with sample facts based on the
# story; 
# - (iii) the unit test is ran against the ontology module. If the result is not
# the expected one i.e. the test is not passed, the module is revised in order to fix
# it, and the unit test ran again until the test is passed; 
# - (iv) run all other unit
# tests associated with the story so far until they all pass.'  <br>
# 
# <br>
# Reference:<br>
# Presutti, V., Daga, E., Gangemi, A., & Blomqvist, E. (2009). eXtreme Design with Content Ontology Design Patterns. WOP.  https://dl.acm.org/doi/10.5555/2889761.2889768

# %%
#%pip install rdflib
from rdflib import *
whataGraph = Graph()
whataGraph.parse("../ontology/knowledge_graph.ttl", format="ttl")

# %% [markdown]
# ## SPARQL queries
# #### Perspectivisation CQs
# 1. Is whataboutism recognisable as an (or part of an ) act of perspectivisation? Which elements of the cognitive perspectivisation are present and manifest concretely in a whataboutist claim?  --> Which is the  specific component of the Perspectivisation which is modified by whataboutism ?  
# <br>Expected result: Sample Eventuality (roomEventuality1)
# 

# %%

cq1 = """PREFIX whata:<https://raw.githubusercontent.com/Salvadana/whata_ontology/main/ontology/whataboutism_ontology.owl#> 
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX per:<http://www.ontologydesignpatterns.org/ont/persp/perspectivisation.owl#>
    
SELECT  ?eventuality  
WHERE {
  ?s a whata:WhataboutistPerspectivisation.
  ?s per:Lens ?lens.
  ?s per:Eventuality ?eventuality.
  ?s per:Conceptualiser ?conceptualiser.
  

}     
"""
results = whataGraph.query(cq1)

for row in results:
    print(row)
    

# %% [markdown]
# 1.a Who is the conceptualiser? <br>
# Expected: ResponsibilityOwner1

# %%

cq1_a = """PREFIX whata:<https://raw.githubusercontent.com/Salvadana/whata_ontology/main/ontology/whataboutism_ontology.owl#> 
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX per:<http://www.ontologydesignpatterns.org/ont/persp/perspectivisation.owl#>
    
SELECT   ?conceptualiser 
WHERE {
  ?s a whata:WhataboutistPerspectivisation.
  ?s per:Lens ?lens.
  ?s per:Eventuality ?eventuality.
  ?s per:Conceptualiser ?conceptualiser.
  

}     
"""
results = whataGraph.query(cq1_a)

for row in results:
    print(row)
    

# %% [markdown]
# 2. By the means of which component of perpectivisation does Whataboutism act? The aim is retrieving the entity type that is responsible in the focus shifting action within a cognitiveperspectivisation. <br> expected:  Lens

# %%

cq2 = """PREFIX whata:<https://raw.githubusercontent.com/Salvadana/whata_ontology/main/ontology/whataboutism_ontology.owl#> 
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX per:<http://www.ontologydesignpatterns.org/ont/persp/perspectivisation.owl#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
SELECT ?s
WHERE {
  ?p a whata:WhataboutistPerspectivisation.
  ?p per:Eventuality ?e.
  ?s whata:shiftsFocusFrom ?e.
  
}
      
"""
results = whataGraph.query(cq2)

for row in results:
    print(row)
    

# %% [markdown]
# 3. What is the action performed by whataboutism on the main perspectivised eventuality? <br> expected:Shift Focus

# %%
#what does whataboutism do? how it acts in the perspectivisation situation?

cq3 = """PREFIX whata:<https://raw.githubusercontent.com/Salvadana/whata_ontology/main/ontology/whataboutism_ontology.owl#> 
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX per:<http://www.ontologydesignpatterns.org/ont/persp/perspectivisation.owl#>
SELECT   ?actsUpon
WHERE {
  ?s a whata:WhataboutistPerspectivisation.
  ?s per:Lens ?lens.
  ?s per:Eventuality ?eventuality.
  ?lens ?actsUpon ?eventuality.
}
      
"""
results = whataGraph.query(cq3)

for row in results:
    print(row)
    

# %% [markdown]
# 3.a What are all the actions performed by a whataboutist lens on the eventualities involved in the whataboutist perspectivisation? <br> Expected:Shift Focus from, shift focus on, creates blended

# %%


cq3_a = """PREFIX whata:<https://raw.githubusercontent.com/Salvadana/whata_ontology/main/ontology/whataboutism_ontology.owl#> 
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX per:<http://www.ontologydesignpatterns.org/ont/persp/perspectivisation.owl#>
SELECT   ?actsUpon 
WHERE {
  
  ?s a whata:WhataboutistLens; 
  ?actsUpon ?eventuality.  
  FILTER (?actsUpon != rdf:type)
  FILTER (?actsUpon != rdfs:subClassOf)
}
      
"""
results = whataGraph.query(cq3_a)

for row in results:
    print(row)
    

# %% [markdown]
# #### Linguistic Features CQs

# %% [markdown]
# 4. Which linguistic elements do denote whataboutism? <br>
# expected result: string with pattern, string with sentence

# %%
# Which linguistic elements do denote whataboutism?
#expected result: string with pattern, string with sentence
cq4 = """PREFIX whata:<https://raw.githubusercontent.com/Salvadana/whata_ontology/main/ontology/whataboutism_ontology.owl#> 
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT  ?pattern ?sentence
WHERE {
  ?s a whata:WhataboutistPerspectivisation;
    
   whata:relatedIdentifyingPattern ?pattern;
   whata:relatedSentence ?sentence.
}
      
"""
results = whataGraph.query(cq4)

for row in results:
    print(row)
    

# %% [markdown]
# #### Blaming Situation

# %% [markdown]
# 5. On which kind of situation does Whataboutism act? <br>
# expected: Blamable Eventuality

# %%

#- Which kind of situation is the one involved in Whataboutism?

cq5 = """
    PREFIX whata:<https://raw.githubusercontent.com/Salvadana/whata_ontology/main/ontology/whataboutism_ontology.owl#> 
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    SELECT DISTINCT ?situation 
   WHERE {
       whata:WhataboutistLens whata:shiftsFocusFrom ?o.
       whata:WhataboutistLens whata:shiftsFocusOn ?o2.
       ?o a ?situation.
       ?o2 a ?situation.
        }
"""
results = whataGraph.query(cq5)

for row in results:
    print(row)
    


    

# %% [markdown]
# 
# 6.  Do these blamable eventualities perspectivised by whataboutism all correspond to a common description? And if so, which is this description? <br>Retrieving the perspectivised eventualities and the description they satisfy:
# <br> Expected:   Blaming description, Eventualities 1 and 2, Blanded Blame Frame
# 

# %%
#- Which kind of situation is the one involved in Whataboutism?
# - What entities are involved in the blaming situation?
cq6 = '''
PREFIX whata: <https://raw.githubusercontent.com/Salvadana/whata_ontology/main/ontology/whataboutism_ontology.owl#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX dns: <http://www.ontologydesignpatterns.org/cp/owl/description.owl#>

SELECT  ?description ?o
WHERE {
whata:WhataboutistLens ?actsUpon ?o.
  ?o dns:satisfies ?description .
}

'''
results = whataGraph.query(cq6)

for row in results:
    print(row)
    

# %% [markdown]
#  7. What kind of entities are involved in the blaming situation frame?
#  <br> Expected: responsibility owner, ought

# %%

# - What entities are involved in the blaming situation?
cq7 = """
    PREFIX whata:<https://raw.githubusercontent.com/Salvadana/whata_ontology/main/ontology/whataboutism_ontology.owl#> 
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    SELECT DISTINCT ?s
   WHERE {
       ?s whata:isParticipantIn ?blamable.
       ?blamable a whata:BlamableEventuality.
        }
"""
results = whataGraph.query(cq7)

for row in results:
    print(row)
    

# %% [markdown]
# Further tests on CQ7: <br>
# - does a blamable eventuality involve an ought and a responsibility owner?
# <br>expected: True

# %%

#what does a blamable eventuality involve?
cq7_a = """PREFIX whata:<https://raw.githubusercontent.com/Salvadana/whata_ontology/main/ontology/whataboutism_ontology.owl#> 
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX per:<http://www.ontologydesignpatterns.org/ont/persp/perspectivisation.owl#>
ASK
WHERE {
  ?s whata:isParticipantIn ?blamable.
  ?blamable a whata:BlamableEventuality.
  ?s a whata:Ought.
}
      
"""
results = whataGraph.query(cq7_a)

for row in results:
    print(row)
    

# %%

#what does a blamable eventuality involve?
cq7_b = """PREFIX whata:<https://raw.githubusercontent.com/Salvadana/whata_ontology/main/ontology/whataboutism_ontology.owl#> 
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX per:<http://www.ontologydesignpatterns.org/ont/persp/perspectivisation.owl#>
ASK
WHERE {
  ?s whata:isParticipantIn ?blamable.
  ?blamable a whata:BlamableEventuality.
  ?s a whata:ResponsibilityOwner.
}
      
"""
results = whataGraph.query(cq7_b)

for row in results:
    print(row)
    

# %% [markdown]
# query with result Responsibility owner acts again ought<br>expected: Responsibility Owner1/2, TidyingRoom

# %%
#query with result Responsibility owner acts again ought
cq='''SELECT ?responsibilityOwner ?ought
WHERE {
  ?responsibilityOwner rdf:type :ResponsibilityOwner ;
                       :actsAgainst ?ought .
}

'''
results = whataGraph.query(cq)

for row in results:
    print(row)

# %% [markdown]
# #### Blending
# 
# 8. Does Whataboutism act accordingly to the Conceptual Blanding Theory? I.e. Does it create a blended space? <br> Expected result:True

# %%


cq8 = """PREFIX whata:<https://raw.githubusercontent.com/Salvadana/whata_ontology/main/ontology/whataboutism_ontology.owl#> 
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX per:<http://www.ontologydesignpatterns.org/ont/persp/perspectivisation.owl#>
ASK
WHERE {
  ?s a whata:WhataboutistPerspectivisation.
  ?s whata:createsBlended ?o.
}
      
"""
results = whataGraph.query(cq8)

for row in results:
    print(row)
    

# %% [markdown]
# 9. Which kind of elements are blended together by whataboutism? i.e. which are the blendable elements involved? 
# <br>
# Expected: Eventualities 1 and 2

# %%

#what does a blamable eventuality involve?
cq9 = """PREFIX whata:<https://raw.githubusercontent.com/Salvadana/whata_ontology/main/ontology/whataboutism_ontology.owl#> 
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX per:<http://www.ontologydesignpatterns.org/ont/persp/perspectivisation.owl#>
    PREFIX dns: <http://www.ontologydesignpatterns.org/cp/owl/description.owl#>
SELECT ?s
WHERE {
  ?s rdfs:subClassOf per:Blendable.
}
      
"""
results = whataGraph.query(cq9)

for row in results:
    print(row)
    

# %% [markdown]
# 10. From which classes does the blanded element inerhits its features?
# <br> Expect

# %%


cq10 = """PREFIX whata:<https://raw.githubusercontent.com/Salvadana/whata_ontology/main/ontology/whataboutism_ontology.owl#> 
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX per:<http://www.ontologydesignpatterns.org/ont/persp/perspectivisation.owl#>
     PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT  distinct  ?class
WHERE {
  ?s a whata:WhataboutistPerspectivisation.
  ?s whata:createsBlended ?o.
  ?o a ?type.
  ?o rdfs:subClassOf ?class.

}
      
"""
results = whataGraph.query(cq10)

for row in results:
    print(row)
    

# %% [markdown]
# #### Whataboutism usage
# 11. Is the arguer in Sample Situation 1 being whataboutist? I.e. is the room eventuality perspectivised using whataboutism?

# %%
cq='''PREFIX whata: <https://raw.githubusercontent.com/Salvadana/whata_ontology/main/ontology/whataboutism_ontology.owl#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX per:<http://www.ontologydesignpatterns.org/ont/persp/perspectivisation.owl#>
ASK 
WHERE{ ?p per:Eventuality whata:RoomEventuality1.
        ?p per:Lens ?lens.
        ?lens a whata:WhataboutistLens. }

  
'''
results = whataGraph.query(cq)

for row in results:
    print(row)

# %% [markdown]
# #### Fallacies and Biases connections with whataboutism

# %% [markdown]
# 12. Is whataboutism connected to any discourse fallacies? And to which kind?
# <br> Expected: Relevance Fallacies Lens

# %%
cq12='''PREFIX : <https://raw.githubusercontent.com/Salvadana/whata_ontology/main/ontology/whataboutism_ontology.owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?relatedLens
WHERE {
  ?relatedLens :relatedToLens :WhataboutistLens .
  ?relatedLens rdf:type :RelevanceFallacyLens .
}'''
results = whataGraph.query(cq12)

for row in results:
    print(row)

# %% [markdown]
# 13.  Is whataboutism connected to any Cognitive Bias? And to which kind? 
# <br> Expected: Confirmation Bias Lens

# %%
cq13='''PREFIX : <https://raw.githubusercontent.com/Salvadana/whata_ontology/main/ontology/whataboutism_ontology.owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?relatedLens
WHERE {
  ?relatedLens :relatedToLens :WhataboutistLens .
  ?relatedLens rdf:type :ConfirmationBiasLens .
}'''
results = whataGraph.query(cq13)

for row in results:
    print(row)


