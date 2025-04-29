# chairman/chairman_summarizer.py

def summarize(cfo_text, coo_text, cmo_text):
    directive = f"""
    Chairman's Weekly Strategic Directive

    Summary of CFO Report:
    {cfo_text}

    Summary of COO Report:
    {coo_text}

    Summary of CMO Report:
    {cmo_text}

    Strategic Focus:
    1. Align financial planning with operational execution.
    2. Improve project velocity and on-time performance.
    3. Optimize marketing efficiency to lower lead costs.
    """

    return directive
