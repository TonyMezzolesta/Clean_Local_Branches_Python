from argparse import ArgumentParser


class PruneArgumentReader(ArgumentParser):
    def __init__(self):
        super().__init__(
            description='Prune Git Branches that no longer exist on remote.'
        )

        self._set_parser_arguments()

    def _set_parser_arguments(self):
        self.add_argument(
            "directory",
            metavar="directory",
            type=str,
            help="Location of git repo to prune.",
            default=None
        )
        self.add_argument(
            "--dryRun", "-d", "--dry-run",
            action="store_true",
            dest="dry_run",
            default=False,
            help="Run without deleting, to see the effects first."
        )

    def get_parsed(self):
        parsed_args = self.parse_args()

        # Required
        directory = parsed_args.directory
        dry_run = parsed_args.dry_run

        return directory, dry_run
