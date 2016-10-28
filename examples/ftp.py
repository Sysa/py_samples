import logging
from ftplib import FTP


class MyFTP(FTP):
    """ 1. наследуемся от класса FTP
        2. переопределяем метод, который печатает в консоль (sanitize)
        3. добавляем логирование сразу в наш класс
        4. логи пишем в 1 файл, полученные данные во 2
    """

    def _init__(self, *args):
        super(MyFTP, self).__init__(*args)

    @staticmethod
    def logger():
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s:  %(levelname)s:  %(name)s:  %(message)s',
            filename="out.log",
            filemode='a'
        )
        logger = logging.getLogger('FTP')
        return logger

    def sanitize(self, *args):
        logger = self.logger()
        response = FTP.sanitize(self, *args)
        logger.debug(response)
        return response

    def write(self, *args):
        with open('cmd.txt', 'a') as f:
            f.write(*args)
            f.write('\n')

ftp = MyFTP('ftp.cqg.com')
ftp.set_debuglevel(2)
ftp.login()
ftp.retrlines('LIST', ftp.write)
