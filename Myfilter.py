def myfilter(anyfunc, sequence):
    result =[]
    for item in sequence:
        if anyfunc(Item):
            result.append(item)
            return result