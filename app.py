import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv('vehicles_us.csv')

models = df['model'].unique()

# Multiselect for selecting models
models = df['model'].unique()
selected_models = st.multiselect("Select car models", models)

# Filter DataFrame based on selected models
if selected_models:
    filtered_df = df[df['model'].isin(selected_models)]
else:
    filtered_df = df  # If no selection, show all data

# Plot the histogram
st.subheader("Days Listed vs Condition Histogram")
if not filtered_df.empty:
    fig, ax = plt.subplots(figsize=(8, 6))
    filtered_df.groupby('condition')['days_listed'].mean().plot(
        kind='bar', ax=ax, color='skyblue', edgecolor='black'
    )
    ax.set_xlabel("Condition")
    ax.set_ylabel("Average Days Listed")
    ax.set_title("Average Days Listed by Condition")
    st.pyplot(fig)
else:
    st.write("No data to display. Select at least one model.")

    # comparing the time listed by condition with a checkbox for selecting the models

st.header("Car type vs Color")

# Dropdown for paint color
paint_color = st.selectbox(
    "Select Paint Color",
    options=df['paint_color'].unique(),
    index=0
)

# Dropdown for car type
car_type = st.selectbox(
    "Select Car Type",
    options=df['type'].unique(),
    index=0
)

# Filter data based on the selections
filtered_df = df[(df['paint_color'] == paint_color) & (df['type'] == car_type)]

# Plot histogram
st.subheader(f"Histogram of Days Listed for {paint_color} {car_type}s")
if not filtered_df.empty:
    fig, ax = plt.subplots()
    ax.hist(filtered_df['days_listed'], bins=10, color='skyblue', edgecolor='black')
    ax.set_xlabel("Days Listed")
    ax.set_ylabel("Frequency")
    ax.set_title(f"Days Listed for {paint_color} {car_type}s")
    st.pyplot(fig)
else:
    st.write("No data available for the selected combination.")


# Title for the Streamlit app
st.title("Car Price vs. Model Scatterplot")

# Create the scatterplot using Plotly Express
fig = px.scatter(
    df,
    x='model',
    y='price',
    title="Car Price vs. Model",
    labels={'model': 'Car Model', 'price': 'Price (in USD)'},
    template='plotly',
)

# Customize the scatterplot
fig.update_traces(marker=dict(size=12, color='blue', line=dict(width=1, color='black')))
fig.update_layout(
    title_font_size=18,
    xaxis_title="Car Model",
    yaxis_title="Price (in USD)",
    xaxis_tickangle=45,
    xaxis_tickfont=dict(size=10),
    yaxis_tickfont=dict(size=12),
)

# Display the plot in the Streamlit app
st.plotly_chart(fig, use_container_width=True)