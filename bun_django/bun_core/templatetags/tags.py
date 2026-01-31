from django import template

register = template.Library()

category={
    "news":{
        "title":"News",
        "url":"news"
    },
    "about":{
        "title":"About",
        "url":"about"
    },
    "test":{
        "title":"Test",
        'url':'test'
    },
    "url":'home'
}

@register.simple_tag()
def workk():
    return category
