import streamlit as st
from datetime import datetime

st.set_page_config(page_title="SC🛡Armor Platform", layout="wide")

# ---------------- STYLE ----------------
st.markdown('''
    <style>
        html, body, [class*="css"] {
            background-color: #0b0f1a;
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
            font-size: 11px;
            text-align: center;
            margin-top: 3rem;
        }
        .logo-title {
            font-size: 32px;
            font-weight: bold;
            letter-spacing: 2px;
            margin-bottom: 0.5rem;
        }
        .mode-label {
            font-size: 16px;
            margin-bottom: 0.2rem;
            color: #AAAAAA;
        }
    </style>
''', unsafe_allow_html=True)

# ---------------- HEADER ----------------
mode = st.radio("Choose Platform Mode", ["🟩 ShieldSync (Civilian)", "🟦 American Shield Command (Gov)"], horizontal=True)
is_gov = "Command" in mode

# Brand
if is_gov:
    st.markdown('<div class="logo-title">🛡 American Shield Command</div>', unsafe_allow_html=True)
    st.caption("National Infrastructure Risk Defense System")
else:
    st.markdown('<div class="logo-title">🛡 ShieldSync</div>', unsafe_allow_html=True)
    st.caption("A division of SC🛡Armor — Civilian Supply Chain Risk Response System")

st.markdown("---")

# ---------------- LAYOUT ----------------
col1, col2 = st.columns([2, 1], gap="large")

with col1:
    st.subheader("📍 Midwest Disruption")
    st.markdown("Blizzard Forecast – 3 Days")
    st.image("https://i.imgur.com/MbI6fcR.png", caption="Blizzard Zone Forecast", use_container_width=True)

    st.subheader("🛡 Suggested Response")
    st.markdown("**Divert shipments via Kansas City distribution corridor**")

    if st.button("🔐 INITIATE RESPONSE"):
        st.success("✅ Response Confirmed")
        st.info("Emergency protocols activated.")

with col2:
    st.subheader("📊 Disruption Pulse")
    severity = st.slider("Current Severity Level", 1, 10, 8)

    pulse_status = (
        "🟢 LOW" if severity < 4 else
        "🟠 MODERATE" if severity < 7 else
        "🔴 HIGH"
    )
    st.markdown(f"**Risk Level:** {pulse_status}")

    st.markdown("### 🚨 Incoming Disruptions")
    st.markdown("**Without Action**")
    st.markdown("- ❌ 36-hour regional shortage")
    st.markdown("- ❌ Est. $12M in spoiled inventory")
    st.markdown("- 🔥 Public Risk Level: RED")

    st.markdown("**With Shield Response**")
    st.markdown("- ✅ Shipments rerouted in <6 hours")
    st.markdown("- ✅ $170K reroute cost")
    st.markdown("- 🟢 Public Risk Level: CONTAINED")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown('<div class="footer">© 2025 SC🛡Armor. All rights reserved. ShieldSync™ and American Shield Command™ are proprietary technologies.<br>Unauthorized use is prohibited. Protected under U.S. copyright law.</div>', unsafe_allow_html=True)
