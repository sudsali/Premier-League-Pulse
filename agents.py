import time
import requests
import os
from dotenv import load_dotenv
from serpapi import GoogleSearch
import together

load_dotenv()

class FootballDataAgent:
    def __init__(self):
        self.api_key = os.getenv("FOOTBALL_DATA_API_KEY")
        self.base_url = "https://api.football-data.org/v4"
        self.headers = {"X-Auth-Token": self.api_key}
    
    def get_league_standings(self, competition_id="PL"):
        """Fetches league standings for the given competition."""
        url = f"{self.base_url}/competitions/{competition_id}/standings"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching standings: {response.status_code}")
            return None

    def get_recent_form(self, team_id):
        """Fetches recent form (last 5 matches) for a team."""
        url = f"{self.base_url}/teams/{team_id}/matches?status=FINISHED&limit=5"
        
        # Throttle requests to avoid rate limits
        time.sleep(6)  # Delay each request by 6 seconds
        
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            matches = response.json().get("matches", [])
            form = []
            for match in matches:
                if match["score"]["winner"] == "HOME_TEAM" and match["homeTeam"]["id"] == team_id:
                    form.append("W")
                elif match["score"]["winner"] == "AWAY_TEAM" and match["awayTeam"]["id"] == team_id:
                    form.append("W")
                elif match["score"]["winner"] == "DRAW":
                    form.append("D")
                else:
                    form.append("L")
            return ",".join(form)
        elif response.status_code == 429:
            print(f"Rate limit exceeded for team {team_id}. Retrying after delay...")
            time.sleep(60)  # Wait for 1 minute before retrying
            return self.get_recent_form(team_id)
        else:
            print(f"Error fetching recent form for team {team_id}: {response.status_code}")
            return "N/A"

class NewsAgent:
    def __init__(self):
        self.api_key = os.getenv("SERPAPI_KEY")

    def fetch_news_articles(self, club_name):
        """Fetches news articles related to a Premier League club using SerpAPI."""
        try:
            search_params = {
                "q": f"{club_name} football news",
                "api_key": self.api_key,
                "engine": "google_news",
                "tbm": "nws"
            }
            
            search = GoogleSearch(search_params)
            results = search.get_dict()
            articles = results.get("news_results", [])
            return articles[:5]  # Limit to top 5 articles
        except Exception as e:
            print(f"Error fetching news for {club_name}: {e}")
            return []

class SummaryAgent:
    def __init__(self):
        self.role = "Expert summarizer."
    
    def summarize(self, news_articles, club_name):
        """Summarizes the news articles using Together AI."""
        if not news_articles:
            return "No significant news to summarize."
        
        try:
            text = ". ".join([f"{article['title']}. {article.get('snippet', 'No summary available')}" for article in news_articles])
            
            prompt = f"""
You are a football expert. Provide a concise, engaging summary (under 200 words) of the following news articles related to {club_name}. Focus on key events, player performances, managerial decisions, and overall sentiment. Ensure the summary is well-structured and directly presentable in a football newsletter.

Articles:

{text}

Respond with ONLY the summary and no other text.
"""
            
            response = together.Complete.create(
                prompt=prompt,
                model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
                max_tokens=300,
                temperature=0.7,
            )
            
            if isinstance(response, dict) and 'choices' in response:
                summary = response['choices'][0]['text'].strip()
                return summary
            else:
                return "Unable to generate summary due to unexpected API response format."
        
        except Exception as e:
            print(f"Error generating summary: {e}")
            return "Unable to generate summary at this time."

class SummaryEditorAgent:
    def remove_extra_summary(self, newsletter_content):
        """Removes redundant summaries from the newsletter."""
        try:
            prompt = f"""
You are an expert editor. Clean up redundant paragraphs in this football newsletter while retaining core content:

{newsletter_content}

Respond with ONLY the cleaned newsletter content.
"""
            
            response = together.Complete.create(
                prompt=prompt,
                model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
                max_tokens=2000,
                temperature=0.7,
            )
            
            if isinstance(response, dict) and 'choices' in response:
                cleaned_newsletter = response['choices'][0]['text'].strip()
                return cleaned_newsletter
            else:
                return newsletter_content
        
        except Exception as e:
            print(f"Error cleaning newsletter: {e}")
            return newsletter_content