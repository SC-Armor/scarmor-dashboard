import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="SC🛡Armor Command Platform", layout="wide")

# ------------------ STYLE -------------------
st.markdown('''
    <style>
        html, body, [class*="css"] {
            background-color: #0a0f1c;
            color: white;
            font-family: 'Segoe UI', sans-serif;
        }
        .block-container {
            padding: 2rem;
        }
        h1, h2, h3 {
            letter-spacing: 1px;
            text-transform: uppercase;
        }
        .footer {
            color: gray;
            font-size: 10px;
            text-align: center;
            margin-top: 3rem;
        }
        .title-bar {
            font-size: 28px;
            font-weight: bold;
            color: #00bfff;
        }
        .subheader {
            font-size: 14px;
            color: #aaa;
        }
        .card {
            background-color: #131a26;
            padding: 20px;
            border-radius: 12px;
        }
    </style>
''', unsafe_allow_html=True)

# ------------------ HEADER -------------------
st.markdown('<div class="title-bar">🛡 SC-Armor | ShieldSync Command</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Civilian & Government Dual-AI Response System</div>', unsafe_allow_html=True)
st.markdown("---")

# ------------------ LAYOUT -------------------
col1, col2 = st.columns([2, 1], gap="large")

with col1:
    st.subheader("📍 Midwest Disruption Detected")
    st.markdown("**Forecast:** Blizzard | ETA: 3 Days")

    # --- INTERACTIVE HEAT MAP ---
    fig = go.Figure()

    fig.add_trace(go.Scattergeo(
        lon=[-93.5],
        lat=[41.6],
        mode='markers',
        marker=dict(
            size=100,
            color='red',
            opacity=0.4
        ),
        hoverinfo='text',
        text='Blizzard Zone'
    ))

    fig.update_geos(
        scope='usa',
        showcountries=True, countrycolor="Black",
        showland=True, landcolor="#1a2633",
        showlakes=True, lakecolor="#0a0f1c",
        showocean=True, oceancolor="#0a0f1c",
        bgcolor='#0a0f1c'
    )

    fig.update_layout(
        margin={"r":0,"t":0,"l":0,"b":0},
        paper_bgcolor="#0a0f1c",
        plot_bgcolor="#0a0f1c",
        geo=dict(projection_scale=3.2, center={"lat": 41.5, "lon": -93.5})
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### 🛡 Shield Response Suggested")
    st.success("Divert shipments via Kansas City distribution corridor")

    if st.button("🔐 INITIATE RESPONSE"):
        st.info("✅ Emergency reroute protocols deployed")
        st.markdown("**Inventory rerouted. Estimated delay reduced to < 6 hrs. Public risk level: CONTAINED.**")

with col2:
    st.subheader("📊 Disruption Pulse")
    severity = st.slider("Severity Index", 1, 10, 8)

    st.progress(severity / 10)

    st.markdown("### 🚨 Incoming Disruption Impact")
    st.markdown("**Without Action**")
    st.markdown("- ❌ 36-hour regional shortage")
    st.markdown("- ❌ Est. $12M in spoiled inventory")
    st.markdown("- 🔴 Public Risk Level: CRITICAL")

    st.markdown("**With Shield Response**")
    st.markdown("- ✅ Shipments rerouted in under 6 hours")
    st.markdown("- ✅ $170K reroute cost")
    st.markdown("- 🟢 Public Risk Level: CONTAINED")

# ------------------ FOOTER -------------------
st.markdown("---")
st.markdown('<div class="footer">© 2025 SC🛡Armor. All rights reserved. ShieldSync™ is a proprietary technology. Unauthorized use is prohibited. Protected under U.S. copyright law.</div>', unsafe_allow_html=True)

