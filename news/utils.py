"""
Fetches news articles from the News API based on the provided parameters.

Parameters:
query (str): The search query for filtering news articles (e.g., "technology", "health"). Defaults to an empty string.
category (str): The category of news to filter by (e.g., "business", "sports"). Defaults to an empty string.
language (str): The language of the articles to be returned. Defaults to "en" for English.
page_size (int): The number of articles per page. Defaults to 12, with a max of 100.
sort_by (str): Criteria to sort the articles by, such as "publishedAt", "popularity". Defaults to an empty string.
page (int): The page number for pagination. Defaults to 1.

Returns:
dict: A dictionary with two keys:
    - "articles" (list): A list of articles (each article is a dictionary with keys like 'title', 'description', etc.).
    - "totalResults" (int): The total number of articles that match the query and filters.

Example:
{
    "articles": [
        {
            "title": "News Title",
            "description": "Description of the article.",
            "url": "https://example.com/article"
        },
        ...
    ],
    "totalResults": 12
}

If the API request is unsuccessful (status code != 200) or the response cannot be parsed as JSON,
the function will return an empty list of articles and a totalResults of 0.

Exceptions:
- ValueError: Raised when the response is not valid JSON.
- Requests exceptions: If there's an issue with the API request, it will return an empty result.

"""
import requests
from FreshNews.settings import API_KEY


def fetch_news(
        query="",
        category="",
        language="en",
        page_size="",
        sort_by="",
        page=1,
):
    url = "https://newsapi.org/v2/everything"
    params = {
        "apiKey": API_KEY,
        "q": query,
        "category": category,
        "language": language,
        "pageSize": page_size,
        "sortBy": sort_by,
        "page": page,
    }
    response = requests.get(url, params=params)

    if response.status_code != 200:
        return {"articles": [], "totalResults": 0}

    try:
        data = response.json()
        return data
    except ValueError:
        return {"articles": [], "totalResults": 0}
