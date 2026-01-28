# ValuationX

ValuationX is a Python-based valuation support system that benchmarks individual equities against State Street Select Sector SPDR ETFs.

## Purpose
This project is designed to provide **context-aware valuation analysis**, not investment recommendations, by comparing company-level multiples to sector benchmarks and explaining relative differences.

## Key Features
- Sector benchmarking using State Street SPDR ETFs
- LLM-assisted sector classification
- Relative valuation multiple analysis
- Narrative explanation of valuation differences

## Disclaimer
This project is for educational and analytical purposes only and does not constitute investment advice.

# ValuationX

ValuationX is a Python-based **equity valuation support system** that benchmarks individual stocks against **State Street Select Sector SPDR ETFs** to provide context-aware relative valuation analysis.

The system is designed to help analysts reason about valuation differences — **not** to generate investment recommendations or price targets.

---

## Purpose & Philosophy

ValuationX is built around a simple idea:

> *Before performing a full valuation (DCF, comparables, etc.), analysts often sanity-check a company against its industry benchmark.*

ValuationX formalizes that process by:
- Mapping a company to an appropriate sector ETF
- Comparing valuation multiples against sector norms
- Explaining *why* a stock may appear over- or under-valued

The emphasis is on **interpretability, judgment, and transparency**, not prediction.

---

## Key Features

- **Sector Benchmarking**  
  Uses State Street Select Sector SPDR ETFs as industry proxies.

- **LLM-Assisted Sector Classification**  
  Maps companies to sector ETFs based on business model and revenue drivers.

- **Relative Valuation Analysis**  
  Compares company-level valuation multiples to sector benchmarks.

- **Narrative Explanations**  
  Generates plain-English explanations for valuation differences.

- **Modular Architecture**  
  Designed to support future integrations (e.g., Power BI, Streamlit).

---

## Project Structure

ValuationX/
│── src/
│   ├── data/
│   │   ├── fetch_financials.py        # Retrieves company financial data
│   │   └── fetch_sector_etfs.py       # Retrieves sector ETF benchmark data
│   │
│   ├── analytics/
│   │   ├── compute_multiples.py       # Calculates valuation multiples
│   │   └── normalize.py               # Normalizes metrics for comparison
│   │
│   └── llm/
│       ├── sector_selector.py         # LLM-assisted sector classification
│       └── mispricing_explainer.py    # Generates valuation explanations
│
│── notebooks/                         # Optional exploratory analysis
│── README.md
│── requirements.txt



---

## Prerequisites

- **Python 3.10+**
- Git
- An OpenAI API key (for sector classification and narrative explanations)

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/techhound/valuationx.git
cd valuationx

python -m venv .venv
source .venv/bin/activate      # macOS/Linux
.venv\Scripts\activate         # Windows


### Install dependencies
pip install -r requirements.txt


Configuration

ValuationX uses environment variables for API credentials.

OpenAI API Key

Set your OpenAI API key as an environment variable:

Windows (PowerShell):
setx OPENAI_API_KEY "your_api_key_here"

macOS/Linux:
export OPENAI_API_KEY="your_api_key_here"

⚠️ Do not hardcode API keys into source files.

# Basic Usage (Conceptual Flow)

A typical ValuationX workflow looks like this:

Select a company

Provide ticker and optional business description

Determine sector benchmark

sector_selector.py maps the company to a State Street sector ETF

Retrieve financial data

Company fundamentals

Sector ETF benchmark metrics

Compute valuation multiples

P/E, EV/EBITDA, etc. (depending on implementation)

Compare and normalize

Normalize company metrics against sector benchmarks

Generate explanation

mispricing_explainer.py produces a narrative explanation of differences

from llm.sector_selector import select_sector_etf
from analytics.compute_multiples import compute_multiples
from llm.mispricing_explainer import explain_valuation

sector = select_sector_etf(
    ticker="XOM",
    company_name="Exxon Mobil",
    business_description="Integrated oil and gas company"
)

multiples = compute_multiples("XOM", sector)

explanation = explain_valuation("XOM", sector, multiples)

print(explanation)
