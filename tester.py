from data import fetch_financials
from data import fetch_sector_etfs
from analytics.compute_multiples import compute_stock_multiples, compute_sector_multiples
from analytics.normalize import normalize_relative_valuation
from pprint import pprint

stock = fetch_financials.fetch_stock_financials("XOM")
sector = fetch_sector_etfs.fetch_sector_etf_metrics("XLE")

stock_metrics = compute_stock_multiples(stock)
sector_metrics = compute_sector_multiples(sector)

comparison = normalize_relative_valuation(stock_metrics, sector_metrics)

pprint(comparison)
