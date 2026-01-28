import yfinance as yf
from typing import Dict, Optional


SECTOR_ETFS = {
    "XLC": "Communication Services",
    "XLY": "Consumer Discretionary",
    "XLP": "Consumer Staples",
    "XLE": "Energy",
    "XLF": "Financials",
    "XLV": "Health Care",
    "XLI": "Industrials",
    "XLB": "Materials",
    "XLRE": "Real Estate",
    "XLK": "Technology",
    "XLU": "Utilities"
}


def fetch_sector_etf_metrics(etf_ticker: str) -> Dict[str, Optional[float]]:
    """
    Fetch valuation metrics for a sector ETF.

    Parameters
    ----------
    etf_ticker : str
        Sector ETF ticker (e.g., 'XLE')

    Returns
    -------
    dict
        Dictionary of sector-level valuation metrics
    """

    etf = yf.Ticker(etf_ticker)
    info = etf.info

    def safe_get(key):
        return info.get(key, None)

    data = {
        "etf_ticker": etf_ticker.upper(),
        "sector_name": SECTOR_ETFS.get(etf_ticker.upper()),

        # Market data
        "market_cap": safe_get("marketCap"),
        "enterprise_value": safe_get("enterpriseValue"),

        # Valuation multiples
        "pe_ratio": safe_get("trailingPE"),
        "forward_pe": safe_get("forwardPE"),
        "price_to_book": safe_get("priceToBook"),
        "ev_to_ebitda": safe_get("enterpriseToEbitda"),

        # Yield & income
        "dividend_yield": safe_get("dividendYield"),
        "payout_ratio": safe_get("payoutRatio"),

        # Growth (ETF-level estimates)
        "revenue_growth": safe_get("revenueGrowth"),
        "earnings_growth": safe_get("earningsGrowth")
    }

    return data


def fetch_all_sector_etfs() -> Dict[str, Dict]:
    """
    Fetch metrics for all State Street sector ETFs.

    Returns
    -------
    dict
        Dictionary keyed by ETF ticker
    """

    results = {}
    for ticker in SECTOR_ETFS:
        results[ticker] = fetch_sector_etf_metrics(ticker)

    return results


if __name__ == "__main__":
    from pprint import pprint
    pprint(fetch_sector_etf_metrics("XLE"))
