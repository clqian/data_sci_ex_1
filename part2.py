import sys
import json
import pandas as pd
import difflib as diff

def check_typos(x):
    cities = ['PHOENIX', 'GOODYEAR', 'GLENDALE', 'SCOTTSDALE', 'MESA', 'GILBERT', 'LITCHFIELD PARK', 'TEMPE', 'PEORIA',
              'CHANDLER', 'SURPRISE', 'BUCKEYE', 'QUEEN CREEK', 'AVONDALE', 'HIGLEY', 'CAVE CREEK', 'SUN CITY',
              'CAREFREE', 'EL MIRAGE', 'PARADISE VALLEY', 'LITCHFIELD', 'FOUNDTAIN HILLS', 'TOLLESON', 'SUN LAKES',
              'FORT MCDOWELL', 'APACHE JUNCTION', 'LAVEEN VILLAGE', 'FORT MCDOWELL', 'YOUNGTOWN', 'ANTHEM',
              'SOMERTON', 'GUADALUPE', 'VALLEYWIDE', 'RIO VERDE', 'LITCHFIELD PARK', 'WADDELL', 'PASADENA',
              'AHWATUKEE', 'SEDONA', 'APACHE TRAIL', 'RAINBOW VALLEY', 'QUEEN CREEK', 'RED ROCK', 'DESERT RIDGE',
              'ESTRELLA VILLAGE', 'MARICOPA', 'SUNNYSLOPE', 'SAN TAN', 'CENTRAL CITY VILLAGE', 'STETSON VALLEY',
              'FOUNTAIN HILLS', 'ARROWHEAD', 'TUCSON', 'GOODYEAR', 'RED MOUNTAIN', 'GREENWAY', 'CENTRAL']
    cities_set = set(cities)
    if x not in cities_set:
        n = diff.get_close_matches(x, cities)
        if n:
            return n[0]
    return x

if __name__ == '__main__':
    path = sys.argv[1]

    d = []
    for l in open(path + 'business.json').readlines():
        d.append(json.loads(l))  # from json str to dict
    df = pd.DataFrame.from_records(d)
    # daz = pd.Series([x.city] for x in df.state["AZ"])
    # daz = pd.Series([x.city] for x in df.query('state == ["AZ"]'))
    daz = df.query('state == ["AZ"]').city
    daz = daz.str.upper()  # account for different lettering
    daz = daz.dropna(axis=0)  # account for missing entries
    daz = daz.str.replace('NORTH|SOUTH|EAST|WEST', '', case=False).str.strip()  # account for directions and whitespace

    daz = daz.apply(lambda x: check_typos(x))

    # print(daz[0:10])
    print(len(daz))
    print(len(daz.unique()))

#     da = []
#     for business in df:
#       if df.state[business] == "AZ":
#         da.append(df.city[business]
#     print(daz)

    df.update(daz)
    print(df[df.state == 'AZ']['city'].unique())