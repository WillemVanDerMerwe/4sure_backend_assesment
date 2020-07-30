from django.conf import settings
from django_hosts import patterns, host

# host_patterns = patterns('',
#     host(r'www', settings.ROOT_URLCONF, name='www'),
#     host(r'(?!www).*', 'URLShortner.hostsconf.urls', name='wildcard'),
# )
host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'(\w+)', 'URLShortner.hostsconf.urls', name='wildcard'),
)