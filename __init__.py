'''
__init__.py
@author: Nicholas Sollazzo
@mail: sollsharp@gmail.com
@version: 0.1
@date: 13/06/17
@status: DEV
'''

from modules.Mail_module import Mail
from modules.Time_module import Time

# costants
MAIL = Mail()
TIME = Time()


def main():
    print(MAIL.get_path())
    print(TIME.get_path())


if __name__ == '__main__':
    main()
