import logging   #стандартна бібліотека для логування перебігу програми
logging.basicConfig(level=logging.DEBUG,
                    filename= "logs.log",
                    filemode= "w",
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug("debug")
logging.info("info")
logging.error("error")
logging.warning("warning")
logging.critical("critical")
try:
    print(10/0)
except Exception:
    logging.exception("pomilka")
#faktorial chisla

def factorial(n):
    logging.info(f"rozpochato obchislennya factorialu chisna {n}")
    result = 1
    for i in range(1, n + 1):
        result += 1 #1*2*3...
    logging.info(f"obchislennya factorialy dlya chisla zaversheno {n}. rezultat vikonannya {result}")
    return result

logging.basicConfig(level=logging.INFO)
factorial(5)