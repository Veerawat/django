from django.core.management.base import BaseCommand, CommandError
# from polls.models import Question as Poll
from core.models import Profile


class Command(BaseCommand):
    help = 'Show Profile'

    def add_arguments(self, parser):
        parser.add_argument('id', nargs=1, type=int)

    def handle(self, *args, **options):
        print(args)
        print(options)

        try:
            id=options.get("id")[0]
            print(id)
            profile = Profile.objects.get(id=id)
            print(profile)
        except Exception:
            raise CommandError("Error!")


        