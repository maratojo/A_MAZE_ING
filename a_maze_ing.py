import sys


def parse_config(file: str) -> dict[str, str]:
    config: dict[str, str] = {}
    try:
        with open(file, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" not in line:
                    print("Error: line must be 'KEY=VALUE'")
                    sys.exit(1)
                key, value = line.split("=", 1)
                config[key.strip()] = value.strip()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    return config


def validate_config(config: dict[str, str]) -> None:
    keys = ["WIDTH", "HEIGHT", "ENTRY", "EXIT",
            "OUTPUT_FILE", "PERFECT"]

    for key in keys:
        if key not in config:
            print("Error: invalid configuration")
            sys.exit(1)
    try:
        width = int(config["WIDTH"])
        height = int(config["HEIGHT"])
    except ValueError:
        print("Error: WIDHT and HEIGHT must be integer")
        sys.exit(1)

    try:
        entry_x, entry_y = config["ENTRY"].split(",")
        exit_x, exit_y = config["EXIT"].split(",")
        entry = (int(entry_x), int(entry_y))
        exit = (int(exit_x), int(exit_y))
    except ValueError:
        print("Error: ENTRY and EXIT must be in format'x,y'")
        sys.exit(1)
    if entry[0] > width and entry[1] > height:
        print("ENTRY must be inside the maze bounds")
        sys.exit(1)
    if exit[0] > width and exit[1] > height:
        print("EXIT must be inside the maze bounds")
        sys.exit(1)
    if exit == entry:
        print("ENTRY and EXIT must be differnt")
        sys.exit(1)
    if config["PERFECT"] not in ("True", "False"):
        print("Error: PERFECT must be True or False")
        sys.exit(1)


if __name__ == "__main__":
    config_file = sys.argv[1]
    config = parse_config(config_file)
    validate_config(config)
    print(config)
