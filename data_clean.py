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
# replace 'current_delimiter' with the delimiter in your txt file
def convert_txt_to_csv(input_filename, output_filename, current_delimiter=';', file_encoding='ISO-8859-1'):
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

# Make sure to replace 'path_to_your_large_input_file.txt' with the actual path to your text file
# Replace 'output_file_name.csv' with the desired output file name
# Adjust the delimiter and encoding as necessary
convert_txt_to_csv('path_to_your_large_input_file.txt', 'output_file_name.csv', ',', 'ISO-8859-1')


#Load and view the data
unclean_df = pd.read_csv('output_file_name.csv')
unclean_df.head(10)


# Display basic information and statistics
print(unclean_df.info())
print(unclean_df.describe())



