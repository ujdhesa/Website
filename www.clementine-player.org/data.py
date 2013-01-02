# -*- coding: utf-8 -*-

def _(x): return x

LATEST_VERSION = '1.1'
SCREENSHOTS = [
  {'version': '1.1', 'entries': [
    {'file': 'clementine-1.1-1.png', 'title': _('Podcasts')},
    {'file': 'clementine-1.1-2.png', 'title': _('Google Drive')},
    {'file': 'clementine-1.1-3.png', 'title': _('New global search interface')},
    {'file': 'clementine-1.1-4.png', 'title': _('Moodbars')},
  ]},
  {'version': '1.0', 'entries': [
    {'file': 'clementine-1.0-1.png', 'title': _('Transcoding settings')},
    {'file': 'clementine-1.0-2.png', 'title': _('Global search finding albums on Spotify')},
    {'file': 'clementine-1.0-3.png', 'title': _('Global search options')},
    {'file': 'clementine-1.0-4.png', 'title': _('Grooveshark integration')},
  ]},
  {'version': '0.7', 'entries': [
    {'file': 'clementine-0.7-1.png', 'title': _('Lyrics and track slider tooltip')},
    {'file': 'clementine-0.7-2.png', 'title': _('MusicBrainz fixing untagged files')},
    {'file': 'clementine-0.7-3.png', 'title': _('New tag editor with autocompletion')},
    {'file': 'clementine-0.7-4.png', 'title': _('Track slider tooltip on Mac OS X')},
  ]},
  {'version': '0.6', 'entries': [
    {'file': 'clementine-0.6-1.png', 'title': _('Artist photos and biographies')},
    {'file': 'clementine-0.6-2.png', 'title': _('Lyrics')},
    {'file': 'clementine-0.6-3.png', 'title': _('Icecast radio stations')},
    {'file': 'clementine-0.6-4.png', 'title': _('Smart playlists and kittens')},
  ]},
  {'version': '0.5', 'entries': [
    {'file': 'clementine-0.5-1.png', 'title': _('The queue manager on Windows 7')},
    {'file': 'clementine-0.5-2.png', 'title': _('Copying music to an iPod in Ubuntu')},
    {'file': 'clementine-0.5-3.png', 'title': _('Clementine 0.5 on Ubu...ALL GLORY TO THE HYPNOTOAD')},
    {'file': 'clementine-0.5-4.jpg', 'title': _('Clementine 0.5 on Mac OS X')},
  ]},
  {'version': '0.4', 'entries': [
    {'file': 'clementine-0.4-1.png', 'title': _('Clementine 0.4 on Ubuntu')},
    {'file': 'clementine-0.4-2.png', 'title': _('Clementine 0.4 on Windows 7')},
    {'file': 'clementine-0.4-3.png', 'title': _('Clementine 0.4 visualisations with projectM')},
    {'file': 'clementine-0.4-4.png', 'title': _('Clementine 0.4 on Mac OS X')},
  ]},
  {'version': '0.2', 'entries': [
    {'file': 'clementine-0.2-1.png', 'title': _('Last.fm tag radio')},
    {'file': 'clementine-0.2-2.png', 'title': _('Searching the library')},
    {'file': 'clementine-0.2-3.png', 'title': _('The tag editor on Windows')},
    {'file': 'clementine-0.2-4.png', 'title': _('The cover manager on Mac OS X')},
  ]},
  {'version': '0.1', 'entries': [
    {'file': 'clementine-0.1-1.png', 'title': _('Playback on Linux')},
    {'file': 'clementine-0.1-2.png', 'title': _('Last.fm support')},
    {'file': 'clementine-0.1-3.png', 'title': _('The tag editor on Windows')},
    {'file': 'clementine-0.1-4.png', 'title': _('Growl notifications on Mac OS X')},
  ]},
]
DOWNLOAD_BASE_URL = 'http://clementine-player.googlecode.com/files/'
DOWNLOADS = [
  {'os': 'ubuntu',      'ver': '1.1', 'arch': 32, 'name': 'clementine_1.1.1~lucid_i386.deb'},
  {'os': 'ubuntu',      'ver': '1.1', 'arch': 64, 'name': 'clementine_1.1.1~lucid_amd64.deb'},
  {'os': 'umaverick',   'ver': '1.1', 'arch': 32, 'name': 'clementine_1.1.1~maverick_i386.deb'},
  {'os': 'umaverick',   'ver': '1.1', 'arch': 64, 'name': 'clementine_1.1.1~maverick_amd64.deb'},
  {'os': 'unatty',      'ver': '1.1', 'arch': 32, 'name': 'clementine_1.1.1~natty_i386.deb'},
  {'os': 'unatty',      'ver': '1.1', 'arch': 64, 'name': 'clementine_1.1.1~natty_amd64.deb'},
  {'os': 'uoneiric',    'ver': '1.1', 'arch': 32, 'name': 'clementine_1.1.1~oneiric_i386.deb'},
  {'os': 'uoneiric',    'ver': '1.1', 'arch': 64, 'name': 'clementine_1.1.1~oneiric_amd64.deb'},
  {'os': 'uprecise',    'ver': '1.1', 'arch': 32, 'name': 'clementine_1.1.1~precise_i386.deb'},
  {'os': 'uprecise',    'ver': '1.1', 'arch': 64, 'name': 'clementine_1.1.1~precise_amd64.deb'},
  {'os': 'uquantal',    'ver': '1.1', 'arch': 64, 'name': 'clementine_1.1.1~quantal_amd64.deb'},
  {'os': 'uquantal',    'ver': '1.1', 'arch': 32, 'name': 'clementine_1.1.1~quantal_i386.deb'},
  {'os': 'squeeze',     'ver': '1.1', 'arch': 32, 'name': 'clementine_1.1.1~squeeze_i386.deb'},
  {'os': 'squeeze',     'ver': '1.1', 'arch': 64, 'name': 'clementine_1.1.1~squeeze_amd64.deb'},
  {'os': 'fedora16',    'ver': '1.1', 'arch': 32, 'name': 'clementine-1.1.1-1.fc16.i686.rpm'},
  {'os': 'fedora16',    'ver': '1.1', 'arch': 64, 'name': 'clementine-1.1.1-1.fc16.x86_64.rpm'},
  {'os': 'fedora17',    'ver': '1.1', 'arch': 32, 'name': 'clementine-1.1.1-1.fc17.i686.rpm'},
  {'os': 'fedora17',    'ver': '1.1', 'arch': 64, 'name': 'clementine-1.1.1-1.fc17.x86_64.rpm'},
  {'os': 'windows',     'ver': '1.1', 'arch': 0,  'name': 'ClementineSetup-1.1.1.exe'},
  {'os': 'snowleopard', 'ver': '1.1', 'arch': 0,  'name': 'clementine-1.1.0.dmg'},
  {'os': 'source',      'ver': '1.1', 'arch': 0,  'name': 'clementine-1.1.1.tar.gz'},

  {'os': 'ubuntu',      'ver': '1.0', 'arch': 32, 'name': 'clementine_1.0.1~lucid_i386.deb'},
  {'os': 'ubuntu',      'ver': '1.0', 'arch': 64, 'name': 'clementine_1.0.1~lucid_amd64.deb'},
  {'os': 'umaverick',   'ver': '1.0', 'arch': 32, 'name': 'clementine_1.0.1~maverick_i386.deb'},
  {'os': 'umaverick',   'ver': '1.0', 'arch': 64, 'name': 'clementine_1.0.1~maverick_amd64.deb'},
  {'os': 'unatty',      'ver': '1.0', 'arch': 32, 'name': 'clementine_1.0.1~natty_i386.deb'},
  {'os': 'unatty',      'ver': '1.0', 'arch': 64, 'name': 'clementine_1.0.1~natty_amd64.deb'},
  {'os': 'uoneiric',    'ver': '1.0', 'arch': 32, 'name': 'clementine_1.0.1~oneiric_i386.deb'},
  {'os': 'uoneiric',    'ver': '1.0', 'arch': 64, 'name': 'clementine_1.0.1~oneiric_amd64.deb'},
  {'os': 'uprecise',    'ver': '1.0', 'arch': 32, 'name': 'clementine_1.0.1~precise_i386.deb'},
  {'os': 'uprecise',    'ver': '1.0', 'arch': 64, 'name': 'clementine_1.0.1~precise_amd64.deb'},
  {'os': 'squeeze',     'ver': '1.0', 'arch': 32, 'name': 'clementine_1.0.1~squeeze_i386.deb'},
  {'os': 'squeeze',     'ver': '1.0', 'arch': 64, 'name': 'clementine_1.0.1~squeeze_amd64.deb'},
  {'os': 'fedora15',    'ver': '1.0', 'arch': 32, 'name': 'clementine-1.0.1-1.fc15.i686.rpm'},
  {'os': 'fedora15',    'ver': '1.0', 'arch': 64, 'name': 'clementine-1.0.1-1.fc15.x86_64.rpm'},
  {'os': 'fedora16',    'ver': '1.0', 'arch': 32, 'name': 'clementine-1.0.1-1.fc16.i686.rpm'},
  {'os': 'fedora16',    'ver': '1.0', 'arch': 64, 'name': 'clementine-1.0.1-1.fc16.x86_64.rpm'},
  {'os': 'windows',     'ver': '1.0', 'arch': 0,  'name': 'ClementineSetup-1.0.1.exe'},
  {'os': 'snowleopard', 'ver': '1.0', 'arch': 0,  'name': 'clementine-1.0.1.dmg'},
  {'os': 'source',      'ver': '1.0', 'arch': 0,  'name': 'clementine-1.0.1.tar.gz'},

  {'os': 'ubuntu',      'ver': '0.7', 'arch': 32, 'name': 'clementine_0.7.1~lucid_i386.deb'},
  {'os': 'ubuntu',      'ver': '0.7', 'arch': 64, 'name': 'clementine_0.7.1~lucid_amd64.deb'},
  {'os': 'umaverick',   'ver': '0.7', 'arch': 32, 'name': 'clementine_0.7.1~maverick_i386.deb'},
  {'os': 'umaverick',   'ver': '0.7', 'arch': 64, 'name': 'clementine_0.7.1~maverick_amd64.deb'},
  {'os': 'unatty',      'ver': '0.7', 'arch': 32, 'name': 'clementine_0.7.1~natty_i386.deb'},
  {'os': 'unatty',      'ver': '0.7', 'arch': 64, 'name': 'clementine_0.7.1~natty_amd64.deb'},
  {'os': 'squeeze',     'ver': '0.7', 'arch': 32, 'name': 'clementine_0.7.1~squeeze_i386.deb'},
  {'os': 'squeeze',     'ver': '0.7', 'arch': 64, 'name': 'clementine_0.7.1~squeeze_amd64.deb'},
  {'os': 'fedora',      'ver': '0.7', 'arch': 32, 'name': 'clementine-0.7.1-1.fc13.i686.rpm'},
  {'os': 'fedora',      'ver': '0.7', 'arch': 64, 'name': 'clementine-0.7.1-1.fc13.x86_64.rpm'},
  {'os': 'fedora14',    'ver': '0.7', 'arch': 32, 'name': 'clementine-0.7.1-1.fc14.i686.rpm'},
  {'os': 'fedora14',    'ver': '0.7', 'arch': 64, 'name': 'clementine-0.7.1-1.fc14.x86_64.rpm'},
  {'os': 'windows',     'ver': '0.7', 'arch': 0,  'name': 'ClementineSetup-0.7.1.exe'},
  {'os': 'snowleopard', 'ver': '0.7', 'arch': 0,  'name': 'clementine-0.7.1.dmg'},
  {'os': 'source',      'ver': '0.7', 'arch': 0,  'name': 'clementine-0.7.1.tar.gz'},
  
  {'os': 'ubuntu',      'ver': '0.6', 'arch': 32, 'name': 'clementine_0.6~lucid_i386.deb'},
  {'os': 'ubuntu',      'ver': '0.6', 'arch': 64, 'name': 'clementine_0.6~lucid_amd64.deb'},
  {'os': 'umaverick',   'ver': '0.6', 'arch': 32, 'name': 'clementine_0.6~maverick_i386.deb'},
  {'os': 'umaverick',   'ver': '0.6', 'arch': 64, 'name': 'clementine_0.6~maverick_amd64.deb'},
  {'os': 'squeeze',     'ver': '0.6', 'arch': 32, 'name': 'clementine_0.6~squeeze_i386.deb'},
  {'os': 'squeeze',     'ver': '0.6', 'arch': 64, 'name': 'clementine_0.6~squeeze_amd64.deb'},
  {'os': 'fedora',      'ver': '0.6', 'arch': 32, 'name': 'clementine-0.6.fc13.i686.rpm'},
  {'os': 'fedora',      'ver': '0.6', 'arch': 64, 'name': 'clementine-0.6.fc13.x86_64.rpm'},
  {'os': 'windows',     'ver': '0.6', 'arch': 0,  'name': 'ClementineSetup-0.6.exe'},
  {'os': 'snowleopard', 'ver': '0.6', 'arch': 0,  'name': 'clementine-0.6.dmg'},
  {'os': 'source',      'ver': '0.6', 'arch': 0,  'name': 'clementine-0.6.tar.gz'},

  {'os': 'ubuntu',      'ver': '0.5', 'arch': 32, 'name': 'clementine_0.5.3~lucid_i386.deb'},
  {'os': 'ubuntu',      'ver': '0.5', 'arch': 64, 'name': 'clementine_0.5.3~lucid_amd64.deb'},
  {'os': 'umaverick',   'ver': '0.5', 'arch': 32, 'name': 'clementine_0.5.3~maverick_i386.deb'},
  {'os': 'umaverick',   'ver': '0.5', 'arch': 64, 'name': 'clementine_0.5.3~maverick_amd64.deb'},
  {'os': 'fedora',      'ver': '0.5', 'arch': 32, 'name': 'clementine-0.5.3.fc13.i686.rpm'},
  {'os': 'fedora',      'ver': '0.5', 'arch': 64, 'name': 'clementine-0.5.3.fc13.x86_64.rpm'},
  {'os': 'windows',     'ver': '0.5', 'arch': 0,  'name': 'ClementineSetup-0.5.3.exe'},
  {'os': 'snowleopard', 'ver': '0.5', 'arch': 0,  'name': 'clementine-0.5.3.dmg'},
  {'os': 'source',      'ver': '0.5', 'arch': 0,  'name': 'clementine-0.5.3.tar.gz'},

  {'os': 'ubuntu',      'ver': '0.4', 'arch': 32, 'name': 'clementine_0.4_i386.deb'},
  {'os': 'ubuntu',      'ver': '0.4', 'arch': 64, 'name': 'clementine_0.4_amd64.deb'},
  {'os': 'fedora',      'ver': '0.4', 'arch': 32, 'name': 'clementine-0.4-1.fc12.i686.rpm'},
  {'os': 'fedora',      'ver': '0.4', 'arch': 64, 'name': 'clementine-0.4-1.fc12.x86_64.rpm'},
  {'os': 'windows',     'ver': '0.4', 'arch': 0,  'name': 'ClementineSetup-0.4.exe'},
  {'os': 'snowleopard', 'ver': '0.4', 'arch': 0,  'name': 'clementine-0.4.1.dmg'},
  {'os': 'leopard',     'ver': '0.4', 'arch': 0,  'name': 'clementine-0.4-Leopard.dmg'},
  {'os': 'source',      'ver': '0.4', 'arch': 0,  'name': 'clementine-0.4.2.tar.gz'},

  {'os': 'ubuntu',      'ver': '0.3', 'arch': 32, 'name': 'clementine_0.3_i386.deb'},
  {'os': 'ubuntu',      'ver': '0.3', 'arch': 64, 'name': 'clementine_0.3_amd64.deb'},
  {'os': 'fedora',      'ver': '0.3', 'arch': 32, 'name': 'clementine-0.3-1.fc12.i686.rpm'},
  {'os': 'fedora',      'ver': '0.3', 'arch': 64, 'name': 'clementine-0.3-1.fc12.x86_64.rpm'},
  {'os': 'windows',     'ver': '0.3', 'arch': 0,  'name': 'ClementineSetup-0.3.exe'},
  {'os': 'leopard',     'ver': '0.3', 'arch': 0,  'name': 'clementine-0.3.2.dmg'},
  {'os': 'source',      'ver': '0.3', 'arch': 0,  'name': 'clementine-0.3.tar.gz'},

  {'os': 'ubuntu',      'ver': '0.2', 'arch': 32, 'name': 'clementine_0.2_i386.deb'},
  {'os': 'ubuntu',      'ver': '0.2', 'arch': 64, 'name': 'clementine_0.2_amd64.deb'},
  {'os': 'fedora',      'ver': '0.2', 'arch': 32, 'name': 'clementine-0.2-1.fc12.i686.rpm'},
  {'os': 'fedora',      'ver': '0.2', 'arch': 64, 'name': 'clementine-0.2-1.fc12.x86_64.rpm'},
  {'os': 'windows',     'ver': '0.2', 'arch': 0,  'name': 'ClementineSetup-0.2.exe'},
  {'os': 'leopard',     'ver': '0.2', 'arch': 0,  'name': 'clementine-0.2.1_beta1.dmg'},
  {'os': 'source',      'ver': '0.2', 'arch': 0,  'name': 'clementine-0.2-1.tar.gz'},

  {'os': 'ubuntu',      'ver': '0.1', 'arch': 32, 'name': 'clementine_0.1-6_i386.deb'},
  {'os': 'ubuntu',      'ver': '0.1', 'arch': 64, 'name': 'clementine_0.1-6_amd64.deb'},
  {'os': 'fedora',      'ver': '0.1', 'arch': 32, 'name': 'clementine-0.1-5.fc12.i686.rpm'},
  {'os': 'fedora',      'ver': '0.1', 'arch': 64, 'name': 'clementine-0.1-5.fc12.x86_64.rpm'},
  {'os': 'windows',     'ver': '0.1', 'arch': 0,  'name': 'clementine-0.1-6.zip'},
  {'os': 'leopard',     'ver': '0.1', 'arch': 0,  'name': 'clementine-0.1-2.dmg'},
  {'os': 'source',      'ver': '0.1', 'arch': 0,  'name': 'clementine-0.1.tar.gz'},
]
DISPLAY_OS = {
  'source':      _('Source code'),
  'ubuntu':      'Ubuntu Lucid (10.04)',
  'umaverick':   'Ubuntu Maverick (10.10)',
  'unatty':      'Ubuntu Natty (11.04)',
  'uoneiric':    'Ubuntu Oneiric (11.10)',
  'uprecise':    'Ubuntu Precise (12.04)',
  'uquantal':    'Ubuntu Quantal (12.10)',
  'squeeze':     'Debian Squeeze',
  'fedora':      'Fedora 13',
  'fedora14':    'Fedora 14',
  'fedora15':    'Fedora 15',
  'fedora16':    'Fedora 16',
  'fedora17':    'Fedora 17',
  'windows':     'Windows',
  'leopard':     'Mac OS X Leopard',
  'snowleopard': 'Mac OS X Snow Leopard',
}
SHORT_DISPLAY_OS = {
  'source':      _('Source'),
  'ubuntu':      'Lucid',
  'umaverick':   'Maverick',
  'unatty':      'Natty',
  'uoneiric':    'Oneiric',
  'uprecise':    'Precise',
  'uquantal':    'Quantal',
  'squeeze':     'Squeeze',
  'fedora':      'Fedora 13',
  'fedora14':    'Fedora 14',
  'fedora15':    'Fedora 15',
  'fedora16':    'Fedora 16',
  'fedora17':    'Fedora 17',
  'windows':     'Windows',
  'leopard':     'Mac OS X',
  'snowleopard': 'Mac OS X',
}
OS_LOGOS = {
  'source':      'source-logo.png',
  'ubuntu':      'ubuntu-logo.png',
  'umaverick':   'ubuntu-logo.png',
  'unatty':      'ubuntu-logo.png',
  'uoneiric':    'ubuntu-logo.png',
  'uprecise':    'ubuntu-logo.png',
  'uquantal':    'ubuntu-logo.png',
  'squeeze':     'squeeze-logo.png',
  'fedora':      'fedora-logo.png',
  'fedora14':    'fedora-logo.png',
  'fedora15':    'fedora-logo.png',
  'fedora16':    'fedora-logo.png',
  'fedora17':    'fedora-logo.png',
  'windows':     'windows-logo.png',
  'leopard':     'leopard-logo.png',
  'snowleopard': 'leopard-logo.png',
}
NEWS = [
  {
    'timestamp': 1269302400,
    'title': _('Version 0.2 released'),
    'content': _("It's been just over a month since we released the first version " \
      "of Clementine. This new version features album cover-art, better " \
      '"Various Artists" detection, support for loading playlists, and much more.')
  },
  {
    'timestamp': 1273276800,
    'title': _('Version 0.3 released'),
    'content': _("In this release we've switched to GStreamer on all platforms, " \
      'meaning the analyzer and crossfading between tracks will now work on ' \
      'Windows. New features include an equalizer, more library grouping ' \
      'options, a nicer OSD, remote control from command-line and MPRIS, and ' \
      'easier tag editing.')
  },
  {
    'timestamp': 1277769600,
    'title': _('Version 0.4 released'),
    'content': _('This release features tabbed playlists, playlist search, ' \
      'projectM visualisations, Magnatune integration, ReplayGain volume ' \
      "normalisation and music transcoding. We've fixed loads of bugs too - " \
      'searching large libraries is now much faster, playback is much more ' \
      'reliable on Windows, character encoding problems are fixed, and remote ' \
      'playlists should load correctly all the time.')
  },
  {
    'timestamp': 1284821496,
    'title': _('Version 0.5 released'),
    'content': _('This release adds support for using portable devices with ' \
      'Clementine.  You can now copy songs to your iPod, iPhone, MTP, or ' \
      'USB mass storage device.  See <a href="http://code.google.com/p/clementine-player/wiki/PortableDevices">' \
      'the wiki for more information</a>.  Support for using a ' \
      '<a href="http://code.google.com/p/clementine-player/wiki/WiiRemotes">' \
      'Wii Remote</a> as a remote control has been added.  Other ' \
      'features include a Queue Manager, an Organise Files dialog, automatically ' \
      'stretching columns in the playlist, loading embedded id3v2 cover art, ' \
      'more library scanning options, drag and drop between playlists, and a ' \
      'hypnotoad.  We\'ve also reduced startup time by more than half, fixed ' \
      'a load of memory leaks and reduced CPU usage while playing music. ' \
      'See the <a href="http://code.google.com/p/clementine-player/source/browse/Changelog">' \
      'full changelog</a> for more information.')
  },
  {
    'timestamp': 1292089537,
    'title': _('Version 0.6 released'),
    'content': _('This release features two new information panes that show ' \
      'lyrics, song statistics, artist biographies, photos and lists of tags ' \
      "and similar artists.  We've redesigned the sidebar (although you can " \
      'switch back by right clicking on it), and also added ratings, play ' \
      'counts and skip counts.  You can create smart and dynamic playlists ' \
      'from songs in your library, and also now listen to music from ' \
      '<a href="http://www.jamendo.com/">Jamendo</a> and Icecast radio stations. ' \
      'See the <a href="http://code.google.com/p/clementine-player/source/browse/Changelog">' \
      'full changelog</a> for more information.')
  },
  {
    'timestamp': 1301245565,
    'title': _('Version 0.7 released'),
    'content': _('In this release Clementine gains a brand new edit tag dialog ' \
      'with autocompletion and the ability to automatically identify music and ' \
      'fetch missing tags from MusicBrainz.  CUE sheets are now supported - ' \
      'they are detected automatically when scanning your library and each track ' \
      "will show up separately.  We've made a load of smaller improvements " \
      'as well such as showing album covers in the Library tab, greying out deleted ' \
      'songs, a "Show in file browser" option, support for network proxies, ' \
      'a "Full library rescan" option, and a new tooltip for the track slider ' \
      'that helps you seek more accurately to a specific place in a song. ' \
      'See the <a href="http://code.google.com/p/clementine-player/source/browse/Changelog">' \
      'full changelog</a> for more information.')
  },
  {
    'timestamp': 1325009906,
    'title': _('Version 1.0 released'),
    'content': _('This release adds <a href="http://www.spotify.com">Spotify</a>, ' \
      '<a href="http://grooveshark.com">Grooveshark</a> and ' \
      '<a href="http://www.sky.fm/">SKY.fm</a>/<a href="http://www.di.fm/">Digitally Imported</a> ' \
      'support.  We\'ve also added a Global Search feature that allows you to ' \
      'easily find music that\'s either in your library or on the Internet. ' \
      'Other features include audio CD support, more transcoder options, an ' \
      'improved settings dialog, smarter album cover searches, and loads of bug fixes. ' \
      'See the <a href="http://code.google.com/p/clementine-player/source/browse/Changelog?name=release-1.0">' \
      'full changelog</a> for more information.')
  },
  {
    'timestamp': 1351141875,
    'title': _('Version 1.1 released'),
    'content': _('This release adds long-awaited Podcast support including ' \
      'integration and synchronisation with <a href="//gpodder.net">gpodder.net</a>. ' \
      'Music from <a href="http://soundcloud.com/">Soundcloud</a> and ' \
      '<a href="http://www.jazzradio.com/">jazzradio.com</a> is available in ' \
      'the Internet tab in the sidebar, as well as any songs you\'ve uploaded ' \
      'to <a href="http://drive.google.com/start">Google Drive</a>. ' \
      'Clementine will also now show moodbars for the music you play from your ' \
      'local disc. ' \
      'See the <a href="http://code.google.com/p/clementine-player/source/browse/Changelog?name=release-1.1">' \
      'full changelog</a> for more information.')
  },
  # For timestamp: python -c "import time; print int(time.time())"
]
LANGUAGES = [
  "de", "en", "hu", "it", "pt", "ru", "sk", "es", "fr", "pt_br", "sv", "uk",
  "vi", "sl", "fi", "br", "tr_tr", "ca", "hr", "lt", "cs", "el", "ka", "uz",
  "eu", "nl", "pl", "zh_cn", "da", "af", "be", "ko", "ja", "ga", "bg", "zh_tw",
]

LANGUAGE_NAMES = {
  "ab": u"Abkhazian",
  "om": u"Afan",
  "aa": u"Afar",
  "af": u"Afrikaans",
  "sq": u"Albanian",
  "am": u"Amharic",
  "ar": u"Arabic",
  "hy": u"Armenian",
  "as": u"Assamese",
  "ay": u"Aymara",
  "az": u"Azerbaijani",
  "ba": u"Bashkir",
  "eu": u"Euskara",
  "bn": u"Bengali",
  "dz": u"Bhutani",
  "bh": u"Bihari",
  "bi": u"Bislama",
  "br": u"Brezhoneg",
  "bg": u"български език",
  "my": u"Burmese",
  "be": u"беларуская мова",
  "km": u"Cambodian",
  "ca": u"Català",
  "zh": u"Chinese",
  "zh_cn": u"中文",
  "zh_tw": u"繁體字",
  "co": u"Corsican",
  "hr": u"hrvatski",
  "cs": u"čeština",
  "da": u"Dansk",
  "nl": u"Nederlands",
  "en": u"English",
  "eo": u"Esperanto",
  "es": u"Español",
  "et": u"eesti",
  "fo": u"Faroese",
  "fj": u"Fiji",
  "fi": u"Suomi",
  "fr": u"Français",
  "fy": u"Frisian",
  "gd": u"Gaelic",
  "gl": u"Galician",
  "ka": u"ქართული",
  "de": u"Deutsch",
  "el": u"Ελληνικά",
  "kl": u"Greenlandic",
  "gn": u"Guarani",
  "gu": u"Gujarati",
  "ha": u"Hausa",
  "he": u"Hebrew",
  "hi": u"Hindi",
  "hu": u"Magyar",
  "is": u"Icelandic",
  "id": u"Indonesian",
  "ia": u"Interlingua",
  "ie": u"Interlingue",
  "iu": u"Inuktitut",
  "ik": u"Inupiak",
  "ga": u"Irish",
  "it": u"Italiano",
  "ja": u"日本語",
  "jv": u"Javanese",
  "kn": u"Kannada",
  "ks": u"Kashmiri",
  "kk": u"Kazakh",
  "rw": u"Kinyarwanda",
  "ky": u"Kirghiz",
  "ko": u"한국말",
  "ku": u"Kurdish",
  "rn": u"Kurundi",
  "lo": u"Laothian",
  "la": u"Latin",
  "lv": u"Latvian",
  "ln": u"Lingala",
  "lt": u"lietuvių",
  "mk": u"Macedonian",
  "mg": u"Malagasy",
  "ms": u"Malay",
  "ml": u"Malayalam",
  "mt": u"Maltese",
  "mi": u"Maori",
  "mr": u"Marathi",
  "mo": u"Moldavian",
  "mn": u"Mongolian",
  "na": u"Nauru",
  "ne": u"Nepali",
  "nb": u"Norwegian",
  "oc": u"Occitan",
  "or": u"Oriya",
  "ps": u"Pashto",
  "fa": u"Persian",
  "pl": u"polski",
  "pt": u"Português",
  "pt_br": u"Português Brasileiro",
  "pa": u"Punjabi",
  "qu": u"Quechua",
  "rm": u"RhaetoRomance",
  "ro": u"Romanian",
  "ru": u"Русский",
  "sm": u"Samoan",
  "sg": u"Sangho",
  "sa": u"Sanskrit",
  "sr": u"Serbian",
  "sh": u"SerboCroatian",
  "st": u"Sesotho",
  "tn": u"Setswana",
  "sn": u"Shona",
  "sd": u"Sindhi",
  "si": u"Singhalese",
  "ss": u"Siswati",
  "sk": u"Slovenský",
  "sl": u"Slovenščina",
  "so": u"Somali",
  "su": u"Sundanese",
  "sw": u"Swahili",
  "sv": u"Svenska",
  "tl": u"Tagalog",
  "tg": u"Tajik",
  "ta": u"Tamil",
  "tt": u"Tatar",
  "te": u"Telugu",
  "th": u"Thai",
  "bo": u"Tibetan",
  "ti": u"Tigrinya",
  "to": u"Tonga",
  "ts": u"Tsonga",
  "tr": u"Türkçe",
  "tr_tr": u"Türkçe",
  "tk": u"Turkmen",
  "tw": u"Twi",
  "ug": u"Uigur",
  "uk": u"Українська",
  "ur": u"Urdu",
  "uz": u"O'zbek tili",
  "vi": u"Tiếng Việt",
  "vo": u"Volapuk",
  "cy": u"Welsh",
  "wo": u"Wolof",
  "xh": u"Xhosa",
  "yi": u"Yiddish",
  "yo": u"Yoruba",
  "za": u"Zhuang",
  "zu": u"Zulu",
  "nn": u"Nynorsk",
  "bs": u"Bosnian",
  "dv": u"Divehi",
  "gv": u"Manx",
  "kw": u"Cornish",
  "ak": u"Akan",
  "ig": u"Igbo",
  "ve": u"Venda",
  "ee": u"Ewe",
  "ny": u"Chewa",
  "ii": u"Sichuan Yi",
  "nr": u"South Ndebele",
  "se": u"Northern Sami",
  "ff": u"Fulah",
  "ki": u"Kikuyu",
  "nd": u"North Ndebele",
  "bm": u"Bambara",
  "lg": u"Ganda",
}
