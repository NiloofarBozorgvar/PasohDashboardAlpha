import streamlit as st
import pandas as pd
import plotly.express as px

# Load the file
file_path = 'final_hectare_analysis_results/final_updated_result_1_12.csv'  # Replace with the actual path to your CSV file
data = pd.read_csv(file_path)

# Prepare the data for visualization
categories = data['Category'].unique()

# Create an empty DataFrame to store aggregated results
aggregated_data = pd.DataFrame()

# Aggregate data for each category
for category in categories:
    category_data = data[data['Category'] == category]

    # Initialize dictionaries to store summed data
    volume_sums = []
    carbon_stock_sums = []
    biomass_sums = []
    height_sums = []

    # Iterate through years and sum the data
    for year in range(1, 31):
        volume_sums.append(category_data[f'volume_year_{year}'].sum())
        carbon_stock_sums.append(category_data[f'carbon_stockyt_year_{year}'].sum())
        biomass_sums.append(category_data[f'biomassyt_year_{year}'].sum())
        height_sums.append(category_data[f'height_year_{year}'].sum())

    # Add to aggregated data
    aggregated_data = pd.concat([
        aggregated_data,
        pd.DataFrame({
            'Year': range(1, 31),
            'Volume': volume_sums,
            'Carbon Stock': carbon_stock_sums,
            'Biomass': biomass_sums,
            'Height': height_sums,
            'Category': category
        })
    ])

# Streamlit interface
st.title('Forest Data Visualization Over 30 Years')
st.markdown(
    "### Explore trends of Volume, Carbon Stock, Biomass, and Height across different categories over 30 years.")

# Category selection
selected_categories = st.multiselect('Select Categories to Display', categories, default=categories)

# Filter aggregated data based on selected categories
filtered_data = aggregated_data[aggregated_data['Category'].isin(selected_categories)]

# Create a layout for charts
col1, col2 = st.columns(2)

# Volume Chart
with col1:
    st.subheader('Volume Over 30 Years')
    fig_volume = px.line(
        filtered_data,
        x='Year',
        y='Volume',
        color='Category',
        labels={'Year': 'Year', 'Volume': 'Volume'},
        title='Volume Trends Over 30 Years',
        template='plotly_white'
    )
    fig_volume.update_layout(
        title={'x': 0.5},
        xaxis=dict(title='Year'),
        yaxis=dict(title='Volume'),
        legend=dict(title='Category', orientation='h', x=0.5, xanchor='center', y=-0.2)
    )
    st.plotly_chart(fig_volume, use_container_width=True)

# Carbon Stock Chart
with col2:
    st.subheader('Carbon Stock Over 30 Years')
    fig_carbon_stock = px.line(
        filtered_data,
        x='Year',
        y='Carbon Stock',
        color='Category',
        labels={'Year': 'Year', 'Carbon Stock': 'Carbon Stock'},
        title='Carbon Stock Trends Over 30 Years',
        template='plotly_white'
    )
    fig_carbon_stock.update_layout(
        title={'x': 0.5},
        xaxis=dict(title='Year'),
        yaxis=dict(title='Carbon Stock'),
        legend=dict(title='Category', orientation='h', x=0.5, xanchor='center', y=-0.2)
    )
    st.plotly_chart(fig_carbon_stock, use_container_width=True)

# Biomass Chart
with col1:
    st.subheader('Biomass Over 30 Years')
    fig_biomass = px.line(
        filtered_data,
        x='Year',
        y='Biomass',
        color='Category',
        labels={'Year': 'Year', 'Biomass': 'Biomass'},
        title='Biomass Trends Over 30 Years',
        template='plotly_white'
    )
    fig_biomass.update_layout(
        title={'x': 0.5},
        xaxis=dict(title='Year'),
        yaxis=dict(title='Biomass'),
        legend=dict(title='Category', orientation='h', x=0.5, xanchor='center', y=-0.2)
    )
    st.plotly_chart(fig_biomass, use_container_width=True)

# Height Chart
with col2:
    st.subheader('Height Over 30 Years')
    fig_height = px.line(
        filtered_data,
        x='Year',
        y='Height',
        color='Category',
        labels={'Year': 'Year', 'Height': 'Height'},
        title='Height Trends Over 30 Years',
        template='plotly_white'
    )
    fig_height.update_layout(
        title={'x': 0.5},
        xaxis=dict(title='Year'),
        yaxis=dict(title='Height'),
        legend=dict(title='Category', orientation='h', x=0.5, xanchor='center', y=-0.2)
    )
    st.plotly_chart(fig_height, use_container_width=True)
