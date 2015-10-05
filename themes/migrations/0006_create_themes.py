# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def create_themes(apps, schema_editor):
    Theme = apps.get_model("themes", "Theme")
    ThemeContent = apps.get_model("themes", "ThemeContent")
    FollowLink = apps.get_model("themes", "FollowLink")
    ContentFollowLink = apps.get_model("themes", "ContentFollowLink")
    TextBlock = apps.get_model("themes", "TextBlock")
    ContentBlockLink = apps.get_model("themes", "ContentBlockLink")
    HomePage = apps.get_model('core', 'HomePage')

    about_block = TextBlock.objects.create(
        name='About Block',
        slug='about-block',
        heading='About',
        content='Open Canada is a Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. quis nostrud exercitation.'
    )

    masthead_block = TextBlock.objects.create(
        name='Masthead Block',
        slug='masthead-block',
        heading='Masthead',
        content="""<p><a href="https://twitter.com/taylor_owen">@Taylor Owen</a> / Editor-in-Chief</p>
                <p><a href="https://twitter.com/eva_sita">@Eva Salinas</a> / Managing Editor</p>
                <p><a href="https://twitter.com/cattsalikis">@Catherine Tsalikis</a> / Journalist &amp; Editor</p>"""
    )

    newsletter_block = TextBlock.objects.create(
        name='Newsletter Block',
        slug='newsletter-block',
        heading='Weekly Newsletter',
        content=""
    )

    follow_block = TextBlock.objects.create(
        name='Follow Block',
        slug='follow-block',
        heading='Follow',
        content=""
    )

    tagline_block = TextBlock.objects.create(
        name='Tagline Block',
        slug='tagline-block',
        heading='',
        content="OpenCanada.org is a publication of the Canadian International Council, the Centre for International Governance Innovation and the Bill Graham Centre"
    )

    twitter = FollowLink.objects.create(
        name="Twitter",
        slug="twitter",
        link="https://twitter.com/opencanada"
    )

    facebook = FollowLink.objects.create(
        name="Facebook",
        slug="facebook",
        link="https://facebook.com/opencanada"
    )

    google_plus = FollowLink.objects.create(
        name="Google Plus",
        slug="google-plus",
        link="#"
    )

    rss_feed = FollowLink.objects.create(
        name="RSS Feed",
        slug="rss-feed",
        link="/feed/"
    )

    default_content = ThemeContent.objects.create(
        name="OpenCanada Standard",
    )

    ContentBlockLink.objects.create(
        theme_content=default_content,
        block=about_block
    )

    ContentBlockLink.objects.create(
        theme_content=default_content,
        block=masthead_block
    )

    ContentBlockLink.objects.create(
        theme_content=default_content,
        block=newsletter_block
    )

    ContentBlockLink.objects.create(
        theme_content=default_content,
        block=follow_block
    )

    ContentBlockLink.objects.create(
        theme_content=default_content,
        block=tagline_block
    )

    ContentFollowLink.objects.create(
        theme_content=default_content,
        block=twitter
    )

    ContentFollowLink.objects.create(
        theme_content=default_content,
        block=facebook
    )

    ContentFollowLink.objects.create(
        theme_content=default_content,
        block=google_plus
    )

    ContentFollowLink.objects.create(
        theme_content=default_content,
        block=rss_feed
    )

    default_theme, created = Theme.objects.get_or_create(
        name="default"
    )
    default_theme.is_default=True
    default_theme.content=default_content
    default_theme.save()

    dark, created = Theme.objects.get_or_create(
        name="dark",
    )
    dark.content = default_content
    dark.save()

    light, created = Theme.objects.get_or_create(
        name="light"
    )
    light.content = default_content
    light.save()

    lind, created = Theme.objects.get_or_create(
        name="lind"
    )
    lind.content = default_content
    lind.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_sitedefaults_contact_email'),
        ('themes', '0005_auto_20151002_2357'),
    ]

    operations = [
        migrations.RunPython(create_themes),
    ]
