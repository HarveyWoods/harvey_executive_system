# agents/cmo_agent.py

def run():
    print("[CMO Agent] Generating marketing report...")

    # Dummy marketing data for prototype
    website_visits = 1200
    new_leads = 45
    ad_spend = 800
    avg_cost_per_lead = round(ad_spend / new_leads, 2)

    report = f"""
    CMO Weekly Report:
    - Website Visits: {website_visits}
    - New Leads Generated: {new_leads}
    - Ad Spend: ${ad_spend}
    - Avg Cost per Lead: ${avg_cost_per_lead}

    Top 3 Marketing Actionables:
    1. Lower Cost per Lead by 10% through A/B testing ads.
    2. Launch 2 new educational blog posts.
    3. Increase retargeting of past website visitors by 15%.
    """

    print(report)
    return report
