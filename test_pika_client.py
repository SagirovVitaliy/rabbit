import unittest
from pika_client import Send
from test_config import (
    HOST,
    QUEUE_NAME,
    HOST_STR,
    HOST_INT,
    MESSAGE_STR,
    MESSAGE_INT,
    QUEUE_NAME_INT
    )

class TestSend(unittest.TestCase):

    def test_send_message_to_rabbit(self):
        '''
        GIVEN a pika client configured for testing
        WHEN the all parameters are normal
        THEN check that the return is valid
        '''
        send = Send(HOST, QUEUE_NAME)
        send_message = send.send_message_to_rabbit(MESSAGE_STR)
        self.assertEqual(send_message, None)

    def test_send_message_to_rabbit_wrong_str_host(self):
        '''
        GIVEN a pika client configured for testing
        WHEN the host is wrong string
        THEN check that the return is valid
        '''
        send = Send(HOST_STR, QUEUE_NAME)
        self.assertRaises(Exception, send.send_message_to_rabbit, MESSAGE_STR)


    def test_send_message_to_rabbit_int_host(self):
        '''
        GIVEN a pika client configured for testing
        WHEN the host is int
        THEN check that the return is valid
        '''
        send = Send(HOST_INT, QUEUE_NAME)
        self.assertRaises(TypeError, send.send_message_to_rabbit, MESSAGE_STR)

    def test_send_message_to_rabbit_int_queue_name(self):
        '''
        GIVEN a pika client configured for testing
        WHEN the queue name is integer
        THEN check that the return is valid
        '''
        send = Send(HOST_INT, QUEUE_NAME_INT)
        self.assertRaises(TypeError, send.send_message_to_rabbit, MESSAGE_STR)

    def test_send_message_to_rabbit_message_int(self):
        '''
        GIVEN a pika client configured for testing
        WHEN the message is integer
        THEN check that the return is valid
        '''
        send = Send(HOST, QUEUE_NAME)
        self.assertRaises(TypeError, send.send_message_to_rabbit, MESSAGE_INT)


if __name__ == '__main__':
    unittest.main()