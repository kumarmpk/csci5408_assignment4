import csv

location_list = []
location_id = 1

fact_table_list = []
fact_table_id = 1

weather_station_list = []

date_time_list = []
date_time_id = 1

year_list = []
month_list = []
date_list = []
hour_list = []

precipitation_list = []
precipitation_id = 1

air_pressure_list = []
air_pressure_id = 1

solar_radiation_list = []
solar_radiation_id = 1

temperature_list = []
temperature_id = 1

dew_point_temperature_list = []
dew_point_temperature_id = 1

relative_humidity_list = []
relative_humidity_id = 1

wind_list = []
wind_id = 1


def get_id(value, list, key):
    for record in list:
        if key in record and value == record[key]:
            return record['id']


def check_value(value, list, key):
    for record in list:
        if key in record and value == record[key]:
            return True


with open('dummy.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        print(fact_table_id)
        fact_table_dict = {}
        location_dict = {}
        if check_value(row['elvt'], location_list, 'elvt'):
            loc_id = get_id(row['elvt'], location_list, 'elvt')
            fact_table_dict['location_id'] = loc_id
        else:
            location_dict['id'] = location_id
            location_dict['elevation'] = row['elvt']
            location_dict['latitude'] = row['lat']
            location_dict['longitude'] = row['lon']
            location_dict['city'] = row['city']
            location_dict['province'] = row['prov']
            location_list.append(location_dict)
            fact_table_dict['location_id'] = location_id
            location_id = location_id + 1

        weather_station_dict = {}
        if check_value(row['wsid'], weather_station_list, 'wsid'):
            station_id = get_id(
                row['wsid'], weather_station_list, 'wsid')
            fact_table_dict['weather_station_id'] = station_id
        else:
            weather_station_dict['station_id'] = row['wsid']
            weather_station_dict['name'] = row['wsnm']
            weather_station_dict['number'] = row['inme']
            weather_station_list.append(weather_station_dict)
            fact_table_dict['weather_station_id'] = row['wsid']

        date_time_dict = {}
        date_time_dict['id'] = date_time_id
        date_time_dict['date_time'] = row['mdct']
        date_time_list.append(date_time_dict)
        fact_table_dict['date_time_id'] = date_time_id
        date_time_id = date_time_id + 1

        if row['yr'] not in year_list:
            year_list.append(row['yr'])

        if row['mo'] not in month_list:
            month_list.append(row['mo'])

        if row['da'] not in date_list:
            date_list.append(row['da'])

        if row['hr'] not in hour_list:
            hour_list.append(row['hr'])

        precipitation_dict = {}
        if check_value(row['prcp'], precipitation_list, 'prcp'):
            prec_id = get_id(row['prcp'], precipitation_list, 'prcp')
            fact_table_dict['precipitation_id'] = prec_id
        elif row['prcp'] != '' and row['prcp'] != 0:
            precipitation_dict['amt_preci'] = row['prcp']
            precipitation_dict['id'] = precipitation_id
            precipitation_list.append(precipitation_dict)
            fact_table_dict['precipitation_id'] = precipitation_id
            precipitation_id = precipitation_id + 1
        else:
            fact_table_dict['precipitation_id'] = ''

        solar_radiation_dict = {}
        if check_value(row['gbrd'], solar_radiation_list, 'gbrd'):
            rad_id = get_id(row['gbrd'], solar_radiation_list, 'gbrd')
            fact_table_dict['solar_radiation_id'] = rad_id
        elif row['gbrd'] != '' and row['gbrd'] != 0:
            solar_radiation_dict['solar_radiation'] = row['gbrd']
            solar_radiation_dict['id'] = solar_radiation_id
            solar_radiation_list.append(solar_radiation_dict)
            fact_table_dict['solar_radiation_id'] = solar_radiation_id
            solar_radiation_id = solar_radiation_id + 1
        else:
            fact_table_dict['solar_radiation_id'] = ''

        air_pressure_dict = {}
        if check_value(row['stp'], air_pressure_list, 'air_pressure'):
            air_press_id = get_id(
                row['stp'], air_pressure_list, 'air_pressure')
            fact_table_dict['air_pressure_id'] = air_press_id
        elif row['stp'] != '' and row['stp'] != 0:
            air_pressure_dict['air_pressure'] = row['stp']
            air_pressure_dict['id'] = air_pressure_id
            air_pressure_list.append(air_pressure_dict)
            fact_table_dict['air_pressure_id'] = air_pressure_id
            air_pressure_id = air_pressure_id + 1
        else:
            fact_table_dict['air_pressure_id'] = ''

        air_pressure_dict = {}
        if check_value(row['smax'], air_pressure_list, 'air_pressure'):
            air_press_id = get_id(
                row['smax'], air_pressure_list, 'air_pressure')
            fact_table_dict['max_air_pressure_id'] = air_press_id
        elif row['smax'] != '' and row['smax'] != 0:
            air_pressure_dict['air_pressure'] = row['smax']
            air_pressure_dict['id'] = air_pressure_id
            air_pressure_list.append(air_pressure_dict)
            fact_table_dict['max_air_pressure_id'] = air_pressure_id
            air_pressure_id = air_pressure_id + 1
        else:
            fact_table_dict['max_air_pressure_id'] = ''

        air_pressure_dict = {}
        if check_value(row['smin'], air_pressure_list, 'air_pressure'):
            air_press_id = get_id(
                row['smin'], air_pressure_list, 'air_pressure')
            fact_table_dict['min_air_pressure_id'] = air_press_id
        elif row['smin'] != '' and row['smin'] != 0:
            air_pressure_dict['air_pressure'] = row['smin']
            air_pressure_dict['id'] = air_pressure_id
            air_pressure_list.append(air_pressure_dict)
            fact_table_dict['min_air_pressure_id'] = air_pressure_id
            air_pressure_id = air_pressure_id + 1
        else:
            fact_table_dict['min_air_pressure_id'] = ''

        temperature_dict = {}
        if check_value(row['temp'], temperature_list, 'temperature'):
            temp_id = get_id(
                row['temp'], temperature_list, 'temperature')
            fact_table_dict['temperature_id'] = temp_id
        elif row['temp'] != '' and row['temp'] != 0:
            temperature_dict['temperature'] = row['temp']
            temperature_dict['id'] = temperature_id
            temperature_list.append(temperature_dict)
            fact_table_dict['temperature_id'] = temperature_id
            temperature_id = temperature_id + 1
        else:
            fact_table_dict['temperature_id'] = ''

        temperature_dict = {}
        if check_value(row['tmax'], temperature_list, 'temperature'):
            temp_id = get_id(
                row['tmax'], temperature_list, 'temperature')
            fact_table_dict['max_temperature_id'] = temp_id
        elif row['tmax'] != '' and row['tmax'] != 0:
            temperature_dict['temperature'] = row['tmax']
            temperature_dict['id'] = temperature_id
            temperature_list.append(temperature_dict)
            fact_table_dict['max_temperature_id'] = temperature_id
            temperature_id = temperature_id + 1
        else:
            fact_table_dict['temperature_id'] = ''

        temperature_dict = {}
        if check_value(row['tmin'], temperature_list, 'temperature'):
            temp_id = get_id(
                row['tmin'], temperature_list, 'temperature')
            fact_table_dict['min_temperature_id'] = temp_id
        elif row['tmin'] != '' and row['tmin'] != 0:
            temperature_dict['temperature'] = row['tmin']
            temperature_dict['id'] = temperature_id
            temperature_list.append(temperature_dict)
            fact_table_dict['min_temperature_id'] = temperature_id
            temperature_id = temperature_id + 1
        else:
            fact_table_dict['temperature_id'] = ''

        dew_point_temperature_dict = {}
        if check_value(row['dewp'], dew_point_temperature_list, 'dp_temperature'):
            temp_id = get_id(
                row['dewp'], dew_point_temperature_list, 'dp_temperature')
            fact_table_dict['dp_temperature_id'] = temp_id
        elif row['dewp'] != '' and row['dewp'] != 0:
            dew_point_temperature_dict['dp_temperature'] = row['dewp']
            dew_point_temperature_dict['id'] = dew_point_temperature_id
            dew_point_temperature_list.append(dew_point_temperature_dict)
            fact_table_dict['dp_temperature_id'] = dew_point_temperature_id
            dew_point_temperature_id = dew_point_temperature_id + 1
        else:
            fact_table_dict['dp_temperature_id'] = ''

        dew_point_temperature_dict = {}
        if check_value(row['dmax'], dew_point_temperature_list, 'dp_temperature'):
            temp_id = get_id(
                row['dmax'], dew_point_temperature_list, 'dp_temperature')
            fact_table_dict['dp_max_temperature_id'] = temp_id
        elif row['dmax'] != '' and row['dmax'] != 0:
            dew_point_temperature_dict['dp_temperature'] = row['dmax']
            dew_point_temperature_dict['id'] = dew_point_temperature_id
            dew_point_temperature_list.append(dew_point_temperature_dict)
            fact_table_dict['dp_max_temperature_id'] = dew_point_temperature_id
            dew_point_temperature_id = dew_point_temperature_id + 1
        else:
            fact_table_dict['dp_max_temperature_id'] = ''

        dew_point_temperature_dict = {}
        if check_value(row['dmin'], dew_point_temperature_list, 'dp_temperature'):
            temp_id = get_id(
                row['dmin'], dew_point_temperature_list, 'dp_temperature')
            fact_table_dict['dp_min_temperature_id'] = temp_id
        elif row['dmin'] != '' and row['dmin'] != 0:
            dew_point_temperature_dict['dp_temperature'] = row['dmin']
            dew_point_temperature_dict['id'] = dew_point_temperature_id
            dew_point_temperature_list.append(dew_point_temperature_dict)
            fact_table_dict['dp_min_temperature_id'] = dew_point_temperature_id
            dew_point_temperature_id = dew_point_temperature_id + 1
        else:
            fact_table_dict['dp_min_temperature_id'] = ''

        relative_humidity_dict = {}
        if check_value(row['hmdy'], relative_humidity_list, 'relative_humidity'):
            temp_id = get_id(
                row['hmdy'], relative_humidity_list, 'relative_humidity')
            fact_table_dict['relative_humidity_id'] = temp_id
        elif row['hmdy'] != '' and row['hmdy'] != 0:
            relative_humidity_dict['relative_humidity'] = row['hmdy']
            relative_humidity_dict['id'] = relative_humidity_id
            relative_humidity_list.append(relative_humidity_dict)
            fact_table_dict['relative_humidity_id'] = relative_humidity_id
            relative_humidity_id = relative_humidity_id + 1
        else:
            fact_table_dict['relative_humidity_id'] = ''

        relative_humidity_dict = {}
        if check_value(row['hmax'], relative_humidity_list, 'relative_humidity'):
            temp_id = get_id(
                row['hmax'], relative_humidity_list, 'relative_humidity')
            fact_table_dict['max_relative_humidity_id'] = temp_id
        elif row['hmax'] != '' and row['hmax'] != 0:
            relative_humidity_dict['relative_humidity'] = row['hmax']
            relative_humidity_dict['id'] = relative_humidity_id
            relative_humidity_list.append(relative_humidity_dict)
            fact_table_dict['max_relative_humidity_id'] = relative_humidity_id
            relative_humidity_id = relative_humidity_id + 1
        else:
            fact_table_dict['max_relative_humidity_id'] = ''

        relative_humidity_dict = {}
        if check_value(row['hmin'], relative_humidity_list, 'relative_humidity'):
            temp_id = get_id(
                row['hmin'], relative_humidity_list, 'relative_humidity')
            fact_table_dict['min_relative_humidity_id'] = temp_id
        elif row['hmin'] != '' and row['hmin'] != 0:
            relative_humidity_dict['relative_humidity'] = row['hmin']
            relative_humidity_dict['id'] = relative_humidity_id
            relative_humidity_list.append(relative_humidity_dict)
            fact_table_dict['min_relative_humidity_id'] = relative_humidity_id
            relative_humidity_id = relative_humidity_id + 1
        else:
            fact_table_dict['min_relative_humidity_id'] = ''

        wind_dict = {}
        wind_dict['speed'] = row['wdsp']
        wind_dict['direction'] = row['wdct']
        wind_dict['gust'] = row['gust']
        wind_dict['id'] = wind_id
        wind_list.append(wind_dict)
        fact_table_dict['wind_id'] = wind_id
        wind_id = wind_id + 1

        fact_table_list.append(fact_table_dict)
        fact_table_id = fact_table_id + 1

headers = fact_table_list[0].keys()
with open('fact_table.csv', 'w', newline='') as fact_table:
    writer = csv.DictWriter(fact_table, headers)
    writer.writeheader()
    writer.writerows(fact_table_list)

headers = location_list[0].keys()
with open('location_dimention.csv', 'w', newline='') as location_table:
    writer = csv.DictWriter(location_table, headers)
    writer.writeheader()
    writer.writerows(location_list)

headers = weather_station_list[0].keys()
with open('weation_station_dimention.csv', 'w', newline='') as weather_station_table:
    writer = csv.DictWriter(weather_station_table, headers)
    writer.writeheader()
    writer.writerows(weather_station_list)

headers = date_time_list[0].keys()
with open('date_time_dimention.csv', 'w', newline='') as date_time_table:
    writer = csv.DictWriter(date_time_table, headers)
    writer.writeheader()
    writer.writerows(date_time_list)

with open('year_dimention.csv', 'w', newline='') as year_table:
    writer = csv.writer(year_table)
    writer.writerow(['year'])
    writer.writerows([year_list])

with open('month_dimention.csv', 'w', newline='') as month_table:
    writer = csv.writer(month_table)
    writer.writerow(['month'])
    writer.writerows([month_list])

with open('date_dimention.csv', 'w', newline='') as date_table:
    writer = csv.writer(date_table)
    writer.writerow(['date'])
    writer.writerows([date_list])

with open('hour_dimention.csv', 'w', newline='') as hour_table:
    writer = csv.writer(hour_table)
    writer.writerow(['hour'])
    writer.writerows([hour_list])

if len(precipitation_list) > 0:
    headers = precipitation_list[0].keys()
    with open('precipitation_dimention.csv', 'w', newline='') as precipitation_table:
        writer = csv.DictWriter(precipitation_table, headers)
        writer.writeheader()
        writer.writerows(precipitation_list)

if len(solar_radiation_list) > 0:
    headers = solar_radiation_list[0].keys()
    with open('solar_radiation_dimention.csv', 'w', newline='') as solar_radiation_table:
        writer = csv.DictWriter(solar_radiation_table, headers)
        writer.writeheader()
        writer.writerows(solar_radiation_list)

headers = air_pressure_list[0].keys()
with open('air_pressure_dimention.csv', 'w', newline='') as air_pressure_table:
    writer = csv.DictWriter(air_pressure_table, headers)
    writer.writeheader()
    writer.writerows(air_pressure_list)

headers = temperature_list[0].keys()
with open('temperature_dimention.csv', 'w', newline='') as temperature_table:
    writer = csv.DictWriter(temperature_table, headers)
    writer.writeheader()
    writer.writerows(temperature_list)

headers = relative_humidity_list[0].keys()
with open('relative_humidity_dimention.csv', 'w', newline='') as relative_humidity_table:
    writer = csv.DictWriter(relative_humidity_table, headers)
    writer.writeheader()
    writer.writerows(relative_humidity_list)

headers = wind_list[0].keys()
with open('wind_dimention.csv', 'w', newline='') as wind_table:
    writer = csv.DictWriter(wind_table, headers)
    writer.writeheader()
    writer.writerows(wind_list)
