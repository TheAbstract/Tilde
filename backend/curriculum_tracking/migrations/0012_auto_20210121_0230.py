# Generated by Django 3.1.4 on 2021-01-21 02:30

import curriculum_tracking.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('curriculum_tracking', '0011_auto_20200920_1126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agilecard',
            old_name='content_flavours',
            new_name='flavours',
        ),
        migrations.RenameField(
            model_name='contentitem',
            old_name='available_flavours',
            new_name='flavours',
        ),
        migrations.CreateModel(
            name='ReviewTrust',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='curriculum_tracking.contentitem')),
                ('flavours', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            bases=(models.Model, curriculum_tracking.models.FlavourMixin, curriculum_tracking.models.ContentItemProxyMixin),
        ),
    ]
