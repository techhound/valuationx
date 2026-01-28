# ValuationX

ValuationX is a Python-based **equity valuation support system** that benchmarks individual stocks against **State Street Select Sector SPDR ETFs** to provide context-aware relative valuation analysis.

The system is designed to support analytical reasoning and valuation sanity-checks — **not** to generate investment recommendations or price targets.

---

## Purpose & Philosophy

ValuationX formalizes a common analyst workflow:

> *Before building a full valuation model (DCF, detailed comps, etc.), analysts often benchmark a company against its sector to understand whether its valuation looks unusual — and why.*

ValuationX supports that process by:
- Mapping a company to an appropriate sector ETF
- Comparing valuation multiples against sector benchmarks
- Explaining potential drivers of relative over- or under-valuation

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
  Produces plain-English explanations for valuation differences.

- **Layered, Modular Architecture**  
  Organized into data ingestion, analytics, and LLM-assisted reasoning layers.

---

## Project Structure

ValuationX/
│── src/
│ ├── data/
│ │ ├── fetch_financials.py # Retrieves company financial data
│ │ └── fetch_sector_etfs.py # Retrieves sector ETF benchmark data
│ │
│ ├── analytics/
│ │ ├── compute_multiples.py # Calculates valuation multiples
│ │ └── normalize.py # Normalizes metrics for comparison
│ │
│ └── llm/
│ ├── sector_selector.py # LLM-assisted sector classification
│ └── mispricing_explainer.py # Generates valuation explanations
│
│── notebooks/ # Optional exploratory analysis
│── README.md
│── requirements.txt


---

## Prerequisites

- **Python 3.10+**
- Git
- An OpenAI API key (used for sector classification and narrative explanations)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/valuationx.git
cd valuationx
2. Create and activate a virtual environment
Windows

python -m venv .venv
.venv\Scripts\activate
macOS / Linux

python -m venv .venv
source .venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
Configuration
ValuationX uses environment variables for API credentials.

OpenAI API Key
Set your OpenAI API key as an environment variable.

Windows (PowerShell)

setx OPENAI_API_KEY "your_api_key_here"
macOS / Linux

export OPENAI_API_KEY="your_api_key_here"
⚠️ Do not hardcode API keys into source files.

Basic Usage (Conceptual Workflow)
A typical ValuationX workflow follows these steps:

Select a company (ticker and optional business description)

Determine the appropriate sector benchmark

Retrieve company and sector financial data

Compute valuation multiples

Normalize metrics for comparison

Generate a narrative explanation of valuation differences

Example (High-Level)
from src.llm.sector_selector import select_sector_etf
from src.analytics.compute_multiples import compute_multiples
from src.llm.mispricing_explainer import explain_valuation

sector = select_sector_etf(
    ticker="XOM",
    company_name="Exxon Mobil",
    business_description="Integrated oil and gas company"
)

multiples = compute_multiples("XOM", sector)

explanation = explain_valuation("XOM", sector, multiples)

print(explanation)
Design Principles
Explainability over automation

Bounded and transparent use of LLMs

Clear separation of data, analytics, and narrative layers

No black-box predictions or trading signals

Limitations
ValuationX does not replace a full valuation model (e.g., DCF).

Sector ETFs are imperfect proxies for individual companies.

Results depend on data quality and benchmark selection.

These limitations are intentional and explicit.

Disclaimer
This project is for educational and analytical purposes only and does not constitute financial, investment, or trading advice.

Future Enhancements
Power BI integration for interactive benchmarking

Streamlit or web-based interface

Expanded factor-based benchmarking

Greater sector and industry granularity

