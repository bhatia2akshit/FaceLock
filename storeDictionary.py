import pickle

def store(dict):
    dictionary = {}
    try:
        dictionary = retrieve()
        dictionary.update(dict)

    except:
        dictionary.update(dict)
    pickle_out = open('./utilities/dict.pickle', 'wb')
    pickle.dump(dictionary, pickle_out)
    pickle_out.close()

def storeFolder(dict):
    dictionary = {}
    try:
        dictionary = retrieve()
        dictionary.update(dict)

    except:
        dictionary.update(dict)
    pickle_out = open('./utilities/folderdictionary.pickle', 'wb')
    pickle.dump(dictionary, pickle_out)
    pickle_out.close()

def retrieve():
    pickle_in=open('./utilities/dict.pickle','rb')
    dictionary=pickle.load(pickle_in)
    return dictionary

def findName(empCode):
    pickle_in = open('./utilities/dict.pickle', 'rb')
    try:
        dictionary = pickle.load(pickle_in)
        answer=dictionary[str(empCode)]
    except:
        answer='not'
    return answer


def findEmpCode(userName):
    pickle_in = open('./utilities/dict.pickle',
                     'rb')
    try:
        dictionary = pickle.load(pickle_in)
        #print dictionary.keys(), ' keys'

        #.value().index(str(userName))
        answer = dictionary.keys()[dictionary.values().index(str(userName))]

    except:
        answer = 'not'
    return answer


