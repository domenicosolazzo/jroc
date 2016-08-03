from . import BasicTask

class MixDataTask(BasicTask):
    """
    MixDataTask: Mix several input in one stream
    """
    __kernel = None # Kernel for this loader

    __inputKey = 'data' # Expected input key
    __language = None

    def __init__(self, name, initial_task=False):
        super(MixDataTask, self).__init__(name, initial_task)

    def execute(self, input):
        """
        Expected input:
        {'input1': ['str1', 'str2',....,'strN'],
         'input2': [('a', 'b'), ('b', 'r'), .... , ('z', 'a')],
         'input3': [{'keyToPick':'value-here', ....,'otherKey':'value'}],
         'metadata':{
           'input1': {'type': 'list', 'itemType': 'string'},
           'input1': {'type': 'list', 'item-type': 'tuple', 'index': 1},
           'input1': {'type': 'list', 'itemType': 'dict', 'key': 'keyToPick'},
         }
        }

        It returns a list of values.
        """
        try:
            assert(isinstance(input, dict))
            super(MixDataTask, self).execute(input)

            # Get the input keys
            inputKeys = [key for key in input.keys() if not key == 'metadata']
            print('keys', inputKeys)
            # Get metadata
            metadata = input.get('metadata', None)
            print('metadata', metadata)
            if metadata is None:
                raise Exception("Impossible to execute this task. Metadata is missing")

            temp = []
            for key in inputKeys:
                data = input.get(key, None)
                print('item %s' % key, data)
                if data is None:
                    continue

                # Get metadata for this key
                keyMetadata = metadata.get(key, None)
                print('metadata', keyMetadata)
                if keyMetadata is None:
                    continue

                if not isinstance(keyMetadata, dict):
                    continue

                typeInput = keyMetadata.get('type', None)
                itemType = keyMetadata.get('item-type', 'string')
                print(typeInput, itemType)
                if typeInput == 'list':
                    if itemType == 'tuple':
                        tupleIndex = keyMetadata.get('index', 0)
                        if not tupleIndex in [0,1]:
                            continue # Ignore this data
                        temp.extend([i[tupleIndex] for i in data])
                    elif itemType == 'dict':
                        dictKey = keyMetadata.get('key', None)
                        if dictKey is None:
                            continue
                        temp.extend( [ i.get(dictKey, None) for i in data ] )
                    elif itemType == 'string':
                        temp.extend(data)
                else:
                    continue

            output = [item for item in temp if not item is None]
            self.finish(data=output, failed=False, error=None)
        except:
            output = "Error Mixing the data"
            self.finish(data=None, failed=True, error=output)

        return self.getOutput()
