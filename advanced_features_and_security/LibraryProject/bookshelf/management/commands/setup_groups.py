from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from bookshelf.models import Book

class Command(BaseCommand):
    help = "Setup initial groups and permissions"

    def handle(self, *args, **kwargs):
        editors, _ = Group.objects.get_or_create(name="Editors")
        viewers, _ = Group.objects.get_or_create(name="Viewers")
        admins, _ = Group.objects.get_or_create(name="Admins")

        perms = Permission.objects.filter(content_type__app_label='bookshelf', content_type__model='book')

        editors.permissions.set(perms.filter(codename__in=['can_create', 'can_edit']))
        viewers.permissions.set(perms.filter(codename__in=['can_view']))
        admins.permissions.set(perms)  # all permissions

        self.stdout.write(self.style.SUCCESS("Groups and permissions set up successfully."))
