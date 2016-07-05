# JRoc
### We ain't afraid of Randy with his candy. You Know What Am I Sayin'?
A REST API for tagging and entity extraction of documents in Norwegian bokmål and nynorsk.


# INSTALLATION
     # Clone the repo
     git clone git@github.com:domenicosolazzo/jroc.git

- Install [Docker](https://www.docker.com/)
- [Deploy](https://github.com/domenicosolazzo/jroc/blob/master/README.md#local-deployment)


#### Instance folder
Add an **instance** folder with a **config.py**, if you want to override some of the configuration values in your local installation.

# Environment variables
- **DEBUG**[True|False]: Enable / Disable debugging for the Flask app (Default: False)
- **SECRET_KEY**: This is a secret key that is used by Flask to sign cookies. It should be a random value
- **BASIC_AUTH_USERNAME**: Username for the basic auth
- **BASIC_AUTH_PASSWORD**: Password for the basic auth
- **OBT_TYPE**: Type of Oslo-Bergen tagger. Check below for the possible values.
```
### Options for OBT_TYPE
##### tag-bm.sh
CG and statistical disambiguation, bokmål

##### tag-nostat-bm.sh
CG disambiguation only, bokmål

##### tag-nostat-nn.sh
CG disambiguation only, nynorsk
```

##### P.S.
For activating basic auth, you need to set both BASIC_AUTH_USERNAME and BASIC_AUTH_PASSWORD

# Deployment
## Heroku Deployment
### Heroku
- Install [Docker](https://www.docker.com/)
- (Mac Only)
  ```
  # Run this command to make docker working on your terminal
  eval "$(docker-machine env default)"
  ```

- Install the Heroku plugin for Docker (Only the first time)
```
heroku plugins:install heroku-container-tools
```

- Create your heroku app
```
heroku create <heroku_app_name>
```

##### Build the Docker image
- Use Docker Compose
```
# It build a new image without using the cache
docker-compose build --no-cache

# Or you can use the cached image
docker-compose build
```

While building a docker image, sometimes can happen that you are consuming all the space in your harddrive.
In that case, run these commands before building the image again:
```
docker-machine rm default
docker-machine create --driver virtualbox default
eval "$(docker-machine env default)"
```

##### Local deployment
- Create a symlink for Dockerfile.local to Dockerfile
```
ln -s Dockerfile.local Dockerfile
```

- Run the web instance with Docker Compose
```
docker-compose up web
```
- Check if it is running on your browser
```
$ open "http://$(docker-machine ip default):8080"
```

##### Remote deployment
- Build the image with Docker Compose
```
# It build a new image without using the cache
docker-compose build --no-cache

# Or you can use the cached image
docker-compose build
```
- Run docker:release
```
heroku container:release
```

# Usage
How to use the **analyze** endpoint

      curl -H "Content-Type: application/json" -X POST -d '{"data":"text_here"}' http://<your-app-domain>/tagger/analyze

How to use the **entities** endpoint

      curl -H "Content-Type: application/json" -X POST -d '{"data":"text_here"}' http://<your-app-domain>/tagger/entities

How to use the **tags** endpoint

      curl -H "Content-Type: application/json" -X POST -d '{"data":"text_here"}' http://<your-app-domain>/tagger/tags

How to use the **entity extraction** endpoint

        curl -H "Content-Type: application/json" -X GET  http://<your-app-domain>/entities/<entity_name>

How to extract all the types connected of a given entity

      curl -H "Content-Type: application/json" -X GET http://<your-app-domain>/entities/<entity_name>/types

How to extract all the properties uri's of a given entity

      curl -H "Content-Type: application/json" -X GET http://<your-app-domain>/entities/<entity_name>/properties

How to extract the property value of given entity

      curl -H "Content-Type: application/json" -X GET http://<your-app-domain>/entities/<entity_name>/properties?name=<property_uri>

How to extract the property value of a given entity in a given language

      curl -H "Content-Type: application/json" -X GET http://<your-app-domain>/entities/<entity_name>/properties?name=<property_uri>&lang=<country_code>


# Endpoints
Description of the API endpoints

## Endpoint: /tagger/entities
**Method**: POST
It will return all the entities for a given text

#### Example
      {"data": [
        "Skriftsprog",
        "Sivert",
        "Aasen",
        ...
        "USA",
        "Ivar Aasen"],
        "uri": "http://<your-app-domain>/tagger/entities"
      }

### Querystring
- **advanced**[0 | 1]: If it is one, it will return the uri for each entity

#### Example
       {"data": [
        { name:"Skriftsprog", uri: "http://<your-app-domain>/entities/Skriftsprog" },
        { name:"Aasen", uri: "http://<your-app-domain>/entities/Aasen"},
        ...
        { name:"USA", uri: "http://<your-app-domain>/entities/USA"},
        { name:"Ivar Aasen", uri: "http://<your-app-domain>/entities/Ivar_Aasen"}],
        "uri": "http://<your-app-domain>/tagger/entities"
      }

## Endpoint: /tagger/tags
It will return all the tags for a given text

#### Example
      data :[
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

## Endpoint: /tagger/analyze
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


## Endpoint: /entities/<entity_name>
**Method**: GET

**Description**: It will extract information from DBPedia about the entities

### Result properties
- **properties_uri**: Properties uri of a given entity
- **types_uri**: Types uri of a given entity
- **uri**: uri of a given entity
- **redirected_from**[optional]: The original entity uri if the entity name has been redirected
- **name**: entity name

#### Example
      data: {
        "properties_uri": "http://<your-app-domain>/entities/Norway/properties",
        "types_uri": "http://<your-app-domain>/entities/Norway/types",
        "uri": "http://<your-app-domain>/entities/Norway",
        "redirected_from": "http://<your-app-domain>/entities/Norway",
        "name": "Norway"
       }


## Endpoint: /entities/[entity_name]/types
**Method**: GET

**Description**: It will extract the types connected to the entity and try to guess the entity type (person, organization, event, location..)

### Result properties
- **entity_detection**: It will contain a guess about the type of the entity
- **types**: List of types connected to the entity

#### Example
      data: {
         entity_detection: {
           is_person: false
           is_location: true
           is_event: false
           other: false
           is_org: false
           type: "Location"
           is_work: false
         },
         types:{
           "http://www.w3.org/2002/07/owl#Thing",
           "http://schema.org/Country",
           "http://schema.org/Place",
           ...
         }
      },
      name: Norway,
      entity_uri: http://<your-app-domain>/entities/Norway,
      uri: http://<your-app-domain>/entities/Norway/types


## Endpoint: /entities/[entity_name]/properties
**Method**: GET

**Description**: It will extract all the properties connected to a given entity

#### Example
      data: {
           "http://www.w3.org/2000/01/rdf-schema#label": {
                "uri": "http://<your-app-domain>/entities/Norway/properties?name=http%3A//www.w3.org/2000/01/rdf-schema%23label",
                "name": "http://www.w3.org/2000/01/rdf-schema#label"
           },
           "http://www.w3.org/2007/05/powder-s#describedby": {
                "uri": "http://<your-app-domain>/entities/Norway/properties?name=http%3A//www.w3.org/2007/05/powder-s%23describedby",
                "name": "http://www.w3.org/2007/05/powder-s#describedby",
           },
           ...
      }
      ,
      name: Norway,
      entity_uri: http://<your-app-domain>/entities/Norway,
      uri: http://<your-app-domain>/entities/Norway/properties

### QueryString
- **name**: It will extract the value for this given property.
- **lang**: It is the country code. It will extract the value for a given property in a given language. Only used in combination with the **name**

#### Example
      uri: http://<your-app-domain>/entities/Norway/properties?name=http%3A//www.w3.org/2000/01/rdf-schema%23label

      data: {
           "http://www.w3.org/2000/01/rdf-schema#label": [
              "Norway",
              "\u0627\u0644\u0646\u0631\u0648\u064a\u062c",  // النرويج
              "Norwegen",
              "Noruega",
              "Norv\u00e8ge", // Norvège
              "Norvegia",
              "\u30ce\u30eb\u30a6\u30a7\u30fc", // ノルウェー
              "Noorwegen",
              "Norwegia",
              "Noruega",
              "\u041d\u043e\u0440\u0432\u0435\u0433\u0438\u044f", // Норвегия
              "\u632a\u5a01" // 挪威
           ]
      },
       "entity_uri": "http://<your-app-domain>/entities/Norway",
       "name": "Norway",
       "uri": "http://<your-app-domain>/entities/Norway/properties?name=http%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema#label"
      }

## Example Text
      Ivar Aasen ble født på gården Åsen i Hovdebygda på Sunnmøre som sønn av småbrukeren Ivar Jonsson.
      Han ble døpt Iver Andreas, formen «Ivar» kom i bruk omkring 1845. Gården han vokste opp på var isolert, så han hadde ingen kamerater.
      Dette førte til at han leste mye i de få bøkene familien hadde, deriblant Bibelen. Faren døde i 1826. Det var åtte søsken, og de mistet begge foreldrene tidlig.
      I foreldrenes fravær ble broren det nye familieoverhodet; han satte Ivar til gårdsarbeid og lot ham ikke utvikle de intellektuelle evnene sine, men Ivar utmerket seg likevel ved konfirmasjonen, og presten skrev rosende om ham i kirkeboken.
      Gården Ekset med Sivert og Rasmus Aarflots boksamling var bare 3 kilometer frå Åsen-garden. Aarflot hadde selv gjort observasjoner om slektskap mellom sunnmørsdialekten og gammelnorsk, og dette kan ha inspirert den unge Aasen.
      Aasen lærte seg norrønt, engelsk, fransk og latin.

[Read more](https://github.com/domenicosolazzo/obt-api/blob/master/TEXTFILE)

# Dependencies
- [The Oslo-Bergen tagger](https://github.com/noklesta/The-Oslo-Bergen-Tagger): morphosyntactic tagger for Norwegian bokmål and nynorsk. [More info about the tagger](http://tekstlab.uio.no/obt-ny/index.html). This is the [output](https://github.com/domenicosolazzo/obt-api/blob/master/OUTPUT) from the tagger.
- [OBT-Stat](https://github.com/andrely/OBT-Stat): Statistical disambiguator for the Oslo-Bergen Part of Speech tagger
- [VISL CG-3](http://beta.visl.sdu.dk/constraint_grammar.html): CG compiler. 3rd version of the CG formalism variant
- [Multitagger](http://www.tekstlab.uio.no/mtag/osx64/mtag-osx64): Multitagger with lexicon for Norwegian Bokmål and Nynorsk.
- [HusPos](https://code.google.com/p/hunpos/): Hunpos is an open source reimplementation of TnT, the well known part-of-speech tagger

#### About Oslo-Bergen Tagger
The Oslo-Bergen Tagger is a morphosyntactic tagger for Norwegian bokmål and nynorsk. For general information about the tagger, visit its home page: [Tekstlab.uio.no](http://www.tekstlab.uio.no/obt-ny/).

# License
[License GPLv3](https://github.com/domenicosolazzo/obt-api/blob/master/LICENSE)

# Author
[Domenico Solazzo](http://www.domenicosolazzo.com) - [Twitter](http://twitter.com/domenicosolazzo)
