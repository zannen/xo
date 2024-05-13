import argparse

from xo import run


def parse_args() -> argparse.Namespace:
    """Parse cmdline arguments"""
    parser = argparse.ArgumentParser(
        description="Interact with KuCoin", usage="%(prog)s [options]"
    )

    parser.add_argument("--configfile", help="", required=True)

    parser.add_argument("--keysfile", help="", required=True)

    return parser.parse_args()


def main() -> None:
    # args = parse_args()
    # bot = Bot(config=args.configfile, keys=args.keysfile)
    # bot.loop()
    run()


if __name__ == "__main__":
    main()
