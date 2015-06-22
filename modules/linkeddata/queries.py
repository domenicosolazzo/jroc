class Queries(object):

    def __init__(self):
        pass

    # Fetch all the properties and values of a given resource
    QUERY_PROPERTIES_VALUES = """
            SELECT ?property ?propValue WHERE {
                <http://dbpedia.org/resource/%s> ?property ?propValue .
            }
    """

    # Fetch all the properties of a given resource
    QUERY_PROPERTIES = """
            SELECT DISTINCT ?property  WHERE {
                <http://dbpedia.org/resource/%s> ?property ?propValue .
            }
    """
    # Fetch all the page disambiguates
    QUERY_WIKI_PAGE_DISAMBIGUATES = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX dbo: <http://dbpedia.org/ontology/>

            SELECT DISTINCT ?syn WHERE {
                {   ?disPage dbpedia-owl:wikiPageDisambiguates <http://dbpedia.org/resource/%s> .
                    ?disPage dbpedia-owl:wikiPageDisambiguates ?syn .
                }
                UNION
                {
                    <http://dbpedia.org/resource/%s> dbpedia-owl:wikiPageDisambiguates ?syn .
                }
            }
    """
    # Fetch the thumbnail of a given resource
    QUERY_THUMBNAIL = """
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            SELECT ?thumbnail
            WHERE {
              <http://dbpedia.org/resource/%s> dbpedia-owl:thumbnail ?thumbnail .
            }
            LIMIT 1
    """

    # Fetch the unique URI of a given resource
    QUERY_SPARQL_URI = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX dbo: <http://dbpedia.org/ontology/>

            SELECT ?s WHERE {
              {
                ?s rdfs:label "%s"@en ;
                   a owl:Thing .
              }
              UNION
              {
                ?altName rdfs:label "%s"@en ;
                         dbo:wikiPageRedirects ?s .
              }
            }
    """

    # Fetch the basic info of a given resource
    QUERY_BASIC_INFO = """
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            SELECT ?comment, ?label, ?abstract, ?name
            WHERE {
              <http://dbpedia.org/resource/%s>  rdfs:label ?label; rdfs:comment ?comment; dbpedia-owl:abstract ?abstract; foaf:name ?name .
              FILTER(langMatches(lang(?name), "EN"))
              FILTER(langMatches(lang(?comment), "EN"))
              FILTER(langMatches(lang(?abstract), "EN"))
              FILTER(langMatches(lang(?label), "EN"))
            }
            LIMIT 5
    """

    # Fetch entity types
    QUERY_ENTITY_TYPES = """
        PREFIX yago: <http://dbpedia.org/class/yago/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        SELECT ?type  WHERE {
            <http://dbpedia.org/resource/%s> rdf:type ?type.
        }LIMIT 100
    """
