# 🤖 Multi-Agent System with Groq and Phi

This project implements a multi-agent system using **Phi** and **Groq’s LLaMA-3 model** to search web content and retrieve financial data dynamically. The agents collaborate to provide structured, source-backed responses with AI-driven insights.

---

## ✨ Features
- 🌐 **Web Search Agent**: Fetches information from the web using DuckDuckGo.  
- 📊 **Finance Agent**: Retrieves real-time financial data (stock prices, analyst recommendations, company info, and news) using YFinance.  
- 🤝 **Team Collaboration**: Combines the two agents to deliver comprehensive, source-rich responses.  
- 📑 Outputs responses in **Markdown with tables** for readability.  
- 🛠️ **Debug Mode**: Enabled for detailed tool call tracking.  

---

## 🧑‍💻 How It Works

1. **Web Search Agent**  
   - Uses **DuckDuckGo** for retrieving general web content.  
   - Adds source URLs to responses.  

2. **Finance Agent**  
   - Uses **YFinanceTools** to get financial data like:  
     - Current stock prices  
     - Analyst recommendations  
     - Company profiles  
     - Latest company news  

3. **Agent Team**  
   - Orchestrates both agents for collaborative tasks.
   - Example: Summarizes analyst recommendations for **NVDA** using structured tables.

---

## 📚 Libraries Used

| Library                         | Purpose                                                                                  |
|----------------------------------|------------------------------------------------------------------------------------------|
| `phi.agent.Agent`               | Defines and manages AI agents.                                                           |
| `phi.model.groq.Groq`           | Connects to Groq’s LLaMA-3 model for processing tasks.                                    |
| `phi.tools.duckduckgo.DuckDuckGo` | Enables web search capabilities.                                                         |
| `phi.tools.yfinance.YFinanceTools` | Fetches financial market data and news.                                                 |
| `dotenv.load_dotenv`            | Loads API keys and environment variables from a `.env` file securely.                    |

