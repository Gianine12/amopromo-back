import math

def haversine(lat1,long1,lat2,long2):
    range_eart = 6371

    lat1Conv = convertLat_long(lat1)
    long1Conv = convertLat_long(long1)
    lat2Conv = convertLat_long(lat2)
    long2Conv = convertLat_long(long2)

    lat1,long1,lat2,long2 = map(math.radians, [lat1Conv,long1Conv,lat2Conv,long2Conv])

    latTot = lat2 - lat1
    longTot = long2 - long1

    distance = math.sin(latTot/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(longTot/2)**2
    res_dist = 2 * math.asin(math.sqrt(distance))

    return round(range_eart * res_dist,4)

def convertLat_long(value):
    graus = float(value)
    min_dec = abs(float(value) - graus) * 60
    min = float(min_dec)
    seg = (min_dec - min_dec) *60

    return graus+min+seg
