import matplotlib.pyplot as plt
from ReadingData import ReadingData

def fetchtempdata():
    readdata=ReadingData()
    df=readdata.readTempLeveldata()
    return df

def gettinggroupbydata(df):
    df=df.groupby('City')['AverageTemperature'].max()
    return df

def generatehist(df):
    df.plot(kind='bar')
    plt.xlabel('City')
    plt.ylabel('Frequency')
    plt.title('Histogram of Temperature Level')
    plt.show()

def main():
    df1=fetchtempdata()
    df2=gettinggroupbydata(df1)
    generatehist(df2)

if __name__ == "__main__":
    main()