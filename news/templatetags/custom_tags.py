from datetime import datetime
from django import template

register = template.Library()


@register.filter(name='format_date')
def format_date(value):
    """
    Formats a datetime value into a string with the format 'YYYY/MM/DD HH:MM'.
    Example => 2066/01/25 04:20

    Args:
        value (str or datetime): The date value to be formatted.

    Returns:
        str: The formatted date string.
    """
    if isinstance(value, str):
        value = datetime.fromisoformat(value)
    return value.strftime('%Y/%m/%d %H:%M')
