import pika
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('log.log',encoding='utf-8')
basic_formater = logging.Formatter('%(asctime)s : [%(name)8s] : [%(levelname)s] : %(message)s')
handler.setFormatter(basic_formater)
logger.addHandler(handler)


class Send:
    def __init__(self, host: str, queue_name: str) -> None:
        self.host = host
        self.queue_name = queue_name

    def send_message_to_rabbit(self, message: str) -> None:

        connection_parametrs = pika.ConnectionParameters(host=self.host)
        logger.info(connection_parametrs)

        connection = pika.BlockingConnection(connection_parametrs)

        channel = connection.channel()

        queue = channel.queue_declare(queue=self.queue_name)
        logger.info(queue)

        channel.basic_publish(
            exchange='',
            routing_key=self.queue_name,
            body=message
            )

        logger.info(f'Сообщение отправленно - {message}\n')

        connection.close()