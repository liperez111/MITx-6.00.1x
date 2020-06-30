animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')



def how_many(aDict):
    counter = 0
    for e in aDict:
        counter += len(aDict[e])

    return counter




