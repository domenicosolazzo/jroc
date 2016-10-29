from . import BasicTask

class NERFormatTask(BasicTask):
    """
    TaggerTask: It returns the tags given some POS tags
    """
    __kernel = None # Kernel for this loader
    __inputKey = 'data' # Expected input key.

    def __init__(self, name, initial_task=False):
        super(NERFormatTask, self).__init__(name, initial_task)


    def execute(self, input):
        """
        Execute a task
        """
        output = None
        try:
            assert(isinstance(input, dict))
            super(NERFormatTask, self).execute(input)

            entities = input.get('entities', [])
            stanford = input.get('entities-stanford', [])
            formattedEntities = {}
            formattedEntities['entities'] = entities
            formattedEntities['entities-stanford'] = stanford
            from sets import Set
            stanford_set = Set([entity[0] for index, entity in enumerate(stanford)])
            entities_set = Set(entities)

            difference = entities_set.difference_update(stanford_set)

            if len(stanford) > 0:
                temp = {}
                temp['OTHERS'] = list(entities_set)
                for index, entity in enumerate(stanford):
                    entityType = entity[1]
                    entityName = entity[0]
                    if entityType in temp:
                        if not entityName in temp[entityType]:
                            temp[entityType].append(entityName)
                    else:
                        temp[entityType] = [entityName]

                formattedEntities['entities-by-type'] = temp


            output = formattedEntities
            self.finish(data=output, failed=False, error=None)
        except:
            output = "Error retrieving the tags from a the POS tags"
            self.finish(data=None, failed=True, error=output)

        return self.getOutput()
