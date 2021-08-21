import argparse


def get_args():
    parser = argparse.ArgumentParser(
        "ghfetch",
        description="""
ghfetch is a CLI GitHub personal README generator by Alessio Celentano.
Inspired by famous fetch such as screenfetch, neofetch and ufetch, 
the purpose of this tool is to introduce yourself as if you were a machine.
        """
    )
    parser.add_argument(
        "--generate_ascii",
        metavar="path/to/image",
        help="convert an image to ascii"
    )
    parser.add_argument(
        "--logo",
        default="github",
        help="which logo ascii print",
        choices=[
            "github", "gitlab", "python",
            "javascript", "c", "cpp",
            "custom"
        ]
    )
    args = parser.parse_args()
    return args

