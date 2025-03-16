from agents import FootballDataAgent, NewsAgent, SummaryAgent, SummaryEditorAgent
from tools import generate_club_update, BIG_SIX
from tasks import generate_newsletter

def main():
    print("Gathering latest updates on the Big Six clubs...\n")

    football_agent = FootballDataAgent()
    
    league_table_response = football_agent.get_league_standings()
    if not league_table_response:
        print("Failed to fetch league table data.")
        return

    standings = league_table_response["standings"][0]["table"]

    all_updates = []

    for club_name, club_id in BIG_SIX.items():
        try:
            update = generate_club_update(club_name, club_id, standings, football_agent)
            all_updates.append(update)
        except Exception as e:
            print(f"Error generating update for {club_name}: {e}")

    # Fetch news summaries for each club
    news_agent = NewsAgent()
    summary_agent = SummaryAgent()
    
    for club_name in BIG_SIX.keys():
        try:
            news_articles = news_agent.fetch_news_articles(club_name)
            news_summary = summary_agent.summarize(news_articles, club_name)
            all_updates.append(f"**{club_name} News Summary:**\n{news_summary}\n\n")
        except Exception as e:
            print(f"Error generating news summary for {club_name}: {e}")

    # Generate and refine newsletter
    try:
        newsletter_content = generate_newsletter(all_updates)
        editor_agent = SummaryEditorAgent()
        refined_newsletter = editor_agent.remove_extra_summary(newsletter_content)
        print(refined_newsletter)
    except Exception as e:
        print(f"Error generating newsletter: {e}")

if __name__ == "__main__":
    main()