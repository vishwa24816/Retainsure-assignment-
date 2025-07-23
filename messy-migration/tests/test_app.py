import unittest
import json
from src.app import create_app
from src.database import execute_query

import os

class AppTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_ENV'] = 'testing'
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        execute_query('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
        ''', commit=True)

    def tearDown(self):
        execute_query("DROP TABLE users", commit=True)
        self.app_context.pop()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'User Management System')

    def test_create_user(self):
        user_data = {'name': 'test', 'email': 'test@test.com', 'password': 'password'}
        response = self.client.post('/users', data=json.dumps(user_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'User created')

    def test_get_user(self):
        user_data = {'name': 'test', 'email': 'test@test.com', 'password': 'password'}
        self.client.post('/users', data=json.dumps(user_data), content_type='application/json')
        user = execute_query("SELECT * FROM users WHERE email = ?", ('test@test.com',), fetchone=True)
        response = self.client.get(f'/user/{user["id"]}')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'test')

    def test_login(self):
        user_data = {'name': 'test', 'email': 'test@test.com', 'password': 'password'}
        self.client.post('/users', data=json.dumps(user_data), content_type='application/json')
        login_data = {'email': 'test@test.com', 'password': 'password'}
        response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')

if __name__ == '__main__':
    unittest.main()
