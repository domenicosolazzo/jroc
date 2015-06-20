# obt-api
An api for using the Oslo-Bergen tagger


# INSTALLATION
     # Create a virtual environment
     virtualenv <name_env>
     source <name_env>/bin/activate
     
     # Install the requirements
     pip install -r requirements.txt
     
     # Clone Oslo-Bergen-Tagger
     git clone https://github.com/noklesta/The-Oslo-Bergen-Tagger
     
     # Install the tagger
     cd The-Oslo-Bergen-Tagger/bin
     wget http://www.tekstlab.uio.no/mtag/osx64/mtag-osx64
     mv mtag-osx64 mtag
     chmod +x mtag
     
     # Install VISL-G3 
     # http://beta.visl.sdu.dk/cg3/chunked/installation.html.
     
     # Clone OBT-Stat
     git clone git://github.com/andrely/OBT-Stat.git
  
  
# Endpoints
These are the endpoints for the API

## Endpoint: /entities
**Method**: POST
It will return all the entities for a given text

#### Example 
      entities :[
          "USA" ,
          "Thoresen" ,
          "Ivar Aasen" ,
          "Herøy" ,
          "Iver Andreas" ,
          "Thoresen" ,
          "Ivar Jonsson" ,
          "Hans Conrad Thoresen" ,
          "Rasmus Aarflots" ,
          "Ludvig Daae" ,
          "Norway" ,
          "Aasen" ,
          "Sweden" ,
          "Stephen Walton" 
      ]

## Endpoint: /tags
It will return all the tags for a given text

#### Example 
      tags :[
          "Andreas" ,
          "USA" ,
          "Thoresen" ,
          "Denmark" ,
          "Daae" ,
          "Skodjestrømmen" ,
          ...
          "Aasen" ,
          "Sweden" 
      ]

## Endpoint: /analyze
**Method**: POST
It will return all the data from the obt tagger, entities and tags for a given text

#### Example

      entities: [
          "USA" ,
          "Thoresen" ,
          "Ivar Aasen" ,
          "Herøy" ,
          "Iver Andreas" ,
          "Thoresen" ,
          "Ivar Jonsson" ,
          "Hans Conrad Thoresen" ,
          "Rasmus Aarflots" ,
          "Ludvig Daae" ,
          "Norway" ,
          "Aasen" ,
          "Sweden" ,
          "Stephen Walton"
      ],
      obt: [
          {               
               word: "Ivar",
               is_verb: false,
               is_number: {
                    ordinal: false,
                    is_number: false,
                    roman: false,
                    quantity: false
               },
               tagging: [
                    "Ivar",
                    "subst",
                    "prop",
                    "mask"
               ],
               options: "Ivar subst prop mask",
               is_subst: true,
               is_prop: true
           },
           {
                word: "Aasen",
                is_verb: false,
                is_number: {
                    ordinal: false,
                    is_number: false,
                    roman: false,
                    quantity: false
                },
                tagging: [
                    "Aasen",
                    "subst",
                    "prop",
                    "<*sen>",
                    "<*>"
                ],
                options: "Aasen subst prop <*sen> <*>",
                is_subst: true,
                is_prop: true
          },
      ...
      ...
      ],
      tags: [
          "Andreas" ,
          "USA" ,
          "Thoresen" ,
          "Denmark" ,
          "Daae" ,
          "Skodjestrømmen" ,
          ...
          "Aasen" ,
          "Sweden" 
      ]
      
## Endpoint: /demo/analyze
**Method**: GET

Test endpoint to demostrate the **analyze** endpoint


## Endpoint: /demo/tags
**Method**: GET

Test endpoint to demostrate the **tags** endpoint


## Endpoint: /demo/entities
**Method**: GET

Test endpoint to demostrate the **entities** endpoint


## Endpoint: /demo/text
**Method**: GET
Test endpoint to demostrate the **text** endpoint
