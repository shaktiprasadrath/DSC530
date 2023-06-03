import numpy as np
import matplotlib.pyplot as plt
import sea_level_histogram as sea

def fetchdata():
    sae_level_df=sea.fetchsealeveldata()
    sae_level_df=sae_level_df['TotalWeightedObservations']
    return sae_level_df

def calculateCDF(sae_level_df):
    # Sort the sea level data in ascending order
    sorted_data = np.sort(sae_level_df)

    # Calculate the CDF
    cdf = np.cumsum(sorted_data) / np.sum(sorted_data)
    return sorted_data,cdf

def generateplot(sorted_data,cdf):
    # Plot the CDF
    plt.plot(sorted_data, cdf)
    plt.xlabel('Sea Level')
    plt.ylabel('Cumulative Probability')
    plt.title('Cumulative Distribution Function (CDF) of Sea Level')
    plt.show()

def calculate_percentile_rank(sea_level_data):

    # Sea level value for which percentile rank is calculated
    sea_level_value = 0.90

    # Calculate the percentile rank
    percentile_rank = np.percentile(sea_level_data, sea_level_value * 100)

    print("Percentile Rank:", percentile_rank)

def main():
    sea_data=fetchdata()
    sorted_data,cdf_data=calculateCDF(sea_data)
    generateplot(sorted_data,cdf_data)
    calculate_percentile_rank(sea_data)

if __name__ == "__main__":
    main()