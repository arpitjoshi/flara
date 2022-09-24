from typing import Any, Dict
from unittest import TestCase

from tests.base import BaseFlaskTest


class ApiTest(BaseFlaskTest):
    def test_root_api(self):
        response: Dict[str, Any] = self.client.get('/ping').json
        self.assertEqual('pong', response['message'])

    def test_fibonacci_api(self):
        response: Dict[str, Any] = self.client.get('/fibonacci?n=0').json
        self.assertEqual('fibonacci', response['algo'])
        self.assertEqual(0, response['result'])

        response: Dict[str, Any] = self.client.get('/fibonacci?n=1').json
        self.assertEqual(1, response['result'])

        response: Dict[str, Any] = self.client.get('/fibonacci?n=2').json
        self.assertEqual(1, response['result'])

        response: Dict[str, Any] = self.client.get('/fibonacci?n=3').json
        self.assertEqual(2, response['result'])

        response: Dict[str, Any] = self.client.get('/fibonacci?n=3').json
        self.assertEqual(2, response['result'])

        response: Dict[str, Any] = self.client.get('/fibonacci?n=3').json
        self.assertEqual(2, response['result'])

        response: Dict[str, Any] = self.client.get('/fibonacci?n=-10').json
        self.assertEqual('failed', response['status'])

        response: Dict[str, Any] = self.client.get('/fibonacci?n=str_input').json
        self.assertEqual('failed', response['status'])

        response: Dict[str, Any] = self.client.get('/fibonacci').json
        self.assertEqual('failed', response['status'])

    def test_factorial_api(self):
        response: Dict[str, Any] = self.client.get('/factorial?n=0').json
        self.assertEqual('factorial', response['algo'])
        self.assertEqual(1, response['result'])

        response: Dict[str, Any] = self.client.get('/factorial?n=1').json
        self.assertEqual(1, response['result'])

        response: Dict[str, Any] = self.client.get('/factorial?n=2').json
        self.assertEqual(2, response['result'])

        response: Dict[str, Any] = self.client.get('/factorial?n=3').json
        self.assertEqual(6, response['result'])

        response: Dict[str, Any] = self.client.get('/factorial?n=4').json
        self.assertEqual(24, response['result'])

        response: Dict[str, Any] = self.client.get('/factorial?n=5').json
        self.assertEqual(120, response['result'])

        response: Dict[str, Any] = self.client.get('/factorial?n=-10').json
        self.assertEqual('failed', response['status'])

        response: Dict[str, Any] = self.client.get('/factorial?n=str_input').json
        self.assertEqual('failed', response['status'])

        response: Dict[str, Any] = self.client.get('/factorial').json
        self.assertEqual('failed', response['status'])

    def test_ackermann_api(self):
        response: Dict[str, Any] = self.client.get('/ackermann?m=0&n=0').json
        self.assertEqual('ackermann', response['algo'])
        self.assertEqual(1, response['result'])

        response: Dict[str, Any] = self.client.get('/ackermann?m=0&n=1').json
        self.assertEqual(2, response['result'])

        response: Dict[str, Any] = self.client.get('/ackermann?m=1&n=0').json
        self.assertEqual(2, response['result'])

        response: Dict[str, Any] = self.client.get('/ackermann?m=1&n=1').json
        self.assertEqual(3, response['result'])

        response: Dict[str, Any] = self.client.get('/ackermann?m=2&n=2').json
        self.assertEqual(7, response['result'])

        response: Dict[str, Any] = self.client.get('/ackermann?m=-1&n=0').json
        self.assertEqual('failed', response['status'])

        response: Dict[str, Any] = self.client.get('/ackermann?m=0&n=-1').json
        self.assertEqual('failed', response['status'])

        response: Dict[str, Any] = self.client.get('/ackermann?m=ack&n=1').json
        self.assertEqual('failed', response['status'])

        response: Dict[str, Any] = self.client.get('/ackermann?m=0').json
        self.assertEqual('failed', response['status'])
