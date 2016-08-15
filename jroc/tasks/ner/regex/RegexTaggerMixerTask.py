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

            # Retrieve the text analysis
            data = input.get(self.__inputKey, None)

            if data is None or not isinstance(data, dict):
                raise Exception("The input for RegexTaggerMixerTask was not available. Please that input of this task! ")

            # Retrieve the keys
            temp = {}
            keys = data.keys()
            for key in keys:
                taggerData = data.get(key)
                if not 'entity' in taggerData or not 'tags' in taggerData:
                    continue # Ignore this data
                entity = taggerData.get('entity')
                tags = taggerData.get('tags', [])
                if entity in temp:
                    temp[entity].extend(tags)
                else:
                    temp[entity] = tags

            result = []
            for key in temp.keys():
                keyTags = temp.get(key,[])
                keyTags = [tag.upper() for tag in keyTags]
                result.append({"entity": key.title(), "tags": list(set(keyTags))})

            output = result

            self.finish(data=output, failed=False, error=None)
        except:
            output = "Error mixing the results from several RegexTaggerTask"
            self.finish(data=None, failed=True, error=output)

        return self.getOutput()
