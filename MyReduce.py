def myreduce(anyfunc, sequence):
    result = sequence[0]
    for item in sequence[1:]:
        result = anyfunc(result, item)
