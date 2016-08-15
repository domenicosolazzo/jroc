from . import BasicTask

class RegexTaggerMixerTask(BasicTask):
    """
    RegexTaggerMixerTask: It mixes results from two or more RegexTaggerTask
    """
    __kernel = None # Kernel for this loader
    __inputKey = 'data' # Expected input key.

    def __init__(self, name, initial_task=False):
        super(RegexTaggerMixerTask, self).__init__(name, initial_task)
        self.__kernel = None


    def execute(self, input):
        """
        Execute a task
        """
        output = None
        try:
            assert(isinstance(input, dict))
            super(RegexTaggerMixerTask, self).execute(input)

            # Retrieve the input keys
            keys = input.keys()
            # Retrieve the keys
            temp = {}
            for key in keys:
                taggerData = input.get(key, None)
                # The data should be a list
                print("t", key, taggerData)
                if taggerData is None or not isinstance(taggerData, list):
                    continue # Ignore this data

                for taggerDataItem in taggerData:
                    print("item", taggerDataItem)
                    if not 'entity' in taggerDataItem or not 'tags' in taggerDataItem:
                        continue # Ignore this data

                    entity = taggerDataItem.get('entity')
                    tags = taggerDataItem.get('tags', [])
                    if entity in temp:
                        temp[entity].extend(tags)
                    else:
                        temp[entity] = tags
            print("temp", temp)
            result = []
            for key in temp.keys():
                keyTags = temp.get(key,[])
                keyTags = [tag.upper() for tag in keyTags]
                result.append({"entity": key.title(), "tags": list(set(keyTags))})
            print("result", result)
            output = result

            self.finish(data=output, failed=False, error=None)
        except:
            output = "Error mixing the results from several RegexTaggerTask"
            self.finish(data=None, failed=True, error=output)

        return self.getOutput()
