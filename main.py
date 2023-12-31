import sys
import os
import logging
import datetime
from pyfiglet import Figlet
from dotenv import load_dotenv
from Processors.OutGoingProcessor import OutGoingProcessor


def init_logger():
    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(FORMAT)

    date = datetime.datetime.now()
    t = date.strftime("%Y%d%m%H%M%S")
    log_file_name = f"log-"+t+".log"
    if not os.path.isdir('logs'):
        os.mkdir("logs")

    file = logging.FileHandler(filename='logs/'+log_file_name)
    file.setFormatter(formatter)
    logging.basicConfig(level=logging.DEBUG, format=FORMAT)
    log = logging.getLogger()
    log.addHandler(file)
    log.setLevel(level=logging.DEBUG)


def startup_splash():
    f = Figlet(font='slant')
    print(f.renderText('Drone Emulator Service'))
    print(f"Version: {os.getenv('VERSION')}")
    print("-------------------------------------------------------")


def main():
    load_dotenv()
    startup_splash()
    init_logger()
    _ = OutGoingProcessor()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting, keyboard interupt")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    except ConnectionError as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        logging.error(f"Connection issue: {e}")
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        logging.error(f"Unhandled Exception: {e}")
