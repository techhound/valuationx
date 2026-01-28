from typing import Dict, Optional


def percent_diff(stock_value: Optional[float], sector_value: Optional[float]) -> Optional[float]:
    if stock_value is None or sector_value in (None, 0):
        return None
    return (stock_value - sector_value) / sector_value


def valuation_signal(pct_diff: Optional[float], threshold: float = 0.15) -> Optional[str]:
    """
    Interprets valuation difference.
    Negative pct_diff means cheaper than sector.
    """
    if pct_diff is None:
        return None
    if pct_diff <= -threshold:
        return "Significantly Cheaper"
    elif pct_diff >= threshold:
        return "Significantly More Expensive"
    else:
        return "In Line with Sector"


def quality_signal(stock: Optional[float], sector: Optional[float]) -> Optional[str]:
    if stock is None or sector is None:
        return None
    if stock > sector:
        return "Above Sector"
    elif stock < sector:
        return "Below Sector"
    return "In Line with Sector"


def normalize_relative_valuation(
    stock_metrics: Dict,
    sector_metrics: Dict
) -> Dict:
    """
    Compare stock metrics to sector ETF metrics and normalize results.
    """

    results = {
        "ticker": stock_metrics.get("ticker"),
        "sector_etf": sector_metrics.get("etf_ticker"),
        "sector_name": sector_metrics.get("sector_name"),

        # Valuation comparisons
        "pe_diff_pct": percent_diff(
            stock_metrics.get("pe_ratio"),
            sector_metrics.get("pe_ratio")
        ),
        "pe_signal": valuation_signal(
            percent_diff(
                stock_metrics.get("pe_ratio"),
                sector_metrics.get("pe_ratio")
            )
        ),

        "ev_ebitda_diff_pct": percent_diff(
            stock_metrics.get("ev_to_ebitda"),
            sector_metrics.get("ev_to_ebitda")
        ),
        "ev_ebitda_signal": valuation_signal(
            percent_diff(
                stock_metrics.get("ev_to_ebitda"),
                sector_metrics.get("ev_to_ebitda")
            )
        ),

        # Yield comparisons
        "fcf_yield_vs_sector": quality_signal(
            stock_metrics.get("fcf_yield"),
            sector_metrics.get("earnings_yield")
        ),

        "dividend_yield_vs_sector": quality_signal(
            stock_metrics.get("dividend_yield"),
            sector_metrics.get("dividend_yield")
        ),

        # Growth comparisons
        "revenue_growth_vs_sector": quality_signal(
            stock_metrics.get("revenue_growth"),
            sector_metrics.get("revenue_growth")
        ),

        "earnings_growth_vs_sector": quality_signal(
            stock_metrics.get("earnings_growth"),
            sector_metrics.get("earnings_growth")
        ),

        # Quality
        "operating_margin_vs_sector": quality_signal(
            stock_metrics.get("operating_margin"),
            None  # sector margins are unreliable at ETF level
        ),
    }

    return results
