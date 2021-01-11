__version__ = "0.0.1"  # DO NOT EDIT THIS LINE MANUALLY. LET bump2version UTILITY DO IT

import subprocess


def format_rust(unformatted: str, _info_str: str) -> str:
    unformatted_bytes = unformatted.encode("utf-8")
    result = subprocess.run(
        ["rustfmt"],
        stdout=subprocess.PIPE,
        input=unformatted_bytes,
    )
    if result.returncode:
        raise Exception("Failed to format Rust code")
    return result.stdout.decode("utf-8")
