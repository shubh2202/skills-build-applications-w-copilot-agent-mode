from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create(name="Test User", email="test@example.com", team=team)
        self.assertEqual(user.name, "Test User")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.team.name, "Test Team")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Team Alpha")
        self.assertEqual(team.name, "Team Alpha")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name="Team Beta")
        user = User.objects.create(name="User Beta", email="beta@example.com", team=team)
        activity = Activity.objects.create(user=user, type="Running", duration=30, calories=300, date="2025-11-20")
        self.assertEqual(activity.type, "Running")
        self.assertEqual(activity.duration, 30)
        self.assertEqual(activity.calories, 300)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Cardio Blast", description="High intensity cardio workout", difficulty="Hard")
        self.assertEqual(workout.name, "Cardio Blast")
        self.assertEqual(workout.difficulty, "Hard")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name="Team Gamma")
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.team.name, "Team Gamma")
        self.assertEqual(leaderboard.points, 100)
