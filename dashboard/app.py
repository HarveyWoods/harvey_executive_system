# dashboard/app.py

from flask import Flask, render_template_string
from agents import cfo_agent, coo_agent, cmo_agent
from chairman import chairman_summarizer

app = Flask(__name__)

@app.route("/")
def home():
    # Run all agents
    cfo_output = cfo_agent.run()
    coo_output = coo_agent.run()
    cmo_output = cmo_agent.run()
    
    # Chairman Summary
    chairman_output = chairman_summarizer.summarize(cfo_output, coo_output, cmo_output)

    # Render the page
    html = f"""
    <h1>Harvey Executive Dashboard</h1>

    <h2>CFO Report</h2>
    <pre>{cfo_output}</pre>

    <h2>COO Report</h2>
    <pre>{coo_output}</pre>

    <h2>CMO Report</h2>
    <pre>{cmo_output}</pre>

    <h2>Chairman's Strategic Directive</h2>
    <pre>{chairman_output}</pre>
    """

    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
