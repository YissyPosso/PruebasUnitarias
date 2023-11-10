import unittest
from unittest.mock import Mock
from mock_ejemplo import UserService  

class TestUserService(unittest.TestCase):

    def test_get_user_by_id(self):
        database_mock = Mock()
        database_mock.get_user_by_id.return_value = {
            'id': 1,
            'name': 'Maria',
            'email': 'maria@gmail.com'
        }
        
        user_service = UserService(database=database_mock)
        user = user_service.get_user_by_id(1)
        database_mock.get_user_by_id.assert_called_with(1)
        
        # Verifica que el resultado sea el esperado
        self.assertEqual(user['name'], 'Maria')
        self.assertEqual(user['email'], 'maria@gmail.com')

if __name__ == '__main__':
    unittest.main()
