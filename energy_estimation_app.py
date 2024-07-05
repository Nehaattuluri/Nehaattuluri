import streamlit as st
import pandas as pd

Appliances= ['Fridge', 'Washing Machine', 'Air Conditioner', 'Oven']

Month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Sample data for demonstration (replace with your actual data)
data = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Energy_Consumption': [1000, 1100, 1050, 1120, 1080, 1150, 1200, 1180, 1220, 1250, 1300, 1350]
})

# Function to calculate estimated energy consumption based on appliances
def calculate_energy_consumption(month, appliances):
    base_energy = data.loc[data['Month'] == month, 'Energy_Consumption'].values[0]
    appliance_factor = len(appliances) * 100  # Dummy factor, replace with actual calculation
    estimated_energy = base_energy + appliance_factor
    return estimated_energy

# Streamlit app
st.title('Energy Consumption Estimation')

# Sidebar for user input
selected_months = st.sidebar.multiselect('Select Months', data['Month'])
selected_appliances = st.sidebar.multiselect('Select Appliances', Appliances)


# Display the selected options
st.write('Selected Months:', selected_months)
st.write('Selected Appliances:', selected_appliances)



# Function to calculate energy consumption
def calculate_energy_consumption(months, appliances):
    # Placeholder logic for energy consumption calculation
    # Replace this with your actual logic
    energy_consumption = {
        'Fridge': 100,
        'Washing Machine': 200,
        'Air Conditioner': 300,
        'Oven': 150
    }

    total_energy = 0
    for month in months:
        for appliance in appliances:
            total_energy += energy_consumption.get(appliance, 0)  # Sum energy consumption for each appliance

    return total_energy

# Calculate energy consumption
if selected_months and selected_appliances:
    total_energy = calculate_energy_consumption(selected_months, selected_appliances)
    st.write(f'Total Energy Consumption for selected months and appliances: {total_energy} kWh')
else:
    st.write('Please select both months and appliances to calculate energy consumption.')

# Button to trigger calculation
if st.sidebar.button('Calculate'):
    estimated_energy = calculate_energy_consumption(selected_months, selected_appliances)
    st.write(f"### Estimated Energy Consumption for {selected_months}: **{estimated_energy} kWh**")
