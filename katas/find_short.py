def find_short(s):
    x = s.split()
    x.sort(key=len)
    l = len(x[0])
    return l
find_short("bitcoin take over the world maybe who knows perhaps")                                                                                          
