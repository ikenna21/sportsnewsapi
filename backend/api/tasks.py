import feedparser
from celery import shared_task
from datetime import datetime
from django.utils.timezone import make_aware, now
from .models import Article


RSS_FEEDS = {
    "ESPN": 'https://www.espn.com/espn/rss/news',
    "FOX Sports": 'https://api.foxsports.com/v2/content/optimized-rss?partnerKey=MB0Wehpmuj2lUhuRhQaafhBjAJqaPU244mlTDK1i&size=30',
    "BBC Sports": 'https://feeds.bbci.co.uk/sport/rss.xml?edition=uk',
    'CBS Sports': 'https://www.cbssports.com/rss/headlines/',
    'Yahoo Sports': 'https://sports.yahoo.com/rss/',
    'PFF News': 'https://www.pff.com/feed'
    
}

@shared_task
def index():
    for source, url in RSS_FEEDS.items():
        parsed_feed = feedparser.parse(url)
        for entry in parsed_feed.entries:
            published_parsed = entry.get('published_parsed')
            if published_parsed and len(published_parsed) >= 6:
                date_published = make_aware(datetime(*published_parsed[:6]))
            else:
                date_published = now()

            Article.objects.get_or_create(
                link=entry.link,
                defaults={
                    'source': source,
                    'title': entry.title,
                    'description': entry.get('description', ''),
                    'published': date_published,
                    'author': entry.get('author', 'Unknown'),
                }
            )
    return 'Completed'