from typing import Dict, Optional


def safe_divide(numerator: Optional[float], denominator: Optional[float]) -> Optional[float]:
    if numerator is None or denominator in (None, 0):
        return None
    return numerator / denominator


def compute_stock_multiples(stock: Dict) -> Dict:
    """
    Compute derived valuation metrics for a stock.
    """

    return {
        "ticker": stock.get("ticker"),

        # Valuation
        "pe_ratio": stock.get("pe_ratio"),
        "forward_pe": stock.get("forward_pe"),
        "price_to_book": stock.get("price_to_book"),
        "ev_to_ebitda": stock.get("ev_to_ebitda"),

        # Yield-style metrics
        "fcf_yield": safe_divide(
            stock.get("free_cash_flow"),
            stock.get("market_cap")
        ),
        "earnings_yield": safe_divide(
            1,
            stock.get("pe_ratio")
        ),

        # Profitability
        "return_on_equity": stock.get("return_on_equity"),
        "operating_margin": stock.get("operating_margin"),

        # Growth
        "revenue_growth": stock.get("revenue_growth"),
        "earnings_growth": stock.get("earnings_growth"),

        # Dividend
        "dividend_yield": stock.get("dividend_yield"),
        "payout_ratio": stock.get("payout_ratio"),
    }


def compute_sector_multiples(sector: Dict) -> Dict:
    """
    Compute derived valuation metrics for a sector ETF.
    """

    return {
        "etf_ticker": sector.get("etf_ticker"),
        "sector_name": sector.get("sector_name"),

        # Valuation
        "pe_ratio": sector.get("pe_ratio"),
        "forward_pe": sector.get("forward_pe"),
        "price_to_book": sector.get("price_to_book"),
        "ev_to_ebitda": sector.get("ev_to_ebitda"),

        # Yield-style metrics
        "earnings_yield": safe_divide(
            1,
            sector.get("pe_ratio")
        ),

        # Growth
        "revenue_growth": sector.get("revenue_growth"),
        "earnings_growth": sector.get("earnings_growth"),

        # Dividend
        "dividend_yield": sector.get("dividend_yield"),
        "payout_ratio": sector.get("payout_ratio"),
    }
