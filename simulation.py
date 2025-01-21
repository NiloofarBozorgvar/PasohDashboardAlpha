def simulation_start():
    def showgraphs():
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
            df = pd.read_csv('DBHPrediction2055.csv')

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
                'Chengal': {conditions[2]: []}
            }

            # Loop over each year
            for year in years:
                # Calculate the number of trees meeting specific conditions for each part
                for part_name, part_data in zip(['Dipterocarp', 'Non-Dipterocarp', 'Chengal'],
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
            ax.set_title("Number of Trees")
            ax.set_xticks(index + bar_width)
            ax.set_xticklabels(years)
            ax.legend()

            # Display the bar chart using Streamlit
            st.pyplot(fig)

    import base64
    from streamlit_card import card
    import pandas as pd

    import folium
    import streamlit as st
    # Streamlit app
    st.title("Harvest Simulation")

    # -----------------------------------------------------------------------
    import streamlit as st


    def display_design_element():
        st.subheader("For Pasoh Forest Reserve")
        st.image('img.jpg')

        # Text content as a single HTML block
        text = """
            We have implemented two approaches for stand prescription for Pasoh Forest Reserve:<br>
            1. <b>Selective Management System (SMS)<br>
            2. <b>BDq<br><br>
            
            Click on the approach of your choice to explore the details and learn more about how each method is applied and see the implications."""

        # Custom styles
        font_size = "20px"  # Define font size as a CSS value
        font_color = "#333333"  # Dark grey
        border_color = "#568203"  # Green
        border_width = "2px"

        # Display the bordered text box with inline CSS
        st.markdown(
            f"""
            <div style="
                padding: 15px;
                border: {border_width} solid {border_color};
                border-radius: 5px;
                background-color: #f9f9f9;
            ">
                <div style="
                    font-size: {font_size};
                    color: {font_color};
                    line-height: 0.8;
                    margin: 0;
                ">
                    {text}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    display_design_element()
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    #-----------------------------------------------------------------------
    selected_objectives = st.selectbox("Select the Prescription Method",
                                       ['BDq', 'Selective Management System (SMS)'])
    if selected_objectives == 'BDq':
        col1, col2= st.columns(2)
        with col1:
            selected_year = st.selectbox("Select the Year", [2019])
        with col2:
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
        st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
        # ------------------------------------------------------------------------------------text box

        with st.expander("See the detail of each biodiversity dynamic prescription scenarios:"):
            st.write \
                ('In the following you see the steps of BDq algorithm, consequently the other steps in prescription scenarios')
            st.image('Pics/bdq algo.png', caption='BDq Algorithm')
            st.image('Pics/Heavy-h1.png', caption='Heavy regim for hectare 1')
            st.image('Pics/Heavy-h2.png', caption='Heavy regim for hectare 2')
            df = pd.read_csv('Result-Heavy.csv')
            df_first_5_columns = df.iloc[:, :5]
            st.dataframe(df_first_5_columns  )# -------------------------------------------------------------------------------------end of text box
        st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

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


            url = f'https://b0e1-34-75-168-12.ngrok-free.app/Predictionto2055{selected_ml}'

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


            showgraphs()
    selected_objectives_Hectar = None
    if selected_objectives == 'Selective Management System (SMS)':
        selected_objectives_Hectar = st.selectbox("Select the Hectar", ['50 Hectar', '2 Hectar'])
    if selected_objectives_Hectar == '50 Hectar':

        import streamlit as st
        import pandas as pd
        data_2021 = pd.read_csv('hectare_sp_cut_total.csv')
        data_2026 = pd.read_csv('hectare_sp_cut_total_2026.csv')  # Replace with actual 2026 data file

        # Remove unnecessary columns and clean data (if required)
        data_2021 = data_2021.drop(columns=['Unnamed: 0'], errors='ignore')
        data_2026 = data_2026.drop(columns=['Unnamed: 0'], errors='ignore')

        data_2021['Year'] = 1986
        data_2026['Year'] = 1991

        combined_data = pd.concat([data_2021, data_2026], ignore_index=True)

        def create_dataframe(filtered_data):
            result = []
            for idx, (_, row) in enumerate(filtered_data.iterrows(), start=1):  # Start index at 1
                entry = {
                    "Plan ID": f"P{idx}",  # Create a unique Plan ID
                    "Action Time": f"Now ({row['Year']})" if row['Year'] == 1986 else f"Next 5 years ({row['Year']})",
                    "Regime": row['Regime'],
                    "Objective": row['type'],  # Objective column from dataset
                    "Total Number of trees to be fell": row['Total Trees'],
                    "Dipterocarp trees to be fell": row['Dipterocarp'],
                    "Non-Dipterocarp trees to be fell": row['Non-Dipterocarp'],
                    "Chengal trees to be fell": row['Chengal'],
                }
                result.append(entry)
            return pd.DataFrame(result)

        # Generate dictionary for the selected hectare

        # Title and Filters
        #st.title("Pasoh Forest Dashboard")
        #st.subheader("Select the Prescription Method")
        st.write("**Selective Management System (SMS)**")

        # Sidebar Filters
        col1, col2 = st.columns(2)
        with col1:
            year = st.selectbox("Prescription for year:", ["1986"], index=0)
        with col2:
            selected_hectare = st.selectbox("Select Hectare", options=sorted(data_2021['Hectare'].unique()))

        filtered_data = combined_data[combined_data['Hectare'] == selected_hectare]

        plans = create_dataframe(filtered_data)

        data = plans

        st.write("Please select your preference to see the Recommended Action Plan.")

        # CSS for Table Design
        st.markdown("""
            <style>
                table {
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                    font-size: 22px;
                }
                th {
                    background-color: #d3d3d3; /* رنگ خاکستری برای سر ستون‌ها */
                    text-align: center;
                    padding: 10px;
                    font-weight: bold;
                    border: none; /* حذف خطوط سر ستون */
                }
                td {
                    text-align: center;
                    padding: 8px;
                    border: none; /* حذف خطوط سلول‌ها */
                }
                tr:nth-child(even) {
                    background-color: #f9f9f9;
                }
                tr:hover {
                    background-color: #f1f1f1;
                }
                .plan-id {
                    background-color: #e7dcc3;
                    color: black;
                    font-weight: bold;
                    text-align: center;
                    border-radius: 5px;
                    padding: 6px;
                }
                .action-time {
                    background-color: #d3d3d3; /* رنگ خاکستری */
                    color: black;
                    font-weight: normal;
                    text-align: center;
                    border-radius: 5px;
                    padding: 6px;
                }
            </style>
        """, unsafe_allow_html=True)

        # Generate the Table
        table_html = """<table>
            <thead>
                <tr>
                    <th>Plan ID</th>
                    <th>Action Time</th>
                    <th>Regime</th>
                    <th>Objective</th>
                    <th>Total Number of trees to be fell</th>
                    <th>Dipterocarp trees to be fell</th>
                    <th>Non-Dipterocarp trees to be fell</th>
                    <th>Chengal trees to be fell</th>
                </tr>
            </thead>
            <tbody>
        """

        for _, row in data.iterrows():
            table_html += f"""<tr>
                <td class="plan-id">{row['Plan ID']}</td>
                <td class="action-time">{row['Action Time']}</td>
                <td>{row['Regime']}</td>
                <td>{row['Objective']}</td>
                <td>{row['Total Number of trees to be fell']}</td>
                <td>{row['Dipterocarp trees to be fell']}</td>
                <td>{row['Non-Dipterocarp trees to be fell']}</td>
                <td>{row['Chengal trees to be fell']}</td>
            </tr>
            """

        table_html += """</tbody>
        </table>
        """

        st.markdown(table_html, unsafe_allow_html=True)

        ######### PAGE 2

        data_1986 = pd.read_csv('Updated_Merged_Dataset.csv')
        data_1986 = data_1986.round(2)
        data_1986['Total Biomassyt'] = (data_1986['Total Biomassyt'] / 1000).round(2)
        data_1986['Total Carbon Stockyt'] = (data_1986['Total Carbon Stockyt'] / 1000).round(2)

        def create_dataframe_now(filtered_data):
            result = []
            for idx, (_, row) in enumerate(filtered_data.iterrows(), start=1):  # Start index at 1
                # Correct the logical condition and adjust "Action Time"
                if row['Year'] == 2001 or row['Year'] == 2006:
                    action_time = f"Now ({row['Year']})"
                else:
                    continue
                entry = {
                    "Plan ID": f"P{idx}",  # Create a unique Plan ID
                    "Action Time": action_time,
                    "Total Volume": row['Total Volume'],
                    "Total Carbon Stockyt": row['Total Carbon Stockyt'],
                    "Total Biomassyt": row['Total Biomassyt'],
                    "Remaining Trees": row['Remaining Trees'],  # Fixed the column name
                    "Unique Species": row['Unique Species'],
                    "Carbon Loss": row['carbon_loss']
                }
                result.append(entry)
            return pd.DataFrame(result)

        def create_dataframe_predicted(filtered_data):
            result = []
            indx = 1
            for idx1, (_, row) in enumerate(filtered_data.iterrows(), start=1):  # Start index at 1
                # Correct the logical condition and adjust "Action Time"
                if row['Year'] == 2031 or row['Year'] == 2036:

                    action_time = f"({row['Year']})"
                else:
                    continue
                entry = {
                    "Plan ID": f"P{indx}",  # Create a unique Plan ID
                    "Action Time": action_time,
                    "Total Volume": row['Total Volume'],
                    "Total Carbon Stockyt": row['Total Carbon Stockyt'],
                    "Total Biomassyt": row['Total Biomassyt'],
                    "Remaining Trees": row['Remaining Trees'],  # Fixed the column name
                    "Unique Species": row['Unique Species'],
                    "Carbon Loss": row['carbon_loss']

                }
                indx += 1
                result.append(entry)
            return pd.DataFrame(result)

        filtered_data = data_1986[data_1986['Hectare'] == selected_hectare]

        column_mapping = {
            "Remaining Carbon (t/ha)": "Total Carbon Stockyt",
            "Carbon Loss (t/ha)": "carbon_loss",
            "Remaining Volume (m3/ha)": "Total Volume",
            "Remaining Biomass (t/ha)": "Total Biomassyt",
        }

        # Create a new DataFrame with only the relevant columns
        mapped_data = filtered_data[list(column_mapping.values())]
        mapped_data.columns = column_mapping.keys()  # Rename columns to target fields

        # Calculate max and min values for the mapped columns
        max_min_values = {
            column: {"max": mapped_data[column].max(), "min": mapped_data[column].min()}
            for column in mapped_data.columns
        }

        def apply_colors(value, column, max_min_values=max_min_values):
            max_val = max_min_values[column]["max"]
            min_val = max_min_values[column]["min"]

            if column == "Carbon Loss (t/ha)":  # Special case for Carbon Loss
                if value == min_val:
                    return "green"
                elif value == max_val:
                    return "red"
            else:  # Default case for other columns
                if value == max_val:
                    return "green"
                elif value == min_val:
                    return "red"

        col1, col2 = st.columns(2)
        ## tbl1
        datanow = create_dataframe_now(filtered_data)
        # HTML for the table, including styles
        st.markdown("""
            <style>
                .table-container {
                    margin-top: 20px;
                    padding: 20px;
                    background-color: #f7f7f7;
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                }

                table {
                    width: 100%;
                    border-collapse: collapse;
                    font-size: 15px;
                    background-color: white;
                }

                th {
                    background-color: #e4e4e4;
                    text-align: center;
                    padding: 10px;
                    font-weight: bold;
                    border: 1px solid #ddd;
                }

                td {
                    text-align: center;
                    padding: 10px;
                    border: 1px solid #ddd;
                }

                tr:nth-child(even) {
                    background-color: #f9f9f9;
                }

                tr:hover {
                    background-color: #f1f1f1;
                }

                .green { background-color: #28a745; color: white; }
                .yellow { background-color: #ffc107; color: black; }
                .red { background-color: #dc3545; color: white; }

                .plan-id {
                    background-color: #d1d3e2;
                    color: #2c3e50;
                    font-weight: bold;
                    text-align: center;
                    border-radius: 5px;
                    padding: 8px;
                }

                .header-row {
                    background-color: #f1f1f1;
                }

            </style>
        """, unsafe_allow_html=True)
        html = """<h3>Immediate</h3>
            <table>
                <thead>
                    <tr class="header-row">
                        <th>Plan ID</th>
                        <th colspan="6" style="text-align:center;">Immediate Implications</th>
                    </tr>
                    <tr>
                        <th></th>
                        <th>Remaining Carbon (t/ha)</th>
                        <th>Carbon Loss (t/ha)</th>
                        <th>Remaining Volume (m3/ha)</th>
                        <th>Remaining Biomass (t/ha)</th>
                        <th>Remaining Species</th>
                        <th>Remaining Trees</th>
                    </tr>
                </thead>
                <tbody>"""

        # Populate rows with data and apply colors dynamically
        for _, row in datanow.iterrows():
            html += f"""<tr>
                    <td class="plan-id">{row['Plan ID']}</td>
                    <td class="{apply_colors(row['Total Carbon Stockyt'], 'Remaining Carbon (t/ha)')}">{row['Total Carbon Stockyt']}</td>
                    <td class="{apply_colors(row['Carbon Loss'], 'Carbon Loss (t/ha)')}">{row['Carbon Loss']}</td>
                    <td class="{apply_colors(row['Total Volume'], 'Remaining Volume (m3/ha)')}">{row['Total Volume']}</td>
                    <td class="{apply_colors(row['Total Biomassyt'], 'Remaining Biomass (t/ha)')}">{row['Total Biomassyt']}</td>
                    <td>{row['Unique Species']}</td>
                    <td>{row['Remaining Trees']}</td>
                </tr>"""

        html += "</tbody></table>"

        with col1:
            st.markdown(html, unsafe_allow_html=True)

        ######## tbl2
        data_2030 = pd.read_csv('Updated_Merged_Dataset_2030.csv')
        data_2030['Total Biomassyt'] = (data_2030['Total Biomassyt'] / 1000).round(2)
        data_2030['Total Carbon Stockyt'] = (data_2030['Total Carbon Stockyt'] / 1000).round(2)
        filtered_data = data_2030[data_2030['Hectare'] == selected_hectare]

        column_mapping = {
            "Remaining Carbon (t/ha)": "Total Carbon Stockyt",
            "Carbon Loss (t/ha)": "carbon_loss",
            "Remaining Volume (m3/ha)": "Total Volume",
            "Remaining Biomass (t/ha)": "Total Biomassyt",
        }

        # Create a new DataFrame with only the relevant columns
        mapped_data = filtered_data[list(column_mapping.values())]
        mapped_data.columns = column_mapping.keys()  # Rename columns to target fields

        # Calculate max and min values for the mapped columns
        max_min_values = {
            column: {"max": mapped_data[column].max(), "min": mapped_data[column].min()}
            for column in mapped_data.columns
        }

        def apply_colors(value, column, max_min_values=max_min_values):
            max_val = max_min_values[column]["max"]
            min_val = max_min_values[column]["min"]

            if column == "Carbon Loss (t/ha)":  # Special case for Carbon Loss
                if value == min_val:
                    return "green"
                elif value == max_val:
                    return "red"
            else:  # Default case for other columns
                if value == max_val:
                    return "green"
                elif value == min_val:
                    return "red"

        datapredicted = create_dataframe_predicted(filtered_data)
        # HTML for the table, including styles
        st.markdown("""
            <style>
                .table-container {
                    margin-top: 20px;
                    padding: 20px;
                    background-color: #f7f7f7;
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                }

                table {
                    width: 100%;
                    border-collapse: collapse;
                    font-size: 15px;
                    background-color: white;
                }

                th {
                    background-color: #e4e4e4;
                    text-align: center;
                    padding: 10px;
                    font-weight: bold;
                    border: 1px solid #ddd;
                }

                td {
                    text-align: center;
                    padding: 10px;
                    border: 1px solid #ddd;
                }

                tr:nth-child(even) {
                    background-color: #f9f9f9;
                }

                tr:hover {
                    background-color: #f1f1f1;
                }

                .green { background-color: #28a745; color: white; }
                .yellow { background-color: #ffc107; color: black; }
                .red { background-color: #dc3545; color: white; }

                .plan-id {
                    background-color: #d1d3e2;
                    color: #2c3e50;
                    font-weight: bold;
                    text-align: center;
                    border-radius: 5px;
                    padding: 8px;
                }

                .header-row {
                    background-color: #f1f1f1;
                }

            </style>
        """, unsafe_allow_html=True)
        html = """<h3>Predicted</h3>
            <table>
                <thead>
                    <tr class="header-row">
                        <th>Plan ID</th>
                        <th colspan="6" style="text-align:center;">Predicted Implications</th>
                    </tr>
                    <tr>
                        <th></th>
                        <th>Remaining Carbon (t/ha)</th>
                        <th>Carbon Loss (t/ha)</th>
                        <th>Remaining Volume (m3/ha)</th>
                        <th>Remaining Biomass (t/ha)</th>
                        <th>Remaining Species</th>
                        <th>Remaining Trees</th>
                    </tr>
                </thead>
                <tbody>"""

        # Populate rows with data and apply colors dynamically
        for _, row in datapredicted.iterrows():
            html += f"""<tr>
                    <td class="plan-id">{row['Plan ID']}</td>
                    <td class="{apply_colors(row['Total Carbon Stockyt'], 'Remaining Carbon (t/ha)')}">{row['Total Carbon Stockyt']}</td>
                    <td class="{apply_colors(row['Carbon Loss'], 'Carbon Loss (t/ha)')}">{row['Carbon Loss']}</td>
                    <td class="{apply_colors(row['Total Volume'], 'Remaining Volume (m3/ha)')}">{row['Total Volume']}</td>
                    <td class="{apply_colors(row['Total Biomassyt'], 'Remaining Biomass (t/ha)')}">{row['Total Biomassyt']}</td>
                    <td>{row['Unique Species']}</td>
                    <td>{row['Remaining Trees']}</td>
                </tr>"""

        html += "</tbody></table>"
        with col2:
            st.markdown(html, unsafe_allow_html=True)

        # ========== PAGE3

        # =========== select the PID
        import streamlit as st
        import pandas as pd

        # Function to load the main data
        @st.cache_data
        def load_data():
            # Replace this with your actual data or file
            return pd.DataFrame({
                "Plan ID": [f"P{i}" for i in range(1, 13)],
                "Objective": ["Volume", "Specie", "Volume", "Specie", "Volume", "Specie", "Volume", "Specie", "Volume",
                              "Specie", "Volume", "Specie"],
                "Regime": [20, 16, 12, 20, 16, 12, 20, 16, 12, 20, 16, 12]})

        # Load the data
        data = load_data()

        # Dropdown selection for Plan ID
        selected_plan = st.selectbox("Select a Plan ID", data["Plan ID"].unique())

        # Display the selected plan's details
        selected_data = data[data["Plan ID"] == selected_plan]

        # Process the selected plan
        if not selected_data.empty:
            # Extract necessary details
            objective = selected_data["Objective"].iloc[0]
            regime = selected_data["Regime"].iloc[0]

            # Construct file name based on format
            if objective.lower() == "volume":
                folder = "hectare_analysis_results"
            elif objective.lower() == "specie":
                folder = "hectare_analysis_results2"
            else:
                folder = None

            if folder:
                file_name = f"{folder}/result_{selected_hectare}_{regime}.csv"

                # Try to load the file
                try:
                    file_data = pd.read_csv(file_name)
                except FileNotFoundError:
                    st.error(f"File {file_name} not found. Please check the directory and file name.")

        import streamlit.components.v1 as components

        total_rows_more_60 = len(file_data[file_data['dbh'] > 60])
        num_rows_more_60 = int(0.2 * total_rows_more_60)

        rows_45_60 = file_data[(file_data['dbh'] > 45) & (file_data['dbh'] <= 60)]
        total_rows_45_60 = len(rows_45_60)
        num_rows_45_60 = int(0.3 * total_rows_45_60)

        rows_30_45 = file_data[(file_data['dbh'] > 30) & (file_data['dbh'] <= 45)]
        total_rows_30_45 = len(rows_30_45)
        num_rows_30_45 = int(0.4 * total_rows_30_45)

        rows_15_30 = file_data[(file_data['dbh'] > 15) & (file_data['dbh'] <= 30)]
        total_rows_15_30 = len(rows_15_30)
        num_rows_15_30 = int(0.5 * total_rows_15_30)

        # HTML code for the animated cards with khaki color
        html_code = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                .card-container {
                    display: flex;
                    justify-content: space-around;
                    margin-top: 30px;
                    flex-wrap: wrap;
                }

                .card {
                    background-color: #F0E68C;  /* Khaki color */
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    padding: 20px;
                    width: 200px;
                    margin: 10px;
                    text-align: center;
                    transition: transform 0.3s ease, box-shadow 0.3s ease;
                }

                .card:hover {
                    transform: translateY(-10px);
                    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
                }

                .card h3 {
                    font-size: 18px;
                    color: #333;
                }

                .card p {
                    font-size: 24px;
                    font-weight: bold;
                    color: #555;
                    animation: fadeIn 1s ease-in-out;
                }

                @keyframes fadeIn {
                    0% { opacity: 0; }
                    100% { opacity: 1; }
                }
            </style>
        </head>"""

        html_code = html_code + f"""<body>
            <div class="card-container">
                <div class="card">
                    <h3>Logging Damage DBH 15-30cm</h3>
                    <p>{num_rows_15_30}</p>
                </div>
                <div class="card">
                    <h3>Logging Damage DBH 30-45cm</h3>
                    <p>{num_rows_30_45}</p>
                </div>
                <div class="card">
                    <h3>Logging Damage DBH 45-60cm</h3>
                    <p>{num_rows_45_60}</p>
                </div>
                <div class="card">
                    <h3>Logging Damage DBH 60cm</h3>
                    <p>{num_rows_more_60}</p>
                </div>
            </div>
        </body>
        </html>
        """

        # Display the HTML in Streamlit
        components.html(html_code, height=220)

        import streamlit as st
        import pandas as pd
        import plotly.express as px

        # Creating the dataset from your provided data
        data = {
            "TAG": [2317, 2318, 2319, 2320, 2321, 2322, 2323, 2323, 2324, 2324, 2325, 2325, 2325, 2325, 2326, 2327,
                    2328, 2328],
            "Species": ["SHORP2", "MESURA", "CANAPA", "PAYELU", "GIROPA", "MACALO", "DACRR1", "MACALO", "KOOMMA",
                        "NAUCOF", "SHORL1",
                        "APORPR", "GREWMI", "MACALO", "EUGEPE", "RYPAKU", "EUGEDE", "AAAAA"],
            "QUAD": [1] * 18,
            "Hectare": [1] * 18,
            "XCO": [1.8, 3.3, 6, 7.9, 7.6, 9.5, 9.7, 0, 10.7, 10.5, 3.9, 4, 1.6, 3.6, 2.3, 2.4, 8.3, 0],
            "YCO": [5, 5, 1.8, 4.7, 6.9, 6.8, 10.9, 0, 11.6, 11.8, 10.8, 12.7, 13.7, 10.6, 11.3, 18.2, 15.9, 0]
        }

        # Converting the data into a pandas DataFrame
        df = pd.DataFrame(data)

        if objective.lower() == "specie":
            folder = "sp"
            file_name = f"{folder}/trees_to_cut_count_h{selected_hectare}.csv"
        elif objective.lower() == "volume":
            folder = "Volume"
            file_name = f"{folder}/trees_to_cut_h{selected_hectare}.csv"

        file_data = pd.read_csv(file_name)

        file_data = file_data[:regime]
        # Streamlit title and instructions
        st.title("Tree Location Visualization")
        st.markdown("""
            This plot shows the location of trees in the forest based on their X and Y coordinates.
            You can interact with the plot, zoom in/out, and hover over data points to see the details.
        """)

        # Create an interactive Plotly scatter plot
        fig = px.scatter(file_data, x="gx", y="gy", text="TreeID",
                         color="Species", hover_data=["Species", "Hectare"],
                         title="Tree Locations in the Forest",
                         labels={"XCO": "X Coordinate", "YCO": "Y Coordinate"})

        # Customize the layout for better UI
        fig.update_layout(
            plot_bgcolor="white",  # White background
            title_font=dict(size=24, family="Montserrat, sans-serif"),
            xaxis_title="X Coordinate",
            yaxis_title="Y Coordinate",
            xaxis=dict(showgrid=True, zeroline=False, showticklabels=True),
            yaxis=dict(showgrid=True, zeroline=False, showticklabels=True),
            hovermode="closest",
            font=dict(size=14, color="black", family="Arial, sans-serif"),
            showlegend=True
        )

        # Adding animation effect on hover (smooth zoom-in/out on hover)
        fig.update_traces(marker=dict(size=12, opacity=0.8, line=dict(width=2, color='DarkSlateGrey')),
                          selector=dict(mode='markers'))

        # Display the plot in Streamlit
        st.plotly_chart(fig, use_container_width=True)
        # +++++++++++++

        import pandas as pd
        import plotly.express as px
        import plotly.graph_objects as go
        import numpy as np

        tree_data = file_data

        # Add canopy radius calculation (smaller canopies)
        K = 0.05  # Reduced empirical constant for smaller canopies
        file_data["Canopy_Radius"] = file_data["DBH"] * K  # Radius in meters

        # Add canopy volume calculation
        file_data["Canopy_Volume"] = (4 / 3) * np.pi * (file_data["Canopy_Radius"] ** 3)
        st.write(file_data)

        # Create the 3D scatter plot (canopies)
        fig = px.scatter_3d(
            file_data,
            x="gx",  # X-axis (Tree location)
            y="gy",  # Y-axis (Tree location)
            z="Height_m",  # Z-axis (Tree height)
            text="TreeID",  # TreeID displayed on hover
            color="Species",  # Color based on tree species
            hover_data=["Species", "Hectare", "DBH", "Canopy_Radius", "Canopy_Volume"],  # Additional hover info
            title="Tree Locations with Canopy Calculations (3D)",
            labels={"gx": "X Coordinate", "gy": "Y Coordinate", "Height_m": "Height (m)"}
        )

        # Customize the layout for better UI and larger plot
        fig.update_layout(
            width=1000,  # Set the width of the plot
            height=800,  # Set the height of the plot
            plot_bgcolor="white",  # White background
            title_font=dict(size=24, family="Montserrat, sans-serif"),
            scene=dict(
                xaxis_title="X Coordinate",
                yaxis_title="Y Coordinate",
                zaxis_title="Height (m)",
                xaxis=dict(showgrid=True, zeroline=False, showticklabels=True),
                yaxis=dict(showgrid=True, zeroline=False, showticklabels=True),
                zaxis=dict(showgrid=True, zeroline=False, showticklabels=True),
            ),
            hovermode="closest",
            font=dict(size=14, color="black", family="Arial, sans-serif"),
            showlegend=True
        )

        # Add tree trunks as vertical lines with thickness based on DBH
        for _, row in file_data.iterrows():
            # Add vertical line (trunk)
            fig.add_trace(go.Scatter3d(
                x=[row["gx"], row["gx"]],
                y=[row["gy"], row["gy"]],
                z=[0, row["Height_m"]],
                mode='lines',
                line=dict(color="brown", width=row["DBH"] / 5),  # Thickness based on DBH
                name=f"Trunk {row['TreeID']}"
            ))

            # Add canopy as a sphere (smaller canopies)
            u = np.linspace(0, 2 * np.pi, 20)
            v = np.linspace(0, np.pi, 20)
            x = row["Canopy_Radius"] * np.outer(np.cos(u), np.sin(v)) + row["gx"]
            y = row["Canopy_Radius"] * np.outer(np.sin(u), np.sin(v)) + row["gy"]
            z = row["Canopy_Radius"] * np.outer(np.ones(np.size(u)), np.cos(v)) + row["Height_m"]

            fig.add_trace(go.Surface(
                x=x, y=y, z=z,
                colorscale="Greens",
                opacity=0.5,
                showscale=False,
                name=f"Canopy {row['TreeID']}"
            ))
        st.plotly_chart(fig, use_container_width=True)

        # Display the dataset in an expander
        with st.expander("View Dataset"):
            st.dataframe(file_data)  # Display the dataset as a table

        if objective.lower() == "specie":
            folder = "sp"
            file_name = f"final_hectare_analysis_results/final_updated_result_{selected_hectare}_{regime}.csv"
        elif objective.lower() == "volume":
            folder = "Volume"
            file_name = f"final_hectare_analysis_results/final_updated_result_{selected_hectare}_{regime}.csv"

        data = pd.read_csv(file_name)

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
                height_sums.append(category_data[f'dbh_year_{year}'].sum())

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
            st.subheader('DBH Over 30 Years')
            fig_height = px.line(
                filtered_data,
                x='Year',
                y='Height',
                color='Category',
                labels={'Year': 'Year', 'Height': 'Height'},
                title='DBH Trends Over 30 Years',
                template='plotly_white'
            )
            fig_height.update_layout(
                title={'x': 0.5},
                xaxis=dict(title='Year'),
                yaxis=dict(title='Height'),
                legend=dict(title='Category', orientation='h', x=0.5, xanchor='center', y=-0.2)
            )
            st.plotly_chart(fig_height, use_container_width=True)

        # Prepare DBH classification
        dbh_classes = {
            '<15': lambda dbh: dbh < 15,
            '15-30': lambda dbh: 15 <= dbh < 30,
            '30-45': lambda dbh: 30 <= dbh < 45,
            '45-60': lambda dbh: 45 <= dbh < 60,
            '>60': lambda dbh: dbh >= 60
        }

        # Create an empty DataFrame to store aggregated results
        aggregated_dbh_data = pd.DataFrame()

        # Iterate through years and classify by DBH classes
        for year in range(1, 31):
            year_data = {'Year': [], 'DBH Class': [], 'Volume': [], 'Carbon Stock': [], 'Biomass': []}

            # Calculate sums for each DBH class
            for dbh_class, condition in dbh_classes.items():
                filtered_data = data[data[f'dbh_year_{year}'].apply(condition)]
                year_data['Year'].append(year)
                year_data['DBH Class'].append(dbh_class)
                year_data['Volume'].append(filtered_data[f'volume_year_{year}'].sum())
                year_data['Carbon Stock'].append(filtered_data[f'carbon_stockyt_year_{year}'].sum())
                year_data['Biomass'].append(filtered_data[f'biomassyt_year_{year}'].sum())

            # Append the year's data to the aggregated DataFrame
            aggregated_dbh_data = pd.concat([aggregated_dbh_data, pd.DataFrame(year_data)])

        # Display bar charts for DBH classes
        metrics = ['Volume', 'Carbon Stock', 'Biomass']

        for metric in metrics:
            st.subheader(f'{metric} Grouped by DBH Class Over 30 Years')

            # Create a bar chart for the metric
            fig = px.bar(
                aggregated_dbh_data,
                x='Year',
                y=metric,
                color='DBH Class',
                barmode='group',
                labels={'Year': 'Year', metric: metric},
                title=f'{metric} Grouped by DBH Class',
                template='plotly_white'
            )

            # Customize layout for better visuals
            fig.update_layout(
                title={'x': 0.5},  # Center the title
                xaxis=dict(title='Year'),
                yaxis=dict(title=metric),
                legend=dict(title='DBH Class', orientation='h', x=0.5, xanchor='center', y=-0.2)
            )

            # Show the chart
            st.plotly_chart(fig, use_container_width=True)
    if selected_objectives_Hectar == '2 Hectar':



        import streamlit as st
        import pandas as pd

        data_2021 = pd.read_csv('2Project_hectare_sp_cut_total (2).csv')
        data_2026 = pd.read_csv('2Project_hectare_sp_cut_total (2).csv')  # Replace with actual 2026 data file

        # Remove unnecessary columns and clean data (if required)
        data_2021 = data_2021.drop(columns=['Unnamed: 0'], errors=  'ignore')
        data_2026 = data_2026.drop(columns=['Unnamed: 0'], errors='ignore')

        data_2021['Year'] = 2021
        data_2026['Year'] = 2026

        combined_data = pd.concat([data_2021, data_2026], ignore_index=True)
        def create_dataframe(filtered_data):
            result = []
            for idx, (_, row) in enumerate(filtered_data.iterrows(), start=1):  # Start index at 1
                entry = {
                    "Plan ID": f"P{idx}",  # Create a unique Plan ID
                    "Action Time": f"Now ({row['Year']})" if row['Year'] == 2021 else f"Next 5 years ({row['Year']})",
                    "Regime": row['Regime'],
                    "Objective": row['type'],  # Objective column from dataset
                    "Total Number of trees to be fell": row['Total Trees'],
                    "Dipterocarp trees to be fell": row['Dipterocarp'],
                    "Non-Dipterocarp trees to be fell": row['Non-Dipterocarp'],
                    "Chengal trees to be fell": row['Chengal'],
                }
                result.append(entry)
            return pd.DataFrame(result)

        # Generate dictionary for the selected hectare

        # Title and Filters
      #  st.title("Pasoh Forest Dashboard")
       # st.subheader("Select the Prescription Method")
        st.write("**Selective Management System (SMS)**")

        # Sidebar Filters
        col1, col2 = st.columns(2)
        with col1:
            year = st.selectbox("Prescription for year:", ["1986"], index=0)
        with col2:
            selected_hectare = st.selectbox("Select Hectare", options=sorted(data_2021['Hectare'].unique()))

        filtered_data = combined_data[combined_data['Hectare'] == selected_hectare]

        plans = create_dataframe(filtered_data)

        data = plans

        st.write("### Please select your preference to see the Recommended Action Plan.")

        # CSS for Table Design
        st.markdown("""
            <style>
                table {
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                    font-size: 22px;
                }
                th {
                    background-color: #d3d3d3; /* رنگ خاکستری برای سر ستون‌ها */
                    text-align: center;
                    padding: 10px;
                    font-weight: bold;
                    border: none; /* حذف خطوط سر ستون */
                }
                td {
                    text-align: center;
                    padding: 8px;
                    border: none; /* حذف خطوط سلول‌ها */
                }
                tr:nth-child(even) {
                    background-color: #f9f9f9;
                }
                tr:hover {
                    background-color: #f1f1f1;
                }
                .plan-id {
                    background-color: #e7dcc3;
                    color: black;
                    font-weight: bold;
                    text-align: center;
                    border-radius: 5px;
                    padding: 6px;
                }
                .action-time {
                    background-color: #d3d3d3; /* رنگ خاکستری */
                    color: black;
                    font-weight: normal;
                    text-align: center;
                    border-radius: 5px;
                    padding: 6px;
                }
            </style>
        """, unsafe_allow_html=True)

        # Generate the Table
        table_html = """<table>
            <thead>
                <tr>
                    <th>Plan ID</th>
                    <th>Action Time</th>
                    <th>Regime</th>
                    <th>Objective</th>
                    <th>Total Number of trees to be fell</th>
                    <th>Dipterocarp trees to be fell</th>
                    <th>Non-Dipterocarp trees to be fell</th>
                    <th>Chengal trees to be fell</th>
                </tr>
            </thead>
            <tbody>
        """

        for _, row in data.iterrows():
            table_html += f"""<tr>
                <td class="plan-id">{row['Plan ID']}</td>
                <td class="action-time">{row['Action Time']}</td>
                <td>{row['Regime']}</td>
                <td>{row['Objective']}</td>
                <td>{row['Total Number of trees to be fell']}</td>
                <td>{row['Dipterocarp trees to be fell']}</td>
                <td>{row['Non-Dipterocarp trees to be fell']}</td>
                <td>{row['Chengal trees to be fell']}</td>
            </tr>
            """

        table_html += """</tbody>
        </table>
        """

        st.markdown(table_html, unsafe_allow_html=True)

        ######### PAGE 2

        data_1986 = pd.read_csv('Updated_Merged_Dataset_2HectarP.csv')
        data_1986 = data_1986.round(2)
        print(data_1986['Total Biomassyt'])

        data_1986['Total Biomassyt'] = (data_1986['Total Biomassyt'] / 1000).round(2)
        #data_1986['Total Carbon Stockyt'] = (data_1986['Total Carbon Stockyt'] / 1000).round(2)
        data_1986['Total Carbon Stockyt'] = pd.to_numeric(data_1986['Total Carbon Stockyt'])


        def create_dataframe_now(filtered_data):
            result = []
            for idx, (_, row) in enumerate(filtered_data.iterrows(), start=1):  # Start index at 1
                # Correct the logical condition and adjust "Action Time"
                if row['Year'] == 2021 or row['Year'] == 2026:
                    action_time = f"Now ({row['Year']})"
                else:
                    continue
                entry = {
                    "Plan ID": f"P{idx}",  # Create a unique Plan ID
                    "Action Time": action_time,
                    "Total Volume": row['Total Volume'],
                    "Total Carbon Stockyt": row['Total Carbon Stockyt'],
                    "Total Biomassyt": row['Total Biomassyt'],
                    "Remaining Trees": row['Remaining Trees'],  # Fixed the column name
                    "Unique Species": row['Unique Species'],
                    "Carbon Loss": row['carbon_loss']
                }
                result.append(entry)
            return pd.DataFrame(result)

        def create_dataframe_predicted(filtered_data):
            result = []
            indx = 1
            for idx1, (_, row) in enumerate(filtered_data.iterrows(), start=1):  # Start index at 1
                # Correct the logical condition and adjust "Action Time"
                if row['Year'] == 2051 or row['Year'] == 2056:

                    action_time = f"({row['Year']})"
                else:
                    continue
                entry = {
                    "Plan ID": f"P{indx}",  # Create a unique Plan ID
                    "Action Time": action_time,
                    "Total Volume": row['Total Volume'],
                    "Total Carbon Stockyt": row['Total Carbon Stockyt'],
                    "Total Biomassyt": row['Total Biomassyt'],
                    "Remaining Trees": row['Remaining Trees'],  # Fixed the column name
                    "Unique Species": row['Unique Species'],
                    "Carbon Loss": row['carbon_loss']

                }
                indx += 1
                result.append(entry)
            return pd.DataFrame(result)

        filtered_data = data_1986[data_1986['Hectare'] == selected_hectare]

        column_mapping = {
            "Remaining Carbon (t/ha)": "Total Carbon Stockyt",
            "Carbon Loss (t/ha)": "carbon_loss",
            "Remaining Volume (m3/ha)": "Total Volume",
            "Remaining Biomass (t/ha)": "Total Biomassyt",
        }

        # Create a new DataFrame with only the relevant columns
        mapped_data = filtered_data[list(column_mapping.values())]
        mapped_data.columns = column_mapping.keys()  # Rename columns to target fields

        # Calculate max and min values for the mapped columns
        max_min_values = {
            column: {"max": mapped_data[column].max(), "min": mapped_data[column].min()}
            for column in mapped_data.columns
        }

        def apply_colors(value, column, max_min_values=max_min_values):
            max_val = max_min_values[column]["max"]
            min_val = max_min_values[column]["min"]

            if column == "Carbon Loss (t/ha)":  # Special case for Carbon Loss
                if value == min_val:
                    return "green"
                elif value == max_val:
                    return "red"
            else:  # Default case for other columns
                if value == max_val:
                    return "green"
                elif value == min_val:
                    return "red"

        col1, col2 = st.columns(2)
        ## tbl1
        datanow = create_dataframe_now(filtered_data)
        # HTML for the table, including styles
        st.markdown("""
            <style>
                .table-container {
                    margin-top: 20px;
                    padding: 20px;
                    background-color: #f7f7f7;
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                }

                table {
                    width: 100%;
                    border-collapse: collapse;
                    font-size: 15px;
                    background-color: white;
                }

                th {
                    background-color: #e4e4e4;
                    text-align: center;
                    padding: 10px;
                    font-weight: bold;
                    border: 1px solid #ddd;
                }

                td {
                    text-align: center;
                    padding: 10px;
                    border: 1px solid #ddd;
                }

                tr:nth-child(even) {
                    background-color: #f9f9f9;
                }

                tr:hover {
                    background-color: #f1f1f1;
                }

                .green { background-color: #28a745; color: white; }
                .yellow { background-color: #ffc107; color: black; }
                .red { background-color: #dc3545; color: white; }

                .plan-id {
                    background-color: #d1d3e2;
                    color: #2c3e50;
                    font-weight: bold;
                    text-align: center;
                    border-radius: 5px;
                    padding: 8px;
                }

                .header-row {
                    background-color: #f1f1f1;
                }

            </style>
        """, unsafe_allow_html=True)
        html = """<h3>Immediate</h3>
            <table>
                <thead>
                    <tr class="header-row">
                        <th>Plan ID</th>
                        <th colspan="6" style="text-align:center;">Immediate Implications</th>
                    </tr>
                    <tr>
                        <th></th>
                        <th>Remaining Carbon (t/ha)</th>
                        <th>Carbon Loss (t/ha)</th>
                        <th>Remaining Volume (m3/ha)</th>
                        <th>Remaining Biomass (t/ha)</th>
                        <th>Remaining Species</th>
                        <th>Remaining Trees</th>
                    </tr>
                </thead>
                <tbody>"""

        # Populate rows with data and apply colors dynamically
        for _, row in datanow.iterrows():
            html += f"""<tr>
                    <td class="plan-id">{row['Plan ID']}</td>
                    <td class="{apply_colors(row['Total Carbon Stockyt'], 'Remaining Carbon (t/ha)')}">{row['Total Carbon Stockyt']}</td>
                    <td class="{apply_colors(row['Carbon Loss'], 'Carbon Loss (t/ha)')}">{row['Carbon Loss']}</td>
                    <td class="{apply_colors(row['Total Volume'], 'Remaining Volume (m3/ha)')}">{row['Total Volume']}</td>
                    <td class="{apply_colors(row['Total Biomassyt'], 'Remaining Biomass (t/ha)')}">{row['Total Biomassyt']}</td>
                    <td>{row['Unique Species']}</td>
                    <td>{row['Remaining Trees']}</td>
                </tr>"""

        html += "</tbody></table>"

        with col1:
            st.markdown(html, unsafe_allow_html=True)

        ######## tbl2
        data_2030 = pd.read_csv('Updated_Merged_Dataset_2030_2HectarP.csv')
        data_2030['Total Biomassyt'] = (data_2030['Total Biomassyt'] / 1000).round(2)
        data_2030['Total Carbon Stockyt'] = (data_2030['Total Carbon Stockyt'] / 1000).round(2)
        filtered_data = data_2030[data_2030['Hectare'] == selected_hectare]

        column_mapping = {
            "Remaining Carbon (t/ha)": "Total Carbon Stockyt",
            "Carbon Loss (t/ha)": "carbon_loss",
            "Remaining Volume (m3/ha)": "Total Volume",
            "Remaining Biomass (t/ha)": "Total Biomassyt",
        }

        # Create a new DataFrame with only the relevant columns
        mapped_data = filtered_data[list(column_mapping.values())]
        mapped_data.columns = column_mapping.keys()  # Rename columns to target fields

        # Calculate max and min values for the mapped columns
        max_min_values = {
            column: {"max": mapped_data[column].max(), "min": mapped_data[column].min()}
            for column in mapped_data.columns
        }

        def apply_colors(value, column, max_min_values=max_min_values):
            max_val = max_min_values[column]["max"]
            min_val = max_min_values[column]["min"]

            if column == "Carbon Loss (t/ha)":  # Special case for Carbon Loss
                if value == min_val:
                    return "green"
                elif value == max_val:
                    return "red"
            else:  # Default case for other columns
                if value == max_val:
                    return "green"
                elif value == min_val:
                    return "red"

        datapredicted = create_dataframe_predicted(filtered_data)
        # HTML for the table, including styles
        st.markdown("""
            <style>
                .table-container {
                    margin-top: 20px;
                    padding: 20px;
                    background-color: #f7f7f7;
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                }

                table {
                    width: 100%;
                    border-collapse: collapse;
                    font-size: 15px;
                    background-color: white;
                }

                th {
                    background-color: #e4e4e4;
                    text-align: center;
                    padding: 10px;
                    font-weight: bold;
                    border: 1px solid #ddd;
                }

                td {
                    text-align: center;
                    padding: 10px;
                    border: 1px solid #ddd;
                }

                tr:nth-child(even) {
                    background-color: #f9f9f9;
                }

                tr:hover {
                    background-color: #f1f1f1;
                }

                .green { background-color: #28a745; color: white; }
                .yellow { background-color: #ffc107; color: black; }
                .red { background-color: #dc3545; color: white; }

                .plan-id {
                    background-color: #d1d3e2;
                    color: #2c3e50;
                    font-weight: bold;
                    text-align: center;
                    border-radius: 5px;
                    padding: 8px;
                }

                .header-row {
                    background-color: #f1f1f1;
                }

            </style>
        """, unsafe_allow_html=True)
        html = """<h3>Predicted</h3>
            <table>
                <thead>
                    <tr class="header-row">
                        <th>Plan ID</th>
                        <th colspan="6" style="text-align:center;">Predicted Implications</th>
                    </tr>
                    <tr>
                        <th></th>
                        <th>Remaining Carbon (t/ha)</th>
                        <th>Carbon Loss (t/ha)</th>
                        <th>Remaining Volume (m3/ha)</th>
                        <th>Remaining Biomass (t/ha)</th>
                        <th>Remaining Species</th>
                        <th>Remaining Trees</th>
                    </tr>
                </thead>
                <tbody>"""

        # Populate rows with data and apply colors dynamically
        for _, row in datapredicted.iterrows():
            html += f"""<tr>
                    <td class="plan-id">{row['Plan ID']}</td>
                    <td class="{apply_colors(row['Total Carbon Stockyt'], 'Remaining Carbon (t/ha)')}">{row['Total Carbon Stockyt']}</td>
                    <td class="{apply_colors(row['Carbon Loss'], 'Carbon Loss (t/ha)')}">{row['Carbon Loss']}</td>
                    <td class="{apply_colors(row['Total Volume'], 'Remaining Volume (m3/ha)')}">{row['Total Volume']}</td>
                    <td class="{apply_colors(row['Total Biomassyt'], 'Remaining Biomass (t/ha)')}">{row['Total Biomassyt']}</td>
                    <td>{row['Unique Species']}</td>
                    <td>{row['Remaining Trees']}</td>
                </tr>"""

        html += "</tbody></table>"
        with col2:
            st.markdown(html, unsafe_allow_html=True)

        # ========== PAGE3

        # =========== select the PID
        import streamlit as st
        import pandas as pd

        # Function to load the main data
        @st.cache_data
        def load_data():
            # Replace this with your actual data or file
            return pd.DataFrame({
                "Plan ID": [f"P{i}" for i in range(1, 13)],
                "Objective": ["Volume", "Specie", "Volume", "Specie", "Volume", "Specie", "Volume", "Specie", "Volume",
                              "Specie", "Volume", "Specie"],
                "Regime": [20, 16, 12, 20, 16, 12, 20, 16, 12, 20, 16, 12]})

        # Load the data
        data = load_data()

        # Dropdown selection for Plan ID
        selected_plan = st.selectbox("Select a Plan ID*", data["Plan ID"].unique())

        # Display the selected plan's details
        selected_data = data[data["Plan ID"] == selected_plan]

        # Process the selected plan
        if not selected_data.empty:
            # Extract necessary details
            objective = selected_data["Objective"].iloc[0]
            regime = selected_data["Regime"].iloc[0]

            # Construct file name based on format
            if objective.lower() == "volume":
                folder = "hectare_analysis_results"
            elif objective.lower() == "specie":
                folder = "hectare_analysis_results2"
            else:
                folder = None

            if folder:
                file_name = f"{folder}/result_{selected_hectare}_{regime}.csv"

                # Try to load the file
                try:
                    file_data = pd.read_csv(file_name)
                except FileNotFoundError:
                    st.error(f"File {file_name} not found. Please check the directory and file name.")

        import streamlit.components.v1 as components

        total_rows_more_60 = len(file_data[file_data['dbh'] > 60])
        num_rows_more_60 = int(0.2 * total_rows_more_60)

        rows_45_60 = file_data[(file_data['dbh'] > 45) & (file_data['dbh'] <= 60)]
        total_rows_45_60 = len(rows_45_60)
        num_rows_45_60 = int(0.3 * total_rows_45_60)

        rows_30_45 = file_data[(file_data['dbh'] > 30) & (file_data['dbh'] <= 45)]
        total_rows_30_45 = len(rows_30_45)
        num_rows_30_45 = int(0.4 * total_rows_30_45)

        rows_15_30 = file_data[(file_data['dbh'] > 15) & (file_data['dbh'] <= 30)]
        total_rows_15_30 = len(rows_15_30)
        num_rows_15_30 = int(0.5 * total_rows_15_30)

        # HTML code for the animated cards with khaki color
        html_code = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                .card-container {
                    display: flex;
                    justify-content: space-around;
                    margin-top: 30px;
                    flex-wrap: wrap;
                }

                .card {
                    background-color: #F0E68C;  /* Khaki color */
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    padding: 20px;
                    width: 200px;
                    margin: 10px;
                    text-align: center;
                    transition: transform 0.3s ease, box-shadow 0.3s ease;
                }

                .card:hover {
                    transform: translateY(-10px);
                    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
                }

                .card h3 {
                    font-size: 18px;
                    color: #333;
                }

                .card p {
                    font-size: 24px;
                    font-weight: bold;
                    color: #555;
                    animation: fadeIn 1s ease-in-out;
                }

                @keyframes fadeIn {
                    0% { opacity: 0; }
                    100% { opacity: 1; }
                }
            </style>
        </head>"""
        import math
        html_code = html_code + f"""<body>
            <div class="card-container">
                <div class="card">
                    <h3>Logging Damage DBH 15-30cm</h3>
                    <p>{math.floor(num_rows_15_30* 0.0983* 0.0983)}</p>
                </div>
                <div class="card">
                    <h3>Logging Damage DBH 30-45cm</h3>
                    <p>{math.floor(num_rows_30_45* 0.0983)}</p>
                </div>
                <div class="card">
                    <h3>Logging Damage DBH 45-60cm</h3>
                    <p>{math.floor(num_rows_45_60* 0.0983)}</p>
                </div>
                <div class="card">
                    <h3>Logging Damage DBH 60cm</h3>
                    <p>{math.floor(num_rows_more_60 * 0.0983)}</p>
                </div>
            </div>
        </body>
        </html>
        """

        # Display the HTML in Streamlit
        components.html(html_code, height=220)

        import streamlit as st
        import pandas as pd
        import plotly.express as px

        # Creating the dataset from your provided data
        data = {
            "TAG": [2317, 2318, 2319, 2320, 2321, 2322, 2323, 2323, 2324, 2324, 2325, 2325, 2325, 2325, 2326, 2327,
                    2328, 2328],
            "Species": ["SHORP2", "MESURA", "CANAPA", "PAYELU", "GIROPA", "MACALO", "DACRR1", "MACALO", "KOOMMA",
                        "NAUCOF", "SHORL1",
                        "APORPR", "GREWMI", "MACALO", "EUGEPE", "RYPAKU", "EUGEDE", "AAAAA"],
            "QUAD": [1] * 18,
            "Hectare": [1] * 18,
            "XCO": [1.8, 3.3, 6, 7.9, 7.6, 9.5, 9.7, 0, 10.7, 10.5, 3.9, 4, 1.6, 3.6, 2.3, 2.4, 8.3, 0],
            "YCO": [5, 5, 1.8, 4.7, 6.9, 6.8, 10.9, 0, 11.6, 11.8, 10.8, 12.7, 13.7, 10.6, 11.3, 18.2, 15.9, 0]
        }

        # Converting the data into a pandas DataFrame
        df = pd.DataFrame(data)

        if objective.lower() == "specie":
            folder = "sp"
            file_name = f"{folder}/trees_to_cut_count_h{selected_hectare}.csv"
        elif objective.lower() == "volume":
            folder = "Volume"
            file_name = f"{folder}/trees_to_cut_h{selected_hectare}.csv"

        file_data = pd.read_csv(file_name)

        file_data = file_data[:regime]
        # Streamlit title and instructions
        st.title("Tree Location Visualization")
        st.markdown("""
            This plot shows the location of trees in the forest based on their X and Y coordinates.
            You can interact with the plot, zoom in/out, and hover over data points to see the details.
        """)

        # Create an interactive Plotly scatter plot
        fig = px.scatter(file_data, x="gx", y="gy", text="TreeID",
                         color="Species", hover_data=["Species", "Hectare"],
                         title="Tree Locations in the Forest",
                         labels={"XCO": "X Coordinate", "YCO": "Y Coordinate"})

        # Customize the layout for better UI
        fig.update_layout(
            plot_bgcolor="white",  # White background
            title_font=dict(size=24, family="Montserrat, sans-serif"),
            xaxis_title="X Coordinate",
            yaxis_title="Y Coordinate",
            xaxis=dict(showgrid=True, zeroline=False, showticklabels=True),
            yaxis=dict(showgrid=True, zeroline=False, showticklabels=True),
            hovermode="closest",
            font=dict(size=14, color="black", family="Arial, sans-serif"),
            showlegend=True
        )

        # Adding animation effect on hover (smooth zoom-in/out on hover)
        fig.update_traces(marker=dict(size=12, opacity=0.8, line=dict(width=2, color='DarkSlateGrey')),
                          selector=dict(mode='markers'))

        # Display the plot in Streamlit
        st.plotly_chart(fig, use_container_width=True)
        # +++++++++++++

        import pandas as pd
        import plotly.express as px
        import plotly.graph_objects as go
        import numpy as np

        tree_data = file_data

        # Add canopy radius calculation (smaller canopies)
        K = 0.05  # Reduced empirical constant for smaller canopies
        file_data["Canopy_Radius"] = file_data["DBH"] * K  # Radius in meters

        # Add canopy volume calculation
        file_data["Canopy_Volume"] = (4 / 3) * np.pi * (file_data["Canopy_Radius"] ** 3)
        st.write(file_data)
        file_data['Height_m'] = (122 * file_data['DBH']) / (2 * file_data['DBH'] + 61)

        # Create the 3D scatter plot (canopies)
        fig = px.scatter_3d(
            file_data,
            x="gx",  # X-axis (Tree location)
            y="gy",  # Y-axis (Tree location)
            z="Height_m",  # Z-axis (Tree height)
            text="TreeID",  # TreeID displayed on hover
            color="Species",  # Color based on tree species
            hover_data=["Species", "Hectare", "DBH", "Canopy_Radius", "Canopy_Volume"],  # Additional hover info
            title="Tree Locations with Canopy Calculations (3D)",
            labels={"gx": "X Coordinate", "gy": "Y Coordinate", "Height_m": "Height (m)"}
        )

        # Customize the layout for better UI and larger plot
        fig.update_layout(
            width=1000,  # Set the width of the plot
            height=800,  # Set the height of the plot
            plot_bgcolor="white",  # White background
            title_font=dict(size=24, family="Montserrat, sans-serif"),
            scene=dict(
                xaxis_title="X Coordinate",
                yaxis_title="Y Coordinate",
                zaxis_title="Height (m)",
                xaxis=dict(showgrid=True, zeroline=False, showticklabels=True),
                yaxis=dict(showgrid=True, zeroline=False, showticklabels=True),
                zaxis=dict(showgrid=True, zeroline=False, showticklabels=True),
            ),
            hovermode="closest",
            font=dict(size=14, color="black", family="Arial, sans-serif"),
            showlegend=True
        )

        # Add tree trunks as vertical lines with thickness based on DBH
        for _, row in file_data.iterrows():
            # Add vertical line (trunk)
            fig.add_trace(go.Scatter3d(
                x=[row["gx"], row["gx"]],
                y=[row["gy"], row["gy"]],
                z=[0, row["Height_m"]],
                mode='lines',
                line=dict(color="brown", width=row["DBH"] / 5),  # Thickness based on DBH
                name=f"Trunk {row['TreeID']}"
            ))

            # Add canopy as a sphere (smaller canopies)
            u = np.linspace(0, 2 * np.pi, 20)
            v = np.linspace(0, np.pi, 20)
            x = row["Canopy_Radius"] * np.outer(np.cos(u), np.sin(v)) + row["gx"]
            y = row["Canopy_Radius"] * np.outer(np.sin(u), np.sin(v)) + row["gy"]
            z = row["Canopy_Radius"] * np.outer(np.ones(np.size(u)), np.cos(v)) + row["Height_m"]

            fig.add_trace(go.Surface(
                x=x, y=y, z=z,
                colorscale="Greens",
                opacity=0.5,
                showscale=False,
                name=f"Canopy {row['TreeID']}"
            ))
        st.plotly_chart(fig, use_container_width=True)

        # Display the dataset in an expander
        with st.expander("View Dataset"):
            st.dataframe(file_data)  # Display the dataset as a table

        if objective.lower() == "specie":
            folder = "sp"
            file_name = f"final_hectare_analysis_results/final_updated_result_{selected_hectare}_{regime}.csv"
        elif objective.lower() == "volume":
            folder = "Volume"
            file_name = f"final_hectare_analysis_results/final_updated_result_{selected_hectare}_{regime}.csv"

        data = pd.read_csv(file_name)

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
                height_sums.append(category_data[f'dbh_year_{year}'].sum())

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
            st.subheader('DBH Over 30 Years')
            fig_height = px.line(
                filtered_data,
                x='Year',
                y='Height',
                color='Category',
                labels={'Year': 'Year', 'Height': 'Height'},
                title='DBH Trends Over 30 Years',
                template='plotly_white'
            )
            fig_height.update_layout(
                title={'x': 0.5},
                xaxis=dict(title='Year'),
                yaxis=dict(title='Height'),
                legend=dict(title='Category', orientation='h', x=0.5, xanchor='center', y=-0.2)
            )
            st.plotly_chart(fig_height, use_container_width=True)

        # Prepare DBH classification
        dbh_classes = {
            '<15': lambda dbh: dbh < 15,
            '15-30': lambda dbh: 15 <= dbh < 30,
            '30-45': lambda dbh: 30 <= dbh < 45,
            '45-60': lambda dbh: 45 <= dbh < 60,
            '>60': lambda dbh: dbh >= 60
        }

        # Create an empty DataFrame to store aggregated results
        aggregated_dbh_data = pd.DataFrame()

        # Iterate through years and classify by DBH classes
        for year in range(1, 31):
            year_data = {'Year': [], 'DBH Class': [], 'Volume': [], 'Carbon Stock': [], 'Biomass': []}

            # Calculate sums for each DBH class
            for dbh_class, condition in dbh_classes.items():
                filtered_data = data[data[f'dbh_year_{year}'].apply(condition)]
                year_data['Year'].append(year)
                year_data['DBH Class'].append(dbh_class)
                year_data['Volume'].append(filtered_data[f'volume_year_{year}'].sum())
                year_data['Carbon Stock'].append(filtered_data[f'carbon_stockyt_year_{year}'].sum())
                year_data['Biomass'].append(filtered_data[f'biomassyt_year_{year}'].sum())

            # Append the year's data to the aggregated DataFrame
            aggregated_dbh_data = pd.concat([aggregated_dbh_data, pd.DataFrame(year_data)])

        # Display bar charts for DBH classes
        metrics = ['Volume', 'Carbon Stock', 'Biomass']

        for metric in metrics:
            st.subheader(f'{metric} Grouped by DBH Class Over 30 Years')

            # Create a bar chart for the metric
            fig = px.bar(
                aggregated_dbh_data,
                x='Year',
                y=metric,
                color='DBH Class',
                barmode='group',
                labels={'Year': 'Year', metric: metric},
                title=f'{metric} Grouped by DBH Class',
                template='plotly_white'
            )

            # Customize layout for better visuals
            fig.update_layout(
                title={'x': 0.5},  # Center the title
                xaxis=dict(title='Year'),
                yaxis=dict(title=metric),
                legend=dict(title='DBH Class', orientation='h', x=0.5, xanchor='center', y=-0.2)
            )

            # Show the chart
            st.plotly_chart(fig, use_container_width=True)