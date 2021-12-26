import os
import unittest
import json
import os
from app import app
from dotenv import load_dotenv
from unittest.mock import patch

#load environment variables
load_dotenv()
URL = os.getenv('URL')

#Mocking pymongo calls
def get_collection():
    class Mock:
        def insert_one(self, data):
            pass
        def find_one(self, slug):
            #slug for "https://www.example.com/"
            if (slug.get('slug') == '8acec5'):
                return {'original_url': "https://www.example.com/"}
            return None
    return Mock()


#Testcases
class URLShortenTest(unittest.TestCase):
    def test_health(self):
        """Test API is reachable"""
        self.client = app.test_client(self)
        res = self.client.get('/api/health')
        self.assertEqual(res.status_code, 200)

    @patch('app.url_collection', get_collection())
    def test_unique_original_url_submit(self):
        """Test API can create a new slug (POST request)"""
        self.client = app.test_client(self)
        #using STORD as an example
        self.data = json.dumps({"longURL":"https://www.stord.com/"})
        res = self.client.post('/api/urls', data=self.data)
        self.assertEqual(res.status_code, 200)
        #testing if unique working, shortened URL is correct
        self.assertEqual(json.loads(res.data)['shortUrl'], URL + '9454df')

    @patch('app.url_collection', get_collection())
    def test_repeat_original_url_submit(self):
        """Test API can return an existing slug (POST request)"""
        self.client = app.test_client(self)
        self.data = json.dumps({"longURL":"https://www.example.com/"})
        res = self.client.post('/api/urls', data=self.data)
        self.assertEqual(res.status_code, 200)
        #testing if existing working, shortened URL is correct
        self.assertEqual(json.loads(res.data)['shortUrl'], URL + '8acec5')

    @patch('app.url_collection', get_collection())
    def test_short_url_resolve(self):
        """Test API can resolve url (GET request)."""
        self.client = app.test_client(self)
        #slug for "https://www.example.com/"
        res = self.client.get('/api/resolve/8acec5')
        self.assertEqual(res.status_code, 200)
        #testing if resolved URL is correct
        self.assertEqual(json.loads(res.data)['originalUrl'], "https://www.example.com/")

    @patch('app.url_collection', get_collection())
    def test_incorrect_resolve1(self):
        """Test API can return 404 code from empty slug (GET request)."""
        self.client = app.test_client(self)
        #Empty space as slug
        res = self.client.get('/api/resolve/ ')
        self.assertEqual(json.loads(res.data)['statusCode'], 404)

    @patch('app.url_collection', get_collection())
    def test_incorrect_resolve2(self):
        """Test API can return 404 code from nonexistent slug (GET request)."""
        self.client = app.test_client(self)
        #Nonexistent slug
        res = self.client.get('/api/resolve/123456')
        self.assertEqual(json.loads(res.data)['statusCode'], 404)


if __name__ == "__main__":
    print('Running Test Cases...')
    unittest.main()