import unittest
import requests

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.base_url = 'https://jsonplaceholder.typicode.com'

    def test_get_posts(self):
        response = requests.get(f'{self.base_url}/posts')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 100)

    def test_get_post_by_id(self):
        response = requests.get(f'{self.base_url}/posts/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], 1)

    def test_create_post(self):
        data = {'title': 'foo', 'body': 'bar', 'userId': 1}
        response = requests.post(f'{self.base_url}/posts', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['title'], 'foo')

if __name__ == '__main__':
    unittest.main()
