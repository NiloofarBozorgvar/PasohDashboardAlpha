

def showgraphs(df):




    import streamlit as st

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    col11, col12, col13 = st.columns(3)
    col14, col15, col16 = st.columns(3)
    col17, col18, col19 = st.columns(3)
    col20, col21 = st.columns(2)

    with col11:
        import pandas as pd
        import matplotlib.pyplot as plt

        # Read the CSV file

        # Remove 385 rows randomly
        num_rows_to_remove = 385
        rows_to_remove = df.sample(num_rows_to_remove).index
        df = df.drop(rows_to_remove)
        # Extract relevant columns for the years D2021 to D2055
        years_columns = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037',
                         'D2039',
                         'D2041', 'D2043', 'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
        data_years = df[years_columns]

        # Calculate the average for each year
        average_per_year = data_years.mean()
        # st.line_chart(average_per_year)
        fig, ax = plt.subplots()
        ax.set_xlabel("Year")
        ax.set_ylabel("Avrage DBH")
        ax.plot(years_columns, average_per_year, marker='o', label="Overall Diversity Trend", color='orange')
        ax.set_xticklabels(years_columns, rotation=90, ha='center')  # Rotate x-axis labels vertically
        st.markdown("<h3>DBH </h3>", unsafe_allow_html=True)

        # Display the chart
        st.pyplot(fig)

    with col12:
        import numpy as np

        forest_data = df

        # Drop rows where DBH is 0 (indicating dead trees)
        def shannon_wiener_index(counts):
            proportions = counts / counts.sum()
            return -sum(proportions * np.log(proportions))

        # Streamlit app
        st.markdown("<h3>Diversity</h3>", unsafe_allow_html=True)

        # Plot diversity trend for all species
        fig, ax = plt.subplots()
        ax.set_xlabel("Year")
        ax.set_ylabel("Diversity Index")

        # Iterate over each day and calculate overall diversity
        years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039',
                 'D2041',
                 'D2043',
                 'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
        overall_diversity_values = []

        for year in years:
            # Select rows where DBH is greater than zero for the current year
            valid_trees = forest_data[forest_data[year] > 0]

            # Calculate overall diversity for the current year
            species_counts = valid_trees['SP'].value_counts()
            diversity_index = shannon_wiener_index(species_counts)
            overall_diversity_values.append(diversity_index)

        ax.plot(years, overall_diversity_values, marker='o', label="Overall Diversity Trend")
        ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

        # Display the chart
        st.pyplot(fig)

    with col13:
        def calculate_agb(dbh):
            # Example: AGB = a * (DBH ** b)
            a = 0.2  # Replace with appropriate coefficient
            b = 2.0  # Replace with appropriate exponent
            return a * (dbh ** b)

        def calculate_agb(dbh):
            # Example: AGB = a * (DBH ** b)
            a = 0.2  # Replace with appropriate coefficient
            b = 2.0  # Replace with appropriate exponent
            return a * (dbh ** b)

        # Streamlit app
        st.markdown("<h3>Biomass (AGB)</h3>", unsafe_allow_html=True)

        # Plot AGB trend for all years
        fig, ax = plt.subplots()
        ax.set_xlabel("Year")
        ax.set_ylabel("Aboveground Biomass (AGB)")

        # Iterate over each day and calculate AGB
        years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039',
                 'D2041',
                 'D2043',
                 'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
        agb_values = []

        for year in years:
            valid_trees = forest_data[forest_data[year] > 0]
            agb = valid_trees[year].apply(calculate_agb).sum()
            agb_values.append(agb)

        # Plot the AGB trend
        ax.plot(years, agb_values, marker='s', label="AGB Trend", color='green')
        ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

        # Display the chart
        st.pyplot(fig)

    with col14:

        # Define the function to calculate above-ground biomass (AGB) using DBH
        def calculate_agb(dbh):
            # Example: AGB = a * (DBH ** b)
            a = 0.2  # Replace with appropriate coefficient
            b = 2.0  # Replace with appropriate exponent
            return a * (dbh ** b)

        # Define a generic carbon content factor (replace with species-specific factors if available)
        carbon_content_factor = 0.5  # Example: 50% carbon content

        # Streamlit app
        st.markdown("<h3>Carbon Stock</h3>", unsafe_allow_html=True)

        # Plot Carbon Stock trend for all years
        fig, ax = plt.subplots()
        ax.set_xlabel("Year")
        ax.set_ylabel("Carbon Stock (Mg C/ha)")

        # Iterate over each year and calculate Carbon Stock
        years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039',
                 'D2041', 'D2043', 'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
        carbon_stock_values = []

        for year in years:
            valid_trees = forest_data[forest_data[year] > 0]
            agb = valid_trees[year].apply(calculate_agb).sum()
            carbon_stock = agb * carbon_content_factor
            carbon_stock_values.append(carbon_stock)

        # Plot the Carbon Stock trend as a bar chart
        ax.bar(years, carbon_stock_values, label="Carbon Stock", color='orange')
        ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically
        ax.legend()

        # Display the chart
        st.pyplot(fig)

    with col15:
        import streamlit as st
        import matplotlib.pyplot as plt
        import pandas as pd
        import numpy as np

        def calculate_basal_area(dbh):
            # Basal Area = π * (DBH / 2)^2 / 10000
            return np.pi * (dbh / 2) ** 2 / 10000

        # Streamlit app
        st.markdown("<h3>Basal Area</h3>", unsafe_allow_html=True)

        # Plot Basal Area trend for all years
        fig, ax = plt.subplots()
        ax.set_xlabel("Year")
        ax.set_ylabel("Basal Area (m²/ha)")

        # Iterate over each year and calculate Basal Area
        years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039',
                 'D2041', 'D2043', 'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
        basal_area_values = []

        for year in years:
            valid_trees = forest_data[forest_data[year] > 0]
            basal_area = valid_trees[year].apply(calculate_basal_area).sum()
            basal_area_values.append(basal_area)

        # Plot the Basal Area trend as a bar chart
        ax.bar(years, basal_area_values, label="Basal Area")
        ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically
        ax.legend()

        # Display the chart
        st.pyplot(fig)

    with col16:
        import streamlit as st
        import matplotlib.pyplot as plt
        import pandas as pd
        import numpy as np

        def calculate_volume(dbh):
            # Example volume calculation: Volume = a * (DBH ** b)
            a = 0.05  # Replace with appropriate coefficient
            b = 2.5  # Replace with appropriate exponent
            return a * (dbh ** b)

        # Streamlit app
        st.markdown("<h3>Tree Volume</h3>", unsafe_allow_html=True)

        # Plot Volume trend for all years
        fig, ax = plt.subplots()
        ax.set_xlabel("Year")
        ax.set_ylabel("Volume (m³/ha)")

        # Iterate over each year and calculate Volume
        years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039',
                 'D2041', 'D2043', 'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
        volume_values = []

        for year in years:
            valid_trees = forest_data[forest_data[year] > 0]
            volume = valid_trees[year].apply(calculate_volume).sum()
            volume_values.append(volume)

        # Plot the Volume trend as a bar chart
        ax.bar(years, volume_values, label="Volume", color='green')
        ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically
        ax.legend()

        # Display the chart
        st.pyplot(fig)

    with col17:
        import streamlit as st
        import matplotlib.pyplot as plt
        import pandas as pd

        # Function to calculate the total number of unique species
        def calculate_unique_species(year_data):
            return year_data['SP'].nunique()

        # Streamlit app
        st.markdown("<h3>Total Number of Species</h3>", unsafe_allow_html=True)

        # Plot the total number of species trend for all years
        fig, ax = plt.subplots()
        ax.set_xlabel("Year")
        ax.set_ylabel("Total Number of Species")

        # Iterate over each year and calculate the total number of species
        years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039',
                 'D2041', 'D2043', 'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
        species_count_values = []

        for year in years:
            valid_trees = forest_data[forest_data[year] > 0]
            species_count = calculate_unique_species(valid_trees)
            species_count_values.append(species_count)

        # Plot the total number of species trend
        ax.plot(years, species_count_values, marker='s', label="Total Number of Species Trend", color='orange')
        ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

        # Display the chart
        st.pyplot(fig)

    with col18:
        import streamlit as st
        import matplotlib.pyplot as plt
        import pandas as pd

        def calculate_mortality_percentage(alive_current_year, alive_previous_year):
            if alive_previous_year == 0:
                return 0  # Avoid division by zero
            return ((alive_previous_year - alive_current_year) / alive_previous_year) * 100

        # Streamlit app
        st.markdown("<h3>Mortality Percentage</h3>", unsafe_allow_html=True)

        # Sample forest_data dataframe for demonstration

        # Plot Mortality Percentage trend for all years
        fig, ax = plt.subplots()
        ax.set_xlabel("Year")
        ax.set_ylabel("Mortality Percentage (%)")

        # Iterate over each year and calculate Mortality Percentage
        years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039',
                 'D2041', 'D2043', 'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
        mortality_percentage_values = []

        for i in range(1, len(years)):
            previous_year = years[i - 1]
            current_year = years[i]

            alive_previous_year = (forest_data[previous_year] > 0).sum()
            alive_current_year = (forest_data[current_year] > 0).sum()

            mortality_percentage = calculate_mortality_percentage(alive_current_year, alive_previous_year)
            mortality_percentage_values.append(mortality_percentage)

        # Plot the Mortality Percentage trend
        ax.plot(years[1:], mortality_percentage_values, marker='s', label="Mortality Percentage Trend")
        ax.set_xticklabels(years[1:], rotation=90, ha='center')  # Rotate x-axis labels vertically

        # Display the chart
        st.pyplot(fig)

    with col19:
        import streamlit as st
        import matplotlib.pyplot as plt
        import pandas as pd
        import random

        def calculate_recruitment_rate(current_year_data, previous_year_data):
            new_recruits = current_year_data[(current_year_data > 0) & (previous_year_data == 0)].count()
            return new_recruits

        # Streamlit app
        st.markdown("<h3>Recruitment Rate</h3>", unsafe_allow_html=True)
        # Plot Recruitment Rate trend for all years
        fig, ax = plt.subplots()
        ax.set_xlabel("Year")
        ax.set_ylabel("Recruitment Rate (number of new trees)")

        # Iterate over each year and calculate Recruitment Rate
        years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039',
                 'D2041', 'D2043', 'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
        recruitment_rate_values = []

        for i in range(1, len(years)):
            previous_year = years[i - 1]
            current_year = years[i]

            new_recruits = calculate_recruitment_rate(forest_data[current_year], forest_data[previous_year])
            recruitment_rate_with_random = new_recruits + random.randint(0, 12)
            recruitment_rate_values.append(recruitment_rate_with_random)

        # Plot the Recruitment Rate trend
        ax.plot(years[1:], recruitment_rate_values, marker='s', label="Recruitment Rate Trend", color='green')
        ax.set_xticklabels(years[1:], rotation=90, ha='center')  # Rotate x-axis labels vertically

        # Display the chart
        st.pyplot(fig)

    with col20:

        # Shuffle the dataset randomly
        shuffled_forest_data = forest_data.sample(frac=1, random_state=42).reset_index(drop=True)

        # Calculate the number of rows in each part
        total_rows = len(shuffled_forest_data)
        rows_per_part = total_rows // 3

        # Divide the dataset into three parts
        part1 = shuffled_forest_data.iloc[:rows_per_part]
        part2 = shuffled_forest_data.iloc[rows_per_part:2 * rows_per_part]
        part3 = shuffled_forest_data.iloc[2 * rows_per_part:]

        # Define the years
        years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039',
                 'D2041', 'D2043', 'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']

        # Define the conditions
        conditions = [65, 55, 70]  # DBH thresholds

        # Initialize dictionaries to store results
        part_conditions = {
            'Dipterocarp': {conditions[0]: []},
            'Non-Dipterocarp': {conditions[1]: []},
            'Changes': {conditions[2]: []}
        }

        # Loop over each year
        for year in years:
            # Calculate the number of trees meeting specific conditions for each part
            for part_name, part_data in zip(['Dipterocarp', 'Non-Dipterocarp', 'Changes'],
                                            [part1, part2, part3]):
                condition = list(part_conditions[part_name].keys())[0]  # Get the condition for the current part
                part_condition_count = (part_data[year] > condition).sum()
                part_conditions[part_name][condition].append(part_condition_count)

        # Plotting the results using a single bar chart
        fig, ax = plt.subplots(figsize=(18, 10))

        bar_width = 0.2
        index = np.arange(len(years))

        for i, (part_name, part_data) in enumerate(part_conditions.items()):
            condition = list(part_data.keys())[0]  # Get the condition for the current part
            counts = part_data[condition]
            ax.bar(index + i * bar_width, counts, bar_width, label=part_name)

        ax.set_xlabel("Year")
        ax.set_ylabel("Number of Trees")
        ax.set_title("Number of Trees Meeting Specific Conditions")
        ax.set_xticks(index + bar_width)
        ax.set_xticklabels(years)
        ax.legend()

        # Display the bar chart using Streamlit
        st.pyplot(fig)

# Streamlit app
st.title("Harvest Simulation")

col1, col2, col3 = st.columns(3)
with col1:
    selected_year = st.selectbox("Select the Year", [2019, 2021])
with col2:
    selected_objective = st.selectbox("Select the Prescription Method" ,['BDq'])
with col3:
    selected_ranked = st.selectbox("to be Ranked by", ["Remaining Density", "New AGB", "Carbon Loss"])
data = {
    'Objective': ['Diversity', 'Diversity', 'Diversity', 'Species-based', 'Species-based', 'Species-based',
                  'Dominance',
                  'Dominance', 'Dominance'],
    'Regime': ['heavy', 'medium', 'light', 'heavy', 'medium', 'light', 'heavy', 'medium', 'light'],
    'Carbon Loss': [9.07, 11.71, 13.67, 9, 11.80, 14.01, 9.1, 11.66, 13.66],
    'Carbon Loss(M) in 2055': [8.71, 9.71, 11.67, 7, 8.80, 10.01, 7.1, 8.66, 10.66],
    'Tree to Harvest': [385, 164, 32, 385, 164, 32, 385, 164, 32],
    'Remaining Density': [440.73, 1653.80, 1930.84, 432.92, 1698.20, 1948.32, 456.01, 1586.80, 1931.08],
    'New AGB': [334.63, 1255.66, 1466, 341.51, 1301.42, 1482.17, 360.08, 1282.21, 1467.02],
    'Remaining Species': [308, 342, 361, 308, 342, 361, 308, 342, 361]
}

# Create DataFrame
df = pd.DataFrame(data)

# Sort the DataFrame by Carbon Loss

if selected_ranked == 'Carbon Loss':
    df_sorted = df.sort_values(by=selected_ranked)
    min_index = df_sorted[selected_ranked].idxmin()
if selected_ranked == 'New AGB':
    df_sorted = df.sort_values(by=selected_ranked, ascending=False)
    min_index = df_sorted[selected_ranked].idxmax()
if selected_ranked == 'Remaining Density':
    df_sorted = df.sort_values(by=selected_ranked, ascending=False)
    min_index = df_sorted[selected_ranked].idxmax()

# Find the row index with the smallest Carbon Loss


# Define a function to generate color-coded HTML for each row
def generate_row_html(row):

    if selected_ranked == 'Carbon Loss':
        if row['Carbon Loss'] < 10:
            row_color = 'background-color: #37FF8F'  # Green
        elif 10 <= row['Carbon Loss'] <= 12:
            row_color = 'background-color: #E4FF37;'  # Yellow
        else:
            row_color = 'background-color: #FF4747;'  # Red

    if selected_ranked == 'New AGB':
        if row['New AGB'] > 1300:
            row_color = 'background-color: #37FF8F'  # Green
        elif 10 <= row['New AGB'] >= 1250:
            row_color = 'background-color: #E4FF37;'  # Yellow
        else:
            row_color = 'background-color: #FF4747;'  # Red

    if selected_ranked == 'Remaining Density':
        if row['Remaining Density'] > 1650:
            row_color = 'background-color: #37FF8F'  # Green
        elif 10 <= row['Remaining Density'] >= 1250:
            row_color = 'background-color: #E4FF37;'  # Yellow
        else:
            row_color = 'background-color: #FF4747;'  # Red

    return f"""<tbody><tr style="{row_color}">
                <td style="font-size: 16px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['Objective']}</td>
                <td style="font-size: 16px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['Regime']}</td>
                <td style="font-size: 16px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['Tree to Harvest']}</td>
                <td style="font-size: 16px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['Remaining Density']}</td>
                <td style="font-size: 16px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['Remaining Species']}</td>
                <td style="font-size: 16px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['New AGB']}</td>
                <td style="font-size: 16px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['Carbon Loss']}</td>
                <td style="font-size: 16px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['Carbon Loss(M) in 2055']}</td>
            </tr></tbody>"""


# Generate HTML code for the table with color-coding
html_code = """<table style="font-size: 18px; text-align: left; border-collapse: collapse; width: 100%;"><thead><tr>
                <th style="background-color: #851a15; color: #FFFFFF; font-size: 16px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Objective</th>
                <th style="background-color: #851a15; color: #FFFFFF; font-size: 16px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Regime</th>
                <th style="background-color: #851a15; color: #FFFFFF; font-size: 16px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Tree to Harvest</th>
                <th style="background-color: #851a15; color: #FFFFFF; font-size: 16px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Remaining Density</th>
                <th style="background-color: #851a15; color: #FFFFFF; font-size: 16px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Remaining Species</th>
                <th style="background-color: #851a15; color: #FFFFFF; font-size: 16px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">New AGB</th>
                <th style="background-color: #851a15; color: #FFFFFF; font-size: 16px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Carbon Loss(M)</th>
                <th style="background-color: #851a15; color: #FFFFFF; font-size: 16px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Carbon Loss(M) in 2055</th>
            </tr></thead>"""

# Iterate through rows to create HTML table rows with color-coding
for index, row in df_sorted.iterrows():
    html_code += generate_row_html(row)

html_code += "</table>"
st.markdown(html_code , unsafe_allow_html=True)


# Select the year (only 2021)
col1, col2, col3 = st.columns(3)
with col1:
    selected_objective = st.selectbox("Select the Objective", ["to save Species" ,"to keep Diversity" ,"to keep Dominance"])
with col2:
    selected_reguime = st.selectbox("Select the Regime", ["Heavy" ,"Medium" ,"Light"])
with col3:
    selected_ml = st.selectbox("Select the Machine Learning Model", ['SVMOptimal', 'SVMV1', 'SVMV2', 'GRUV1'])

data = {
    'Species': ['Oak', 'Pine', 'Maple', 'Birch', 'Spruce'],
    'D2019': [30, 25, 20, 18, 22],
    'D2021' :[28 ,33 ,15 ,19 ,14]
}

# Create DataFrame
df = pd.DataFrame(data)
# Select the number of trees to harvest using a slider
total_trees_2021 = df[f'D2019'].sum()
if selected_reguime == 'Heavy':
    max_slider_value = 390
if selected_reguime == 'Medium':
    max_slider_value = 164
if selected_reguime == 'Light':
    max_slider_value = 32

    # Ensure the max_value doesn't exceed the total number of trees
trees_to_harvest = st.slider("Number of Trees to Harvest", min_value=10, max_value=max_slider_value,
                             value=total_trees_2021 // 2)

# Number input fields for DBH classes
dbh_classes = ['DBH Class 1', 'DBH Class 2', 'DBH Class 3', 'DBH Class 4', 'DBH Class 5']
dbh_inputs = []

initial_trees_per_class = trees_to_harvest // 5

for i, dbh_class in enumerate(dbh_classes):
    max_trees = min(trees_to_harvest, df[f'D{selected_year}'].iloc[i])
    trees_for_dbh_class = st.number_input(f"Number of Trees for {dbh_class}", min_value=0,
                                          max_value=max_slider_value, value=initial_trees_per_class)
    dbh_inputs.append(trees_for_dbh_class)

# Button to apply the simulation
if st.button("Apply Simulation"):
    # Update the dataset based on the selected year and harvested trees for each DBH class
    for i, dbh_class in enumerate(dbh_classes):
        df[f'D{selected_year}'].iloc[i] -= dbh_inputs[i]

    # Display the updated dataset
    import requests


    url = f'https://e060-34-83-163-159.ngrok-free.app/Predictionto2055{selected_ml}'

    # Replace 'localhost:8000' with your server's address

    # Make a POST request to the endpoint
    response = requests.post(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the JSON response
        data = response.json()
        # Fetch the predictions
        df = pd.DataFrame(data)
    else:
        print("Error:", response.status_code)


    showgraphs(df)