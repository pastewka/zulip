from zerver.lib.actions import Realm, do_create_realm
from zerver.lib.domains import validate_domain
from zerver.lib.management import ZulipBaseCommand

import re
import sys

class Command(ZulipBaseCommand):
    help = """Create a realm."""

    def add_arguments(self, parser):
        parser.add_argument('-s', '--string_id',
                            dest='string_id',
                            type=str,
                            help="A short name for the realm. If this "
                                 "installation uses subdomains, this will be "
                                 "used as the realm's subdomain.")

        parser.add_argument('-n', '--name',
                            dest='name',
                            type=str,
                            help='The user-visible name for the realm.')

    def handle(self, *args, **options):
        string_id = options["string_id"]
        name = options["name"]

        if string_id is None or name is None:
            print("Please provide a name and a string_id.", file=sys.stderr)
            self.print_help("./manage.py", "create_realm")
            exit(1)

        realm = do_create_realm(string_id, name)
