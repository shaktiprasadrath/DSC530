import numpy as np
import statistics as st
import disaster_histogram as dis
import rainfall_level_histogram as rain
import sea_level_histogram as sea
import temperature_level_histogram as temp
import co2_level_histogram as ch
class MMST:
    def calculateMean(self,df):
        return np.mean(df)

    def calculateMode(self,df):
        return st.mode(df)

    def calculateSpread(self,df):
        return st.variance(df)

    def calculateTail(self,df):
        mn=self.calculateMean(df)
        stdv=st.stdev(df)
        tail_threshold=10
        tail_values = [x for x in df if abs(x - mn) > tail_threshold*stdv]
        return tail_values

    def mmst_of_disaster_freq(self,obj):
        msg="Disaster Freq"
        df=dis.fetchingdisasterdata()
        dis_df=df['Total number of disaster']
        obj.printMMST(msg,obj,dis_df)

    def mmst_of_rainfall(self,obj):
        msg="Rainfall Level"
        df=rain.fetchrainfalldata()
        rain_df=df['9-year moving average']
        obj.printMMST(msg,obj,rain_df)

    def mmst_of_sea_level(self,obj):
        msg="Sea Level"
        df=sea.fetchsealeveldata()
        sea_df=df['TotalWeightedObservations']
        obj.printMMST(msg,obj,sea_df)

    def mmst_of_temp_level(self,obj):
        msg="Temperature Level"
        df=temp.fetchtempdata()
        df=df.dropna().reset_index(drop=True)
        temp_df=df['AverageTemperature']
        obj.printMMST(msg,obj,temp_df)

    def mmst_of_co2_level(self,obj):
        msg="C02 Level"
        df=ch.fetchco2data()
        co2_df=df['Total']
        obj.printMMST(msg,obj,co2_df)

    def printMMST(self,msg,obj,df):
        print(f"For {msg}, Mean is: {obj.calculateMean(df)}, Mode is: {obj.calculateMode(df)}, Spread is: {obj.calculateSpread(df)} and Tails is: {obj.calculateTail(df)} ")

def main():
    obj = MMST()
    obj.mmst_of_disaster_freq(obj)
    obj.mmst_of_rainfall(obj)
    obj.mmst_of_co2_level(obj)
    obj.mmst_of_sea_level(obj)
    obj.mmst_of_temp_level(obj)

if __name__ == "__main__":
    main()

