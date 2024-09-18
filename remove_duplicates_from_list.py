def distinct(seq):
    # convert list into a dictionary as dictionary cannot contain duplicates
    seq =  list(dict.fromkeys(seq))
    return seq