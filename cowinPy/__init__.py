from cowinPy import cowinApis


def getStates():
    return cowinApis.getStates()


def getDistricts(stateId):
    return cowinApis.getDistricts(stateId)