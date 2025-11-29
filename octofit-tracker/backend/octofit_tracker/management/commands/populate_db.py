from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear existing data
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        Activity.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Create users (super heroes)
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='password', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc)

        # Create activities
        act1 = Activity.objects.create(user=ironman, type='run', duration=30, distance=5)
        act2 = Activity.objects.create(user=batman, type='cycle', duration=60, distance=20)
        act3 = Activity.objects.create(user=captain, type='swim', duration=45, distance=2)
        act4 = Activity.objects.create(user=superman, type='fly', duration=120, distance=100)

        # Create workouts
        Workout.objects.create(user=ironman, name='Chest Day', description='Bench press and pushups')
        Workout.objects.create(user=batman, name='Leg Day', description='Squats and lunges')

        # Create leaderboard
        Leaderboard.objects.create(user=ironman, score=100)
        Leaderboard.objects.create(user=batman, score=90)
        Leaderboard.objects.create(user=captain, score=80)
        Leaderboard.objects.create(user=superman, score=110)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
