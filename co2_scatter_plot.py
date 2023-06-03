import co2_level_histogram as ch
import matplotlib.pyplot as plt

def fetch_co2_data():
    co2_level_df=ch.fetchco2data()
    return co2_level_df

def generate_co2_scatterplot(df):
    yr_data=df['Year']
    tot_data=df['Total']

    # Create scatter plot
    plt.scatter(yr_data,tot_data)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Total')
    plt.title('Scatter Plot for CO2 Level')

    # Display the plot
    plt.show()

def main():
    co2_df=fetch_co2_data()
    generate_co2_scatterplot(co2_df)

if __name__ == "__main__":
    main()