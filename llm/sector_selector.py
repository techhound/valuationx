from typing import Dict
from openai import OpenAI
import json

client = OpenAI()

SYSTEM_PROMPT = """
You are a financial classification assistant.

Your task is to map a public company to the most appropriate
State Street Select Sector SPDR ETF.

Rules:
- Use ONLY the provided list of ETFs.
- Choose ONE primary ETF.
- Optionally choose ONE secondary ETF if justified.
- Do NOT invent financial data.
- Provide a concise rationale grounded in business model and revenue drivers.
- Output MUST be valid JSON.
"""

ETF_LIST = {
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


def select_sector_etf(
    ticker: str,
    company_name: str,
    business_description: str = ""
) -> Dict:
    """
    Use an LLM to determine the most appropriate sector ETF.
    """

    user_prompt = f"""
Company Ticker: {ticker}
Company Name: {company_name}

Business Description:
{business_description}

Available Sector ETFs:
{json.dumps(ETF_LIST, indent=2)}

Respond in JSON with:
- primary_etf
- secondary_etf (or null)
- rationale
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.2,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ]
    )

    raw = response.choices[0].message.content

    if not raw:
        raise ValueError("LLM returned empty response")

    return json.loads(raw)

#    return json.loads(response.choices[0].message.content)


if __name__ == "__main__":
    from pprint import pprint

    pprint(
        select_sector_etf(
            ticker="XOM",
            company_name="Exxon Mobil Corporation",
            business_description="Integrated oil and gas company with upstream, downstream, and chemicals operations."
        )
    )
