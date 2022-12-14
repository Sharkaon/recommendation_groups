# Generated by Django 4.1.1 on 2022-10-24 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation_circle', '0006_remove_recommendation_circle_edition_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circle',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='circles', to='recommendation_circle.profile'),
        ),
        migrations.AlterField(
            model_name='edition',
            name='circle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='editions', to='recommendation_circle.circle'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='edition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', to='recommendation_circle.edition'),
        ),
    ]
