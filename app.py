import streamlit as st
from datetime import datetime

# --- CONFIG ---
st.set_page_config(page_title="AMERICAN SHIELD COMMAND", layout="wide")

# --- STYLE OVERRIDES ---
st.markdown('''
    <style>
        html, body, [class*="css"]  {
            background-color: #0a0f1a;
            color: #ffffff;
            font-family: "Segoe UI", sans-serif;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }
        h1, h2, h3, h4 {
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .metric-label {
            font-size: 14px;
            font-weight: 500;
            color: #AAAAAA;
        }
        .section-divider {
            border-top: 1px solid #333333;
            margin: 20px 0;
        }
        .response-button {
            background-color: #17375e;
            color: white;
            padding: 10px 25px;
            border-radius: 6px;
            font-size: 14px;
        }
    </style>
''', unsafe_allow_html=True)

# --- HEADER ---
st.markdown("### 🛡 AMERICAN SHIELD COMMAND")
st.caption("National Infrastructure Risk Command Interface")

# --- TOP LAYOUT ---
col1, col2 = st.columns([2, 1], gap="medium")

with col1:
    st.image("https://i.imgur.com/66XbnqE.png", caption="Simulated Blizzard Zone", use_column_width=True)  # Placeholder map image
    st.markdown("### SHIELD RESPONSE SUGGESTED")
    st.markdown("**Divert shipments via Kansas City distribution corridor**", unsafe_allow_html=True)
    if st.button("INITIATE RESPONSE"):
        st.success("✅ Shield response deployed")
        st.info("Routes updated. Emergency inventory dispatched.")

with col2:
    st.markdown("### DISRUPTION PULSE")
    st.progress(0.88, text="Risk Level: HIGH")

    st.markdown("---")
    st.markdown("### INCOMING DISRUPTIONS")
    
    st.markdown("#### Without Action")
    st.markdown("- 36-hour regional shortage")
    st.markdown("- Est. $12M in spoiled inventory")
    st.markdown("- Public Risk Level: RED (critical)")
    
    st.markdown("#### With Shield Response")
    st.markdown("- Shipments rerouted in < 6 hours")
    st.markdown("- $170K reroute cost")
    st.markdown("- Public Risk Level: GREEN (contained)")

# --- FOOTER ---
st.markdown("---")
st.markdown("© 2025 American Shield Systems LLC — Proprietary & Confidential")
st.markdown("*This platform and all source code are protected under U.S. copyright law. Unauthorized duplication or use is prohibited.*")
