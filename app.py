import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title="SC-Armor | American Shield Command", layout="wide")

# ---------- STYLE ----------
custom_style = '''
    <style>
    body {
        background-color: #0b0f1a;
        color: #ffffff;
    }
    .stApp {
        background-color: #0b0f1a;
        color: #ffffff;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    </style>
'''
st.markdown(custom_style, unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<h1 style='color: #ffffff;'>🛡️ AMERICAN SHIELD COMMAND</h1>", unsafe_allow_html=True)
st.markdown("---")

# ---------- LAYOUT ----------
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🌨️ Blizzard Forecast")
    st.markdown("**Location:** Midwest (Iowa, Missouri, Illinois)")
    st.markdown("**Time to Impact:** 3 days")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/USA_blank_map.svg/1024px-USA_blank_map.svg.png", width=500, caption="Simulated Disruption Map")

    st.markdown("### 🛡️ SHIELD RESPONSE SUGGESTED")
    st.success("✅ Divert shipments via Kansas City distribution corridor")
    if st.button("🔐 INITIATE RESPONSE"):
        st.info("Shield Response Initiated...")
        time.sleep(1)
        st.success("Response Confirmed. Emergency routes activated.")

with col2:
    st.markdown("### 📈 DISRUPTION PULSE")
    severity = st.slider("Current Severity Index", 1, 10, 8)
    gauge_color = "🟢" if severity < 4 else "🟠" if severity < 7 else "🔴"
    st.markdown(f"**Risk Level:** {gauge_color} {'HIGH' if severity >= 7 else 'MODERATE' if severity >= 4 else 'LOW'}")

    st.markdown("---")
    st.markdown("### 🚨 INCOMING DISRUPTIONS")
    st.write("**WITHOUT ACTION**")
    st.markdown("- ⏳ 36-hour regional shortage")
    st.markdown("- 💸 Est $12M in spoiled inventory")
    st.markdown("- 🔥 Public Risk Level: RED (critical)")

    st.write("**WITH SHIELD RESPONSE**")
    st.markdown("- 🚛 Shipments rerouted in under 6 hours")
    st.markdown("- 💵 $170K reroute cost")
    st.markdown("- 🟢 Public Risk Level: CONTAINED")

# ---------- FOOTER ----------
st.markdown("---")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.markdown(f"<small style='color:gray;'>Live simulation generated {timestamp}</small>", unsafe_allow_html=True)
