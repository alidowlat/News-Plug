from FreshNews.settings import API_KEY
from django.shortcuts import render
from news.utils import fetch_news
import requests


def news_list(request):
    # Get query parameters with defaults
    query = request.GET.get("q", "")
    category = request.GET.get("category", "")
    language = request.GET.get("language", "en")
    page_size = int(request.GET.get("pageSize", 100))
    sort_by = request.GET.get("sortBy", "publishedAt")
    page = int(request.GET.get("page", 1))

    # Fetch news data
    news_data = fetch_news(
        query=query,
        category=category,
        language=language,
        page_size=page_size,
        sort_by=sort_by,
        page=page,
    )

    # Extract articles and total results
    news_articles = news_data.get("articles", [])
    total_results = news_data.get("totalResults", 0)

    # Calculate total pages for pagination
    total_pages = (total_results // page_size) + (1 if total_results % page_size else 0)

    # Handle rate limit for external API call
    response = requests.get(f"https://newsapi.org/v2/everything?q=example&apiKey={API_KEY}")
    error_message = None
    if response.status_code == 429:
        error_message = "Too many requests. Please try again later."

    # Prepare context for rendering the template
    context = {
        "news_articles": news_articles,
        "total_pages": total_pages,
        "current_page": page,
        "query_params": {
            "q": query,
            "category": category,
            "language": language,
            "pageSize": page_size,
            "sortBy": sort_by,
        },
        "pagination": range(1, total_pages + 1),
        "error_message": error_message,
    }

    return render(request, "news/news_list.html", context)


def footer_component(request):
    return render(request, "shared/footer_comp.html", {})
