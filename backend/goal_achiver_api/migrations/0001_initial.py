# Generated by Django 3.2.20 on 2023-08-23 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GoalsGroup',
            fields=[
                ('title', models.TextField()),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='CounterGoal',
            fields=[
                ('goal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='goal_achiver_api.goal')),
                ('counter', models.IntegerField(default=0)),
            ],
            bases=('goal_achiver_api.goal',),
        ),
        migrations.CreateModel(
            name='LimitCounterGoal',
            fields=[
                ('goal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='goal_achiver_api.goal')),
                ('counter', models.IntegerField(default=0)),
                ('limit', models.IntegerField(default=0)),
            ],
            bases=('goal_achiver_api.goal',),
        ),
        migrations.CreateModel(
            name='StarsGoal',
            fields=[
                ('goal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='goal_achiver_api.goal')),
                ('stars', models.IntegerField(default=0)),
            ],
            bases=('goal_achiver_api.goal',),
        ),
        migrations.CreateModel(
            name='UserGoalsGroups',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GoalsGroupTemplate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('goals_group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='template', to='goal_achiver_api.goalsgroup')),
            ],
        ),
        migrations.AddField(
            model_name='goal',
            name='goals_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goal_achiver_api.goalsgroup'),
        ),
    ]
