import yfinance as yf
from typing import Dict, Optional


def fetch_stock_financials(ticker: str) -> Dict[str, Optional[float]]:
    """
    Fetch core valuation and profitability metrics for a single stock.

    Parameters
    ----------
    ticker : str
        Stock ticker symbol (e.g., 'XOM')

    Returns
    -------
    dict
        Dictionary of financial metrics suitable for valuation comparison
    """

    stock = yf.Ticker(ticker)
    info = stock.info

    def safe_get(key):
        return info.get(key, None)

    data = {
        "ticker": ticker.upper(),

        # Market data
        "market_cap": safe_get("marketCap"),
        "enterprise_value": safe_get("enterpriseValue"),
        "shares_outstanding": safe_get("sharesOutstanding"),

        # Valuation multiples
        "pe_ratio": safe_get("trailingPE"),
        "forward_pe": safe_get("forwardPE"),
        "price_to_book": safe_get("priceToBook"),
        "ev_to_ebitda": safe_get("enterpriseToEbitda"),

        # Profitability
        "profit_margin": safe_get("profitMargins"),
        "operating_margin": safe_get("operatingMargins"),
        "return_on_equity": safe_get("returnOnEquity"),
        "return_on_assets": safe_get("returnOnAssets"),

        # Growth
        "revenue_growth": safe_get("revenueGrowth"),
        "earnings_growth": safe_get("earningsGrowth"),

        # Cash flow
        "free_cash_flow": safe_get("freeCashflow"),
        "operating_cash_flow": safe_get("operatingCashflow"),

        # Dividend
        "dividend_yield": safe_get("dividendYield"),
        "payout_ratio": safe_get("payoutRatio"),

        # Metadata
        "sector": safe_get("sector"),
        "industry": safe_get("industry")
    }

    return data


# if __name__ == "__main__":
#     # Quick smoke test
#     from pprint import pprint
#     pprint(fetch_stock_financials("XOM"))
