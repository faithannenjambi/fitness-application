from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['octofit_db']

        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create test users
        users = [
            {"email": "john.doe@example.com", "name": "John Doe", "age": 25},
            {"email": "jane.smith@example.com", "name": "Jane Smith", "age": 30},
            {"email": "alice.wonderland@example.com", "name": "Alice Wonderland", "age": 28},
            {"email": "bob.builder@example.com", "name": "Bob Builder", "age": 35}
        ]
        db.users.insert_many(users)

        # Create test teams
        teams = [
            {"name": "Team Alpha", "members": ["john.doe@example.com", "jane.smith@example.com"]},
            {"name": "Team Beta", "members": ["alice.wonderland@example.com", "bob.builder@example.com"]}
        ]
        db.teams.insert_many(teams)

        # Create test activities
        activities = [
            {"user_email": "john.doe@example.com", "activity": "Running", "duration": 30},
            {"user_email": "jane.smith@example.com", "activity": "Cycling", "duration": 45},
            {"user_email": "alice.wonderland@example.com", "activity": "Swimming", "duration": 60},
            {"user_email": "bob.builder@example.com", "activity": "Yoga", "duration": 20}
        ]
        db.activity.insert_many(activities)

        # Create test leaderboard
        leaderboard = [
            {"team": "Team Alpha", "points": 100},
            {"team": "Team Beta", "points": 80}
        ]
        db.leaderboard.insert_many(leaderboard)

        # Create test workouts
        workouts = [
            {"name": "Morning Run", "description": "A quick morning run to start the day", "duration": 30},
            {"name": "Evening Yoga", "description": "Relaxing yoga session", "duration": 45}
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
