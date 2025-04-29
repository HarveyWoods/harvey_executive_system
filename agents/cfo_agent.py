# agents/cfo_agent.py

def run():
    print("[CFO Agent] Generating financial report...")

    # Dummy data for prototype
    revenue = 25000
    expenses = 18000
    cash_on_hand = 47000

    report = f"""
    CFO Weekly Report:
    - Revenue: ${revenue}
    - Expenses: ${expenses}
    - Cash on Hand: ${cash_on_hand}

    Top 3 Financial Actionables:
    1. Review operating expenses for further savings.
    2. Accelerate outstanding receivables.
    3. Reforecast Q2 cash runway based on new leads pipeline.
    """

    print(report)
    return report
