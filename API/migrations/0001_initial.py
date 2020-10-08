# Generated by Django 3.1 on 2020-08-11 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='matchData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HomeTeam', models.CharField(max_length=20)),
                ('AwayTeam', models.CharField(max_length=20)),
                ('Referee', models.CharField(max_length=20)),
                ('AttackRateH', models.FloatField()),
                ('AttackRateA', models.FloatField()),
                ('DefenceRateH', models.FloatField()),
                ('DefenceRateA', models.FloatField()),
                ('DGH', models.FloatField()),
                ('DGA', models.FloatField()),
                ('HomeRank', models.FloatField()),
                ('AwayRank', models.FloatField()),
                ('AvgHST', models.FloatField()),
                ('AvgAST', models.FloatField()),
                ('AvgHF', models.FloatField()),
                ('AvgAF', models.FloatField()),
                ('AvgHC', models.FloatField()),
                ('AvgAC', models.FloatField()),
                ('AvgHR', models.FloatField()),
                ('AvgAR', models.FloatField()),
                ('AvgHY', models.FloatField()),
                ('AvgAY', models.FloatField()),
            ],
        ),
    ]
