
def start_home():
    import base64
    from streamlit_card import card
    import pandas as pd

    import folium
    import streamlit as st
    def clustering2019(x_axis_ranges, df):
        df_ranges = pd.DataFrame(index=x_axis_ranges)
        for column in df.columns:
            col_values = []
            for x_range in x_axis_ranges:
                if '-' in x_range:
                    start, end = map(int, x_range.split('-'))
                    filtered_values = df[column][(df[column] >= start) & (df[column] <= end)]
                else:
                    filtered_values = df[column][df[column] == int(x_range)]
                col_values.append(filtered_values.count())
            df_ranges[column] = col_values

        # Create a bar chart using Plotly

        # Using Plotly Express to create a grouped bar chart with custom colors
        fig = px.bar(df_ranges, x=['1-5', '6-11', '12-17', '18-23', '24<'], y=df_ranges.columns, barmode='group',
                     color_discrete_sequence=px.colors.qualitative.Dark24)

        # Updating the layout
        fig.update_layout(
            title=dict(text='Actual and Predicted Number of Trees (In each DBH Classes) 2019', x=0.10,
                       font=dict(color='dark green')),

            xaxis_title=dict(text='DBH Class', font=dict(color='purple')),
            yaxis_title=dict(text='Number of Trees', font=dict(color='purple')),
            xaxis=dict(tickangle=45)

        )
        # Displaying the chart using Streamlit
        st.plotly_chart(fig)


    # -----------------------------------------------------------------------------------------------bar chart function 2021
    def clustering2021(x_axis_ranges, df):
        df_ranges = pd.DataFrame(index=x_axis_ranges)
        for column in df.columns:
            col_values = []
            for x_range in x_axis_ranges:
                if '-' in x_range:
                    start, end = map(int, x_range.split('-'))
                    filtered_values = df[column][(df[column] >= start) & (df[column] <= end)]
                else:
                    filtered_values = df[column][df[column] == int(x_range)]
                col_values.append(filtered_values.count())
            df_ranges[column] = col_values

        custom_colors = ['orange', 'blue', 'orange', 'blue', 'orange']  # Add more colors as needed

        fig = px.bar(df_ranges, x=['1-5', '6-11', '12-17', '18-23', '24<'], y=df_ranges.columns, barmode='group',
                     color_discrete_sequence=custom_colors * 2)

        # Updating the layout
        fig.update_layout(
            title=dict(text='Actual and Predicted Number of Trees (In each DBH Classes) 2021', x=0.10,
                       font=dict(color='dark green')),

            xaxis_title=dict(text='DBH Class', font=dict(color='Blue')),
            yaxis_title=dict(text='Number of Trees', font=dict(color='Blue')),
            xaxis=dict(tickangle=45)
        )

        # Displaying the chart using Streamlit
        st.plotly_chart(fig)


    # ------------------------------------------------------------------------------------------------------Add Space
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    # ------------------------------------------------------------------------------------------------Scatter function
    import plotly.express as px


    def mapshow2019(df):
        df['SP'] = df['SP'].astype('category')  # Convert 'SP' column to categorical

        fig = px.scatter(df, x='XCO', y='YCO', color='SP')

        # Update title attributes
        fig.update_layout(
            title=dict(text='Actual Location of Trees', x=0.3, y=0.9,  # Adjust x and y to change title position
                       font=dict(color='dark green', size=20, family='Arial')),  # Change title font attributes
            xaxis_title=dict(text='XCO Title', font=dict(color='green')),  # Change x-axis title and color
            yaxis_title=dict(text='YCO Title', font=dict(color='green'))  # Change y-axis title and color
        )

        st.plotly_chart(fig)




    # ------------------------------------------------------------------------------------------------------text box
    import streamlit as st


    def display_design_element():

        st.subheader("for Pasoh Forest Reserve")
        st.image('Pasoh.jpeg', caption='Pasoh Forest Reserve')

        text = (" The Pasoh Forest Reserve, \na nature reserve located about 8 km from Simpang Pertang, "
                "Malaysia and around 70 km southeast of Kuala Lumpur. It has a total area of 2,450 hectares,"
                " with a core area of 600 ha surrounded by a buffer zone. "
                "Palm oil plantations surround the reserve on three sides while the other side "
                "adjoins a selectively logged dipterocarp forest. An average of 2 metres of rain fall each year, "
                "ranging from 1,728 to 3,112 mm. In 1987, a 50 hectare forest dynamics plot was established in the reserve."
                " Several censuses of sever population in the plot have been carried out, "
                "the first in 1989, and have counted about 340,000 trees belonging to more that 800 species in that plot.")
        font_size = 17
        font_color = "#333333"  # Dark grey
        border_color = "#568203"  # green
        border_width = 2

        # Display the bordered text box for design visualization
        st.markdown(
            f"""
            <div style="padding:10px; border: {border_width}px solid {border_color}; border-radius: 5px;">
                <p style="font-size: {font_size}px; color: {font_color};">{text}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


    # -----------------------------------------------------------------------------------Call first text
    st.title('Ecology Simulator')

    # Display the design element
    display_design_element()
    # -------------------------------------------------------------------------------Call Text Box


    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    # ----------------------------------------------------------------------------------------Text in colomns
    import streamlit as st


    st.title("Pasoh Forest Reserve Information")

    left_column, right_column = st.columns(2)

    # Left column content
    with left_column:
        st.header("Ecological Zone")
        st.write("Forest Type:  Tropical rainforest")
        st.write("Number of species:  948")
        st.write("Number of stems:  444,338")
        st.write("Number of Trees:  435,839")

    # Right column content
    with right_column:
        st.header("Details")
        st.write("Size: 50.00ha")
        st.write("Dimensions: 1000 x 500")
        st.write("Latitude: 2.982000000000")
        st.write("Longitude: 102.313000000000")



        # ---------------------------------------------------------------------------------------------------map
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

        import streamlit as st
        import folium
        def folium_static_map(m):
            width, height = 700, 400
            html = m.get_root().render()
            st.components.v1.html(html, width=width, height=height)

        st.title("Pasoh Forest Reserve Location")

        # Coordinates for Pasoh Forest Reserve
        pasoh_coords = (2.982000000000, 102.313000000000)

        # Create a Folium map centered around Pasoh Forest Reserve
        map_pasoh = folium.Map(location=pasoh_coords, zoom_start=10)

        # Add a marker for Pasoh Forest Reserve
        folium.Marker(location=pasoh_coords, popup="Pasoh Forest Reserve").add_to(map_pasoh)

        # Display the map using st.write()
        folium_static_map(map_pasoh)
    #if option_tomenu == 'Summary':

    df = pd.read_csv("Datasets/NewDataset.csv")

    def read_pics(path):
        with open(path, "rb") as f:
            data = f.read()
            encoded = base64.b64encode(data)
        data = "data:image/png;base64," + encoded.decode("utf-8")
        return  data


    def calculate_average_growth_rate(selected_years):
        selected_data = df[df['Year'].isin(selected_years)]
        average_growth_rate = selected_data['Growth rate'].mean()
        return average_growth_rate


    def calculate_mortality_rate(selected_years):
        selected_data = df[df['Year'].isin(selected_years)]
        total_trees = selected_data.shape[0]
        dead_trees = selected_data[selected_data['Status'] == 'Dead'].shape[0]
        if total_trees == 0:
            return 0
        mortality_rate = (dead_trees / total_trees) * 100
        return mortality_rate


    def calculate_new_recruitment_rate(selected_years):
        total_recruits = 0
        for year in selected_years:
            current_year_data = df[(df['Year'] == year) & (df['DBH'] != 0)]
            previous_year_data = df[(df['Year'] == year - 2) & (df['DBH'] == 0)]
            recruits = current_year_data.shape[0] - previous_year_data.shape[0]
            total_recruits += recruits
        avg_recruits = total_recruits / len(selected_years)
        return avg_recruits


    def get_top_species(selected_years):
        # Filter data for selected years
        selected_data = df[df['Year'].isin(selected_years)]
        # Group by 'SP' and sum 'Dom' for each species
        species_dom_sum = selected_data.groupby('Species')['Dom'].sum()
        # Get top 5 species with highest sum of 'Dom'
        top_species = species_dom_sum.nlargest(5)
        return top_species


    def calculate_dbh_growth(selected_years):
        # Filter data for selected years
        selected_data = df[df['Year'].isin(selected_years)]
        # Group by 'Species' and calculate DBH growth between consecutive years
        species_dbh_growth = selected_data.groupby('Species').apply(
            lambda x: x[x['Year'] == max(selected_years)]['DBH'].mean() - x[x['Year'] == min(selected_years)][
                'DBH'].mean())
        # Get top 5 species with highest DBH growth
        top_species_growth = species_dbh_growth.nlargest(5)
        return top_species_growth


    def calculate_species_carbon(selected_years):
        # Filter data for selected years
        selected_data = df[df['Year'].isin(selected_years)]
        # Group by 'Species' and calculate sum of carbon for each species
        species_carbon_sum = selected_data.groupby('Species')['Carbon'].sum()
        # Get top 5 species with highest sum of carbon
        top_species_carbon = species_carbon_sum.nlargest(5)
        return top_species_carbon


    def calculate_species_mortality_rate(selected_years):
        # Filter data for selected years
        selected_data = df[df['Year'].isin(selected_years)]
        # Group by 'Species' and calculate mortality rate for each species
        species_total = selected_data.groupby(['Species', 'Status']).size().unstack().fillna(0)
        species_total['Mortality Rate'] = (species_total['Dead'] / (
                species_total['Dead'] + species_total['Alive'])) * 100
        species_mortality_rate = species_total['Mortality Rate'].sort_values(ascending=False)
        # Get top 5 species with highest mortality rate
        top_species_mortality_rate = species_mortality_rate.nlargest(5)
        return top_species_mortality_rate


    def calculate_size_class_count(selected_years):
        # Filter data for selected years
        selected_data = df[df['Year'].isin(selected_years)]
        # Group by 'Size Class' and count occurrences for each Size Class
        size_class_count = selected_data.groupby('Size Class').size().reset_index(name='Count')
        # Calculate total count across all Size Classes
        total_count = size_class_count['Count'].sum()
        return size_class_count, total_count


    def create_scatter_plot(selected_years):
        # Filter data for selected years
        selected_data = df[df['Year'].isin(selected_years)]
        # Create scatter plot for each selected year
        for year in selected_years:
            fig = px.scatter(selected_data[selected_data['Year'] == year], x='XCO', y='YCO', color='Species',
                             title=f'Species Distribution in Year {year}',
                             labels={'XCO': 'X Coordinate', 'YCO': 'Y Coordinate'})
            st.plotly_chart(fig)

    selected_years = st.sidebar.multiselect("Select Years", sorted(df['Year'].unique()), default=[2019, 2021])
    if selected_years:
        average_growth_rate = calculate_average_growth_rate(selected_years)
        mortality_rate = calculate_mortality_rate(selected_years)
        new_recruitment_rate = calculate_new_recruitment_rate(selected_years)

        col1, col2 = st.columns(2)
        with col1:
            st.image('pages/Pics/weather1.png')
            st.image('pages/Pics/weather2.png')
        with col2:
            st.image('pages/Pics/weather4.png')

        col1, col2, col3 = st.columns(3)
        with col1:
            growthRate = card(
                title=f'Growth Rate {average_growth_rate:.2f}',
                text='Avrage (mm/year)' ,
                image=read_pics('Pics/growthrate.jpg'),
                url = "https://github.com/gamcoh/st-card"
            )
        with col2:
            mortalityrate = card(
                title=f"Mortality Rate {mortality_rate:.2f}",
                text="Avrage (number/year)",
                image=read_pics('Pics/Mortality.jpeg'),
                url="https://github.com/gamcoh/st-card"
            )
        with col3:
            newrecrit = card(
                title=f"New Recruit {new_recruitment_rate:.2f}",
                text="Avrage (number/year)",
                image=read_pics('Pics/newtree.jpeg'),
                url="https://github.com/gamcoh/st-card"
            )


        col1 , col2 = st.columns(2)

        #---------------- DOM
        with col1:
            import plotly.express as px

            # Adjust these parameters according to your preference
            bar_width = 0.1  # Width of the bars
            bar_gap = 0.1  # Gap between bars

            top_species = get_top_species(selected_years)

            # Plot bar chart with adjusted size and width
            import plotly.express as px

            fig = px.bar(top_species,
                         x=top_species.index,
                         y=top_species.values,
                         labels={'x': 'Species', 'y': 'Sum of DOM'},
                         title='Top 5 Species with Highest Sum of DOM',
                         width=700,  # Adjust width of the chart
                         height=450,  # Adjust height of the chart
                         barmode='group',  # Set barmode to 'group' to group bars
                         opacity=0.6,  # Adjust opacity of the bars
                         color_discrete_sequence=['green'],  # Adjust color of the bars
                         )

            st.plotly_chart(fig)

        #------------------ growth
        with col2:
            top_species_growth = calculate_dbh_growth(selected_years)
            # Plot bar chart with Plotly Express
            fig = px.bar(top_species_growth, x=top_species_growth.index, y=top_species_growth.values,
                         labels={'x': 'Species', 'y': 'DBH Growth'}, title='Top 5 Species with Highest DBH Growth')
            st.plotly_chart(fig)


        col1 , col2 = st.columns(2)

        #------------------------ Carbon
        with col1:
            import plotly.express as px

            top_species_carbon = calculate_species_carbon(selected_years)

            # Plot bar chart with adjusted width
            fig = px.bar(top_species_carbon,
                         x=top_species_carbon.index,
                         y=top_species_carbon.values,
                         labels={'x': 'Species', 'y': 'Carbon Content'},
                         title='Top 5 Species with Highest Carbon Content',
                         width=700,  # Adjust width of the chart
                         height=450,  # Adjust height of the chart
                         barmode='group',  # Set barmode to 'group' to group bars
                         opacity=0.7,  # Adjust opacity of the bars
                         color_discrete_sequence=['green']
                         )

            st.plotly_chart(fig)

        # ------------------- Mortality
        with col2:
            top_species_mortality_rate = calculate_species_mortality_rate(selected_years)
            # Plot bar chart with Plotly Express
            fig = px.bar(top_species_mortality_rate, x=top_species_mortality_rate.index,
                         y=top_species_mortality_rate.values, labels={'x': 'Species', 'y': 'Mortality Rate'},
                         title='Top 5 Species with Highest Mortality Rate')
            st.plotly_chart(fig)


        col1 , col2 = st.columns(2)


        # ----- ----- ----- ----- ----- DHB
        with col1:
            size_class_count, total_count = calculate_size_class_count(selected_years)
            # Plot bar chart with Plotly Express

            fig = px.bar(size_class_count,
                         x='Size Class',
                         y='Count',
                         labels={'x': 'Size Class', 'y': 'Count'},
                         title='Count of Each Size Class for Selected Years',
                         width=700,  # Adjust width of the chart
                         height=450,  # Adjust height of the chart
                         barmode='group',  # Set barmode to 'group' to group bars
                         opacity=0.9,  # Adjust opacity of the bars
                         color_discrete_sequence=['green']
                         )


            st.plotly_chart(fig)

        # ---------------------------------- MAP

        with col2:
            import folium
            def folium_static_map(m):
                width, height = 700, 400
                html = m.get_root().render()
                st.components.v1.html(html, width=width, height=height)

            st.title("Pasoh Forest Reserve Location")

            # Coordinates for Pasoh Forest Reserve
            pasoh_coords = (2.982000000000, 102.313000000000)

            # Create a Folium map centered around Pasoh Forest Reserve
            map_pasoh = folium.Map(location=pasoh_coords, zoom_start=10)

            # Add a marker for Pasoh Forest Reserve
            folium.Marker(location=pasoh_coords, popup="Pasoh Forest Reserve").add_to(map_pasoh)

            # Display the map using st.write()
            folium_static_map(map_pasoh)


        # ----- --- --- --- --- --- --- --- --- --- --- 2D

        create_scatter_plot(selected_years)