import streamlit as st

# SC-Armor / ShieldSync Core Prototype Dashboard

st.set_page_config(page_title="SC-Armor Dashboard", layout="wide")

# Branding Header
st.markdown("# SC🛡Armor – ShieldSync Core")
st.markdown("**AI-Enhanced Supply Chain Risk Response System**")
st.markdown("---")

# Simulated disruption data
st.subheader("Disruption Simulation")
region = st.selectbox("Select Region", ["Midwest", "Northeast", "South", "West Coast"])
disruption_type = st.selectbox("Type of Disruption", ["Storm", "Cyber Attack", "Fuel Shortage", "Labor Strike"])
severity = st.slider("Severity Level", 1, 5, 3)
time_to_impact = st.slider("Time to Impact (Hours)", 0, 24, 6)

# AI Recommendation Engine (Prototype)
def generate_response(sev):
    if sev >= 4:
        return ["Reroute Supplies", "Activate Emergency Inventory", "Notify 3PL"]
    elif sev == 3:
        return ["Notify 3PL", "Increase Monitoring"]
    else:
        return ["Monitor Situation", "Run AI Recheck in 1 Hour"]

if st.button("Run AI Risk Response"):
    result = generate_response(severity)
    st.success("Recommended Action Plan:")
    for step in result:
        st.write(f"- {step}")
