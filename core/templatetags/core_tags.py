from django import template
from django.db.models import ObjectDoesNotExist

from articles.models import Topic

register = template.Library()


@register.assignment_tag
def suggested_searches(number_of_suggestions):
    search_suggestions = Topic.objects.all().order_by('article_links__article__first_published_at')[:number_of_suggestions]

    return search_suggestions


@register.filter
def search_string(topic):
    return topic.name.replace(" ", "+")


@register.assignment_tag(takes_context=True)
def get_site_defaults(context):
    try:
        return context['request'].site.default_settings
    except ObjectDoesNotExist:
        return None


@register.assignment_tag(takes_context=True)
def section_image(context, item):
    if hasattr(item, "source"):
        if item.source and item.source.logo:
            return item.source.logo
        else:
            try:
                default_settings = context['request'].site.default_settings
                return default_settings.default_external_article_source_logo
            except ObjectDoesNotExist:
                pass
    return item.main_image
