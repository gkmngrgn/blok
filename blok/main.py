from blok.http_server import app
from argparse import ArgumentParser, Namespace


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("-b", "--bind", default="0.0.0.0")
    parser.add_argument("-d", "--debug", default=False, type=bool)
    parser.add_argument("-p", "--port", default=8080, type=int)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    app.run(host=args.bind, port=args.port, debug=args.debug)
