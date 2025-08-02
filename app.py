import streamlit as st
import numpy as np
import joblib  

# Load the trained model
model = joblib.load(r"C:\Users\archa\Downloads\Farm_Irrigation_System.pkl")  

st.title("SMART IRRIGATION SYSTEM")
st.subheader("Enter scaled sensor values (0 to 1) to predict sprinkler status")

# 3. Add Info Section
st.info("Use the sliders below to simulate sensor readings (scaled 0 to 1). Then click 'Predict Sprinklers' to see the system's recommendation.")

# Collect sensor inputs (scaled values)
sensor_values = []
for i in range(20):
    val = st.slider(f"Sensor {i}", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    sensor_values.append(val)

# Predict button
if st.button("Predict Sprinklers"):
    input_array = np.array(sensor_values).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    st.markdown("### Prediction:")
    for i, status in enumerate(prediction):
        # 2. Display Output with Color or Emojis
        emoji = "🟢 ON" if status == 1 else "🔴 OFF"
        st.write(f"Sprinkler {i} (parcel_{i}): {emoji}")

#  Option 3: Add collapsible "About this Project" section
with st.expander("About this Project"):
    st.write(
        "This web app was developed as part of the AICTE-offered internship by Archana J Dev. "
        "It uses a machine learning model trained on historical irrigation data to predict which sprinklers should be turned ON or OFF "
        "based on simulated sensor inputs. Built using Python and Streamlit."
    )
