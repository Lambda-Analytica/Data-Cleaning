# Core imports
import csv
import numpy as np
import pandas as pd
import scipy as sc
from datetime import datetime
from collections import Counter
import statistics

# Visualization imports
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import geopandas as gpd

# Statistical and modeling imports
from scipy.stats import norm
from sklearn import linear_model
import statsmodels.formula.api as sm

# IPython configuration for inline plots
%matplotlib inline
plt.rcParams['figure.figsize'] = (10, 6)


#convert .txt to .csv
def convert_txt_to_csv(input_filename, output_filename, current_delimiter=';', file_encoding='ISO-8859-1'):
    import csv
    
    # Open the input file and the output file with the specified encoding
    with open(input_filename, 'r', encoding=file_encoding) as infile, \
         open(output_filename, 'w', newline='', encoding='utf-8') as outfile:
        
        # Create a CSV writer object which will write to the output file with commas as delimiters
        writer = csv.writer(outfile, delimiter=',')
        
        # Read each line from the input file
        for line in infile:
            # Split the line into fields using the current delimiter
            line_fields = line.split(current_delimiter)
            # Write the fields as a row in the CSV file
            writer.writerow(line_fields)

# Specify your input file, output file, the current delimiter, and possibly the encoding
convert_txt_to_csv('Dinex_HCV_VIO_forecast_2023_2033.txt', 'Dinex_HCV_VIO_forecast_2023_2033.csv', ';', 'ISO-8859-1')  # Adjust encoding as needed



#Load and view the data
unclean_df = pd.read_csv('output_file_name.csv')
unclean_df.head(10)


# Display basic information and statistics
print(unclean_df.info())
print(unclean_df.describe())

# Get all unique values from the 'SOS (TecDoc)' column
unique_values = unclean_df['SOS (TecDoc)'].unique()

# Print the unique values
#print(unique_values_sos)

# If you want to further inspect or manipulate the unique values, you can convert them to a list
unique_values_list = list(unique_values)
print(unique_values_list)

# Data type conversions
num_columns_to_convert = [
    "Global Sales Price Class",
    "K-Typ",
    "N-Typ",
    "TecDoc Engine Number",
    "Count_2023",
    "Count_2024",
    "Count_2025",
    "Count_2026",
    "Count_2027",
    "Count_2028",
    "Count_2029",
    "Count_2030",
    "Count_2031",
    "Count_2032",
    "Count_2033"
]
for column in num_columns_to_convert:
    unclean_df[column] = pd.to_numeric(unclean_df[column], errors='coerce')

str_columns_to_convert = [
    "Country/Territory",
    "ISO-Code",
    "Global Sales Segment",
    "Global Sales Sub-Segment",
    "Global Sales Price Class",
    "MHCV Segmentation",
    "Registration Type",
    "Make Group",
    "Make",
    "Model Group",
    "Model",
    "Model-short",
    "Body Group",
    "Body Type",
    "Fuel Type",
    "Cylinder Conf.",
    "Fuel System Type text (TecDoc)",
    "Engine Code",
    "Age"
]
for column in str_columns_to_convert:
    unclean_df[column] = unclean_df[column].astype(str)

# convert to datetime
#conversion function for 'last available date' column
def convert_last_available_date(date_str):
    try:
        return pd.to_datetime(date_str, format='%m/%Y')
    except:
        return pd.NaT

#conversion function for 'year of first registration' column
def convert_year_of_first_registration(year):
    try:
        return pd.to_datetime(year, format='%Y')
    except:
        return pd.NaT

#conversion function for 'TecDoc' columns
def convert_tecdoc(date_str):
    try:
        return pd.to_datetime(date_str, format='%Y%m')
    except:
        return pd.NaT

# Apply conversion functions to DataFrame
unclean_df['Last Available Date'] = unclean_df['Last Available Date'].apply(convert_last_available_date)
unclean_df['Year of first registration'] = unclean_df['Year of first registration'].apply(convert_year_of_first_registration)
unclean_df['SOS (TecDoc)'] = unclean_df['SOS (TecDoc)'].apply(convert_tecdoc)
unclean_df['EOS (TecDoc)'] = unclean_df['EOS (TecDoc)'].apply(convert_tecdoc)

# Print the updated DataFrame
unclean_df.head(20)


