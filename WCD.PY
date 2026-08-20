import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Centum Working Capital Command Center",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Centum Working Capital Command Center")
st.markdown(
"""
### Forecast • Benchmark • Optimize • Create Value
"""
)

# ==========================================
# INPUT DATA
# ==========================================

forecast_revenue = 8086.73
forecast_dso = 119.45
forecast_dio = 261.27
forecast_dpo = 132.21
forecast_ccc = 248.51

benchmark_ccc = 149.54
benchmark_dso = 91.19
benchmark_dio = 177.83
benchmark_dpo = 119.49

gap_ccc = 103.18

benchmark_df = pd.DataFrame({
    "Company":[
        "Kaynes Technologies",
        "Centum",
        "Astra",
        "Apollo Micro Systems",
        "Datapatterns"
    ],
    "Avg CCC":[
        149.54,
        252.72,
        422.08,
        489.20,
        868.91
    ]
})

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.header("Scenario Inputs")

interest_rate = st.sidebar.slider(
    "Interest Rate (%)",
    1.0,
    20.0,
    10.0
)

dio_reduction = st.sidebar.slider(
    "Reduce DIO By (Days)",
    0,
    60,
    10
)

dso_reduction = st.sidebar.slider(
    "Reduce DSO By (Days)",
    0,
    30,
    5
)

dpo_increase = st.sidebar.slider(
    "Increase DPO By (Days)",
    0,
    30,
    0
)

# ==========================================
# TABS
# ==========================================

tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8 = st.tabs([
    "Executive Summary",
    "Forecasting",
    "Benchmarking",
    "Gap Analysis",
    "Opportunity Ranking",
    "Scenario Simulator",
    "Value Creation",
    "Sensitivity Analysis"
])

# ======================================================
# TAB 1
# ======================================================

with tab1:

    st.subheader("Executive KPI Summary")

    c1,c2,c3,c4,c5 = st.columns(5)

    c1.metric(
        "FY2026 Revenue 'Mns'",
        f"₹{forecast_revenue:,.2f} Mn"
    )

    c2.metric(
        "Forecast CCC",
        f"{forecast_ccc:.2f} Days"
    )

    c3.metric(
        "Benchmark CCC",
        f"{benchmark_ccc:.2f}"
    )

    c4.metric(
        "CCC Gap",
        f"{gap_ccc:.2f}"
    )

    c5.metric(
        "Top Driver",
        "DIO"
    )

# ======================================================
# TAB 2
# ======================================================

with tab2:

    st.subheader("Forecast Summary")

    final_forecast = pd.DataFrame({
        "Financial Year":[
            "FY2026F",
            "FY2027F",
            "FY2028F"
        ],
        "Revenue (M)":[
            8086.73,
            8571.69,
            9056.66
        ],
        "DSO":[119.45]*3,
        "DIO":[261.27]*3,
        "DPO":[132.21]*3,
        "CCC":[248.51]*3
    })

    st.dataframe(
        final_forecast,
        use_container_width=True,
hide_index=True
    )

# ======================================================
# TAB 3
# ======================================================

with tab3:

    benchmark_display = benchmark_df.copy()

    benchmark_display.index = range(
        1,
        len(benchmark_display) + 1
    )

    st.dataframe(
        benchmark_display,
        use_container_width=True
    )

    fig = px.bar(
        benchmark_df,
        x="Company",
        y="Avg CCC",
        color="Avg CCC",
        text="Avg CCC",
        color_continuous_scale="RdYlGn_r",
        title="Peer CCC Benchmarking"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ======================================================
# TAB 4
# ======================================================

with tab4:

    gap_table = pd.DataFrame({
        "Metric":[
            "DSO",
            "DIO",
            "DPO",
            "CCC"
        ],
        "Benchmark":[
            91.19,
            177.83,
            119.49,
            149.54
        ],
        "Centum":[
            113.94,
            269.70,
            130.93,
            252.72
        ],
        "Gap":[
            22.75,
            91.87,
            11.44,
            103.18
        ]
    })

    st.dataframe(
        gap_table,
        use_container_width=True,
hide_index=True
    )

# ======================================================
# TAB 5
# ======================================================

with tab5:

    opportunity_df = pd.DataFrame({
        "Driver":[
            "DIO",
            "DSO",
            "DPO"
        ],
        "Opportunity":[
            91.87,
            22.75,
            -11.44
        ]
    })

    fig = px.bar(
        opportunity_df,
        x="Driver",
        y="Opportunity",
        text="Opportunity",
        color="Opportunity",
        title="Opportunity Ranking Across CCC Drivers"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ======================================================
# TAB 6
# ======================================================

with tab6:

    revised_ccc = (
        (forecast_dso - dso_reduction)
        +
        (forecast_dio - dio_reduction)
        -
        (forecast_dpo + dpo_increase)
    )

    ccc_reduction = (
        forecast_ccc - revised_ccc
    )

    scenario_df = pd.DataFrame({
        "Metric":[
            "Current CCC",
            "Optimized CCC",
            "Reduction"
        ],
        "Value":[
            forecast_ccc,
            revised_ccc,
            ccc_reduction
        ]
    })

    st.dataframe(
        scenario_df,
        use_container_width=True,
hide_index=True
    )

# ======================================================
# TAB 7
# ======================================================

with tab7:

    cash_release = (
        forecast_revenue / 360
    ) * ccc_reduction

    interest_saved = (
        cash_release
        * interest_rate
        / 100
    )

    k1,k2,k3,k4 = st.columns(4)

    k1.metric(
        "Optimized CCC",
        f"{revised_ccc:.2f}"
    )

    k2.metric(
        "CCC Reduction",
        f"{ccc_reduction:.2f} Days"
    )

    k3.metric(
        "Cash Released",
        f"₹{cash_release:,.2f} Mn"
    )

    k4.metric(
        "Interest Savings",
        f"₹{interest_saved:,.2f} Mn"
    )

# ======================================================
# TAB 8
# ======================================================

with tab8:

    sensitivity_df = pd.DataFrame({
        "Company":[
            "Centum",
            "Astra",
            "Datapatterns",
            "Kaynes Technologies",
            "Apollo Micro Systems"
        ],
        "Avg CCC":[
            252.72,
            422.08,
            868.91,
            149.54,
            489.20
        ],
        "Rank (All Data)":[
            2,3,5,1,4
        ],
        "Avg9 CCC":[
            261.15,
            444.35,
            706.91,
            149.54,
            517.11
        ],
        "Rank (9Y)":[
            2,3,5,1,4
        ]
    })

    st.dataframe(
        sensitivity_df,
        use_container_width=True,
hide_index=True
    )

# ======================================================
# RECOMMENDATION
# ======================================================

st.markdown("---")

st.subheader("Executive Recommendation")

st.success(
f"""
✅ Inventory Optimization remains the highest-priority lever.

✅ Current Forecast CCC: {forecast_ccc:.2f} Days

✅ Optimized CCC: {revised_ccc:.2f} Days

✅ Cash Release Potential: ₹{cash_release:,.2f} Mn

✅ Interest Savings Potential: ₹{interest_saved:,.2f} Mn

✅ Recommended Focus:
Inventory Optimization (DIO) followed by Receivables Optimization (DSO).
"""
)