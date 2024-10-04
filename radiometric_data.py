import pandas as pd
import numpy as np
import scipy.stats as stats
import geopandas as gpd
import folium
from folium.plugins import HeatMap
import seaborn as sns
import matplotlib.pyplot as plt

# Helper function to convert DMS to DD
def dms_to_dd(dms):
    # Split DMS into degrees, minutes, and seconds
    parts = dms.split()
    degrees = float(parts[0][:-1])
    minutes = float(parts[1][:-1])
    seconds = float(parts[2][:-1])
    direction = parts[3]
    
    # Convert to decimal degrees
    dd = degrees + (minutes / 60) + (seconds / 3600)
    
    # Adjust for direction
    if direction in ['S', 'W']:
        dd *= -1
    
    return dd

# Load the radiometric data
file_path = 'C://Users//Administration//Downloads//radiometric_data.xlsx'
radiometric_data = pd.read_excel(file_path, sheet_name=None)

# Load data from each sheet
ruirihills_data = radiometric_data['RUIRIHILLS']
gembehills_data = radiometric_data['GEMBEHILLS']

# Add a column indicating the source of the data
ruirihills_data['Hill'] = 'Ruirihills'
gembehills_data['Hill'] = 'Gembehills'

# Combine the data from both hills into a single DataFrame
combined_data = pd.concat([ruirihills_data, gembehills_data])

# Ensure Latitude and Longitude are converted to DD and are floats
combined_data['Latitude'] = combined_data['Latitude'].apply(dms_to_dd)
combined_data['Longitude'] = combined_data['Longitude'].apply(dms_to_dd)

# Print the first few rows to verify the conversion
print(combined_data.head())

# Calculate descriptive statistics for both datasets
ruirihills_stats = ruirihills_data.describe()
gembehills_stats = gembehills_data.describe()

print("Descriptive Statistics for Ruirihills:")
print(ruirihills_stats)
print("\nDescriptive Statistics for Gembehills:")
print(gembehills_stats)

# Visualization: Boxplot for Ionization Levels
plt.figure(figsize=(10, 6))
sns.boxplot(x='Hill', y='Gamma (nGy/h)', data=combined_data)
plt.title('Distribution of Gamma Ionization Levels')
plt.xlabel('Hill')
plt.ylabel('Gamma (nGy/h)')
plt.show()

# ANOVA test for ionization levels across different geographical regions (latitude clusters)
ruirihills_data['Latitude'] = combined_data[combined_data['Hill'] == 'Ruirihills']['Latitude']
gembehills_data['Latitude'] = combined_data[combined_data['Hill'] == 'Gembehills']['Latitude']

# Convert Latitude values to floats to ensure pd.cut works
ruirihills_data['Latitude'] = ruirihills_data['Latitude'].astype(float)
gembehills_data['Latitude'] = gembehills_data['Latitude'].astype(float)

ruirihills_data['Latitude_cluster'] = pd.cut(ruirihills_data['Latitude'], bins=3, labels=['Low', 'Medium', 'High'])
gembehills_data['Latitude_cluster'] = pd.cut(gembehills_data['Latitude'], bins=3, labels=['Low', 'Medium', 'High'])

# ANOVA test for Ruirihills
f_val_ruiri, p_val_ruiri = stats.f_oneway(
    ruirihills_data[ruirihills_data['Latitude_cluster'] == 'Low']['Gamma (nGy/h)'],
    ruirihills_data[ruirihills_data['Latitude_cluster'] == 'Medium']['Gamma (nGy/h)'],
    ruirihills_data[ruirihills_data['Latitude_cluster'] == 'High']['Gamma (nGy/h)']
)

# ANOVA test for Gembehills
f_val_gembe, p_val_gembe = stats.f_oneway(
    gembehills_data[gembehills_data['Latitude_cluster'] == 'Low']['Gamma (nGy/h)'],
    gembehills_data[gembehills_data['Latitude_cluster'] == 'Medium']['Gamma (nGy/h)'],
    gembehills_data[gembehills_data['Latitude_cluster'] == 'High']['Gamma (nGy/h)']
)

print(f"\nANOVA results for Ruirihills: F-value = {f_val_ruiri}, p-value = {p_val_ruiri}")
print(f"ANOVA results for Gembehills: F-value = {f_val_gembe}, p-value = {p_val_gembe}")

# Calculate correlation for both datasets, selecting only numeric columns
ruirihills_correlation = ruirihills_data.select_dtypes(include=[np.number]).corr()
gembehills_correlation = gembehills_data.select_dtypes(include=[np.number]).corr()

print("\nCorrelation Matrix for Ruirihills:")
print(ruirihills_correlation)
print("\nCorrelation Matrix for Gembehills:")
print(gembehills_correlation)

# Visualization: Correlation Matrix Heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(ruirihills_correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix for Ruirihills')
plt.show()

plt.figure(figsize=(12, 8))
sns.heatmap(gembehills_correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix for Gembehills')
plt.show()

# GIS Mapping for High Radioactivity Areas
# Load Kenya county boundaries shapefile and convert to GeoJSON (adjust path)
county_shapefile = 'C://Users//Administration//Downloads//110m_physical//ne_110m_geography_regions_elevation_points.shp'
county_gdf = gpd.read_file(county_shapefile)

# Create a base map
m = folium.Map(location=[combined_data['Latitude'].mean(), combined_data['Longitude'].mean()], zoom_start=10)

# Create a HeatMap layer
heat_data = [[row['Latitude'], row['Longitude'], row['Gamma (nGy/h)']] for index, row in combined_data.iterrows()]
HeatMap(heat_data).add_to(m)

# Add markers with labels for each data point
for idx, row in combined_data.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"Hill: {row['Hill']}\nGamma (nGy/h): {row['Gamma (nGy/h)']}",
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

# Optionally, overlay the shapefile if available
folium.GeoJson(county_gdf).add_to(m)  # Ensure you use county_gdf

# Save the map to an HTML file
m.save('radioactivity_heatmap_with_labels.html')
