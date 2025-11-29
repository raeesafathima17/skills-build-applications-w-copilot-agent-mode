from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass', team=self.team)
        self.activity = Activity.objects.create(user=self.user, type='run', duration=30, distance=5)
        self.workout = Workout.objects.create(user=self.user, name='Test Workout', description='Test Desc')
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100)

    def test_user_team(self):
        self.assertEqual(self.user.team, self.team)
    def test_activity(self):
        self.assertEqual(self.activity.user, self.user)
    def test_workout(self):
        self.assertEqual(self.workout.user, self.user)
    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.user, self.user)
