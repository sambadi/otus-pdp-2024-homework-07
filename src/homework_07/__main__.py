from pathlib import Path
import logging
import argparse

from homework_07 import start_server

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--bind-to", action="store", default="localhost")
    parser.add_argument("-p", "--port", action="store", type=int, default=8080)
    parser.add_argument("-l", "--log", action="store", default=None)
    parser.add_argument("-r", "--document_root", action="store", default="./www")

    args = parser.parse_args()
    logging.basicConfig(
        filename=args.log,
        level=logging.INFO,
        format="[%(asctime)s] [%(levelname)s] %(message)s",
        datefmt="%Y.%m.%d %H:%M:%S",
    )
    document_root = Path().cwd().joinpath(args.document_root)
    start_server(args.bind_to.strip(), args.port, document_root)
