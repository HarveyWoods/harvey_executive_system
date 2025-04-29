# run_harvey.py

from agents import cfo_agent, coo_agent, cmo_agent
from chairman import chairman_summarizer

def start_agents():
    print("🧠 Launching Harvey Executive Agents...\n")
    cfo_output = cfo_agent.run()
    coo_output = coo_agent.run()
    cmo_output = cmo_agent.run()
    return cfo_output, coo_output, cmo_output

def start_chairman(cfo_output, coo_output, cmo_output):
    print("\n🧠 Chairman Harvey is reviewing the system...\n")
    summary = chairman_summarizer.summarize(cfo_output, coo_output, cmo_output)
    return summary

if __name__ == "__main__":
    print("🚀 Starting Harvey Woods Executive System...\n")
    
    # Step 1: Run all Agents
    cfo_output, coo_output, cmo_output = start_agents()
    
    # Step 2: Chairman generates strategic directive
    chairman_summary = start_chairman(cfo_output, coo_output, cmo_output)

    print("\n✅ System Startup Complete.\n")
    print("📋 Weekly Strategic Directive:\n")
    print(chairman_summary)
