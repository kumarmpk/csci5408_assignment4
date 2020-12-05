import pandas as pd
import numpy as np

df = pd.read_csv("sudeste_original.csv")
df = df.head(300000)

wsidpair = df[['wsid', 'wsnm', 'inme']].copy()
wsidUniq = wsidpair.drop_duplicates(
    'wsid').reset_index().drop(['index'], axis=1)

wsidFact = df[['wsid']].copy().reset_index()

elvtPair = df[['elvt', 'lat', 'lon', 'city', 'prov']].copy()
elvtUniq = elvtPair.drop_duplicates(
    'elvt').reset_index().drop(['index'], axis=1)

elvtFact = df[['elvt']].copy().reset_index()

mdctFact = df[['mdct']].copy().reset_index()

mdctUniq = pd.DataFrame(df.mdct.unique(), columns=['mdct'])

yearFact = df[['yr']].copy().reset_index()

yrUniq = pd.DataFrame(df.yr.unique(), columns=['yr'])

moFact = df[['mo']].copy().reset_index()

moUniq = pd.DataFrame(df.mo.unique(), columns=['mo'])

daFact = df[['da']].copy().reset_index()

daUniq = pd.DataFrame(df.da.unique(), columns=['da'])

hrFact = df[['hr']].copy().reset_index()

hrUniq = pd.DataFrame(df.hr.unique(), columns=['hr'])

prcpFact = df[['prcp']].copy().reset_index()

prcpNoNan = pd.DataFrame(prcpFact.prcp.dropna())

prcpFactProcessed = prcpNoNan[~(prcpNoNan == 0).any(axis=1)]

prcpUniq = prcpFactProcessed.drop_duplicates(
    'prcp').reset_index().drop(['index'], axis=1)

stpPair = df[['stp', 'smax', 'smin']].copy()

stpNoNan = pd.DataFrame(stpPair.dropna())

stpFactProcessed = stpNoNan[~(stpNoNan == 0).any(axis=1)].reset_index()

stpUniq = pd.DataFrame(
    np.unique(stpFactProcessed[['stp', 'smax', 'smin']].values))
stpUniq.columns = ['stp']
stpUniq['index'] = stpUniq.index

rename_dict = stpUniq.set_index('stp').to_dict()['index']
stpFact = stpPair.replace(rename_dict)

gbrdFact = df[['gbrd']].copy()

gbrdNoNan = pd.DataFrame(gbrdFact.gbrd.dropna())

gbrdFactProcessed = gbrdNoNan[~(gbrdNoNan == 0).any(axis=1)]

gbrdUniq = gbrdFactProcessed.drop_duplicates(
    'gbrd').reset_index().drop(['index'], axis=1)

tempPair = df[['temp', 'tmax', 'tmin']].copy()

tmaxNoNan = pd.DataFrame(tempPair.dropna())

tmaxFactProcessed = tmaxNoNan[~(tmaxNoNan == 0).any(axis=1)].reset_index()

tmaxUniq = pd.DataFrame(
    np.unique(tmaxFactProcessed[['temp', 'tmax', 'tmin']].values))
tmaxUniq.columns = ['tmax']
tmaxUniq['index'] = tmaxUniq.index

rename_dict = tmaxUniq.set_index('tmax').to_dict()['index']
tmaxFact = tempPair.replace(rename_dict)

dwepPair = df[['dewp', 'dmax', 'dmin']].copy()

dewpNoNan = pd.DataFrame(dwepPair.dropna())

dewpFactProcessed = dewpNoNan[~(dewpNoNan == 0).any(axis=1)].reset_index()

dewpUniq = pd.DataFrame(
    np.unique(dewpFactProcessed[['dewp', 'dmax', 'dmin']].values))
dewpUniq.columns = ['dewp']
dewpUniq['index'] = dewpUniq.index

rename_dict = dewpUniq.set_index('dewp').to_dict()['index']
dwepFact = dwepPair.replace(rename_dict)

hmdyPair = df[['hmdy', 'hmax', 'hmin']].copy()

hmdyNoNan = pd.DataFrame(hmdyPair.dropna())

hmdyFactProcessed = hmdyNoNan[~(hmdyNoNan == 0).any(axis=1)].reset_index()

hmdyUniq = pd.DataFrame(
    np.unique(hmdyFactProcessed[['hmdy', 'hmax', 'hmin']].values))
hmdyUniq.columns = ['hmdy']
hmdyUniq['index'] = hmdyUniq.index

rename_dict = hmdyUniq.set_index('hmdy').to_dict()['index']
hmdyFact = hmdyPair.replace(rename_dict)

wdsp = df[['wdsp']].copy()
wdct = df[['wdct']].copy()
gust = df[['gust']].copy()

winddf = pd.concat([wdsp, wdct, gust], axis=1)

finadf = pd.concat([wsidFact, elvtFact, mdctFact, prcpFactProcessed, stpFact,
                    gbrdFactProcessed, tmaxFact, dwepFact, hmdyFact, wdsp, wdct, gust], axis=1)
finadf.drop(['index'], axis=1, inplace=True)


wsidUniq.to_csv('weather_station_dimension.csv')
elvtUniq.to_csv('location_dimension.csv')
mdctUniq.to_csv('datetime_dimension.csv')
yrUniq.to_csv('year_dimention.csv')
moUniq.to_csv('month_dimention.csv')
daUniq.to_csv('day_dimention.csv')
hrUniq.to_csv('hour_dimention.csv')
prcpUniq.to_csv('precipitation_dimention.csv')
stpUniq.to_csv('air_pressure_dimention.csv')
gbrdUniq.to_csv('solar_radiation_dimention.csv')
tmaxUniq.to_csv('temperature_dimention.csv')
dewpUniq.to_csv('dew_point_dimention.csv')
hmdyUniq.to_csv('humidity_dimention.csv')
finadf.to_csv('fact_table.csv')
winddf.to_csv('wind_dimension.csv')
