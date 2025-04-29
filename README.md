# Harvey Executive System 🧠⚡

The **Harvey Executive System** is an open-source, AI-powered business operating system designed to simulate the critical thinking and weekly strategic reporting of a high-functioning executive team.

Built by [Gregory J. Dubela](https://www.harveywoods.io), founder of Harvey Woods — this project bridges artificial intelligence, operational systems, and solar infrastructure into one modular executive assistant framework.

---

## 🚀 What It Does

- 🧠 **Agent Architecture**  
  Modular agents simulate the roles of:
  - **CFO**: Financial insights and actionables  
  - **COO**: Project health, operations, and maintenance  
  - **CMO**: Lead generation, content, and marketing strategy  
  - *(Future additions: CTO, CLO, CSSO, etc.)*

- 📊 **Chairman Harvey**  
  A central summarizer that synthesizes agent reports into a **Weekly Strategic Directive** — the AI equivalent of a shareholder meeting output.

- 💻 **Local Dashboard Interface**  
  Flask-based executive web dashboard served locally. View reports, track strategy, and manage insights securely and privately.

- ⚙️ **One-Click Startup**  
  Fully scriptable environment via `start_harvey.sh`, powered by `venv`, Flask, and modular Python architecture.

---

## 📁 Project Structure

```
harvey_executive_system/
├── agents/ # Modular AI agents (CFO, COO, CMO, etc.)
├── chairman/ # Chairman Harvey: synthesizes cross-agent insights
├── dashboard/ # Flask dashboard for live reporting
├── data_feeds/ # (Future) Real data integrations (Salesforce, QuickBooks)
├── reports/ # Weekly generated reports (MD or audio)
├── run_harvey.py # Main system launcher
├── start_harvey.sh # One-click startup script
├── requirements.txt # Python dependencies
├── .gitignore # Local environment and key protection

---

## 🛠️ Setup Instructions

1. **Clone the Repo**

```bash
git clone https://github.com/HarveyWoods/harvey_executive_system.git
cd harvey_executive_system
