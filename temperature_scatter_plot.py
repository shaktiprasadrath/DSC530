import matplotlib.pyplot as plt
import temperature_level_histogram as tmp
def fetch_temp_data():
    tmp_df=tmp.fetchtempdata()
    tmp_df=tmp_df.groupby('City')['AverageTemperature'].first().reset_index()
    tmp_df=tmp_df.nlargest(10, 'AverageTemperature') ## Fetching 10 records based on AverageTemperature
    return tmp_df

def generate_temp_scatterplot(df):
    yr_data=df['City']
    tot_data=df['AverageTemperature']

    # Create scatter plot
    plt.scatter(yr_data,tot_data)

    # Add labels and title
    plt.xlabel('City')
    plt.ylabel('AverageTemperature')
    plt.title('Scatter Plot for Temperature Level')

    # Display the plot
    plt.show()

def main():
    tmp_df=fetch_temp_data()
    generate_temp_scatterplot(tmp_df)

if __name__ == "__main__":
    main()