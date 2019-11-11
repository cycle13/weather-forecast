import pandas as pd
import package as pkg


class Cleaning:

    def __init__(self, src):
        self.src = src

    def reference_index(self):
        # filter the dataframe based on station number
        station = pkg.ProcessFunctions(self.src).get_column('STATION')
        unique = pkg.ProcessFunctions(station).get_unique()
        index = pkg.ProcessFunctions(station).get_index_unique(unique)
        return index

    def station_processing(self, index):
        # create one dataframe per station
        stations = pkg.ProcessFunctions(self.src).split_dataframes(index)
        # rename headers (e.g., from DATE to DATE_XXXXX (with XXXXX the station number)
        stations = [pkg.ProcessFunctions(station).rename_stations() for station in stations]
        # concatenate dataframes with dates along the Y axis and regular columns along the X axis
        stations = pkg.ProcessFunctions(stations).concatenate_stations()
        return stations

    def date_processing(self, index):
        # date
        date = pkg.ProcessFunctions(self.src).get_column('DATE')
        date = pkg.ProcessFunctions(date).split_dataframes(index)
        # consider the first dataframe
        date = date[0]
        date = [pkg.ProcessFunctions(d).remove_strip() for d in date]
        date = [pkg.ProcessFunctions(d).format_date() for d in date]
        
        return date #day, month, year

    def hour_processing(self, index):
        # hour
        hour = pkg.ProcessFunctions(self.src).get_column('HOUR')
        hour = pkg.ProcessFunctions(hour).split_dataframes(index)
        # consider the first dataframe
        hour = hour[0]
        return hour

        return hour


class Formatting:
    """Formats IO"""

    def __init__(self, src):
        self.src = src

    def to_dataframe(self):
        df = pkg.ProcessFunctions(self.src).read_csv()
        df = pkg.ProcessFunctions(df).rename_input_headers()
        return df

    def to_series(self, name):
        df = pd.Series(self.src, name=name)
        return df

    def to_concat_dataframe(self, year, month, day, hour):
        return pd.concat([year, month, day, hour, self.src], axis=1)
