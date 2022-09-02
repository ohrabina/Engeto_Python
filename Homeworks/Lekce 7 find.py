def my_find(sekvence, hledat):
    for i, obj in enumerate(sekvence):
        if obj == hledat:
            return i
       
    return -1