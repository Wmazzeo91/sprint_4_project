import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("vehicles.csv")

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