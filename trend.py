def start_trend():
    import pandas as pd
    import folium
    import streamlit as st
    from streamlit_option_menu import option_menu

    df = pd.read_csv("Datasets/NewDataset.csv")
    option_tomenutype = option_menu(None, ["Growth", "DBH size class", "AGB", 'Carbon stock', 'Mortality', 'Lifespan'],
                                menu_icon="cast", default_index=0, orientation="horizontal")
    import plotly.express as px
    import streamlit as st

    if option_tomenutype == 'Growth':
        def create_bar_chart_growth(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'size class' and calculate average 'Growth' for each size class
            size_class_growth = selected_data.groupby('Size Class')['Growth'].sum().reset_index()
            # Calculate average growth across all size classes
            average_growth = size_class_growth['Growth'].mean()
            # Create bar chart
            fig = px.bar(size_class_growth, x='Size Class', y='Growth',
                         title=f'Sum of Growth Across Size Classes for Year {selected_year}',
                         labels={'Size Class': 'Size Class', 'Growth': 'Growth'})
            # Change bar color and size
            fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.6)
            # Add dashed line for average growth
            fig.add_shape(type='line', x0=size_class_growth['Size Class'].iloc[0], y0=average_growth,
                          x1=size_class_growth['Size Class'].iloc[-1], y1=average_growth,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=500, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Total Growth Across Size Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_growth(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative growth values
            selected_data = selected_data[selected_data['Growth'] >= 0]

            # Group by 'Size Class' and calculate sum of 'Growth' for each size class
            size_class_growth = selected_data.groupby('Size Class')['Growth'].sum().reset_index()

            # Calculate total growth
            total_growth = size_class_growth['Growth'].sum()

            # Create pie chart
            fig = px.pie(size_class_growth, values='Growth', names='Size Class',
                         title=f'Total Growth Across Size Classes for Year {selected_year}',
                         labels={'Growth': 'Growth', 'Size Class': 'Size Class'},
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)
        # Function to create bar chart for growth rate distribution across size classes for a selected year
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st



        def create_bar_chart_growth_rate(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'size class' and calculate average 'Growth rate' for each size class
            size_class_growth_rate = selected_data.groupby('Size Class')['Growth rate'].mean().reset_index()
            # Calculate average growth rate across all size classes
            average_growth_rate = size_class_growth_rate['Growth rate'].mean()
            # Create bar chart
            fig = px.bar(size_class_growth_rate, x='Size Class', y='Growth rate',
                         title=f'Average Growth Rate Across Size Classes for Year {selected_year}')
            fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.6)

            # Add dashed line for average growth rate
            fig.add_shape(type='line', x0=-0.5, y0=average_growth_rate, x1=len(size_class_growth_rate) - 0.5,
                          y1=average_growth_rate,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=500, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Average Growth Rate Across Size Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_growth_rate(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative growth rate values
            selected_data = selected_data[selected_data['Growth rate'] >= 0]

            # Group by 'Size Class' and calculate average 'Growth rate' for each size class
            size_class_growth_rate = selected_data.groupby('Size Class')['Growth rate'].mean().reset_index()

            # Calculate average growth rate across all size classes
            average_growth_rate = size_class_growth_rate['Growth rate'].mean()

            # Create pie chart
            fig = px.pie(size_class_growth_rate, values='Growth rate', names='Size Class',
                         title=f'Average Growth Rate Across Size Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_bar_chart_growth_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'Age Class' and calculate average 'Growth' for each age class
            age_class_growth = selected_data.groupby('Age Class')['Growth'].mean().reset_index()
            # Calculate average growth across all age classes
            average_growth = age_class_growth['Growth'].mean()
            # Create bar chart
            fig = px.bar(age_class_growth, x='Age Class', y='Growth',
                         title=f'Average Growth Across Age Classes for Year {selected_year}')
            # Change bar color and size
            fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=0.7)
            # Add dashed line for average growth
            fig.add_shape(type='line', x0=-0.5, y0=average_growth, x1=len(age_class_growth) - 0.5, y1=average_growth,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=450, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Total Growth Across Age Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_growth_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative growth values
            selected_data = selected_data[selected_data['Growth'] >= 0]

            # Group by 'Age Class' and calculate average 'Growth' for each age class
            age_class_growth = selected_data.groupby('Age Class')['Growth'].mean().reset_index()

            # Calculate average growth across all age classes
            average_growth = age_class_growth['Growth'].mean()

            # Create pie chart
            fig = px.pie(age_class_growth, values='Growth', names='Age Class',
                         title=f'Average Growth Across Age Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=450, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        # Function to create bar chart for average growth rate across age classes for a selected year
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_bar_chart_growth_rate_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'Age Class' and calculate average 'Growth rate' for each age class
            age_class_growth_rate = selected_data.groupby('Age Class')['Growth rate'].mean().reset_index()
            # Calculate average growth rate across all age classes
            average_growth_rate = age_class_growth_rate['Growth rate'].mean()
            # Create bar chart
            fig = px.bar(age_class_growth_rate, x='Age Class', y='Growth rate',
                         title=f'Average Growth Rate Across Age Classes for Year {selected_year}')
            # Change bar color and size
            fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=0.7)
            # Add dashed line for average growth rate
            fig.add_shape(type='line', x0=-0.5, y0=average_growth_rate, x1=len(age_class_growth_rate) - 0.5,
                          y1=average_growth_rate,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=450, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Average Growth Rate Across Age Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_growth_rate_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative growth rate values
            selected_data = selected_data[selected_data['Growth rate'] >= 0]

            # Group by 'Age Class' and calculate average 'Growth rate' for each age class
            age_class_growth_rate = selected_data.groupby('Age Class')['Growth rate'].mean().reset_index()

            # Calculate average growth rate across all age classes
            average_growth_rate = age_class_growth_rate['Growth rate'].mean()

            # Create pie chart
            fig = px.pie(age_class_growth_rate, values='Growth rate', names='Age Class',
                         title=f'Average Growth Rate Across Age Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=450, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_growth_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Age Class' and calculate average 'Growth' for each age class
                age_class_growth = selected_data.groupby('Age Class')['Growth'].mean().reset_index()

                # Calculate average growth across all age classes
                average_growth = age_class_growth['Growth'].mean()

                # Filter out negative growth values
                age_class_growth = age_class_growth[age_class_growth['Growth'] >= 0]

                # Create pie chart
                fig = px.pie(age_class_growth, values='Growth', names='Age Class',
                             title=f'Total Growth Across Age Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)
        def create_bar_chart_growth_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'Growth' for each age class
                age_class_growth = selected_data.groupby('Age Class')['Growth'].mean().reset_index()
                # Calculate average growth across all age classes
                average_growth = age_class_growth['Growth'].mean()
                # Create bar chart
                fig = px.bar(age_class_growth, x='Age Class', y='Growth',
                             title=f'Sum of Growth Across Age Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.8)
                # Add dashed line for average growth
                fig.add_shape(type='line', x0=-0.5, y0=average_growth, x1=len(age_class_growth) - 0.5, y1=average_growth,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Total Growth Across Age Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        # Function to create bar chart for average growth rate across age classes for selected hectares
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_growth_rate_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Age Class' and calculate average 'Growth rate' for each age class
                age_class_growth_rate = selected_data.groupby('Age Class')['Growth rate'].mean().reset_index()

                # Calculate average growth rate across all age classes
                average_growth_rate = age_class_growth_rate['Growth rate'].mean()

                # Filter out negative growth rate values
                age_class_growth_rate = age_class_growth_rate[age_class_growth_rate['Growth rate'] >= 0]

                # Create pie chart
                fig = px.pie(age_class_growth_rate, values='Growth rate', names='Age Class',
                             title=f'Average Growth Rate Across Age Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)

        def create_bar_chart_growth_rate_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'Growth rate' for each age class
                age_class_growth_rate = selected_data.groupby('Age Class')['Growth rate'].mean().reset_index()
                # Calculate average growth rate across all age classes
                average_growth_rate = age_class_growth_rate['Growth rate'].mean()
                # Create bar chart
                fig = px.bar(age_class_growth_rate, x='Age Class', y='Growth rate',
                             title=f'Average Growth Rate Across Age Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.8)
                # Add dashed line for average growth rate
                fig.add_shape(type='line', x0=-0.5, y0=average_growth_rate, x1=len(age_class_growth_rate) - 0.5,
                              y1=average_growth_rate,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Average Growth Rate Across Age Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_growth_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Filter out negative growth values
                selected_data = selected_data[selected_data['Growth'] >= 0]

                # Group by 'Size Class' and calculate average 'Growth' for each size class
                size_class_growth = selected_data.groupby('Size Class')['Growth'].mean().reset_index()

                # Calculate average growth across all size classes
                average_growth = size_class_growth['Growth'].mean()

                # Create pie chart
                fig = px.pie(size_class_growth, values='Growth', names='Size Class',
                             title=f'Average Growth Across Size Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)


        def create_bar_chart_growth_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'Growth' for each age class
                age_class_growth = selected_data.groupby('Size Class')['Growth'].mean().reset_index()
                # Calculate average growth across all age classes
                average_growth = age_class_growth['Growth'].mean()
                # Create bar chart
                fig = px.bar(age_class_growth, x='Size Class', y='Growth',
                             title=f'Average Growth Across Size Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=1)
                # Add dashed line for average growth
                fig.add_shape(type='line', x0=-0.5, y0=average_growth, x1=len(age_class_growth) - 0.5, y1=average_growth,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Total Growth Across Size Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        # Function to create bar chart for average growth rate across age classes for selected hectares
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_growth_rate_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Filter out negative growth rate values
                selected_data = selected_data[selected_data['Growth rate'] >= 0]

                # Group by 'Size Class' and calculate average 'Growth rate' for each size class
                size_class_growth_rate = selected_data.groupby('Size Class')['Growth rate'].mean().reset_index()

                # Calculate average growth rate across all size classes
                average_growth_rate = size_class_growth_rate['Growth rate'].mean()

                # Create pie chart
                fig = px.pie(size_class_growth_rate, values='Growth rate', names='Size Class',
                             title=f'Average Growth Rate Across Size Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)
        def create_bar_chart_growth_rate_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'Growth rate' for each age class
                age_class_growth_rate = selected_data.groupby('Size Class')['Growth rate'].mean().reset_index()
                # Calculate average growth rate across all age classes
                average_growth_rate = age_class_growth_rate['Growth rate'].mean()
                # Create bar chart
                fig = px.bar(age_class_growth_rate, x='Size Class', y='Growth rate',
                             title=f'Average Growth Rate Across Size Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=1)
                # Add dashed line for average growth rate
                fig.add_shape(type='line', x0=-0.5, y0=average_growth_rate, x1=len(age_class_growth_rate) - 0.5,
                              y1=average_growth_rate,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Average Growth Rate Across Size Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        def create_bar_chart_5_top_sp(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'Hectare' and 'Species' and calculate mean 'Growth rate' for each species in each hectare
            species_growth_rate = selected_data.groupby(['Hectare', 'Species'])['Growth rate'].mean().reset_index()
            # Sort by 'Growth rate' in descending order within each hectare
            species_growth_rate['Rank'] = species_growth_rate.groupby('Hectare')['Growth rate'].rank(ascending=False)
            top_species = species_growth_rate[species_growth_rate['Rank'] <= 5]  # Select top 5 species in each hectare
            # Calculate average growth rate across all species
            average_growth_rate = top_species['Growth rate'].mean()
            # Create bar chart
            fig = px.bar(top_species, x='Hectare', y='Growth rate', color='Species',
                         title=f'Top 5 Species with Highest Growth Rates for Each Hectare - Year {selected_year}',
                         labels={'Growth rate': 'Mean Growth Rate', 'Hectare': 'Hectare'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(top_species['Hectare']), y0=average_growth_rate,
                          x1=max(top_species['Hectare']), y1=average_growth_rate,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        def create_pie_chart_5_top_sp(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Group by 'Hectare' and 'Species' and calculate mean 'Growth rate' for each species in each hectare
            species_growth_rate = selected_data.groupby(['Hectare', 'Species'])['Growth rate'].mean().reset_index()

            # Sort by 'Growth rate' in descending order within each hectare
            species_growth_rate['Rank'] = species_growth_rate.groupby('Hectare')['Growth rate'].rank(ascending=False)
            top_species = species_growth_rate[species_growth_rate['Rank'] <= 5]  # Select top 5 species in each hectare

            # Exclude negative growth rates
            top_species = top_species[top_species['Growth rate'] >= 0]

            # Calculate average growth rate across all species
            average_growth_rate = top_species['Growth rate'].mean()

            # Create pie chart
            fig = px.pie(top_species, values='Growth rate', names='Species',
                         title=f'Top 5 Species with Highest Growth Rates for Each Hectare - Year {selected_year}',
                         labels={'Growth rate': 'Mean Growth Rate', 'Species': 'Species'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average Growth Rate: {average_growth_rate:.2f}',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        def create_bar_chart_sp_year(df, selected_species):
            # Filter data for selected species
            selected_data = df[df['Species'].isin(selected_species)]
            # Group by 'Year' and 'Species' and calculate mean 'Growth rate' for each species in each year
            species_growth_rate = selected_data.groupby(['Year', 'Species'])['Growth rate'].mean().reset_index()
            # Calculate average growth rate across all years for selected species
            average_growth_rate = species_growth_rate['Growth rate'].mean()
            # Create bar chart
            fig = px.bar(species_growth_rate, x='Year', y='Growth rate', color='Species',
                         title='Mean Growth Rate of Selected Species Across Years',
                         labels={'Growth rate': 'Mean Growth Rate', 'Year': 'Year'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(species_growth_rate['Year']), y0=average_growth_rate,
                          x1=max(species_growth_rate['Year']), y1=average_growth_rate,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        def create_pie_chart_sp_year(df, selected_species):
            # Filter data for selected species
            selected_data = df[df['Species'].isin(selected_species)]

            # Filter out negative growth rates
            selected_data = selected_data[selected_data['Growth rate'] >= 0]

            # Group by 'Year' and 'Species' and calculate mean 'Growth rate' for each species in each year
            species_growth_rate = selected_data.groupby(['Year', 'Species'])['Growth rate'].mean().reset_index()

            # Calculate average growth rate across all years for selected species
            average_growth_rate = species_growth_rate['Growth rate'].mean()

            # Create pie chart
            fig = px.pie(species_growth_rate, values='Growth rate', names='Species',
                         title='Mean Growth Rate of Selected Species Across Years',
                         labels={'Growth rate': 'Mean Growth Rate', 'Species': 'Species'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average Growth Rate: {average_growth_rate:.2f}',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        def create_bar_chart_BDH_all_years_growthrate(df):
            # Group by 'Year' and 'DBH Size Class' and calculate mean 'Growth rate' for each DBH size class in each year
            dbh_growth_rate = df.groupby(['Year', 'Size Class'])['Growth rate'].mean().reset_index()
            # Calculate average growth rate across all years
            average_growth_rate = dbh_growth_rate['Growth rate'].mean()
            # Create bar chart
            fig = px.bar(dbh_growth_rate, x='Year', y='Growth rate', color='Size Class',
                         title='Mean Growth Rate for Each DBH Size Class Across Years',
                         labels={'Growth rate': 'Mean Growth Rate', 'Year': 'Year', 'Size Class': 'Size Class'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(dbh_growth_rate['Year']), y0=average_growth_rate,
                          x1=max(dbh_growth_rate['Year']), y1=average_growth_rate,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        def create_pie_chart_BDH_all_years_growthrate(df):
            # Group by 'DBH Size Class' and calculate mean 'Growth rate' for each DBH size class across all years
            dbh_growth_rate = df.groupby('Size Class')['Growth rate'].mean().reset_index()

            # Calculate average growth rate across all size classes
            average_growth_rate = dbh_growth_rate['Growth rate'].mean()

            # Create pie chart
            fig = px.pie(dbh_growth_rate, values='Growth rate', names='Size Class',
                         title='Mean Growth Rate for Each DBH Size Class Across Years',
                         labels={'Growth rate': 'Mean Growth Rate', 'Size Class': 'Size Class'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average Growth Rate: {average_growth_rate:.2f}',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        def create_bar_chart_BDH_all_years_growth(df):
            # Group by 'Year' and 'DBH Size Class' and calculate sum 'Growth' for each DBH size class in each year
            dbh_growth = df.groupby(['Year', 'Size Class'])['Growth'].sum().reset_index()
            # Calculate average growth across all years
            average_growth = dbh_growth['Growth'].mean()
            # Create bar chart
            fig = px.bar(dbh_growth, x='Year', y='Growth', color='Size Class',
                         title='Sum Growth for Each DBH Size Class Across Years',
                         labels={'Growth': 'Sum Growth', 'Year': 'Year', 'Size Class': 'Size Class'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(dbh_growth['Year']), y0=average_growth,
                          x1=max(dbh_growth['Year']), y1=average_growth,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)






        st.sidebar.header("Setting")
        selected_year = st.sidebar.radio("Select Year", df['Year'].unique())
        selected_hectares = st.sidebar.multiselect("Select Hectares", df['Hectare'].unique(),
                                                   default=df['Hectare'].unique())
        selected_species = st.sidebar.multiselect("Select Species", df['Species'].unique() , default=['CANAPA' , 'PAYELU' , 'SHORP2'])


        #--------- Most SP

        chart_type = st.sidebar.radio("Select Chart Type", ("Bar Chart", "Pie Chart"))
        if chart_type == "Bar Chart":
            # ----------------------------------- the Main
            col1, col2 = st.columns(2)
            with col1:
                create_bar_chart_BDH_all_years_growthrate(df)
            with col2:
                create_bar_chart_BDH_all_years_growth(df)
            with st.expander("Growth Trends in Species"):
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_5_top_sp(df, selected_year)
                with col2:
                    create_bar_chart_sp_year(df, selected_species)

            with st.expander("Growth Trends in All Hectares (By Size class and Age Class)"):
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_growth(df, selected_year)
                with col2:
                    create_bar_chart_growth_rate(df, selected_year)
                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_growth_age(df, selected_year)
                with col2:
                    create_bar_chart_growth_rate_age(df, selected_year)

            with st.expander("Growth Trends in Selected Hectare (By Size class and Age Class)"):
                st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

                st.write("To see the trend in selected hectare please first choose your desire hectares")
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_growth_hectare(df, selected_hectares)
                with col2:
                    create_bar_chart_growth_rate_hectare(df, selected_hectares)

                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_growth_hectare_age(df, selected_hectares)
                with col2:
                    create_bar_chart_growth_rate_hectare_age(df, selected_hectares)


        if chart_type == "Pie Chart":
            col1, col2 = st.columns(2)
            with col1:
                create_bar_chart_BDH_all_years_growthrate(df)
            with col2:
                create_bar_chart_BDH_all_years_growth(df)
            with st.expander("Growth Trends in Species"):
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_5_top_sp(df, selected_year)
                with col2:
                    create_pie_chart_sp_year(df, selected_species)

            with st.expander("Growth Trends in All Hectares (By Size class and Age Class)"):
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_growth(df, selected_year)
                with col2:
                    create_pie_chart_growth_rate(df, selected_year)
                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_growth_age(df, selected_year)
                with col2:
                    create_pie_chart_growth_rate_age(df, selected_year)

            with st.expander("Growth Trends in Selected Hectare (By Size class and Age Class)"):
                st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

                st.write("To see the trend in selected hectare please first choose your desire hectares")
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_growth_hectare(df, selected_hectares)
                with col2:
                    create_pie_chart_growth_rate_hectare(df, selected_hectares)

                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_growth_hectare_age(df, selected_hectares)
                with col2:
                    create_pie_chart_growth_rate_hectare_age(df, selected_hectares)

    if option_tomenutype == "DBH size class":
        st.subheader("")


        def create_bar_chart_DBH_distribution(df, selected_years):
            # Filter data for the selected years
            selected_data = df[df['Year'].isin(selected_years)]
            # Pivot the data to have years as columns and size classes as rows
            pivoted_data = selected_data.pivot_table(index='Size Class', columns='Year', aggfunc='size', fill_value=0)
            # Reset the index to make 'Size Class' a column
            pivoted_data = pivoted_data.reset_index()
            # Melt the pivoted DataFrame to have a long format suitable for plotting
            melted_data = pd.melt(pivoted_data, id_vars='Size Class', var_name='Year', value_name='Count')
            # Create bar chart
            fig = px.bar(melted_data, x='Size Class', y='Count', color='Year',
                         title='Distribution of DBH Size Classes Across Selected Years',
                         labels={'Count': 'Count', 'Size Class': 'DBH Size Class', 'Year': 'Year'},
                         barmode='group')
            st.plotly_chart(fig)

        def create_bar_chart_DBH_distribution_BaslArea(df, selected_years):
            # Filter data for the selected years
            selected_data = df[df['Year'].isin(selected_years)]
            # Pivot the data to have years as columns and size classes as rows
            pivoted_data = selected_data.pivot_table(index='Size Class', columns='Year', values='Basal Area',
                                                     aggfunc='sum', fill_value=0)
            # Reset the index to make 'Size Class' a column
            pivoted_data = pivoted_data.reset_index()
            # Melt the pivoted DataFrame to have a long format suitable for plotting
            melted_data = pd.melt(pivoted_data, id_vars='Size Class', var_name='Year', value_name='Total Basal Area')
            # Create bar chart
            fig = px.bar(melted_data, x='Size Class', y='Total Basal Area', color='Year',
                         title='Total Basal Area for Each Size Class Across Selected Years',
                         labels={'Total Basal Area': 'Total Basal Area', 'Size Class': 'DBH Size Class',
                                 'Year': 'Year'},
                         barmode='group')
            st.plotly_chart(fig)


        def create_bar_chart_DBH_distribution_Density(df, selected_years):
            # Filter data for the selected years
            selected_data = df[df['Year'].isin(selected_years)]
            # Pivot the data to have years as columns and size classes as rows
            pivoted_data = selected_data.pivot_table(index='Size Class', columns='Year', values='Density',
                                                     aggfunc='sum', fill_value=0)
            # Reset the index to make 'Size Class' a column
            pivoted_data = pivoted_data.reset_index()
            # Melt the pivoted DataFrame to have a long format suitable for plotting
            melted_data = pd.melt(pivoted_data, id_vars='Size Class', var_name='Year', value_name='Total Density')
            # Create bar chart
            fig = px.bar(melted_data, x='Size Class', y='Total Density', color='Year',
                         title='Total Density for Each Size Class Across Selected Years',
                         labels={'Total Basal Area': 'Total Basal Area', 'Size Class': 'DBH Size Class',
                                 'Year': 'Year'},
                         barmode='group')
            st.plotly_chart(fig)





        def create_bar_chart_DBH_distribution_hectare(df, selected_years, selected_hectares):
            for year in selected_years:
                # Filter data for the selected year and hectares
                selected_data = df[(df['Year'] == year) & df['Hectare'].isin(selected_hectares)]
                # Pivot the data to have size classes as rows and hectares as columns
                pivoted_data = selected_data.pivot_table(index='Size Class', columns='Hectare', aggfunc='size',
                                                         fill_value=0)
                # Reset the index to make 'Size Class' a column
                pivoted_data = pivoted_data.reset_index()
                # Melt the pivoted DataFrame to have a long format suitable for plotting
                melted_data = pd.melt(pivoted_data, id_vars='Size Class', var_name='Hectare', value_name='Count')
                # Create bar chart for the current year
                fig = px.bar(melted_data, x='Size Class', y='Count', color='Hectare',
                             title=f'Distribution of DBH Size Classes for Year {year} Across Selected Hectares',
                             labels={'Count': 'Count', 'Size Class': 'DBH Size Class', 'Hectare': 'Hectare'},
                             barmode='group')
                st.plotly_chart(fig)

        def create_bar_chart_DBH_distribution_BaslArea_hectare(df, selected_years, selected_hectares):
            for year in selected_years:
                # Filter data for the selected year and hectares
                selected_data = df[(df['Year'] == year) & (df['Hectare'].isin(selected_hectares))]
                # Pivot the data to have size classes as rows and years as columns, summing basal area
                pivoted_data = selected_data.pivot_table(index='Size Class', columns='Hectare', values='Basal Area',
                                                         aggfunc='sum', fill_value=0)
                # Reset index to make 'Size Class' a column
                pivoted_data = pivoted_data.reset_index()
                # Melt the pivoted DataFrame to have a long format suitable for plotting
                melted_data = pd.melt(pivoted_data, id_vars='Size Class', var_name='Year',
                                      value_name='Total Basal Area')
                # Create bar chart for the current year
                fig = px.bar(melted_data, x='Size Class', y='Total Basal Area', color='Year',
                             title=f'Total Basal Area for Each Size Class - Year {year}',
                             labels={'Total Basal Area': 'Total Basal Area', 'Size Class': 'DBH Size Class',
                                     'Year': 'Year'},
                             barmode='group')
                st.plotly_chart(fig)


        def create_bar_chart_DBH_distribution_Density_hectare(df, selected_years):
            for year in selected_years:
                # Filter data for the selected year and hectares
                selected_data = df[(df['Year'] == year) & (df['Hectare'].isin(selected_hectares))]
                # Pivot the data to have size classes as rows and years as columns, summing basal area
                pivoted_data = selected_data.pivot_table(index='Size Class', columns='Hectare', values='Density',
                                                         aggfunc='sum', fill_value=0)
                # Reset index to make 'Size Class' a column
                pivoted_data = pivoted_data.reset_index()
                # Melt the pivoted DataFrame to have a long format suitable for plotting
                melted_data = pd.melt(pivoted_data, id_vars='Size Class', var_name='Year',
                                      value_name='Total Density')
                # Create bar chart for the current year
                fig = px.bar(melted_data, x='Size Class', y='Total Density', color='Year',
                             title=f'Total Density for Each Size Class - Year {year}',
                             labels={'Total Density': 'TotalDensity', 'Size Class': 'DBH Size Class',
                                     'Year': 'Year'},
                             barmode='group')
                st.plotly_chart(fig)
        default_selected_years = df['Year'].unique()
        selected_years = st.sidebar.multiselect("Select Years", df['Year'].unique(), default_selected_years)
        selected_hectares = st.sidebar.multiselect("Select Hectares", df['Hectare'].unique())

        # Streamlit UI
        col1, col2 = st.columns(2)
        with col1:
            create_bar_chart_DBH_distribution(df, selected_years)

        with col2:
            create_bar_chart_DBH_distribution_BaslArea(df, selected_years)

        col1, col2 = st.columns(2)

        with col1:
            create_bar_chart_DBH_distribution_Density(df, selected_years)

        col1, col2 = st.columns(2)
        with col1:
            create_bar_chart_DBH_distribution_hectare(df, selected_years, selected_hectares)
        with col2:
            create_bar_chart_DBH_distribution_BaslArea_hectare(df, selected_years, selected_hectares)

        create_bar_chart_DBH_distribution_Density_hectare(df, selected_years)

    if option_tomenutype == 'AGB':
        def create_bar_chart_AGB(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'size class' and calculate average 'AGB' for each size class
            size_class_AGB = selected_data.groupby('Size Class')['AGB'].sum().reset_index()
            # Calculate average AGB across all size classes
            average_AGB = size_class_AGB['AGB'].mean()
            # Create bar chart
            fig = px.bar(size_class_AGB, x='Size Class', y='AGB',
                         title=f'Sum of AGB Across Size Classes for Year {selected_year}',
                         labels={'Size Class': 'Size Class', 'AGB': 'AGB'})
            # Change bar color and size
            fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.6)
            # Add dashed line for average AGB
            fig.add_shape(type='line', x0=size_class_AGB['Size Class'].iloc[0], y0=average_AGB,
                          x1=size_class_AGB['Size Class'].iloc[-1], y1=average_AGB,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=500, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Total AGB Across Size Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_AGB(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative AGB values
            selected_data = selected_data[selected_data['AGB'] >= 0]

            # Group by 'Size Class' and calculate sum of 'AGB' for each size class
            size_class_AGB = selected_data.groupby('Size Class')['AGB'].sum().reset_index()

            # Calculate total AGB
            total_AGB = size_class_AGB['AGB'].sum()

            # Create pie chart
            fig = px.pie(size_class_AGB, values='AGB', names='Size Class',
                         title=f'Total AGB Across Size Classes for Year {selected_year}',
                         labels={'AGB': 'AGB', 'Size Class': 'Size Class'},
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        # Function to create bar chart for AGB distribution across size classes for a selected year
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_bar_chart_AGB_rate(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'size class' and calculate average 'AGB' for each size class
            size_class_AGB_rate = selected_data.groupby('Size Class')['AGB'].mean().reset_index()
            # Calculate average AGB across all size classes
            average_AGB_rate = size_class_AGB_rate['AGB'].mean()
            # Create bar chart
            fig = px.bar(size_class_AGB_rate, x='Size Class', y='AGB',
                         title=f'Average AGB Across Size Classes for Year {selected_year}')
            fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.6)

            # Add dashed line for average AGB
            fig.add_shape(type='line', x0=-0.5, y0=average_AGB_rate, x1=len(size_class_AGB_rate) - 0.5,
                          y1=average_AGB_rate,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=500, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Average AGB Across Size Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_AGB_rate(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative AGB values
            selected_data = selected_data[selected_data['AGB'] >= 0]

            # Group by 'Size Class' and calculate average 'AGB' for each size class
            size_class_AGB_rate = selected_data.groupby('Size Class')['AGB'].mean().reset_index()

            # Calculate average AGB across all size classes
            average_AGB_rate = size_class_AGB_rate['AGB'].mean()

            # Create pie chart
            fig = px.pie(size_class_AGB_rate, values='AGB', names='Size Class',
                         title=f'Average AGB Across Size Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_bar_chart_AGB_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'Age Class' and calculate average 'AGB' for each age class
            age_class_AGB = selected_data.groupby('Age Class')['AGB'].mean().reset_index()
            # Calculate average AGB across all age classes
            average_AGB = age_class_AGB['AGB'].mean()
            # Create bar chart
            fig = px.bar(age_class_AGB, x='Age Class', y='AGB',
                         title=f'Average AGB Across Age Classes for Year {selected_year}')
            # Change bar color and size
            fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=0.7)
            # Add dashed line for average AGB
            fig.add_shape(type='line', x0=-0.5, y0=average_AGB, x1=len(age_class_AGB) - 0.5, y1=average_AGB,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=450, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Total AGB Across Age Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_AGB_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative AGB values
            selected_data = selected_data[selected_data['AGB'] >= 0]

            # Group by 'Age Class' and calculate average 'AGB' for each age class
            age_class_AGB = selected_data.groupby('Age Class')['AGB'].mean().reset_index()

            # Calculate average AGB across all age classes
            average_AGB = age_class_AGB['AGB'].mean()

            # Create pie chart
            fig = px.pie(age_class_AGB, values='AGB', names='Age Class',
                         title=f'Average AGB Across Age Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=450, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        # Function to create bar chart for average AGB across age classes for a selected year
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_bar_chart_AGB_rate_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'Age Class' and calculate average 'AGB' for each age class
            age_class_AGB_rate = selected_data.groupby('Age Class')['AGB'].mean().reset_index()
            # Calculate average AGB across all age classes
            average_AGB_rate = age_class_AGB_rate['AGB'].mean()
            # Create bar chart
            fig = px.bar(age_class_AGB_rate, x='Age Class', y='AGB',
                         title=f'Average AGB Across Age Classes for Year {selected_year}')
            # Change bar color and size
            fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=0.7)
            # Add dashed line for average AGB
            fig.add_shape(type='line', x0=-0.5, y0=average_AGB_rate, x1=len(age_class_AGB_rate) - 0.5,
                          y1=average_AGB_rate,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=450, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Average AGB Across Age Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_AGB_rate_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative AGB values
            selected_data = selected_data[selected_data['AGB'] >= 0]

            # Group by 'Age Class' and calculate average 'AGB' for each age class
            age_class_AGB_rate = selected_data.groupby('Age Class')['AGB'].mean().reset_index()

            # Calculate average AGB across all age classes
            average_AGB_rate = age_class_AGB_rate['AGB'].mean()

            # Create pie chart
            fig = px.pie(age_class_AGB_rate, values='AGB', names='Age Class',
                         title=f'Average AGB rate Across Age Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=450, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_AGB_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Age Class' and calculate average 'AGB' for each age class
                age_class_AGB = selected_data.groupby('Age Class')['AGB'].mean().reset_index()

                # Calculate average AGB across all age classes
                average_AGB = age_class_AGB['AGB'].mean()

                # Filter out negative AGB values
                age_class_AGB = age_class_AGB[age_class_AGB['AGB'] >= 0]

                # Create pie chart
                fig = px.pie(age_class_AGB, values='AGB', names='Age Class',
                             title=f'Total AGB Across Age Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)


        def create_bar_chart_AGB_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'AGB' for each age class
                age_class_AGB = selected_data.groupby('Age Class')['AGB'].mean().reset_index()
                # Calculate average AGB across all age classes
                average_AGB = age_class_AGB['AGB'].mean()
                # Create bar chart
                fig = px.bar(age_class_AGB, x='Age Class', y='AGB',
                             title=f'Sum of AGB Across Age Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.8)
                # Add dashed line for average AGB
                fig.add_shape(type='line', x0=-0.5, y0=average_AGB, x1=len(age_class_AGB) - 0.5, y1=average_AGB,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Total AGB Across Age Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        # Function to create bar chart for average AGB across age classes for selected hectares
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_AGB_rate_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Age Class' and calculate average 'AGB' for each age class
                age_class_AGB_rate = selected_data.groupby('Age Class')['AGB'].mean().reset_index()

                # Calculate average AGB across all age classes
                average_AGB_rate = age_class_AGB_rate['AGB'].mean()

                # Filter out negative AGB values
                age_class_AGB_rate = age_class_AGB_rate[age_class_AGB_rate['AGB'] >= 0]

                # Create pie chart
                fig = px.pie(age_class_AGB_rate, values='AGB', names='Age Class',
                             title=f'Average AGB Across Age Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)


        def create_bar_chart_AGB_rate_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'AGB' for each age class
                age_class_AGB_rate = selected_data.groupby('Age Class')['AGB'].mean().reset_index()
                # Calculate average AGB across all age classes
                average_AGB_rate = age_class_AGB_rate['AGB'].mean()
                # Create bar chart
                fig = px.bar(age_class_AGB_rate, x='Age Class', y='AGB',
                             title=f'Average AGB Across Age Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.8)
                # Add dashed line for average AGB
                fig.add_shape(type='line', x0=-0.5, y0=average_AGB_rate, x1=len(age_class_AGB_rate) - 0.5,
                              y1=average_AGB_rate,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Average AGB Across Age Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_AGB_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Filter out negative AGB values
                selected_data = selected_data[selected_data['AGB'] >= 0]

                # Group by 'Size Class' and calculate average 'AGB' for each size class
                size_class_AGB = selected_data.groupby('Size Class')['AGB'].mean().reset_index()

                # Calculate average AGB across all size classes
                average_AGB = size_class_AGB['AGB'].mean()

                # Create pie chart
                fig = px.pie(size_class_AGB, values='AGB', names='Size Class',
                             title=f'Average AGB Across Size Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)


        def create_bar_chart_AGB_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'AGB' for each age class
                age_class_AGB = selected_data.groupby('Size Class')['AGB'].mean().reset_index()
                # Calculate average AGB across all age classes
                average_AGB = age_class_AGB['AGB'].mean()
                # Create bar chart
                fig = px.bar(age_class_AGB, x='Size Class', y='AGB',
                             title=f'Average AGB Across Size Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=1)
                # Add dashed line for average AGB
                fig.add_shape(type='line', x0=-0.5, y0=average_AGB, x1=len(age_class_AGB) - 0.5, y1=average_AGB,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Total AGB Across Size Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        # Function to create bar chart for average AGB across age classes for selected hectares
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_AGB_rate_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Filter out negative AGB values
                selected_data = selected_data[selected_data['AGB'] >= 0]

                # Group by 'Size Class' and calculate average 'AGB' for each size class
                size_class_AGB_rate = selected_data.groupby('Size Class')['AGB'].mean().reset_index()

                # Calculate average AGB across all size classes
                average_AGB_rate = size_class_AGB_rate['AGB'].mean()

                # Create pie chart
                fig = px.pie(size_class_AGB_rate, values='AGB', names='Size Class',
                             title=f'Average AGB Rate Across Size Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)


        def create_bar_chart_AGB_rate_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'AGB' for each age class
                age_class_AGB_rate = selected_data.groupby('Size Class')['AGB'].mean().reset_index()
                # Calculate average AGB across all age classes
                average_AGB_rate = age_class_AGB_rate['AGB'].mean()
                # Create bar chart
                fig = px.bar(age_class_AGB_rate, x='Size Class', y='AGB',
                             title=f'Average AGB Across Size Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=1)
                # Add dashed line for average AGB
                fig.add_shape(type='line', x0=-0.5, y0=average_AGB_rate, x1=len(age_class_AGB_rate) - 0.5,
                              y1=average_AGB_rate,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Average AGB Across Size Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        def create_bar_chart_5_top_sp(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'Hectare' and 'Species' and calculate mean 'AGB' for each species in each hectare
            species_AGB_rate = selected_data.groupby(['Hectare', 'Species'])['AGB'].mean().reset_index()
            # Sort by 'AGB' in descending order within each hectare
            species_AGB_rate['Rank'] = species_AGB_rate.groupby('Hectare')['AGB'].rank(ascending=False)
            top_species = species_AGB_rate[species_AGB_rate['Rank'] <= 5]  # Select top 5 species in each hectare
            # Calculate average AGB across all species
            average_AGB_rate = top_species['AGB'].mean()
            # Create bar chart
            fig = px.bar(top_species, x='Hectare', y='AGB', color='Species',
                         title=f'Top 5 Species with Highest AGBs for Each Hectare - Year {selected_year}',
                         labels={'AGB': 'Mean AGB', 'Hectare': 'Hectare'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(top_species['Hectare']), y0=average_AGB_rate,
                          x1=max(top_species['Hectare']), y1=average_AGB_rate,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        def create_pie_chart_5_top_sp(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Group by 'Hectare' and 'Species' and calculate mean 'AGB' for each species in each hectare
            species_AGB_rate = selected_data.groupby(['Hectare', 'Species'])['AGB'].mean().reset_index()

            # Sort by 'AGB' in descending order within each hectare
            species_AGB_rate['Rank'] = species_AGB_rate.groupby('Hectare')['AGB'].rank(ascending=False)
            top_species = species_AGB_rate[species_AGB_rate['Rank'] <= 5]  # Select top 5 species in each hectare

            # Exclude negative AGBs
            top_species = top_species[top_species['AGB'] >= 0]

            # Calculate average AGB across all species
            average_AGB_rate = top_species['AGB'].mean()

            # Create pie chart
            fig = px.pie(top_species, values='AGB', names='Species',
                         title=f'Top 5 Species with Highest AGBs for Each Hectare - Year {selected_year}',
                         labels={'AGB': 'Mean AGB', 'Species': 'Species'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average AGB: {average_AGB_rate:.2f}',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        def create_bar_chart_sp_year(df, selected_species):
            # Filter data for selected species
            selected_data = df[df['Species'].isin(selected_species)]
            # Group by 'Year' and 'Species' and calculate mean 'AGB' for each species in each year
            species_AGB_rate = selected_data.groupby(['Year', 'Species'])['AGB'].mean().reset_index()
            # Calculate average AGB across all years for selected species
            average_AGB_rate = species_AGB_rate['AGB'].mean()
            # Create bar chart
            fig = px.bar(species_AGB_rate, x='Year', y='AGB', color='Species',
                         title='Mean AGB of Selected Species Across Years',
                         labels={'AGB': 'Mean AGB', 'Year': 'Year'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(species_AGB_rate['Year']), y0=average_AGB_rate,
                          x1=max(species_AGB_rate['Year']), y1=average_AGB_rate,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        def create_pie_chart_sp_year(df, selected_species):
            # Filter data for selected species
            selected_data = df[df['Species'].isin(selected_species)]

            # Filter out negative AGBs
            selected_data = selected_data[selected_data['AGB'] >= 0]

            # Group by 'Year' and 'Species' and calculate mean 'AGB' for each species in each year
            species_AGB_rate = selected_data.groupby(['Year', 'Species'])['AGB'].mean().reset_index()

            # Calculate average AGB across all years for selected species
            average_AGB_rate = species_AGB_rate['AGB'].mean()

            # Create pie chart
            fig = px.pie(species_AGB_rate, values='AGB', names='Species',
                         title='Mean AGB of Selected Species Across Years',
                         labels={'AGB': 'Mean AGB', 'Species': 'Species'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average AGB: {average_AGB_rate:.2f}',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        def create_bar_chart_BDH_all_years_AGBrate(df):
            # Group by 'Year' and 'DBH Size Class' and calculate mean 'AGB' for each DBH size class in each year
            dbh_AGB_rate = df.groupby(['Year', 'Size Class'])['AGB'].mean().reset_index()
            # Calculate average AGB across all years
            average_AGB_rate = dbh_AGB_rate['AGB'].mean()
            # Create bar chart
            fig = px.bar(dbh_AGB_rate, x='Year', y='AGB', color='Size Class',
                         title='Mean AGB for Each DBH Size Class Across Years',
                         labels={'AGB': 'Mean AGB', 'Year': 'Year', 'Size Class': 'Size Class'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(dbh_AGB_rate['Year']), y0=average_AGB_rate,
                          x1=max(dbh_AGB_rate['Year']), y1=average_AGB_rate,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        def create_pie_chart_BDH_all_years_AGBrate(df):
            # Group by 'DBH Size Class' and calculate mean 'AGB' for each DBH size class across all years
            dbh_AGB_rate = df.groupby('Size Class')['AGB'].mean().reset_index()

            # Calculate average AGB across all size classes
            average_AGB_rate = dbh_AGB_rate['AGB'].mean()

            # Create pie chart
            fig = px.pie(dbh_AGB_rate, values='AGB', names='Size Class',
                         title='Mean AGB for Each DBH Size Class Across Years',
                         labels={'AGB': 'Mean AGB', 'Size Class': 'Size Class'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average AGB: {average_AGB_rate:.2f}',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        def create_bar_chart_BDH_all_years_AGB(df):
            # Group by 'Year' and 'DBH Size Class' and calculate sum 'AGB' for each DBH size class in each year
            dbh_AGB = df.groupby(['Year', 'Size Class'])['AGB'].sum().reset_index()
            # Calculate average AGB across all years
            average_AGB = dbh_AGB['AGB'].mean()
            # Create bar chart
            fig = px.bar(dbh_AGB, x='Year', y='AGB', color='Size Class',
                         title='Sum AGB for Each DBH Size Class Across Years',
                         labels={'AGB': 'Sum AGB', 'Year': 'Year', 'Size Class': 'Size Class'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(dbh_AGB['Year']), y0=average_AGB,
                          x1=max(dbh_AGB['Year']), y1=average_AGB,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        st.sidebar.header("Setting")
        selected_year = st.sidebar.radio("Select Year", df['Year'].unique())
        selected_hectares = st.sidebar.multiselect("Select Hectares", df['Hectare'].unique(),
                                                   default=df['Hectare'].unique())
        selected_species = st.sidebar.multiselect("Select Species", df['Species'].unique(),
                                                  default=['CANAPA', 'PAYELU', 'SHORP2'])

        # -----------------------------------------

        # --------- Most SP
        chart_type = st.sidebar.radio("Select Chart Type", ("Bar Chart", "Pie Chart"))
        if chart_type == "Bar Chart":
            # ----------------------------------- the Main
            col1, col2 = st.columns(2)
            with col1:
                create_bar_chart_BDH_all_years_AGB(df)
            with st.expander("AGB Trends in Species"):
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_5_top_sp(df, selected_year)
                with col2:
                    create_bar_chart_sp_year(df, selected_species)

            with st.expander("AGB Trends in All Hectares (By Size class and Age Class)"):
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_AGB(df, selected_year)
                with col2:
                    create_bar_chart_AGB_rate(df, selected_year)
                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_AGB_age(df, selected_year)
                with col2:
                    create_bar_chart_AGB_rate_age(df, selected_year)

            with st.expander("AGB Trends in Selected Hectare (By Size class and Age Class)"):
                st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

                st.write("To see the trend in selected hectare please first choose your desire hectares")
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_AGB_hectare(df, selected_hectares)
                with col2:
                    create_bar_chart_AGB_rate_hectare(df, selected_hectares)

                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_AGB_hectare_age(df, selected_hectares)
                with col2:
                    create_bar_chart_AGB_rate_hectare_age(df, selected_hectares)

        if chart_type == "Pie Chart":
            col1, col2 = st.columns(2)
            with col2:
                create_bar_chart_BDH_all_years_AGB(df)
            with st.expander("AGB Trends in Species"):
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_5_top_sp(df, selected_year)
                with col2:
                    create_pie_chart_sp_year(df, selected_species)

            with st.expander("AGB Trends in All Hectares (By Size class and Age Class)"):
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_AGB(df, selected_year)
                with col2:
                    create_pie_chart_AGB_rate(df, selected_year)
                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_AGB_age(df, selected_year)
                with col2:
                    create_pie_chart_AGB_rate_age(df, selected_year)

            with st.expander("AGB Trends in Selected Hectare (By Size class and Age Class)"):
                st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

                st.write("To see the trend in selected hectare please first choose your desire hectares")
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_AGB_hectare(df, selected_hectares)
                with col2:
                    create_pie_chart_AGB_rate_hectare(df, selected_hectares)

                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_AGB_hectare_age(df, selected_hectares)
                with col2:
                    create_pie_chart_AGB_rate_hectare_age(df, selected_hectares)

    if option_tomenutype == 'Carbon stock':
        st.write("asdasd")
        def create_bar_chart_Carbon(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'size class' and calculate average 'Carbon' for each size class
            size_class_Carbon = selected_data.groupby('Size Class')['Carbon'].sum().reset_index()
            # Calculate average Carbon across all size classes
            average_Carbon = size_class_Carbon['Carbon'].mean()
            # Create bar chart
            fig = px.bar(size_class_Carbon, x='Size Class', y='Carbon',
                         title=f'Sum of Carbon Across Size Classes for Year {selected_year}',
                         labels={'Size Class': 'Size Class', 'Carbon': 'Carbon'})
            # Change bar color and size
            fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.6)
            # Add dashed line for average Carbon
            fig.add_shape(type='line', x0=size_class_Carbon['Size Class'].iloc[0], y0=average_Carbon,
                          x1=size_class_Carbon['Size Class'].iloc[-1], y1=average_Carbon,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=500, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Total Carbon Across Size Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_Carbon(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative Carbon values
            selected_data = selected_data[selected_data['Carbon'] >= 0]

            # Group by 'Size Class' and calculate sum of 'Carbon' for each size class
            size_class_Carbon = selected_data.groupby('Size Class')['Carbon'].sum().reset_index()

            # Calculate total Carbon
            total_Carbon = size_class_Carbon['Carbon'].sum()

            # Create pie chart
            fig = px.pie(size_class_Carbon, values='Carbon', names='Size Class',
                         title=f'Total Carbon Across Size Classes for Year {selected_year}',
                         labels={'Carbon': 'Carbon', 'Size Class': 'Size Class'},
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        # Function to create bar chart for Carbon distribution across size classes for a selected year
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_bar_chart_Carbon_rate(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'size class' and calculate average 'Carbon' for each size class
            size_class_Carbon_rate = selected_data.groupby('Size Class')['Carbon'].mean().reset_index()
            # Calculate average Carbon across all size classes
            average_Carbon_rate = size_class_Carbon_rate['Carbon'].mean()
            # Create bar chart
            fig = px.bar(size_class_Carbon_rate, x='Size Class', y='Carbon',
                         title=f'Average Carbon Across Size Classes for Year {selected_year}')
            fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.6)

            # Add dashed line for average Carbon
            fig.add_shape(type='line', x0=-0.5, y0=average_Carbon_rate, x1=len(size_class_Carbon_rate) - 0.5,
                          y1=average_Carbon_rate,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=500, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Average Carbon Across Size Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_Carbon_rate(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative Carbon values
            selected_data = selected_data[selected_data['Carbon'] >= 0]

            # Group by 'Size Class' and calculate average 'Carbon' for each size class
            size_class_Carbon_rate = selected_data.groupby('Size Class')['Carbon'].mean().reset_index()

            # Calculate average Carbon across all size classes
            average_Carbon_rate = size_class_Carbon_rate['Carbon'].mean()

            # Create pie chart
            fig = px.pie(size_class_Carbon_rate, values='Carbon', names='Size Class',
                         title=f'Average Carbon Across Size Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_bar_chart_Carbon_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'Age Class' and calculate average 'Carbon' for each age class
            age_class_Carbon = selected_data.groupby('Age Class')['Carbon'].mean().reset_index()
            # Calculate average Carbon across all age classes
            average_Carbon = age_class_Carbon['Carbon'].mean()
            # Create bar chart
            fig = px.bar(age_class_Carbon, x='Age Class', y='Carbon',
                         title=f'Average Carbon Across Age Classes for Year {selected_year}')
            # Change bar color and size
            fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=0.7)
            # Add dashed line for average Carbon
            fig.add_shape(type='line', x0=-0.5, y0=average_Carbon, x1=len(age_class_Carbon) - 0.5, y1=average_Carbon,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=450, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Total Carbon Across Age Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_Carbon_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative Carbon values
            selected_data = selected_data[selected_data['Carbon'] >= 0]

            # Group by 'Age Class' and calculate average 'Carbon' for each age class
            age_class_Carbon = selected_data.groupby('Age Class')['Carbon'].mean().reset_index()

            # Calculate average Carbon across all age classes
            average_Carbon = age_class_Carbon['Carbon'].mean()

            # Create pie chart
            fig = px.pie(age_class_Carbon, values='Carbon', names='Age Class',
                         title=f'Average Carbon Across Age Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=450, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        # Function to create bar chart for average Carbon across age classes for a selected year
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_bar_chart_Carbon_rate_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'Age Class' and calculate average 'Carbon' for each age class
            age_class_Carbon_rate = selected_data.groupby('Age Class')['Carbon'].mean().reset_index()
            # Calculate average Carbon across all age classes
            average_Carbon_rate = age_class_Carbon_rate['Carbon'].mean()
            # Create bar chart
            fig = px.bar(age_class_Carbon_rate, x='Age Class', y='Carbon',
                         title=f'Average Carbon Across Age Classes for Year {selected_year}')
            # Change bar color and size
            fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=0.7)
            # Add dashed line for average Carbon
            fig.add_shape(type='line', x0=-0.5, y0=average_Carbon_rate, x1=len(age_class_Carbon_rate) - 0.5,
                          y1=average_Carbon_rate,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=450, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Average Carbon Across Age Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_Carbon_rate_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative Carbon values
            selected_data = selected_data[selected_data['Carbon'] >= 0]

            # Group by 'Age Class' and calculate average 'Carbon' for each age class
            age_class_Carbon_rate = selected_data.groupby('Age Class')['Carbon'].mean().reset_index()

            # Calculate average Carbon across all age classes
            average_Carbon_rate = age_class_Carbon_rate['Carbon'].mean()

            # Create pie chart
            fig = px.pie(age_class_Carbon_rate, values='Carbon', names='Age Class',
                         title=f'Average Carbon Rate Across Age Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=450, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_Carbon_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Age Class' and calculate average 'Carbon' for each age class
                age_class_Carbon = selected_data.groupby('Age Class')['Carbon'].mean().reset_index()

                # Calculate average Carbon across all age classes
                average_Carbon = age_class_Carbon['Carbon'].mean()

                # Filter out negative Carbon values
                age_class_Carbon = age_class_Carbon[age_class_Carbon['Carbon'] >= 0]

                # Create pie chart
                fig = px.pie(age_class_Carbon, values='Carbon', names='Age Class',
                             title=f'Total Carbon Across Age Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)


        def create_bar_chart_Carbon_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'Carbon' for each age class
                age_class_Carbon = selected_data.groupby('Age Class')['Carbon'].mean().reset_index()
                # Calculate average Carbon across all age classes
                average_Carbon = age_class_Carbon['Carbon'].mean()
                # Create bar chart
                fig = px.bar(age_class_Carbon, x='Age Class', y='Carbon',
                             title=f'Sum of Carbon Across Age Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.8)
                # Add dashed line for average Carbon
                fig.add_shape(type='line', x0=-0.5, y0=average_Carbon, x1=len(age_class_Carbon) - 0.5,
                              y1=average_Carbon,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Total Carbon Across Age Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        # Function to create bar chart for average Carbon across age classes for selected hectares
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_Carbon_rate_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Age Class' and calculate average 'Carbon' for each age class
                age_class_Carbon_rate = selected_data.groupby('Age Class')['Carbon'].mean().reset_index()

                # Calculate average Carbon across all age classes
                average_Carbon_rate = age_class_Carbon_rate['Carbon'].mean()

                # Filter out negative Carbon values
                age_class_Carbon_rate = age_class_Carbon_rate[age_class_Carbon_rate['Carbon'] >= 0]

                # Create pie chart
                fig = px.pie(age_class_Carbon_rate, values='Carbon', names='Age Class',
                             title=f'Average Carbon Across Age Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)


        def create_bar_chart_Carbon_rate_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'Carbon' for each age class
                age_class_Carbon_rate = selected_data.groupby('Age Class')['Carbon'].mean().reset_index()
                # Calculate average Carbon across all age classes
                average_Carbon_rate = age_class_Carbon_rate['Carbon'].mean()
                # Create bar chart
                fig = px.bar(age_class_Carbon_rate, x='Age Class', y='Carbon',
                             title=f'Average Carbon Across Age Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.8)
                # Add dashed line for average Carbon
                fig.add_shape(type='line', x0=-0.5, y0=average_Carbon_rate, x1=len(age_class_Carbon_rate) - 0.5,
                              y1=average_Carbon_rate,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Average Carbon Across Age Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_Carbon_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Filter out negative Carbon values
                selected_data = selected_data[selected_data['Carbon'] >= 0]

                # Group by 'Size Class' and calculate average 'Carbon' for each size class
                size_class_Carbon = selected_data.groupby('Size Class')['Carbon'].mean().reset_index()

                # Calculate average Carbon across all size classes
                average_Carbon = size_class_Carbon['Carbon'].mean()

                # Create pie chart
                fig = px.pie(size_class_Carbon, values='Carbon', names='Size Class',
                             title=f'Average Carbon Across Size Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)


        def create_bar_chart_Carbon_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'Carbon' for each age class
                age_class_Carbon = selected_data.groupby('Size Class')['Carbon'].mean().reset_index()
                # Calculate average Carbon across all age classes
                average_Carbon = age_class_Carbon['Carbon'].mean()
                # Create bar chart
                fig = px.bar(age_class_Carbon, x='Size Class', y='Carbon',
                             title=f'Average Carbon Across Size Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=1)
                # Add dashed line for average Carbon
                fig.add_shape(type='line', x0=-0.5, y0=average_Carbon, x1=len(age_class_Carbon) - 0.5,
                              y1=average_Carbon,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Total Carbon Across Size Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        # Function to create bar chart for average Carbon across age classes for selected hectares
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_Carbon_rate_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Filter out negative Carbon values
                selected_data = selected_data[selected_data['Carbon'] >= 0]

                # Group by 'Size Class' and calculate average 'Carbon' for each size class
                size_class_Carbon_rate = selected_data.groupby('Size Class')['Carbon'].mean().reset_index()

                # Calculate average Carbon across all size classes
                average_Carbon_rate = size_class_Carbon_rate['Carbon'].mean()

                # Create pie chart
                fig = px.pie(size_class_Carbon_rate, values='Carbon', names='Size Class',
                             title=f'Average Carbon Rate Across Size Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)


        def create_bar_chart_Carbon_rate_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'Carbon' for each age class
                age_class_Carbon_rate = selected_data.groupby('Size Class')['Carbon'].mean().reset_index()
                # Calculate average Carbon across all age classes
                average_Carbon_rate = age_class_Carbon_rate['Carbon'].mean()
                # Create bar chart
                fig = px.bar(age_class_Carbon_rate, x='Size Class', y='Carbon',
                             title=f'Average Carbon Across Size Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=1)
                # Add dashed line for average Carbon
                fig.add_shape(type='line', x0=-0.5, y0=average_Carbon_rate, x1=len(age_class_Carbon_rate) - 0.5,
                              y1=average_Carbon_rate,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Average Carbon Across Size Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        def create_bar_chart_5_top_sp(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'Hectare' and 'Species' and calculate mean 'Carbon' for each species in each hectare
            species_Carbon_rate = selected_data.groupby(['Hectare', 'Species'])['Carbon'].mean().reset_index()
            # Sort by 'Carbon' in descending order within each hectare
            species_Carbon_rate['Rank'] = species_Carbon_rate.groupby('Hectare')['Carbon'].rank(ascending=False)
            top_species = species_Carbon_rate[species_Carbon_rate['Rank'] <= 5]  # Select top 5 species in each hectare
            # Calculate average Carbon across all species
            average_Carbon_rate = top_species['Carbon'].mean()
            # Create bar chart
            fig = px.bar(top_species, x='Hectare', y='Carbon', color='Species',
                         title=f'Top 5 Species with Highest Carbons for Each Hectare - Year {selected_year}',
                         labels={'Carbon': 'Mean Carbon', 'Hectare': 'Hectare'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(top_species['Hectare']), y0=average_Carbon_rate,
                          x1=max(top_species['Hectare']), y1=average_Carbon_rate,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        def create_pie_chart_5_top_sp(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Group by 'Hectare' and 'Species' and calculate mean 'Carbon' for each species in each hectare
            species_Carbon_rate = selected_data.groupby(['Hectare', 'Species'])['Carbon'].mean().reset_index()

            # Sort by 'Carbon' in descending order within each hectare
            species_Carbon_rate['Rank'] = species_Carbon_rate.groupby('Hectare')['Carbon'].rank(ascending=False)
            top_species = species_Carbon_rate[species_Carbon_rate['Rank'] <= 5]  # Select top 5 species in each hectare

            # Exclude negative Carbons
            top_species = top_species[top_species['Carbon'] >= 0]

            # Calculate average Carbon across all species
            average_Carbon_rate = top_species['Carbon'].mean()

            # Create pie chart
            fig = px.pie(top_species, values='Carbon', names='Species',
                         title=f'Top 5 Species with Highest Carbons for Each Hectare - Year {selected_year}',
                         labels={'Carbon': 'Mean Carbon', 'Species': 'Species'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average Carbon: {average_Carbon_rate:.2f}',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        def create_bar_chart_sp_year(df, selected_species):
            # Filter data for selected species
            selected_data = df[df['Species'].isin(selected_species)]
            # Group by 'Year' and 'Species' and calculate mean 'Carbon' for each species in each year
            species_Carbon_rate = selected_data.groupby(['Year', 'Species'])['Carbon'].mean().reset_index()
            # Calculate average Carbon across all years for selected species
            average_Carbon_rate = species_Carbon_rate['Carbon'].mean()
            # Create bar chart
            fig = px.bar(species_Carbon_rate, x='Year', y='Carbon', color='Species',
                         title='Mean Carbon of Selected Species Across Years',
                         labels={'Carbon': 'Mean Carbon', 'Year': 'Year'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(species_Carbon_rate['Year']), y0=average_Carbon_rate,
                          x1=max(species_Carbon_rate['Year']), y1=average_Carbon_rate,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        def create_pie_chart_sp_year(df, selected_species):
            # Filter data for selected species
            selected_data = df[df['Species'].isin(selected_species)]

            # Filter out negative Carbons
            selected_data = selected_data[selected_data['Carbon'] >= 0]

            # Group by 'Year' and 'Species' and calculate mean 'Carbon' for each species in each year
            species_Carbon_rate = selected_data.groupby(['Year', 'Species'])['Carbon'].mean().reset_index()

            # Calculate average Carbon across all years for selected species
            average_Carbon_rate = species_Carbon_rate['Carbon'].mean()

            # Create pie chart
            fig = px.pie(species_Carbon_rate, values='Carbon', names='Species',
                         title='Mean Carbon of Selected Species Across Years',
                         labels={'Carbon': 'Mean Carbon', 'Species': 'Species'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average Carbon: {average_Carbon_rate:.2f}',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        def create_bar_chart_BDH_all_years_Carbonrate(df):
            # Group by 'Year' and 'DBH Size Class' and calculate mean 'Carbon' for each DBH size class in each year
            dbh_Carbon_rate = df.groupby(['Year', 'Size Class'])['Carbon'].mean().reset_index()
            # Calculate average Carbon across all years
            average_Carbon_rate = dbh_Carbon_rate['Carbon'].mean()
            # Create bar chart
            fig = px.bar(dbh_Carbon_rate, x='Year', y='Carbon', color='Size Class',
                         title='Mean Carbon for Each DBH Size Class Across Years',
                         labels={'Carbon': 'Mean Carbon', 'Year': 'Year', 'Size Class': 'Size Class'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(dbh_Carbon_rate['Year']), y0=average_Carbon_rate,
                          x1=max(dbh_Carbon_rate['Year']), y1=average_Carbon_rate,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        def create_pie_chart_BDH_all_years_Carbonrate(df):
            # Group by 'DBH Size Class' and calculate mean 'Carbon' for each DBH size class across all years
            dbh_Carbon_rate = df.groupby('Size Class')['Carbon'].mean().reset_index()

            # Calculate average Carbon across all size classes
            average_Carbon_rate = dbh_Carbon_rate['Carbon'].mean()

            # Create pie chart
            fig = px.pie(dbh_Carbon_rate, values='Carbon', names='Size Class',
                         title='Mean Carbon for Each DBH Size Class Across Years',
                         labels={'Carbon': 'Mean Carbon', 'Size Class': 'Size Class'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average Carbon: {average_Carbon_rate:.2f}',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        def create_bar_chart_BDH_all_years_Carbon(df):
            # Group by 'Year' and 'DBH Size Class' and calculate sum 'Carbon' for each DBH size class in each year
            dbh_Carbon = df.groupby(['Year', 'Size Class'])['Carbon'].sum().reset_index()
            # Calculate average Carbon across all years
            average_Carbon = dbh_Carbon['Carbon'].mean()
            # Create bar chart
            fig = px.bar(dbh_Carbon, x='Year', y='Carbon', color='Size Class',
                         title='Sum Carbon for Each DBH Size Class Across Years',
                         labels={'Carbon': 'Sum Carbon', 'Year': 'Year', 'Size Class': 'Size Class'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(dbh_Carbon['Year']), y0=average_Carbon,
                          x1=max(dbh_Carbon['Year']), y1=average_Carbon,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        st.sidebar.header("Setting")
        selected_year = st.sidebar.radio("Select Year", df['Year'].unique())
        selected_hectares = st.sidebar.multiselect("Select Hectares", df['Hectare'].unique(),
                                                   default=df['Hectare'].unique())
        selected_species = st.sidebar.multiselect("Select Species", df['Species'].unique(),
                                                  default=['CANAPA', 'PAYELU', 'SHORP2'])

        # -----------------------------------------

        # --------- Most SP
        chart_type = st.sidebar.radio("Select Chart Type", ("Bar Chart", "Pie Chart"))
        if chart_type == "Bar Chart":
            # ----------------------------------- the Main
            col1, col2 = st.columns(2)
            with col1:
                create_bar_chart_BDH_all_years_Carbon(df)
            with st.expander("Carbon Trends in Species"):
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_5_top_sp(df, selected_year)
                with col2:
                    create_bar_chart_sp_year(df, selected_species)

            with st.expander("Carbon Trends in All Hectares (By Size class and Age Class)"):
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_Carbon(df, selected_year)
                with col2:
                    create_bar_chart_Carbon_rate(df, selected_year)
                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_Carbon_age(df, selected_year)
                with col2:
                    create_bar_chart_Carbon_rate_age(df, selected_year)

            with st.expander("Carbon Trends in Selected Hectare (By Size class and Age Class)"):
                st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

                st.write("To see the trend in selected hectare please first choose your desire hectares")
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_Carbon_hectare(df, selected_hectares)
                with col2:
                    create_bar_chart_Carbon_rate_hectare(df, selected_hectares)

                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_Carbon_hectare_age(df, selected_hectares)
                with col2:
                    create_bar_chart_Carbon_rate_hectare_age(df, selected_hectares)

        if chart_type == "Pie Chart":
            col1, col2 = st.columns(2)
            with col2:
                create_bar_chart_BDH_all_years_Carbon(df)
            with st.expander("Carbon Trends in Species"):
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_5_top_sp(df, selected_year)
                with col2:
                    create_pie_chart_sp_year(df, selected_species)

            with st.expander("Carbon Trends in All Hectares (By Size class and Age Class)"):
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_Carbon(df, selected_year)
                with col2:
                    create_pie_chart_Carbon_rate(df, selected_year)
                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_Carbon_age(df, selected_year)
                with col2:
                    create_pie_chart_Carbon_rate_age(df, selected_year)

            with st.expander("Carbon Trends in Selected Hectare (By Size class and Age Class)"):
                st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

                st.write("To see the trend in selected hectare please first choose your desire hectares")
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_Carbon_hectare(df, selected_hectares)
                with col2:
                    create_pie_chart_Carbon_rate_hectare(df, selected_hectares)

                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_Carbon_hectare_age(df, selected_hectares)
                with col2:
                    create_pie_chart_Carbon_rate_hectare_age(df, selected_hectares)

    if option_tomenutype == 'Mortality':


        def calculate_mortality_rate(selected_data):
            total_trees = selected_data.shape[0]
            dead_trees = selected_data[selected_data['Status'] == 'Dead'].shape[0]
            if total_trees == 0:
                return 0
            mortality_rate = (dead_trees / total_trees) * 100
            return mortality_rate

        def create_bar_chart_mortality(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Group by 'Size Class' and calculate mortality rate for each size class
            size_class_mortality = selected_data.groupby('Size Class').apply(calculate_mortality_rate).reset_index(
                name='Mortality Rate')

            # Calculate average mortality rate across all size classes
            average_mortality_rate = size_class_mortality['Mortality Rate'].mean()

            # Create bar chart
            fig = px.bar(size_class_mortality, x='Size Class', y='Mortality Rate',
                         title=f'Mortality Rate Across Size Classes for Year {selected_year}',
                         labels={'Size Class': 'Size Class', 'Mortality Rate': 'Mortality Rate (%)'})

            # Change bar color and size
            fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.6)

            # Add dashed line for average mortality rate
            fig.add_shape(type='line', x0=size_class_mortality['Size Class'].iloc[0], y0=average_mortality_rate,
                          x1=size_class_mortality['Size Class'].iloc[-1], y1=average_mortality_rate,
                          line=dict(color="black", width=1, dash='dash'))

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Mortality Rate Across Size Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        def create_pie_chart_mortality(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Group by 'Size Class' and calculate the count of dead trees for each size class
            size_class_mortality = selected_data[selected_data['Status'] == 'Dead'].groupby('Size Class')[
                'Status'].count().reset_index()
            size_class_mortality.rename(columns={'Status': 'Count'}, inplace=True)

            # Calculate total mortality
            total_mortality = size_class_mortality['Count'].sum()

            # Create pie chart
            fig = px.pie(size_class_mortality, values='Count', names='Size Class',
                         title=f'Mortality Distribution Across Size Classes for Year {selected_year}',
                         labels={'Count': 'Count', 'Size Class': 'Size Class'},
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        def create_bar_chart_mortality_rate(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Group by 'Size Class' and calculate mortality rate for each size class
            size_class_mortality_rate = selected_data.groupby('Size Class').apply(calculate_mortality_rate).reset_index(
                name='Mortality Rate')

            # Calculate average mortality rate across all size classes
            average_mortality_rate = size_class_mortality_rate['Mortality Rate'].mean()

            # Create bar chart
            fig = px.bar(size_class_mortality_rate, x='Size Class', y='Mortality Rate',
                         title=f'Average Mortality Rate Across Size Classes for Year {selected_year}')

            # Customize bar appearance
            fig.update_traces(marker_color='red', marker_line_color='black', marker_line_width=1.3, opacity=0.6)

            # Add dashed line for average mortality rate
            fig.add_shape(type='line', x0=-0.5, y0=average_mortality_rate, x1=len(size_class_mortality_rate) - 0.5,
                          y1=average_mortality_rate,
                          line=dict(color="black", width=1, dash='dash'))

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Average Mortality Rate Across Size Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        def create_pie_chart_mortality_rate(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Group by 'Size Class' and calculate the count of dead trees for each size class
            size_class_mortality = selected_data[selected_data['Status'] == 'Dead'].groupby('Size Class')[
                'Status'].count().reset_index()
            size_class_mortality.rename(columns={'Status': 'Count'}, inplace=True)

            # Calculate total mortality
            total_mortality = size_class_mortality['Count'].sum()

            # Create pie chart
            fig = px.pie(size_class_mortality, values='Count', names='Size Class',
                         title=f'Mortality Distribution Rate Across Size Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        def create_bar_chart_mortality_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Group by 'Age Class' and calculate mortality rate for each age class
            age_class_mortality_rate = selected_data.groupby('Age Class').apply(calculate_mortality_rate).reset_index(
                name='Mortality Rate')

            # Calculate average mortality rate across all age classes
            average_mortality_rate = age_class_mortality_rate['Mortality Rate'].mean()

            # Create bar chart
            fig = px.bar(age_class_mortality_rate, x='Age Class', y='Mortality Rate',
                         title=f'Average Mortality Rate Across Age Classes for Year {selected_year}')

            # Change bar color and size
            fig.update_traces(marker_color='darkred', marker_line_color='black', marker_line_width=1.3, opacity=0.7)

            # Add dashed line for average mortality rate
            fig.add_shape(type='line', x0=-0.5, y0=average_mortality_rate, x1=len(age_class_mortality_rate) - 0.5,
                          y1=average_mortality_rate,
                          line=dict(color="black", width=1, dash='dash'))

            # Change chart size
            fig.update_layout(height=450, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Average Mortality Rate Across Age Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        def create_pie_chart_mortality_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Group by 'Age Class' and calculate the count of dead trees for each age class
            age_class_mortality = selected_data[selected_data['Status'] == 'Dead'].groupby('Age Class')[
                'Status'].count().reset_index()
            age_class_mortality.rename(columns={'Status': 'Count'}, inplace=True)

            # Create pie chart
            fig = px.pie(age_class_mortality, values='Count', names='Age Class',
                         title=f'Mortality Distribution Across Age Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=450, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        def create_bar_chart_mortality_rate_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Group by 'Age Class' and calculate mortality rate for each age class
            age_class_mortality_rate = selected_data.groupby('Age Class').apply(calculate_mortality_rate).reset_index(
                name='Mortality Rate')

            # Calculate average mortality rate across all age classes
            average_mortality_rate = age_class_mortality_rate['Mortality Rate'].mean()

            # Create bar chart
            fig = px.bar(age_class_mortality_rate, x='Age Class', y='Mortality Rate',
                         title=f'Average Mortality Rate Across Age Classes for Year {selected_year}')

            # Change bar color and size
            fig.update_traces(marker_color='darkred', marker_line_color='black', marker_line_width=1.3, opacity=0.7)

            # Add dashed line for average mortality rate
            fig.add_shape(type='line', x0=-0.5, y0=average_mortality_rate, x1=len(age_class_mortality_rate) - 0.5,
                          y1=average_mortality_rate,
                          line=dict(color="black", width=1, dash='dash'))

            # Change chart size
            fig.update_layout(height=450, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Average Mortality Rate Across Age Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        def create_pie_chart_mortality_rate_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Group by 'Age Class' and calculate mortality rate for each age class
            age_class_mortality_rate = selected_data.groupby('Age Class').apply(calculate_mortality_rate).reset_index(
                name='Mortality Rate')

            # Create pie chart
            fig = px.pie(age_class_mortality_rate, values='Mortality Rate', names='Age Class',
                         title=f'Mortality Rate Distribution Across Age Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=450, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        def create_pie_chart_mortality_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Age Class' and calculate mortality rate for each age class
                age_class_mortality_rate = selected_data.groupby('Age Class').apply(
                    calculate_mortality_rate).reset_index(name='Mortality Rate')

                # Create pie chart
                fig = px.pie(age_class_mortality_rate, values='Mortality Rate', names='Age Class',
                             title=f'Mortality Rate Across Age Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)

        def create_bar_chart_mortality_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Age Class' and calculate mortality rate for each age class
                age_class_mortality_rate = selected_data.groupby('Age Class').apply(
                    calculate_mortality_rate).reset_index(name='Mortality Rate')

                # Calculate average mortality rate across all age classes
                average_mortality_rate = age_class_mortality_rate['Mortality Rate'].mean()

                # Create bar chart
                fig = px.bar(age_class_mortality_rate, x='Age Class', y='Mortality Rate',
                             title=f'Mortality Rate Across Age Classes for Hectare {hectare}')

                # Change bar color and size
                fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.8)

                # Add dashed line for average mortality rate
                fig.add_shape(type='line', x0=-0.5, y0=average_mortality_rate, x1=len(age_class_mortality_rate) - 0.5,
                              y1=average_mortality_rate,
                              line=dict(color="black", width=1, dash='dash'))

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Mortality Rate Across Age Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)

        def create_pie_chart_mortality_rate_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Age Class' and calculate mortality rate for each age class
                age_class_mortality_rate = selected_data.groupby('Age Class').apply(
                    calculate_mortality_rate).reset_index(name='Mortality Rate')

                # Create pie chart
                fig = px.pie(age_class_mortality_rate, values='Mortality Rate', names='Age Class',
                             title=f'Mortality Across Age Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)

        def create_bar_chart_mortality_rate_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Age Class' and calculate mortality rate for each age class
                age_class_mortality_rate = selected_data.groupby('Age Class').apply(
                    calculate_mortality_rate).reset_index(name='Mortality Rate')

                # Calculate average mortality rate across all age classes
                average_mortality_rate = age_class_mortality_rate['Mortality Rate'].mean()

                # Create bar chart
                fig = px.bar(age_class_mortality_rate, x='Age Class', y='Mortality Rate',
                             title=f'Mortality Rate Across Age Classes for Hectare {hectare}')

                # Change bar color and size
                fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.8)

                # Add dashed line for average mortality rate
                fig.add_shape(type='line', x0=-0.5, y0=average_mortality_rate, x1=len(age_class_mortality_rate) - 0.5,
                              y1=average_mortality_rate, line=dict(color="black", width=1, dash='dash'))

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Mortality Rate Across Age Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)

        def create_pie_chart_mortality_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Size Class' and calculate mortality rate for each size class
                size_class_mortality_rate = selected_data.groupby('Size Class').apply(
                    calculate_mortality_rate).reset_index(name='Mortality Rate')

                # Create pie chart
                fig = px.pie(size_class_mortality_rate, values='Mortality Rate', names='Size Class',
                             title=f'Mortality Across Size Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)

        def create_bar_chart_mortality_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Size Class' and calculate mortality rate for each size class
                size_class_mortality_rate = selected_data.groupby('Size Class').apply(
                    calculate_mortality_rate).reset_index(name='Mortality Rate')

                # Calculate average mortality rate across all size classes
                average_mortality_rate = size_class_mortality_rate['Mortality Rate'].mean()

                # Create bar chart
                fig = px.bar(size_class_mortality_rate, x='Size Class', y='Mortality Rate',
                             title=f'Mortality Rate Across Size Classes for Hectare {hectare}')

                # Change bar color and size
                fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=1)

                # Add dashed line for average mortality rate
                fig.add_shape(type='line', x0=-0.5, y0=average_mortality_rate, x1=len(size_class_mortality_rate) - 0.5,
                              y1=average_mortality_rate,
                              line=dict(color="black", width=1, dash='dash'))

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Mortality Rate Across Size Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)

        def create_pie_chart_mortality_rate_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Size Class' and calculate mortality rate for each size class
                size_class_mortality_rate = selected_data.groupby('Size Class').apply(
                    calculate_mortality_rate).reset_index(name='Mortality Rate')

                # Create pie chart
                fig = px.pie(size_class_mortality_rate, values='Mortality Rate', names='Size Class',
                             title=f'Mortality Rate Across Size Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)

        def create_bar_chart_mortality_rate_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Size Class' and calculate mortality rate for each size class
                size_class_mortality_rate = selected_data.groupby('Size Class').apply(
                    calculate_mortality_rate).reset_index(name='Mortality Rate')

                # Calculate average mortality rate across all size classes
                average_mortality_rate = size_class_mortality_rate['Mortality Rate'].mean()

                # Create bar chart
                fig = px.bar(size_class_mortality_rate, x='Size Class', y='Mortality Rate',
                             title=f'Mortality Rate Across Size Classes for Hectare {hectare}')

                # Change bar color and size
                fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=1)

                # Add dashed line for average mortality rate
                fig.add_shape(type='line', x0=-0.5, y0=average_mortality_rate, x1=len(size_class_mortality_rate) - 0.5,
                              y1=average_mortality_rate,
                              line=dict(color="black", width=1, dash='dash'))

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Mortality Rate Across Size Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)

        def create_bar_chart_5_top_sp(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Group by 'Hectare' and 'Species' and calculate mortality rate for each species in each hectare
            species_mortality_rate = selected_data.groupby(['Hectare', 'Species']).apply(
                calculate_mortality_rate).reset_index(name='Mortality Rate')

            # Sort by 'Mortality Rate' in descending order within each hectare
            species_mortality_rate['Rank'] = species_mortality_rate.groupby('Hectare')['Mortality Rate'].rank(
                ascending=False)

            # Select top 5 species in each hectare
            top_species = species_mortality_rate[species_mortality_rate['Rank'] <= 5]

            # Calculate average mortality rate across all top species
            average_mortality_rate = top_species['Mortality Rate'].mean()

            # Create bar chart
            fig = px.bar(top_species, x='Hectare', y='Mortality Rate', color='Species',
                         title=f'Top 5 Species with Highest Mortality Rates for Each Hectare - Year {selected_year}',
                         labels={'Mortality Rate': 'Mean Mortality Rate', 'Hectare': 'Hectare'},
                         barmode='group')

            # Add average line
            fig.add_shape(type='line', x0=min(top_species['Hectare']), y0=average_mortality_rate,
                          x1=max(top_species['Hectare']), y1=average_mortality_rate,
                          line=dict(color="black", width=1, dash='dash'))

            st.plotly_chart(fig)

        def create_pie_chart_5_top_sp(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Group by 'Hectare' and 'Species' and calculate mortality rate for each species in each hectare
            species_mortality_rate = selected_data.groupby(['Hectare', 'Species']).apply(
                calculate_mortality_rate).reset_index(name='Mortality Rate')

            # Sort by 'Mortality Rate' in descending order within each hectare
            species_mortality_rate['Rank'] = species_mortality_rate.groupby('Hectare')['Mortality Rate'].rank(
                ascending=False)

            # Select top 5 species in each hectare
            top_species = species_mortality_rate[species_mortality_rate['Rank'] <= 5]

            # Calculate average mortality rate across all top species
            average_mortality_rate = top_species['Mortality Rate'].mean()

            # Create pie chart
            fig = px.pie(top_species, values='Mortality Rate', names='Species',
                         title=f'Top 5 Species with Highest Mortality Rates for Each Hectare - Year {selected_year}',
                         labels={'Mortality Rate': 'Mean Mortality Rate', 'Species': 'Species'},
                         hole=0.3)

            # Add average annotation
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average Mortality Rate: {average_mortality_rate:.2f}%',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        def create_bar_chart_sp_year(df, selected_species):
            # Filter data for selected species
            selected_data = df[df['Species'].isin(selected_species)]

            # Group by 'Year' and 'Species' and calculate mortality rate for each species in each year
            species_mortality_rate = selected_data.groupby(['Year', 'Species']).apply(
                calculate_mortality_rate).reset_index(name='Mortality Rate')

            # Calculate average mortality rate across all years for selected species
            average_mortality_rate = species_mortality_rate['Mortality Rate'].mean()

            # Create bar chart
            fig = px.bar(species_mortality_rate, x='Year', y='Mortality Rate', color='Species',
                         title='Mean Mortality Rate of Selected Species Across Years',
                         labels={'Mortality Rate': 'Mean Mortality Rate', 'Year': 'Year'},
                         barmode='group')

            # Add average line
            fig.add_shape(type='line', x0=min(species_mortality_rate['Year']), y0=average_mortality_rate,
                          x1=max(species_mortality_rate['Year']), y1=average_mortality_rate,
                          line=dict(color="black", width=1, dash='dash'))

            # Update layout
            fig.update_layout(
                height=500,
                width=700,
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        def create_pie_chart_sp_year(df, selected_species):
            # Filter data for selected species
            selected_data = df[df['Species'].isin(selected_species)]

            # Group by 'Year' and 'Species' and calculate mortality rate for each species in each year
            species_mortality_rate = selected_data.groupby(['Year', 'Species']).apply(
                calculate_mortality_rate).reset_index(name='Mortality Rate')

            # Calculate average mortality rate across all years for selected species
            average_mortality_rate = species_mortality_rate['Mortality Rate'].mean()

            # Create pie chart
            fig = px.pie(species_mortality_rate, values='Mortality Rate', names='Species',
                         title='Mean Mortality Rate of Selected Species Across Years',
                         labels={'Mortality Rate': 'Mean Mortality Rate', 'Species': 'Species'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average Mortality Rate: {average_mortality_rate:.2f}%',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        def calculate_mortality(group):
            return group[group['Status'] == 'Dead'].shape[0]

        def create_bar_chart_BDH_all_years_mortality(df):
            # Group by 'Year' and 'Size Class' and calculate mortality rate for each DBH size class in each year
            dbh_mortality_rate = df.groupby(['Year', 'Size Class']).apply(calculate_mortality_rate).reset_index(
                name='Mortality Rate')

            # Calculate average mortality rate across all years
            average_mortality_rate = dbh_mortality_rate['Mortality Rate'].mean()

            # Create bar chart
            fig = px.bar(dbh_mortality_rate, x='Year', y='Mortality Rate', color='Size Class',
                         title='Mean Mortality Rate for Each DBH Size Class Across Years',
                         labels={'Mortality Rate': 'Mean Mortality Rate (%)', 'Year': 'Year',
                                 'Size Class': 'Size Class'},
                         barmode='group')

            # Add average line
            fig.add_shape(type='line', x0=min(dbh_mortality_rate['Year']), y0=average_mortality_rate,
                          x1=max(dbh_mortality_rate['Year']), y1=average_mortality_rate,
                          line=dict(color="black", width=1, dash='dash'))

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        def create_pie_chart_BDH_all_years_mortality(df):
            # Group by 'DBH Size Class' and calculate mortality rate for each DBH size class across all years
            dbh_mortality_rate = df.groupby('Size Class').apply(calculate_mortality_rate).reset_index(
                name='Mortality Rate')

            # Calculate average mortality rate across all size classes
            average_mortality_rate = dbh_mortality_rate['Mortality Rate'].mean()

            # Create pie chart
            fig = px.pie(dbh_mortality_rate, values='Mortality Rate', names='Size Class',
                         title='Mean Mortality Rate for Each DBH Size Class Across Years',
                         labels={'Mortality Rate': 'Mean Mortality Rate (%)', 'Size Class': 'Size Class'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average Mortality Rate: {average_mortality_rate:.2f}%',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        def calculate_mortality_rate(group):
            total_population = group.shape[0]
            dead_population = group[group['Status'] == 'Dead'].shape[0]
            if total_population == 0:
                return 0
            return dead_population / total_population

        def create_bar_chart_BDH_all_years_mortality_rate(df):
            # Group by 'Year' and 'DBH Size Class' and calculate mean 'Mortality rate' for each DBH size class in each year
            dbh_mortality_rate = df.groupby(['Year', 'Size Class']).apply(calculate_mortality_rate).reset_index(
                name='Mortality Rate')

            # Calculate average mortality rate across all years
            average_mortality_rate = dbh_mortality_rate['Mortality Rate'].mean()

            # Create bar chart
            fig = px.bar(dbh_mortality_rate, x='Year', y='Mortality Rate', color='Size Class',
                         title='Mean Mortality Rate for Each DBH Size Class Across Years',
                         labels={'Mortality Rate': 'Mean Mortality Rate', 'Year': 'Year', 'Size Class': 'Size Class'},
                         barmode='group')

            # Add average line
            fig.add_shape(type='line', x0=min(dbh_mortality_rate['Year']), y0=average_mortality_rate,
                          x1=max(dbh_mortality_rate['Year']), y1=average_mortality_rate,
                          line=dict(color="black", width=1, dash='dash'))

            st.plotly_chart(fig)


        def create_pie_chart_BDH_all_years_mortality_rate(df):
            # Group by 'DBH Size Class' and calculate mean 'Mortality rate' for each DBH size class across all years
            dbh_mortality_rate = df.groupby('Size Class').apply(calculate_mortality_rate).reset_index(
                name='Mortality Rate')

            # Calculate average mortality rate across all size classes
            average_mortality_rate = dbh_mortality_rate['Mortality Rate'].mean()

            # Create pie chart
            fig = px.pie(dbh_mortality_rate, values='Mortality Rate', names='Size Class',
                         title='Mean Mortality Rate for Each DBH Size Class Across Years',
                         labels={'Mortality Rate': 'Mean Mortality Rate', 'Size Class': 'Size Class'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average Mortality Rate: {average_mortality_rate:.2f}',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)





        st.sidebar.header("Setting")
        selected_year = st.sidebar.radio("Select Year", df['Year'].unique())
        selected_hectares = st.sidebar.multiselect("Select Hectares", df['Hectare'].unique(),default=df['Hectare'].unique())
        selected_species = st.sidebar.multiselect("Select Species", df['Species'].unique(), default=['CANAPA', 'PAYELU', 'SHORP2'])

        chart_type = st.sidebar.radio("Select Chart Type", ("Bar Chart", "Pie Chart"))
        if chart_type == "Bar Chart":
            # ----------------------------------- the Main
            col1, col2 = st.columns(2)
            with col1:
                create_bar_chart_BDH_all_years_mortality_rate(df)
            with col2:
                create_bar_chart_BDH_all_years_mortality(df)
            with st.expander("Mortality Trends in Species"):
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_5_top_sp(df, selected_year)
                with col2:
                    create_bar_chart_sp_year(df, selected_species)

            with st.expander("Mortality Trends in All Hectares (By Size class and Age Class)"):
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_mortality(df, selected_year)
                with col2:
                    create_bar_chart_mortality_rate(df, selected_year)
                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_mortality_age(df, selected_year)
                with col2:
                    create_bar_chart_mortality_rate_age(df, selected_year)
            with st.expander("Mortality Trends in Selected Hectare (By Size class and Age Class)"):
                st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

                st.write("To see the trend in selected hectare please first choose your desire hectares")
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_mortality_hectare(df, selected_hectares)
                with col2:
                    create_bar_chart_mortality_rate_hectare(df, selected_hectares)

                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_mortality_hectare_age(df, selected_hectares)
                with col2:
                    create_bar_chart_mortality_rate_hectare_age(df, selected_hectares)


        if chart_type == "Pie Chart":
            col1, col2 = st.columns(2)
            with col1:
                create_bar_chart_BDH_all_years_mortality_rate(df)
            with col2:
                create_bar_chart_BDH_all_years_mortality(df)
            with st.expander("Growth Trends in Species"):
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_5_top_sp(df, selected_year)
                with col2:
                    create_pie_chart_sp_year(df, selected_species)

            with st.expander("Mortality Trends in All Hectares (By Size class and Age Class)"):
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_mortality(df, selected_year)
                with col2:
                    create_pie_chart_mortality_rate(df, selected_year)

                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_mortality_age(df, selected_year)
                with col2:
                    create_pie_chart_mortality_rate_age(df, selected_year)

            with st.expander("Mortality Trends in Selected Hectare (By Size class and Age Class)"):
                st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

                st.write("To see the trend in selected hectare please first choose your desire hectares")
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_mortality_hectare(df, selected_hectares)
                with col2:
                    create_pie_chart_mortality_rate_hectare(df, selected_hectares)

                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_mortality_hectare_age(df, selected_hectares)
                with col2:
                    create_pie_chart_mortality_rate_hectare_age(df, selected_hectares)

    if option_tomenutype == 'Lifespan':
        def create_bar_chart_Lifespan(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'size class' and calculate average 'Lifespan' for each size class
            size_class_Lifespan = selected_data.groupby('Size Class')['Lifespan'].sum().reset_index()
            # Calculate average Lifespan across all size classes
            average_Lifespan = size_class_Lifespan['Lifespan'].mean()
            # Create bar chart
            fig = px.bar(size_class_Lifespan, x='Size Class', y='Lifespan',
                         title=f'Sum of Lifespan Across Size Classes for Year {selected_year}',
                         labels={'Size Class': 'Size Class', 'Lifespan': 'Lifespan'})
            # Change bar color and size
            fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.6)
            # Add dashed line for average Lifespan
            fig.add_shape(type='line', x0=size_class_Lifespan['Size Class'].iloc[0], y0=average_Lifespan,
                          x1=size_class_Lifespan['Size Class'].iloc[-1], y1=average_Lifespan,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=500, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Total Lifespan Across Size Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_Lifespan(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative Lifespan values
            selected_data = selected_data[selected_data['Lifespan'] >= 0]

            # Group by 'Size Class' and calculate sum of 'Lifespan' for each size class
            size_class_Lifespan = selected_data.groupby('Size Class')['Lifespan'].sum().reset_index()

            # Calculate total Lifespan
            total_Lifespan = size_class_Lifespan['Lifespan'].sum()

            # Create pie chart
            fig = px.pie(size_class_Lifespan, values='Lifespan', names='Size Class',
                         title=f'Total Lifespan Across Size Classes for Year {selected_year}',
                         labels={'Lifespan': 'Lifespan', 'Size Class': 'Size Class'},
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        # Function to create bar chart for Lifespan distribution across size classes for a selected year
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_bar_chart_Lifespan_rate(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'size class' and calculate average 'Lifespan' for each size class
            size_class_Lifespan_rate = selected_data.groupby('Size Class')['Lifespan'].mean().reset_index()
            # Calculate average Lifespan across all size classes
            average_Lifespan_rate = size_class_Lifespan_rate['Lifespan'].mean()
            # Create bar chart
            fig = px.bar(size_class_Lifespan_rate, x='Size Class', y='Lifespan',
                         title=f'Average Lifespan Across Size Classes for Year {selected_year}')
            fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.6)

            # Add dashed line for average Lifespan
            fig.add_shape(type='line', x0=-0.5, y0=average_Lifespan_rate, x1=len(size_class_Lifespan_rate) - 0.5,
                          y1=average_Lifespan_rate,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=500, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Average Lifespan Across Size Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_Lifespan_rate(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative Lifespan values
            selected_data = selected_data[selected_data['Lifespan'] >= 0]

            # Group by 'Size Class' and calculate average 'Lifespan' for each size class
            size_class_Lifespan_rate = selected_data.groupby('Size Class')['Lifespan'].mean().reset_index()

            # Calculate average Lifespan across all size classes
            average_Lifespan_rate = size_class_Lifespan_rate['Lifespan'].mean()

            # Create pie chart
            fig = px.pie(size_class_Lifespan_rate, values='Lifespan', names='Size Class',
                         title=f'Average Lifespan Across Size Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_bar_chart_Lifespan_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'Age Class' and calculate average 'Lifespan' for each age class
            age_class_Lifespan = selected_data.groupby('Age Class')['Lifespan'].mean().reset_index()
            # Calculate average Lifespan across all age classes
            average_Lifespan = age_class_Lifespan['Lifespan'].mean()
            # Create bar chart
            fig = px.bar(age_class_Lifespan, x='Age Class', y='Lifespan',
                         title=f'Average Lifespan Across Age Classes for Year {selected_year}')
            # Change bar color and size
            fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=0.7)
            # Add dashed line for average Lifespan
            fig.add_shape(type='line', x0=-0.5, y0=average_Lifespan, x1=len(age_class_Lifespan) - 0.5,
                          y1=average_Lifespan,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=450, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Total Lifespan Across Age Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_Lifespan_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative Lifespan values
            selected_data = selected_data[selected_data['Lifespan'] >= 0]

            # Group by 'Age Class' and calculate average 'Lifespan' for each age class
            age_class_Lifespan = selected_data.groupby('Age Class')['Lifespan'].mean().reset_index()

            # Calculate average Lifespan across all age classes
            average_Lifespan = age_class_Lifespan['Lifespan'].mean()

            # Create pie chart
            fig = px.pie(age_class_Lifespan, values='Lifespan', names='Age Class',
                         title=f'Average Lifespan Across Age Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=450, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        # Function to create bar chart for average Lifespan across age classes for a selected year
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_bar_chart_Lifespan_rate_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'Age Class' and calculate average 'Lifespan' for each age class
            age_class_Lifespan_rate = selected_data.groupby('Age Class')['Lifespan'].mean().reset_index()
            # Calculate average Lifespan across all age classes
            average_Lifespan_rate = age_class_Lifespan_rate['Lifespan'].mean()
            # Create bar chart
            fig = px.bar(age_class_Lifespan_rate, x='Age Class', y='Lifespan',
                         title=f'Average Lifespan Across Age Classes for Year {selected_year}')
            # Change bar color and size
            fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=0.7)
            # Add dashed line for average Lifespan
            fig.add_shape(type='line', x0=-0.5, y0=average_Lifespan_rate, x1=len(age_class_Lifespan_rate) - 0.5,
                          y1=average_Lifespan_rate,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=450, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Average Lifespan Across Age Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_Lifespan_rate_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative Lifespan values
            selected_data = selected_data[selected_data['Lifespan'] >= 0]

            # Group by 'Age Class' and calculate average 'Lifespan' for each age class
            age_class_Lifespan_rate = selected_data.groupby('Age Class')['Lifespan'].mean().reset_index()

            # Calculate average Lifespan across all age classes
            average_Lifespan_rate = age_class_Lifespan_rate['Lifespan'].mean()

            # Create pie chart
            fig = px.pie(age_class_Lifespan_rate, values='Lifespan', names='Age Class',
                         title=f'Average Lifespan Rate Across Age Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=450, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_Lifespan_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Age Class' and calculate average 'Lifespan' for each age class
                age_class_Lifespan = selected_data.groupby('Age Class')['Lifespan'].mean().reset_index()

                # Calculate average Lifespan across all age classes
                average_Lifespan = age_class_Lifespan['Lifespan'].mean()

                # Filter out negative Lifespan values
                age_class_Lifespan = age_class_Lifespan[age_class_Lifespan['Lifespan'] >= 0]

                # Create pie chart
                fig = px.pie(age_class_Lifespan, values='Lifespan', names='Age Class',
                             title=f'Total Lifespan Across Age Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)


        def create_bar_chart_Lifespan_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'Lifespan' for each age class
                age_class_Lifespan = selected_data.groupby('Age Class')['Lifespan'].mean().reset_index()
                # Calculate average Lifespan across all age classes
                average_Lifespan = age_class_Lifespan['Lifespan'].mean()
                # Create bar chart
                fig = px.bar(age_class_Lifespan, x='Age Class', y='Lifespan',
                             title=f'Sum of Lifespan Across Age Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.8)
                # Add dashed line for average Lifespan
                fig.add_shape(type='line', x0=-0.5, y0=average_Lifespan, x1=len(age_class_Lifespan) - 0.5,
                              y1=average_Lifespan,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Total Lifespan Across Age Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        # Function to create bar chart for average Lifespan across age classes for selected hectares
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_Lifespan_rate_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Age Class' and calculate average 'Lifespan' for each age class
                age_class_Lifespan_rate = selected_data.groupby('Age Class')['Lifespan'].mean().reset_index()

                # Calculate average Lifespan across all age classes
                average_Lifespan_rate = age_class_Lifespan_rate['Lifespan'].mean()

                # Filter out negative Lifespan values
                age_class_Lifespan_rate = age_class_Lifespan_rate[age_class_Lifespan_rate['Lifespan'] >= 0]

                # Create pie chart
                fig = px.pie(age_class_Lifespan_rate, values='Lifespan', names='Age Class',
                             title=f'Average Lifespan Across Age Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)


        def create_bar_chart_Lifespan_rate_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'Lifespan' for each age class
                age_class_Lifespan_rate = selected_data.groupby('Age Class')['Lifespan'].mean().reset_index()
                # Calculate average Lifespan across all age classes
                average_Lifespan_rate = age_class_Lifespan_rate['Lifespan'].mean()
                # Create bar chart
                fig = px.bar(age_class_Lifespan_rate, x='Age Class', y='Lifespan',
                             title=f'Average Lifespan Across Age Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.8)
                # Add dashed line for average Lifespan
                fig.add_shape(type='line', x0=-0.5, y0=average_Lifespan_rate, x1=len(age_class_Lifespan_rate) - 0.5,
                              y1=average_Lifespan_rate,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Average Lifespan Across Age Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_Lifespan_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Filter out negative Lifespan values
                selected_data = selected_data[selected_data['Lifespan'] >= 0]

                # Group by 'Size Class' and calculate average 'Lifespan' for each size class
                size_class_Lifespan = selected_data.groupby('Size Class')['Lifespan'].mean().reset_index()

                # Calculate average Lifespan across all size classes
                average_Lifespan = size_class_Lifespan['Lifespan'].mean()

                # Create pie chart
                fig = px.pie(size_class_Lifespan, values='Lifespan', names='Size Class',
                             title=f'Average Lifespan Across Size Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)


        def create_bar_chart_Lifespan_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'Lifespan' for each age class
                age_class_Lifespan = selected_data.groupby('Size Class')['Lifespan'].mean().reset_index()
                # Calculate average Lifespan across all age classes
                average_Lifespan = age_class_Lifespan['Lifespan'].mean()
                # Create bar chart
                fig = px.bar(age_class_Lifespan, x='Size Class', y='Lifespan',
                             title=f'Average Lifespan Across Size Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=1)
                # Add dashed line for average Lifespan
                fig.add_shape(type='line', x0=-0.5, y0=average_Lifespan, x1=len(age_class_Lifespan) - 0.5,
                              y1=average_Lifespan,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Total Lifespan Across Size Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        # Function to create bar chart for average Lifespan across age classes for selected hectares
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_Lifespan_rate_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Filter out negative Lifespan values
                selected_data = selected_data[selected_data['Lifespan'] >= 0]

                # Group by 'Size Class' and calculate average 'Lifespan' for each size class
                size_class_Lifespan_rate = selected_data.groupby('Size Class')['Lifespan'].mean().reset_index()

                # Calculate average Lifespan across all size classes
                average_Lifespan_rate = size_class_Lifespan_rate['Lifespan'].mean()

                # Create pie chart
                fig = px.pie(size_class_Lifespan_rate, values='Lifespan', names='Size Class',
                             title=f'Average Lifespan Rate Across Size Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)


        def create_bar_chart_Lifespan_rate_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'Lifespan' for each age class
                age_class_Lifespan_rate = selected_data.groupby('Size Class')['Lifespan'].mean().reset_index()
                # Calculate average Lifespan across all age classes
                average_Lifespan_rate = age_class_Lifespan_rate['Lifespan'].mean()
                # Create bar chart
                fig = px.bar(age_class_Lifespan_rate, x='Size Class', y='Lifespan',
                             title=f'Average Lifespan Across Size Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=1)
                # Add dashed line for average Lifespan
                fig.add_shape(type='line', x0=-0.5, y0=average_Lifespan_rate, x1=len(age_class_Lifespan_rate) - 0.5,
                              y1=average_Lifespan_rate,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Average Lifespan Across Size Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        def create_bar_chart_5_top_sp(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'Hectare' and 'Species' and calculate mean 'Lifespan' for each species in each hectare
            species_Lifespan_rate = selected_data.groupby(['Hectare', 'Species'])['Lifespan'].mean().reset_index()
            # Sort by 'Lifespan' in descending order within each hectare
            species_Lifespan_rate['Rank'] = species_Lifespan_rate.groupby('Hectare')['Lifespan'].rank(ascending=False)
            top_species = species_Lifespan_rate[
                species_Lifespan_rate['Rank'] <= 5]  # Select top 5 species in each hectare
            # Calculate average Lifespan across all species
            average_Lifespan_rate = top_species['Lifespan'].mean()
            # Create bar chart
            fig = px.bar(top_species, x='Hectare', y='Lifespan', color='Species',
                         title=f'Top 5 Species with Highest Lifespans for Each Hectare - Year {selected_year}',
                         labels={'Lifespan': 'Mean Lifespan', 'Hectare': 'Hectare'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(top_species['Hectare']), y0=average_Lifespan_rate,
                          x1=max(top_species['Hectare']), y1=average_Lifespan_rate,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        def create_pie_chart_5_top_sp(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Group by 'Hectare' and 'Species' and calculate mean 'Lifespan' for each species in each hectare
            species_Lifespan_rate = selected_data.groupby(['Hectare', 'Species'])['Lifespan'].mean().reset_index()

            # Sort by 'Lifespan' in descending order within each hectare
            species_Lifespan_rate['Rank'] = species_Lifespan_rate.groupby('Hectare')['Lifespan'].rank(ascending=False)
            top_species = species_Lifespan_rate[
                species_Lifespan_rate['Rank'] <= 5]  # Select top 5 species in each hectare

            # Exclude negative Lifespans
            top_species = top_species[top_species['Lifespan'] >= 0]

            # Calculate average Lifespan across all species
            average_Lifespan_rate = top_species['Lifespan'].mean()

            # Create pie chart
            fig = px.pie(top_species, values='Lifespan', names='Species',
                         title=f'Top 5 Species with Highest Lifespans for Each Hectare - Year {selected_year}',
                         labels={'Lifespan': 'Mean Lifespan', 'Species': 'Species'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average Lifespan: {average_Lifespan_rate:.2f}',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        def create_bar_chart_sp_year(df, selected_species):
            # Filter data for selected species
            selected_data = df[df['Species'].isin(selected_species)]
            # Group by 'Year' and 'Species' and calculate mean 'Lifespan' for each species in each year
            species_Lifespan_rate = selected_data.groupby(['Year', 'Species'])['Lifespan'].mean().reset_index()
            # Calculate average Lifespan across all years for selected species
            average_Lifespan_rate = species_Lifespan_rate['Lifespan'].mean()
            # Create bar chart
            fig = px.bar(species_Lifespan_rate, x='Year', y='Lifespan', color='Species',
                         title='Mean Lifespan of Selected Species Across Years',
                         labels={'Lifespan': 'Mean Lifespan', 'Year': 'Year'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(species_Lifespan_rate['Year']), y0=average_Lifespan_rate,
                          x1=max(species_Lifespan_rate['Year']), y1=average_Lifespan_rate,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        def create_pie_chart_sp_year(df, selected_species):
            # Filter data for selected species
            selected_data = df[df['Species'].isin(selected_species)]

            # Filter out negative Lifespans
            selected_data = selected_data[selected_data['Lifespan'] >= 0]

            # Group by 'Year' and 'Species' and calculate mean 'Lifespan' for each species in each year
            species_Lifespan_rate = selected_data.groupby(['Year', 'Species'])['Lifespan'].mean().reset_index()

            # Calculate average Lifespan across all years for selected species
            average_Lifespan_rate = species_Lifespan_rate['Lifespan'].mean()

            # Create pie chart
            fig = px.pie(species_Lifespan_rate, values='Lifespan', names='Species',
                         title='Mean Lifespan of Selected Species Across Years',
                         labels={'Lifespan': 'Mean Lifespan', 'Species': 'Species'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average Lifespan: {average_Lifespan_rate:.2f}',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        def create_bar_chart_BDH_all_years_Lifespanrate(df):
            # Group by 'Year' and 'DBH Size Class' and calculate mean 'Lifespan' for each DBH size class in each year
            dbh_Lifespan_rate = df.groupby(['Year', 'Size Class'])['Lifespan'].mean().reset_index()
            # Calculate average Lifespan across all years
            average_Lifespan_rate = dbh_Lifespan_rate['Lifespan'].mean()
            # Create bar chart
            fig = px.bar(dbh_Lifespan_rate, x='Year', y='Lifespan', color='Size Class',
                         title='Mean Lifespan for Each DBH Size Class Across Years',
                         labels={'Lifespan': 'Mean Lifespan', 'Year': 'Year', 'Size Class': 'Size Class'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(dbh_Lifespan_rate['Year']), y0=average_Lifespan_rate,
                          x1=max(dbh_Lifespan_rate['Year']), y1=average_Lifespan_rate,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        def create_pie_chart_BDH_all_years_Lifespanrate(df):
            # Group by 'DBH Size Class' and calculate mean 'Lifespan' for each DBH size class across all years
            dbh_Lifespan_rate = df.groupby('Size Class')['Lifespan'].mean().reset_index()

            # Calculate average Lifespan across all size classes
            average_Lifespan_rate = dbh_Lifespan_rate['Lifespan'].mean()

            # Create pie chart
            fig = px.pie(dbh_Lifespan_rate, values='Lifespan', names='Size Class',
                         title='Mean Lifespan for Each DBH Size Class Across Years',
                         labels={'Lifespan': 'Mean Lifespan', 'Size Class': 'Size Class'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average Lifespan: {average_Lifespan_rate:.2f}',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        def create_bar_chart_BDH_all_years_Lifespan(df):
            # Group by 'Year' and 'DBH Size Class' and calculate sum 'Lifespan' for each DBH size class in each year
            dbh_Lifespan = df.groupby(['Year', 'Size Class'])['Lifespan'].sum().reset_index()
            # Calculate average Lifespan across all years
            average_Lifespan = dbh_Lifespan['Lifespan'].mean()
            # Create bar chart
            fig = px.bar(dbh_Lifespan, x='Year', y='Lifespan', color='Size Class',
                         title='Sum Lifespan for Each DBH Size Class Across Years',
                         labels={'Lifespan': 'Sum Lifespan', 'Year': 'Year', 'Size Class': 'Size Class'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(dbh_Lifespan['Year']), y0=average_Lifespan,
                          x1=max(dbh_Lifespan['Year']), y1=average_Lifespan,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        st.sidebar.header("Setting")
        selected_year = st.sidebar.radio("Select Year", df['Year'].unique())
        selected_hectares = st.sidebar.multiselect("Select Hectares", df['Hectare'].unique(),
                                                   default=df['Hectare'].unique())
        selected_species = st.sidebar.multiselect("Select Species", df['Species'].unique(),
                                                  default=['CANAPA', 'PAYELU', 'SHORP2'])

        # -----------------------------------------

        # --------- Most SP
        chart_type = st.sidebar.radio("Select Chart Type", ("Bar Chart", "Pie Chart"))
        if chart_type == "Bar Chart":
            # ----------------------------------- the Main
            col1, col2 = st.columns(2)
            with col1:
                create_bar_chart_BDH_all_years_Lifespan(df)
            with st.expander("Lifespan Trends in Species"):
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_5_top_sp(df, selected_year)
                with col2:
                    create_bar_chart_sp_year(df, selected_species)

            with st.expander("Lifespan Trends in All Hectares (By Size class and Age Class)"):
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_Lifespan(df, selected_year)
                with col2:
                    create_bar_chart_Lifespan_rate(df, selected_year)
                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_Lifespan_age(df, selected_year)
                with col2:
                    create_bar_chart_Lifespan_rate_age(df, selected_year)

            with st.expander("Lifespan Trends in Selected Hectare (By Size class and Age Class)"):
                st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

                st.write("To see the trend in selected hectare please first choose your desire hectares")
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_Lifespan_hectare(df, selected_hectares)
                with col2:
                    create_bar_chart_Lifespan_rate_hectare(df, selected_hectares)

                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_Lifespan_hectare_age(df, selected_hectares)
                with col2:
                    create_bar_chart_Lifespan_rate_hectare_age(df, selected_hectares)

        if chart_type == "Pie Chart":
            col1, col2 = st.columns(2)
            with col2:
                create_bar_chart_BDH_all_years_Lifespan(df)
            with st.expander("Lifespan Trends in Species"):
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_5_top_sp(df, selected_year)
                with col2:
                    create_pie_chart_sp_year(df, selected_species)

            with st.expander("Lifespan Trends in All Hectares (By Size class and Age Class)"):
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_Lifespan(df, selected_year)
                with col2:
                    create_pie_chart_Lifespan_rate(df, selected_year)
                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_Lifespan_age(df, selected_year)
                with col2:
                    create_pie_chart_Lifespan_rate_age(df, selected_year)

            with st.expander("Lifespan Trends in Selected Hectare (By Size class and Age Class)"):
                st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

                st.write("To see the trend in selected hectare please first choose your desire hectares")
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_Lifespan_hectare(df, selected_hectares)
                with col2:
                    create_pie_chart_Lifespan_rate_hectare(df, selected_hectares)

                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_Lifespan_hectare_age(df, selected_hectares)
                with col2:
                    create_pie_chart_Lifespan_rate_hectare_age(df, selected_hectares)