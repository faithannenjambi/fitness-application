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
            {"email": "jane.smith@example.com", "name": "Jane Smith", "age": 30}
        ]
        db.users.insert_many(users)

        # Create test teams
        teams = [
            {"name": "Team Alpha", "members": ["john.doe@example.com", "jane.smith@example.com"]}
        ]
        db.teams.insert_many(teams)

        # Create test activities
        activities = [
            {"user": "john.doe@example.com", "type": "Running", "duration": 30},
            {"user": "jane.smith@example.com", "type": "Cycling", "duration": 45}
        ]
        db.activity.insert_many(activities)

        # Create test leaderboard entries
        leaderboard = [
            {"user": "john.doe@example.com", "score": 100},
            {"user": "jane.smith@example.com", "score": 150}
        ]
        db.leaderboard.insert_many(leaderboard)

        # Create test workouts
        workouts = [
            {"name": "Morning Yoga", "description": "A relaxing yoga session to start your day."},
            {"name": "HIIT", "description": "High-Intensity Interval Training for quick results."}
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
