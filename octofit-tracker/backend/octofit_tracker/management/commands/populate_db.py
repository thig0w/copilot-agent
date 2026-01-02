from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

# Define models if not already present (for demonstration)
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    score = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    class Meta:
        app_label = 'octofit_tracker'

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        tony = User.objects.create_user(username='tony', email='tony@marvel.com', password='ironman')
        bruce = User.objects.create_user(username='bruce', email='bruce@marvel.com', password='hulk')
        clark = User.objects.create_user(username='clark', email='clark@dc.com', password='superman')
        diana = User.objects.create_user(username='diana', email='diana@dc.com', password='wonderwoman')

        # Create activities
        Activity.objects.create(user='tony', type='run', points=50)
        Activity.objects.create(user='bruce', type='walk', points=30)
        Activity.objects.create(user='clark', type='run', points=60)
        Activity.objects.create(user='diana', type='walk', points=40)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', score=80)
        Leaderboard.objects.create(team='DC', score=100)

        # Create workouts
        Workout.objects.create(name='Pushups', difficulty='Easy')
        Workout.objects.create(name='Sprints', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
