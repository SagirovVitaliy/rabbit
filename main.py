from pika_client import Send
from config import HOST, QUEUE_NAME
import logging
import traceback

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('log.log',encoding='utf-8')
basic_formater = logging.Formatter('%(asctime)s : [%(name)8s] : [%(levelname)s] : %(message)s')
handler.setFormatter(basic_formater)
logger.addHandler(handler)


def main():
    logger.info('Программа начала работать')
    send = Send(HOST, QUEUE_NAME)
    try:
        while True:
            message = input('Введите своё сообщение:')
            logger.info(f'Сообщеие перед отправкой - {message}')

            if message == 'End':
                logger.info('Программа закончила работу')
                break

            send.send_message_to_rabbit(message)
    except Exception:
        print('Вышла ошибка смотри log')
        logger.error(traceback.format_exc())

if __name__ == '__main__':
    main()
