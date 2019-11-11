import pandas as pd


class ProcessFunctions:
    def __init__(self, src):
        self.src = src

    def read_csv(self):
        """
        Returns a pandas dataframe.
        All the processing is conducted from a dataframe.
        """
        dataframe = pd.read_csv(self.src)
        return dataframe

    def rename_input_headers(self):
        """
        Translates norwegian to english header
        """
        output = self.src.copy()
        output = output.rename(columns={
            'DATO': 'DATE',
            'STNR': 'STATION',
            'HR': 'HOUR',
            'PO': 'PR',
            'TA': 'TAS',
            'UH': 'RH',
            'TD': 'DEW_POINT',
            'DD': 'WIND_DIRECTION',
            'FF': 'WIND_SPEED'})

        return output

    def get_column(self, variable):
        """
        Input: dataframe
        Output: series
        """
        return self.src[variable]

    def remove_strip(self):
        '''
        Requires to loop over the function and to store in list comprehension
        Input: string
        Output: string
        '''
        output = self.src.strip()
        return output

    def format_date(self):
        '''
        Requires to loop over the function and to store in list comprehension
        Input: string
        Output: string
        '''
        # from format DD-MMM-YY
        day = self.src[0:2]
        month = self.src[3:6]
        year = self.src[7:9]

        month = str(month)
        dict_month = {'JAN': '01', 'FEB': '02', 'MAR': '03', 'APR': '04',
                      'MAI': '05', 'JUN': '06', 'JUL': '07', 'AUG': '08',
                      'SEP': '09', 'OKT': '10', 'NOV': '11', 'DES': '12'}
        for key, value in dict_month.items():
            if month == key:
                month_num = value

        day = '{:2s}'.format(day)
        month = '{:2s}'.format(month_num)
        year = '20{:2s}'.format(year)

        return day, month, year

    def get_unique(self):
        '''
        Input: numpy array
        Output: array
        '''
        return pd.unique(self.src)

    def get_index_unique(self, reference):
        # src : list
        # reference: array with reference values to compare with src
        # takes the first element of the array to get the station index
        output = [self.src.index[self.src == ref][0] for ref in reference]
        return output

    def split_dataframes(self, index):
        '''
        Returns a list of dataframes per station
        '''
        # index corresponds to the unique station index list retrieved from get_index_unique_station()
        output = [self.src.iloc[index[i]:index[i+1]] for i in range(len(index)-1)]
        output = [o.reset_index(drop=True) for o in output]
        return output

    def rename_stations(self):
        output = self.src.copy()
        cols = output.columns
        station = self.src['STATION']
        station = str(station[0])
        string = cols + '_' + station
        # replace dataframe columns
        output.columns = string
        return output

    def concatenate_stations(self):
        output = self.src.copy()
        output = pd.concat([d for d in self.src], axis=1)
        return output
