import pandas as pd

class ReadingData:

    def readCO2data(self):
        df=pd.read_csv('resources\CO2_emission.csv', usecols= ['Year','Total'])
        return df

    def readDisasterdata(self):
        df=pd.read_csv('resources\Frequency_of_natural_disaster.csv', usecols= ['Year','Total number of disaster'])
        return df
    def readRainfalldata(self):
        df=pd.read_csv('resources\\rainfall.csv', usecols= ['Year','9-year moving average'])
        return df
    def readSeaLeveldata(self):
        df=pd.read_csv('resources\sea_level.csv', usecols= ['Year','TotalWeightedObservations'])
        return df
    def readTempLeveldata(self):
        df=pd.read_csv('resources\\temp.csv', usecols= ['City','AverageTemperature'])
        return df

if __name__ == "__main__":
    obj = ReadingData()