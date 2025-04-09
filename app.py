import streamlit as st
from datetime import datetime

st.set_page_config(page_title="SC-Armor | ShieldSync AI", layout="wide")

# ----------------- HEADER -------------------
st.markdown("## 🛡️ SC-Armor – ShieldSync AI Dashboard")
st.markdown("**Protecting National Supply Chain Infrastructure with Live AI-Driven Risk Detection**")
st.markdown("---")

# ----------------- SIMULATION INPUTS -------------------
st.sidebar.header("🛰️ Disruption Simulation Input")
region = st.sidebar.selectbox("Region", ["Midwest", "Northeast", "South", "West Coast"])
disruption_type = st.sidebar.selectbox("Disruption Type", ["Storm", "Cyber Attack", "Fuel Shortage", "Labor Strike", "Sabotage"])
severity = st.sidebar.slider("Severity Level", 1, 5, 3)
hours_to_impact = st.sidebar.slider("Hours to Impact", 0, 24, 6)
today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ----------------- GUARDIAN STRAND VERIFICATION -------------------
def guardian_strand_active():
    return True  # always active for demo purposes

st.sidebar.markdown("---")
if guardian_strand_active():
    st.sidebar.success("✅ Guardian Strand: VERIFIED")
else:
    st.sidebar.error("❌ Guardian Strand: INACTIVE")

# ----------------- RISK RESPONSE ENGINE -------------------
def generate_response(sev):
    if sev >= 4:
        return [
            "🔁 Reroute regional supply chain",
            "📦 Deploy emergency reserves to hospitals & food hubs",
            "📡 Notify 3PL partners & reroute trucks via safest path"
        ]
    elif sev == 3:
        return [
            "📡 Notify 3PL partners",
            "📊 Increase AI risk monitoring frequency to hourly",
            "⏳ Deploy early-warning notice to warehouses"
        ]
    else:
        return [
            "⏳ Continue monitoring conditions",
            "🧠 AI auto-check scheduled in 60 minutes"
        ]

# ----------------- MAIN DASHBOARD -------------------
st.subheader("📊 Disruption Summary")
st.write(f"**Detected Region:** {region}")
st.write(f"**Type of Disruption:** {disruption_type}")
st.write(f"**Severity Level:** {severity} / 5")
st.write(f"**Estimated Time to Impact:** {hours_to_impact} hours")
st.write(f"**Timestamp:** {today}")
st.markdown("---")

if st.button("🔐 Initiate AI Risk Assessment"):
    action_plan = generate_response(severity)
    st.success("✅ AI Recommended Action Plan:")
    for step in action_plan:
        st.write(f"- {step}")
    st.info("🛡️ SC-Armor AI recommendation delivered. Awaiting human confirmation or auto-execution based on client setting.")
else:
    st.warning("⚠️ No simulation running. Adjust parameters and press the button to initiate AI analysis.")
