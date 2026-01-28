import streamlit as st
import pandas as pd
from pprint import pformat

# --- Backend imports ---
from data.fetch_financials import fetch_stock_financials
from data.fetch_sector_etfs import fetch_sector_etf_metrics
from analytics.compute_multiples import compute_stock_multiples, compute_sector_multiples
from analytics.normalize import normalize_relative_valuation
from llm.sector_selector import select_sector_etf
from llm.mispricing_explainer import explain_relative_mispricing

# --- Page config ---
st.set_page_config(
    page_title="Sector-Based Valuation Estimator",
    layout="wide"
)

st.title("📊 Sector-Based Valuation Estimator")
st.caption(
    "A ballpark valuation tool using State Street Select Sector ETFs "
    "as sector proxies. Not a DCF. Not investment advice."
)

st.divider()

# --- User input ---
with st.form("valuation_form"):
    ticker = st.text_input("Enter Stock Ticker", value="XOM")
    company_name = st.text_input("Company Name", value="Exxon Mobil Corporation")
    business_description = st.text_area(
        "Business Description (optional)",
        value="Integrated oil and gas company with upstream, downstream, and chemicals operations.",
        height=100
    )

    submitted = st.form_submit_button("Run Valuation")

# --- Main workflow ---
if submitted:
    with st.spinner("Running sector-based valuation analysis..."):
        try:
            # 1️⃣ LLM: sector selection
            sector_selection = select_sector_etf(
                ticker=ticker,
                company_name=company_name,
                business_description=business_description
            )

            primary_etf = sector_selection["primary_etf"]

            # 2️⃣ Fetch financials
            stock_raw = fetch_stock_financials(ticker)
            sector_raw = fetch_sector_etf_metrics(primary_etf)

            # 3️⃣ Compute multiples
            stock_metrics = compute_stock_multiples(stock_raw)
            sector_metrics = compute_sector_multiples(sector_raw)

            # 4️⃣ Normalize valuation
            comparison = normalize_relative_valuation(
                stock_metrics,
                sector_metrics
            )

            # 5️⃣ LLM: explain mispricing
            explanation = explain_relative_mispricing(
                stock_metrics,
                sector_metrics,
                comparison
            )

        except Exception as e:
            st.error(f"Something went wrong: {e}")
            st.stop()

    # --- Results layout ---
    st.success("Valuation complete")

    # --- Sector selection ---
    st.subheader("🧭 Sector Classification (LLM)")
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Primary Sector ETF", primary_etf)
        if sector_selection.get("secondary_etf"):
            st.metric("Secondary Sector ETF", sector_selection["secondary_etf"])

    with col2:
        st.markdown("**Rationale**")
        st.write(sector_selection["rationale"])

    st.divider()

    # --- Valuation comparison ---
    st.subheader("📐 Valuation Comparison")

    valuation_df = pd.DataFrame(
        {
            "Stock": stock_metrics,
            "Sector ETF": sector_metrics
        }
    ).dropna(how="all")

    st.dataframe(valuation_df, use_container_width=True)

    st.divider()

    # --- Normalized signals ---
    st.subheader("⚖️ Relative Valuation Signals")

    signals_df = pd.DataFrame(
        comparison.items(),
        columns=["Metric", "Signal / Value"]
    )

    st.dataframe(signals_df, use_container_width=True)

    st.divider()

    # --- LLM explanation ---
    st.subheader("🧠 Valuation Interpretation (LLM)")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Summary**")
        st.write(explanation["valuation_summary"])

        st.markdown("**Classification**")
        st.info(explanation["classification"])

    with col2:
        st.markdown("**Key Drivers**")
        st.write(explanation["key_drivers"])

        st.markdown("**Risk Factors**")
        st.write(explanation["risk_factors"])

    # --- Optional debug section ---
    with st.expander("🔍 Debug / Raw Outputs"):
        st.markdown("**Stock Metrics**")
        st.code(pformat(stock_metrics))

        st.markdown("**Sector Metrics**")
        st.code(pformat(sector_metrics))

        st.markdown("**Normalized Comparison**")
        st.code(pformat(comparison))

        st.markdown("**LLM Explanation (Raw)**")
        st.code(pformat(explanation))
