import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv('vehicles_us.csv')

models = df['model'].unique()

st.title("Car Listings Analysis")

# Checkbox for selecting models
selected_models = []
for model in models:
    if st.checkbox(model, key=model):
        selected_models.append(model)

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


plt.figure(figsize=(10, 6))
plt.scatter(df['model'], df['price'], color='blue', alpha=0.7, edgecolors='black')

# Customize the plot
plt.title("Car Price vs. Model", fontsize=16)
plt.xlabel("Model", fontsize=14)
plt.ylabel("Price (in USD)", fontsize=14)
plt.xticks(rotation=45, ha="right", fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()