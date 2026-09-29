import streamlit as st
import pandas as pd

# Mission Control: initialize the AstroGuard dashboard
st.set_page_config(
    page_title="AstroGuard AI",
    page_icon="🚀",
    layout="wide"
)

# Mission Control: load sample space-object telemetry
data = pd.read_csv("data/sample_objects.csv")

# Mission Control: application title
st.title("🚀 AstroGuard AI")
st.subheader("AI-Powered Space Object Risk & Observation Assistant")

st.write(
    "Analyze space-object characteristics and estimate "
    "their observation priority."
)

st.divider()

# Mission Control: collect telemetry
st.header("🛰️ Space Object Telemetry")

# Mission Control: select a known space object
selected_object = st.selectbox(
    "🛰️ Select Space Object",
    data["object_name"]
)

# Mission Control: retrieve telemetry for the selected object
object_data = data[data["object_name"] == selected_object].iloc[0]

distance = float(object_data["distance_km"])
velocity = float(object_data["velocity_km_s"])
size = float(object_data["size_m"])

st.info(
    f"Selected Object: {selected_object} | "
    f"Distance: {distance:,.0f} km | "
    f"Velocity: {velocity:.1f} km/s | "
    f"Size: {size:.1f} m"
)

st.divider()

# Mission Control: analyze the incoming telemetry
if st.button("🔍 Analyze Object", use_container_width=True):

    # Mission Control: calculate prototype risk score
    score = 0

    if distance < 30000:
        score += 2
    elif distance < 100000:
        score += 1

    if velocity > 7:
        score += 2
    elif velocity > 4:
        score += 1

    if size > 50:
        score += 2
    elif size > 20:
        score += 1

    # Mission Control: classify observation priority
    if score >= 4:
        risk = "HIGH"
        priority = "Urgent Observation"
        explanation = (
            "The object has characteristics that require "
            "closer monitoring."
        )

    elif score >= 2:
        risk = "MEDIUM"
        priority = "Increased Observation"
        explanation = (
            "The object should be monitored regularly "
            "using available observation resources."
        )

    else:
        risk = "LOW"
        priority = "Routine Observation"
        explanation = (
            "The entered characteristics indicate "
            "a lower observation priority."
        )

    # Mission Control: display analysis result
    st.header("📊 Analysis Result")

    if risk == "HIGH":
        st.error(f"🚨 Risk Level: {risk}")

    elif risk == "MEDIUM":
        st.warning(f"⚠️ Risk Level: {risk}")

    else:
        st.success(f"✅ Risk Level: {risk}")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Risk Score", f"{score}/6")

    with col2:
        st.metric("Observation Priority", priority)

    # Mission Control: explain the analysis
    st.subheader("💡 Analysis")
    st.info(explanation)

    # Mission Control: display telemetry summary
    st.subheader("📋 Telemetry Summary")

    summary_col1, summary_col2, summary_col3 = st.columns(3)

    with summary_col1:
        st.metric("Distance", f"{distance:,.0f} km")

    with summary_col2:
        st.metric("Velocity", f"{velocity:.1f} km/s")

    with summary_col3:
        st.metric("Size", f"{size:.1f} m")

    # Mission Control: visualize incoming telemetry
    st.subheader("📈 Risk Factor Visualization")

    chart_data = pd.DataFrame({
        "Factor": ["Distance", "Velocity", "Size"],
        "Value": [distance, velocity, size]
    })

    st.bar_chart(
        chart_data.set_index("Factor")
    )

st.divider()

st.caption("AstroGuard AI | Asteria '26 Open Challenge")