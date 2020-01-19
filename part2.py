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
        return ''
    return x

if __name__ == '__main__':
    path = sys.argv[1]

    d = []
    for l in open(path + 'business.json').readlines():
        d.append(json.loads(l))  # from json str to dict
    df = pd.DataFrame.from_records(d)
    daz = df.query('state == ["AZ"]').city
    daz = daz.str.upper()  # account for different lettering
    daz = daz.dropna(axis=0)  # account for missing entries
    daz = daz.str.replace('NORTH|SOUTH|EAST|WEST', '', case=False).str.strip()  # account for directions and whitespace

    daz = daz.apply(lambda x: check_typos(x))   # account for any typos and change invalid cities to ''

    df.update(daz)

    # account for any invalid city names
    indices = df[(df.city == 'AZ') | (df.city == 'Arizona') | ((df.state == 'AZ') & (df.city == ''))].index
    df.drop(indices, inplace=True)

    print(df[df.state == 'AZ']['city'].unique())
    print(len(df[df.state == 'AZ']['city'].unique()))
