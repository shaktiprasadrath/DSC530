import matplotlib.pyplot as plt
from ReadingData import ReadingData

def fetchrainfalldata():
    readdata=ReadingData()
    df=readdata.readRainfalldata()
    return df

def gettinggroupbydata(df):
    df=df.groupby(['Year']).max().reset_index()
    return df

def geneartehist(df):
    df['Year'].plot.hist(edgecolor='black')
    plt.xlabel('Year')
    plt.ylabel('Frequency')
    plt.title('Histogram of Rainfall Level')
    plt.show()

def main():
    df1=fetchrainfalldata()
    df2=gettinggroupbydata(df1)
    geneartehist(df2)

if __name__ == "__main__":
    main()
