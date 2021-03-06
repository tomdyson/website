from django.conf.urls import url
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from wagtail.wagtailadmin.menu import MenuItem
from wagtail.wagtailcore import hooks

from .invalidate import cloudflare_purge_all


def clear_cache_view(request):
    if request.method == 'POST':
        cloudflare_purge_all()
        messages.info(request, "The Cloudflare Cache was cleared.")
        return redirect('wagtailadmin_home')

    return render(
        request,
        'wagtailadmin/cache/clear.html'
    )


@hooks.register('register_admin_urls')
def urlconf_time():
    return [
        url(r'^clear_cache/$', clear_cache_view, name='admin_clear_cache'),
    ]


@hooks.register('register_admin_menu_item')
def register_frank_menu_item():
    return MenuItem('Clear Cache', reverse('admin_clear_cache'), classnames='icon icon-cross', order=10000)
