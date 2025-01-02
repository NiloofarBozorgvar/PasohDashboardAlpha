import streamlit as st
import pandas as pd


st.set_page_config(page_title="Pasoh Forest Dashboard", layout="wide")

# Load dataset
def load_data():
    data = pd.DataFrame({
        "Plan ID": ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10", "P12"],
        "Action Time": ["Now (1986)", "Now (1986)", "Now (1986)", "Next 5 years (1991)",
                        "Next 5 years (1991)", "Next 5 years (1991)", "Now (1986)",
                        "Now (1986)", "Now (1986)", "Next 5 years (1991)", "Next 5 years (1991)"],
        "Regime": ["Heavy", "Medium", "Light", "Heavy", "Medium", "Light", "Heavy",
                   "Medium", "Light", "Heavy", "Medium"],
        "Objective": ["Specie", "Specie", "Specie", "Specie", "Specie", "Specie",
                      "Volume", "Volume", "Volume", "Volume", "Volume"],
        "Total Number of trees to be fell": [20, 16, 12, 20, 16, 12, 20, 16, 12, 20, 16],
        "Dipterocarp trees to be fell": [8, 6, 6, 15, 8, 8, 12, 8, 7, 7, 8],
        "Non-Dipterocarp trees to be fell": [10, 6, 4, 3, 7, 2, 4, 6, 2, 11, 5],
        "Chengal trees to be fell": [2, 2, 2, 2, 1, 2, 4, 2, 2, 2, 3],
    })
    return data

data = load_data()


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
st.title("Pasoh Forest Dashboard")
st.subheader("Select the Prescription Method")
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


data_1986 = pd.read_csv('Updated_Merged_Dataset.csv')
st.write(data_1986)
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
        indx +=1
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


def apply_colors(value, column, max_min_values = max_min_values):
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


def apply_colors(value, column, max_min_values = max_min_values):
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




#========== PAGE3

#=========== select the PID
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
        "Regime": [20, 16, 12, 20, 16, 12, 20, 16, 12, 20, 16, 12]    })


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
    "TAG": [2317, 2318, 2319, 2320, 2321, 2322, 2323, 2323, 2324, 2324, 2325, 2325, 2325, 2325, 2326, 2327, 2328, 2328],
    "Species": ["SHORP2", "MESURA", "CANAPA", "PAYELU", "GIROPA", "MACALO", "DACRR1", "MACALO", "KOOMMA", "NAUCOF", "SHORL1",
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
                 color="Species", hover_data=[ "Species", "Hectare"],
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

tree_data =file_data

# Add canopy radius calculation (smaller canopies)
K = 0.05  # Reduced empirical constant for smaller canopies
file_data["Canopy_Radius"] = file_data["DBH"] * K  # Radius in meters

# Add canopy volume calculation
file_data["Canopy_Volume"] = (4 / 3) * np.pi * (file_data["Canopy_Radius"] ** 3)

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