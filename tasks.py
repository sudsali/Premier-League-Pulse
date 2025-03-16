from datetime import datetime

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def generate_newsletter(updates):
    """Generates a professional football newsletter."""
    newsletter_content = f"**Today's ({current_time}) Premier League Update: The Big Six Clubs**\n\n"
    newsletter_content += "Hello Football Fans,\n\n"
    newsletter_content += "Here's the latest updates from the Premier League's Big Six clubs:\n\n"

    for update in updates:
        newsletter_content += update + "\n"

    newsletter_content += "\nStay tuned for more updates.\n\n"
    newsletter_content += "- **Premier League Pulse**\n"

    return newsletter_content
