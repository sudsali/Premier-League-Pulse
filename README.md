# Premier League Pulse: Big Six Insights

## Overview
Premier League Pulse is an AI-powered newsletter generator that provides real-time updates and news summaries for the Premier League's Big Six clubs: Arsenal, Chelsea, Liverpool, Manchester City, Manchester United, and Tottenham Hotspur. This project uses LLMs (Llama Model) and APIs to deliver concise and engaging football insights tailored for fans and analysts.

## Features
- **Real-Time Data Integration**:
  Fetches live standings, recent form, and performance metrics of the Big Six clubs using the Football-Data.org API.
  
- **News Summaries**:
  Scrapes transfer-related and general football news articles using SerpAPI and summarizes them using the Llama Model.

- **Newsletter Refinement**:
  Edits the generated newsletter to ensure clean, concise content.

## Installation

### Prerequisites
API keys for:
   - [Football-Data.org](https://www.football-data.org/)
   - [SerpAPI](https://serpapi.com/)
   - [Together AI](https://together.xyz/)

### Steps
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/premier-league-pulse.git
   cd premier-league-pulse
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory with the following keys:
   ```
   FOOTBALL_DATA_API_KEY=your_football_data_api_key_here
   SERPAPI_KEY=your_serpapi_key_here
   TOGETHER_API_KEY=your_together_ai_key_here
   ```

## Usage

Run the main script to generate the newsletter:
```
python main.py
```

The newsletter will be printed in the console.

---

## Project Structure

```
.
├── agents.py          # Contains agents for fetching data and generating summaries.
├── tasks.py           # Handles newsletter generation tasks.
├── tools.py           # Utility functions for club updates.
├── main.py            # Entry point of the application.
├── requirements.txt   # List of dependencies.
├── .env               # Environment variables (API keys).
```

---

## Demo Output
```
Gathering latest updates on the Big Six clubs...

**Today's (2025-03-16 13:35:35) Premier League Update: The Big Six Clubs**

Hello Football Fans,

Here are the latest updates from the Premier League's Big Six clubs:

**Arsenal**
Current Position: 2  
Points: 58  
Goal Difference: 29  
Recent Form: D,W,D,D,W  

Arsenal secured a crucial 1-0 win over Chelsea in their Premier League clash, with the victory highlighting the team's growing momentum under Mikel Arteta. The manager has outlined plans for Bukayo Saka's return and emphasized the importance of careful management. Transfer news continues to swirl around the Emirates, with updates on potential targets and contract discussions with key players.

**Chelsea**
Current Position: 4  
Points: 49  
Goal Difference: 16  
Recent Form: L,L,W,W,L  

Chelsea suffered a narrow 1-0 defeat to Arsenal in their recent Premier League clash. Enzo Fernandez expressed unhappiness towards Arsenal's Gabriel, accusing him of unsportsmanlike behavior. The Blues are already looking ahead to the summer transfer window, with reports suggesting that they plan to offload 7-8 players in a bid to revamp their squad.

**Liverpool**
Current Position: 1  
Points: 70  
Goal Difference: 42  
Recent Form: W,W,W,W,L  

Liverpool are eyeing a summer move for Julian Alvarez, with the player's agent confirming the Reds' interest in the River Plate forward. The club is preparing for the Carabao Cup final against Newcastle. Barcelona are reportedly interested in signing Liverpool's Luis Diaz, but the Reds are unlikely to let him go.

**Manchester City**
Current Position: 5  
Points: 48  
Goal Difference: 15  
Recent Form: L,L,W,L,D  

Manchester City is undergoing significant changes following the dismissal of Gareth Taylor. Adrien Rabiot's tearful departure to PSG has left fans stunned, with the player citing "just business" as the reason. The EDS team suffered a narrow defeat to Crystal Palace in a PL2 clash, with Bobb making a return to action. Nick Cushing remains optimistic about the team's chances against Chelsea in Europe.


**Manchester United**
Current Position: 15  
Points: 34  
Goal Difference: -6  
Recent Form: L,L,D,W,D  

Manchester United prepare to face Leicester City in the Premier League, with key decisions to be made on the lineup. Patrick Dorgu, a young wing-back, recently expressed his disagreement with a referee's penalty decision, showcasing his confidence and passion for the game. Sir Jim Ratcliffe, a potential investor, has publicly stated that Manchester United should never have appointed a particular manager, sparking debate among fans.

**Tottenham Hotspur**
Current Position: 13  
Points: 34  
Goal Difference: 12  
Recent Form: W,W,L,D,L  

Tottenham Hotspur suffered a disappointing week, losing to both Fulham and Brighton in the Premier League. The team fell 2-0 to Fulham and were also defeated 1-0 by Brighton. The losses signify a concerning spell for Spurs, who are struggling to find consistency.

Stay tuned for more updates.

- **Premier League Pulse**
```
