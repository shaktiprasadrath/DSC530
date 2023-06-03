import matplotlib.pyplot as plt
from ReadingData import ReadingData

def fetchingdisasterdata():
    readdata=ReadingData()
    df=readdata.readDisasterdata()
    df=df.dropna().reset_index(drop=True)
    return df
def gettinggroupbydata(df):
    df=df.groupby(['Year']).max().reset_index()
    return df
def generatehist(df):
    df['Year'].plot.hist(edgecolor='black')
    plt.xlabel('Year')
    plt.ylabel('Frequency')
    plt.title('Histogram of Disaster frequency')
    plt.show()

def main():
    df1=fetchingdisasterdata()
    df2=gettinggroupbydata(df1)
    generatehist(df2)

if __name__ == "__main__":
    main()
