

class CredentialBuilder:

    def create(self, parser):
        parser.add_argument('-l', '--login', action='store', type=str, required=True, help='Login field to enter pergamun')
        parser.add_argument('-p', '--password', action='store', type=str, required=True, help='Password field to enter pergamun')

        args = parser.parse_args()

        return args.login, args.password
