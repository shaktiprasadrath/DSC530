
import matplotlib.pyplot as plt
from ReadingData import ReadingData

def fetchco2data():
    readdata=ReadingData()
    df=readdata.readCO2data()
    return df

def gettinggroupbydata(df):
    df=df.groupby(['Year']).max().reset_index()
    return df

def generatehist(df):
    df['Year'].plot.hist(edgecolor='black')
    plt.xlabel('Year')
    plt.ylabel('Frequency')
    plt.title('Histogram of CO2 Level')
    plt.show()

def main():
    df1=fetchco2data()
    df2=gettinggroupbydata(df1)
    generatehist(df2)

if __name__ == "__main__":
    main()
