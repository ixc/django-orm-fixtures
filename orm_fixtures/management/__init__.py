from django.core.management import call_command
from django.db.models import signals

def post_syncdb(app, verbosity, **kwargs):
    app_label = app.__name__.split('.')[-2]
    fixtures = ['%s.%s' % (app_label, app_label), '%s.post_syncdb' % app_label]
    call_command('orm_fixtures', verbosity=verbosity, *fixtures)

signals.post_syncdb.connect(post_syncdb)
