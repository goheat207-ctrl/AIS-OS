"""
run_trading_agents.py — run the TradingAgents full analysis for a ticker.

Usage:
    python scripts/run_trading_agents.py AAPL 2026-01-15
    python scripts/run_trading_agents.py AAPL              # defaults to today

Requires:
    cd d:\AIS-OS\TradingAgents && pip install .
    ANTHROPIC_API_KEY must be set in the environment.
"""

import sys
import os
from datetime import date

# Ensure TradingAgents package is importable
TRADING_AGENTS_DIR = os.path.join(os.path.dirname(__file__), "..", "TradingAgents")
sys.path.insert(0, TRADING_AGENTS_DIR)

from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

def run(ticker: str, analysis_date: str) -> None:
    config = DEFAULT_CONFIG.copy()
    config["llm_provider"] = "anthropic"
    config["deep_think_llm"] = "claude-sonnet-4-6"
    config["quick_think_llm"] = "claude-haiku-4-5-20251001"
    config["max_debate_rounds"] = 1
    config["max_risk_discuss_rounds"] = 1

    print(f"\n=== TradingAgents Analysis: {ticker} | {analysis_date} ===\n")

    ta = TradingAgentsGraph(debug=True, config=config)
    _, decision = ta.propagate(ticker, analysis_date)

    print("\n=== FINAL DECISION ===\n")
    print(decision)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_trading_agents.py TICKER [YYYY-MM-DD]")
        sys.exit(1)

    ticker = sys.argv[1].upper()
    analysis_date = sys.argv[2] if len(sys.argv) > 2 else date.today().isoformat()

    run(ticker, analysis_date)
