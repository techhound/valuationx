from typing import Dict
from urllib import response
from openai import OpenAI
import json

client = OpenAI()


SYSTEM_PROMPT = """
You are a financial analyst assistant.

Your role is to interpret relative valuation differences between
a stock and its sector ETF.

Rules:
- Use ONLY the metrics provided.
- Do NOT invent financial data.
- Do NOT provide investment advice.
- Explain potential drivers of valuation differences.
- Highlight risks and justifications.
- Output MUST be valid JSON.
"""


def explain_relative_mispricing(
    stock_metrics: Dict,
    sector_metrics: Dict,
    normalized_comparison: Dict
) -> Dict:
    """
    Use an LLM to explain valuation differences vs sector.
    """

    user_prompt = f"""
Stock Metrics:
{json.dumps(stock_metrics, indent=2)}

Sector ETF Metrics:
{json.dumps(sector_metrics, indent=2)}

Relative Comparison:
{json.dumps(normalized_comparison, indent=2)}

Tasks:
1. Explain why the stock trades at a premium or discount vs the sector.
2. Assess whether the valuation difference appears justified.
3. Identify potential risks or structural factors.
4. Classify the situation as one of:
   - "Potential Undervaluation"
   - "Potential Overvaluation"
   - "Likely Justified Valuation"
   - "Inconclusive"

Respond in JSON with:
- valuation_summary
- key_drivers
- risk_factors
- classification
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.3,
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

    # Dummy test inputs
    pprint(
        explain_relative_mispricing(
            stock_metrics={"pe_ratio": 10, "fcf_yield": 0.12},
            sector_metrics={"pe_ratio": 14, "earnings_yield": 0.07},
            normalized_comparison={"pe_signal": "Significantly Cheaper"}
        )
    )
