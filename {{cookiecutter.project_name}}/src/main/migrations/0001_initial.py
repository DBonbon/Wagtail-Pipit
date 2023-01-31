# Generated by Django 4.1.5 on 2023-01-31 19:39

from django.db import migrations, models
import django.db.models.deletion
import main.mixins
import wagtail.fields
import wagtail_headless_preview.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("customimage", "0001_initial"),
        ("wagtailcore", "0078_referenceindex"),
    ]

    operations = [
        migrations.CreateModel(
            name="BasePage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "og_title",
                    models.CharField(
                        blank=True,
                        help_text="Fallbacks to seo title if empty",
                        max_length=40,
                        null=True,
                        verbose_name="Facebook title",
                    ),
                ),
                (
                    "og_description",
                    models.CharField(
                        blank=True,
                        help_text="Fallbacks to seo description if empty",
                        max_length=300,
                        null=True,
                        verbose_name="Facebook description",
                    ),
                ),
                (
                    "twitter_title",
                    models.CharField(
                        blank=True,
                        help_text="Fallbacks to facebook title if empty",
                        max_length=40,
                        null=True,
                        verbose_name="Twitter title",
                    ),
                ),
                (
                    "twitter_description",
                    models.CharField(
                        blank=True,
                        help_text="Fallbacks to facebook description if empty",
                        max_length=300,
                        null=True,
                        verbose_name="Twitter description",
                    ),
                ),
                (
                    "robot_noindex",
                    models.BooleanField(
                        default=False,
                        help_text="Check to add noindex to robots",
                        verbose_name="No index",
                    ),
                ),
                (
                    "robot_nofollow",
                    models.BooleanField(
                        default=False,
                        help_text="Check to add nofollow to robots",
                        verbose_name="No follow",
                    ),
                ),
                (
                    "canonical_link",
                    models.URLField(
                        blank=True, null=True, verbose_name="Canonical link"
                    ),
                ),
                (
                    "og_image",
                    models.ForeignKey(
                        blank=True,
                        help_text="If you want to override the image used on Facebook for                     this item, upload an image here.                     The recommended image size for Facebook is 1200 × 630px",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="customimage.customimage",
                    ),
                ),
                (
                    "twitter_image",
                    models.ForeignKey(
                        blank=True,
                        help_text="Fallbacks to facebook image if empty",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="customimage.customimage",
                        verbose_name="Twitter image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(main.mixins.EnhancedEditHandlerMixin, "wagtailcore.page"),
        ),
        migrations.CreateModel(
            name="ArticlePage",
            fields=[
                (
                    "basepage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="main.basepage",
                    ),
                ),
                (
                    "rich_text",
                    wagtail.fields.RichTextField(
                        blank=True, null=True, verbose_name="Rich text"
                    ),
                ),
            ],
            options={
                "verbose_name": "Article",
            },
            bases=(
                wagtail_headless_preview.models.HeadlessPreviewMixin,
                "main.basepage",
            ),
        ),
        migrations.CreateModel(
            name="HomePage",
            fields=[
                (
                    "basepage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="main.basepage",
                    ),
                ),
            ],
            options={
                "verbose_name": "Home",
            },
            bases=(
                wagtail_headless_preview.models.HeadlessPreviewMixin,
                "main.basepage",
            ),
        ),
    ]
