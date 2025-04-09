
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="ShieldSync Dashboard", layout="wide")

# ----------- STYLE -------------
st.markdown('''
    <style>
        body {
            background-color: #0b0f1a;
            color: #ffffff;
        }
        .stApp {
            background-color: #0b0f1a;
        }
        h1, h2, h3 {
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .footer {
            color: gray;
            font-size: 11px;
            text-align: center;
            margin-top: 30px;
        }
        .division {
            font-size: 12px;
            color: #888888;
            text-align: center;
            margin-bottom: -20px;
        }
    </style>
''', unsafe_allow_html=True)

# ----------- HEADER / BRANDING -------------
st.markdown("## 🛡 SHIELDSYNC")
st.markdown("<div class='division'>A division of SC🛡Armor</div>", unsafe_allow_html=True)
st.markdown("### NATIONAL SUPPLY CHAIN COMMAND INTERFACE")
st.markdown("---")

col1, col2 = st.columns([2, 1], gap="large")

# ----------- MAP / FORECAST SECTION -------------
with col1:
    st.subheader("📍 Midwest Disruption")
    st.markdown("**Blizzard Forecast - 3 Days**")
    
    # Glowing hotspot effect using Plotly
    fig = go.Figure(go.Scattergeo(
        lon=[-93.5], lat=[41.9],
        mode='markers',
        marker=dict(size=120, color='red', opacity=0.3),
        text=["Blizzard Forecast"],
    ))

    fig.update_geos(
        scope="usa",
        showland=True, landcolor="#1f2c3d",
        showcountries=True, countrycolor="#444",
        showlakes=False,
        lataxis=dict(range=[30, 50]),
        lonaxis=dict(range=[-105, -80])
    )

    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="#0b0f1a",
        geo_bgcolor="#0b0f1a",
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### 🛡 SHIELD RESPONSE SUGGESTED")
    st.markdown("**Divert shipments via Kansas City distribution corridor**")

    if st.button("🔐 INITIATE RESPONSE"):
        st.success("✅ Response Confirmed")
        st.info("Emergency routes activated. Simulation logged.")

# ----------- METRICS SECTION -------------
with col2:
    st.subheader("📊 Disruption Pulse")
    severity = st.slider("Current Severity Level", 1, 10, 8)
    gauge_color = "#3adb76" if severity < 4 else "#f39c12" if severity < 7 else "#e74c3c"
    
    fig2 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=severity,
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [0, 10]},
            'bar': {'color': gauge_color},
            'steps': [
                {'range': [0, 3], 'color': "#1e5631"},
                {'range': [3, 7], 'color': "#f1c40f"},
                {'range': [7, 10], 'color': "#c0392b"}
            ],
        }
    ))
    fig2.update_layout(height=250, margin=dict(t=0, b=0, l=10, r=10), paper_bgcolor="#0b0f1a", font_color="#ffffff")
    st.plotly_chart(fig2)

    st.markdown("---")
    st.subheader("📦 Incoming Disruptions")

    st.markdown("**WITHOUT ACTION**")
    st.markdown("- ❌ 36-hour regional shortage")
    st.markdown("- ❌ Est. $12M in spoiled inventory")
    st.markdown("- 🔥 Public Risk Level: RED")

    st.markdown("**WITH SHIELD RESPONSE**")
    st.markdown("- ✅ Shipments rerouted in < 6 hours")
    st.markdown("- ✅ $170K reroute cost")
    st.markdown("- 🟢 Public Risk Level: CONTAINED")

# ----------- FOOTER / COPYRIGHT -------------
st.markdown("---")
st.markdown("<div class='footer'>© 2025 SC🛡Armor. All rights reserved. ShieldSync™ is a proprietary technology. Unauthorized use is prohibited.</div>", unsafe_allow_html=True)
