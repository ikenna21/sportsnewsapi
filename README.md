Sports News API

Installation:
<br />

pip install -r requirements.txt

Endpoints:
/api/feeds/	GET	Retrieves first 20 articles
<br />
<br />
/api/favorites/	GET	List all favorites articles
<br />
<br />
/api/favorites/	POST	Add a new favorite article
<br />
<br />
/api/favorites/{id}/	GET	Retrieve a specific favorite
<br />
<br />
/api/favorites/{id}/	DELETE	Delete a specific favorite
<br />
<br />
Examples:
GET /api/feeds/
Response:
[
  {
    "id": 1,
    "title": "Exciting NBA Finals Game Highlights",
    "summary": "An overview of the thrilling game last night...",
    "published_at": "2025-05-28T14:32:00Z",
    "url": "https://sportsnews.com/article/1"
  },
  {
    "id": 2,
    "title": "Soccer World Cup Qualifiers Begin",
    "summary": "Teams prepare for the upcoming qualifying rounds...",
    "published_at": "2025-05-27T11:00:00Z",
    "url": "https://sportsnews.com/article/2"
  }
]
