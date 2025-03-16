from agents import FootballDataAgent

BIG_SIX = {
    "Arsenal": 57,
    "Chelsea": 61,
    "Liverpool": 64,
    "Manchester City": 65,
    "Manchester United": 66,
    "Tottenham Hotspur": 73
}

def generate_club_update(club_name, club_id, standings, football_agent):
    """Generates an update string for a club."""
    club_data = next((team for team in standings if team["team"]["id"] == club_id), None)

    if club_data:
        position = club_data["position"]
        points = club_data["points"]
        goal_difference = club_data["goalDifference"]

        # Fetch recent form dynamically
        recent_form = football_agent.get_recent_form(club_id)

        update = (
            f"**{club_name}**\n"
            f"Current Position: {position}\n"
            f"Points: {points}\n"
            f"Goal Difference: {goal_difference}\n"
            f"Recent Form: {recent_form}\n\n"
        )
        return update
    else:
        return f"Could not retrieve data for {club_name}\n\n"
