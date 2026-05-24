# ACC102 Group: White Liquor Industry DCF Valuation Agent

## 1. Project Background

This project develops an AI‑assisted equity research agent for the Chinese White Liquor (Baijiu) industry, as part of the ACC102 coursework at XJTLU. The agent generates industry analysis, company analysis, DuPont financial ratios, and a three‑stage Discounted Cash Flow (DCF) valuation.

**Target Company**: Kweichow Moutai (600519.SH)  
**Peer Companies**: Wuliangye (000858.SZ), Shanxi Xingjiacun Fenjiu (600809.SH)  
**Valuation Base Date**: 31 December 2024

---

## 2. Repository Structure

The repository contains the following folders and files:

- `README.md` – this file
- `docs/` – industry and company analysis reports, presentation slides, figures
- `notebook/` – Python DCF model (Jupyter Notebook .ipynb)
- `data/` – financial data (Excel/CSV files)
- `excel/` – Excel DCF model (.xlsx)

---

## 3. DCF Model Description

We use a three-stage Free Cash Flow to Firm (FCFF) model, following the methodology taught in ACC102 Week 10-11.

| Stage | Years | Description |
|-------|-------|-------------|
| Stage 1 | 2025-2029 | Explicit forecast period – each year's FCFF is projected separately |
| Stage 2 | 2030-2039 | Fade period with a constant growth rate |
| Stage 3 | 2040 onward | Perpetual growth (Gordon Growth model) |

All inputs are derived from historical financial statements (2021-2024).

---

## 4. Key Valuation Assumptions

The following assumptions are used in the DCF model. These numbers are provided by the team member responsible for financial analysis and DCF valuation.

| Assumption | Value | Source / Justification |
|------------|-------|------------------------|
| Risk‑free rate (Rf) | 1.7% | Long‑term government bond yield |
| Equity risk premium | 6.3% | CSI 300 historical average |
| Beta (β) | 1.05 | 5‑year monthly regression vs CSI 300 |
| Cost of equity (Re) | 8.3% | CAPM: Rf + β × ERP |
| Cost of debt (Rd) | 2.66% | 5‑year average interest expense / total debt |
| Tax rate (Tc) | 25% | Statutory corporate income tax |
| WACC | 8.5% | Weighted average of Re and after‑tax Rd |
| Stage 1 revenue growth (2025-2029) | 8% per year | Conservative estimate based on historical average (~14%) adjusted for market maturity |
| NOPAT margin | 52.3% | Based on 2024 actual performance |
| Depreciation & Amortization rate | 7% | Historical average |
| CapEx / Revenue | 2.5% | Mature company with low reinvestment needs |
| Stage 2 growth (2030-2039) | 4% | Between Stage 1 exit and terminal growth |
| Terminal growth (g) | 2.5% | Aligned with China's long-term GDP growth |

---

## 5. How to Run the Code

### Prerequisites
- Python 3.9 or higher
- Jupyter Notebook (or VS Code with Python extension)
- WRDS account (optional – if using provided CSV file, no WRDS needed)

### Install Dependencies
Open a terminal (or Anaconda Prompt) and run:

    pip install pandas numpy matplotlib openpyxl

### Run the Jupyter Notebook
1. Navigate to the `notebook/` folder.
2. Launch Jupyter Notebook:

    jupyter notebook moutai_dcf_valuation.ipynb

3. Run all cells in order (Kernel → Restart & Run All).

The notebook will load historical data, calculate ratios, project FCFF, and output valuation results.

---

## 6. Valuation Results (Kweichow Moutai)

| Metric | Value |
|--------|-------|
| Enterprise Value (RMB million) | 1,896,061 |
| Equity Value (RMB million) | 1,955,357 |
| Shares Outstanding (million) | 1,256 |
| **DCF Intrinsic Value per Share (RMB)** | **1,557** |
| Current Market Price (RMB) | *User input required* |
| Implied Upside/Downside | *Depends on current market price* |

### Sensitivity Analysis (Value per Share in RMB)

| Revenue Growth Rate (Forecast) \ WACC | 7.5% | 8.5% | 9.5% |
|--------------------------------------|------|------|------|
| 7% | 1,812 | 1,475 | 1,232 |
| 8% | 1,958 | 1,557 | 1,301 |
| 9% | 2,115 | 1,648 | 1,378 |

The valuation is most sensitive to changes in WACC and long‑term growth assumptions.

---

## 7. Dependencies and Requirements

The Python environment requires the following packages (tested versions):

| Package | Version | Purpose |
|---------|---------|---------|
| pandas | ≥1.5.0 | Data manipulation |
| numpy | ≥1.23.0 | Numerical calculations |
| matplotlib | ≥3.6.0 | Charts and sensitivity graphs |
| openpyxl | ≥3.1.0 | Excel file export (optional) |

To install all at once, create a `requirements.txt` file with:

    pandas>=1.5.0
    numpy>=1.23.0
    matplotlib>=3.6.0
    openpyxl>=3.1.0

Then run `pip install -r requirements.txt`.

---

## 8. Limitations

- The DCF model relies on forward‑looking assumptions (growth, margins, WACC) that may not materialize.
- No probabilistic analysis (e.g., Monte Carlo simulation) is performed.
- Qualitative factors (management changes, new regulations, brand reputation) are not captured.
- Beta is estimated from historical data and may not reflect future volatility.
- The tool is designed **only for Chinese white liquor companies listed on A‑share markets**.

---

## 9. AI Disclosure

As required by ACC102 coursework policy, we disclose the use of AI tools:

| Tool | Version | Purpose |
|------|---------|---------|
| ChatGPT | GPT‑4 | README structure, code comments, dependency list |
| GitHub Copilot | latest | Assistance in Python code (Jupyter notebook) |
| Coze (XIPU AI) | built‑in | Agent prompts for industry/company analysis |

All AI‑generated content has been reviewed, verified, and adjusted by team members.

---

## 10. References

- ACC102 Lecture Slides (Week 8 – Industry analysis, Week 9 – Financial analysis, Week 10 – DCF valuation, Week 11 – Chatflow)
- CSMAR database accessed via WRDS
- Guizhou Moutai annual reports (2021-2024)
- Wuliangye and Shanxi Fenjiu annual reports (for peer comparison)
- GitHub documentation: https://docs.github.com/
