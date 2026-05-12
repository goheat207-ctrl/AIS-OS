# Fincept Tools — Extracted from FinceptTerminal

Source: https://github.com/Fincept-Corporation/FinceptTerminal (20k+ stars)
Extracted: 2026-05-11
License: See original repo (commercial license applies to full terminal)

Selected modules extracted for Blaine's trading OS. Only HIGH and MED value files copied.

---

## What's Here

### `data/sec_data.py` — SEC EDGAR Integration
Pull any SEC filing, insider trades, institutional ownership, company facts.

**Key functions:**
- `get_company_filings(ticker, form_type)` — get 8-K, 10-K, 10-Q, Form 4 etc.
- `get_insider_trading(ticker)` — Form 4 insider buy/sell transactions
- `get_institutional_ownership(ticker)` — 13F institutional holdings
- `get_company_facts(ticker)` — XBRL financial metrics (revenue, EPS, etc.)

**Use case:** Pre-trade catalyst research. Called by the `small-cap-catalyst` agent.

---

### `data/yfinance_data.py` — Free Market Data
Real-time quotes, historical OHLCV, fundamentals, batch ops. No API key needed.

**Key functions:**
- `get_quote(symbol)` — real-time price, volume, change
- `get_historical(symbol, interval, period)` — OHLCV data (intraday to monthly)
- `get_batch_quotes(symbols_list)` — multi-ticker quote fetch
- `get_info(symbol)` — PE, float, insider%, institutional%, 52-week range
- `get_news(symbol)` — latest news headlines

**Use case:** Feed historical data to the backtester. Pull float/ownership data.

---

### `technicals/compute_technicals.py` — 40+ Technical Indicators
Computes trend, momentum, volatility, and volume indicators from OHLCV data.

**Key functions:**
- `calculate_all_momentum_indicators(df)` — RSI, Stochastic, MACD, Williams %R, AO
- `calculate_all_volatility_indicators(df)` — ATR, Bollinger Bands, Keltner, Donchian
- `calculate_all_volume_indicators(df)` — VWAP, OBV, CMF, MFI, EOM
- `calculate_all_trend_indicators(df)` — SMA, EMA, ADX, Aroon, Ichimoku

**Use case:** Compute indicators for TOS backtester strategies. Feed signals into scanner.

---

### `analytics/quantstats_analysis.py` — Performance Metrics
Sharpe, Sortino, Calmar, max drawdown, win rate, profit factor from price series.

**Use case:** Backtest evaluation. Post-trade analysis supplement to the journal API.

---

### `edgar/` — EDGAR MCP Tool Suite
CLI-callable modules for structured EDGAR data extraction.

| File | What it pulls |
|------|---------------|
| `forms_8k.py` | 8-K material events, categorized |
| `forms_insider.py` | Form 4 insider transactions |
| `forms_13f.py` | 13F institutional holdings |
| `forms_10k.py` | 10-K annual report sections |
| `forms_10q.py` | 10-Q quarterly report sections |
| `financials.py` | XBRL financial data |
| `base.py` | Shared SEC API helpers |
| `main.py` | CLI entry point |

**Use case:** Run `python edgar/main.py 8k_events_categorized TICKER` for instant 8-K triage.

---

### `backtesting/` — Backtesting Framework
Base provider + backtestingpy integration for strategy simulation.

| File | Role |
|------|------|
| `base_provider.py` | Abstract base for all backtest providers |
| `advanced_metrics.py` | Sharpe, Sortino, Calmar, drawdown, equity curve |
| `fincept_strategy_runner.py` | Strategy execution engine |
| `backtestingpy_provider.py` | Bridge to `backtesting.py` library |
| `btp_strategies.py` | Pre-built strategies (SMA crossover, RSI, MACD) |
| `btp_indicators.py` | Indicator helpers for backtestingpy |
| `btp_optimize.py` | Parameter optimization |
| `btp_signals.py` | Signal generation |
| `btp_data.py` | Data fetching for backtestingpy |

**Use case:** Foundation for the TOS strategy backtester (Q2 goal).

---

## Quick Start

```bash
# Pull latest 8-K filings for a ticker
python edgar/main.py 8k_events_categorized AEYE

# Get insider transactions
python edgar/main.py insider_transactions AEYE

# Get real-time quote
python -c "from data.yfinance_data import get_quote; print(get_quote('AEYE'))"

# Compute technicals on historical data
python -c "from data.yfinance_data import get_historical; from technicals.compute_technicals import calculate_all_momentum_indicators; ..."
```

## Dependencies

```
pip install yfinance sec-api pandas numpy quantstats backtesting
```

---

## What Was NOT Copied

- 200+ global macro data scripts (OECD, World Bank, UNESCO, etc.) — not relevant
- C++/Qt terminal source (different tech stack)
- Crypto, derivatives, fixed income modules
- agno_trading_service.py (multi-LLM competition framework — needs heavy customization)
- economic_calendar.py (requires Selenium/Chrome — heavy dependency)
