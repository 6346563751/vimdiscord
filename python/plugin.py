import logging
import time
import vim

import rpc

logger = logging.getLogger(__name__)
logger.setLevel(20)

#START_TIME = int(time.time())

BASE_ACTIVITY = {
    'details': 'Idle',
    #'timestamps': {
    #    'start': START_TIME
    # },
    'assets': {
        'large_text': 'Vim',
        'large_image': 'vim_logo',
        'small_text': 'Best editeur :)',
        'small_image': 'https://github.com/vbe0201/vimdiscord'
     }
 }

CLIENT_ID = '589111267986243624'

thumbnails = {
    'html': 'HTML',
    'css': 'CSS',
    'js': 'JavaScript',
    'php': 'PHP',
    'scss': 'Sass',
    'py': 'Python',
    'rs': 'Rust',
    'c': 'C',
    'h': 'C Header',
    'cpp': 'C++',
    'hpp': 'C++ Header',
    'cxx': 'C++',
    'cc': 'C++',
    'cs': 'C#',
    'capnp': "Cap'n' Proto",
    'java': 'Java',
    'ex': 'Elixir',
    'md': 'Markdown',
    'ts': 'TypeScript',
    'go': 'Go',
    'kt': 'Kotlin',
    'kts': 'Kotlin',
    'cr': 'Crystal',
    'rb': 'Ruby',
    'clj': 'Clojure',
    'hs': 'Haskell',
    'json': 'JSON',
    'vue': 'Vue',
    'groovy': 'Groovy',
    'swift': 'Swift',
    'lua': 'Lua',
    'jl': 'Julia',
    'dart': 'Dart',
    'pp': 'Pascal',
}


def get_filename():
    return vim.eval('expand("%:t")')


def get_extension():
    return vim.eval('expand("%:e")')


def get_cwd():
    return vim.eval('getcwd()')


def update_presence(connection):
    if rpc.connection_closed:
        rpc.close(connection)
        logger.error('Connection to Discord closed.')
        return

    activity = BASE_ACTIVITY
    filename = get_filename()
    cwd = get_cwd()
    if not filename or not cwd:
        return
    
    activity['details'] = 'Fichier :' + cwd
    activity['assets']['small_text'] = 'https://github.com/vbe0201/vimdiscord'

    extension = get_extension()
    if extension and extension in thumbnails.keys():
        activity['assets']['large_image'] = extension
        activity['assets']['large_text'] = 'Langage : {}'.format(thumbnails[extension])
        activity['details'] = 'Fichier : {}'.format(cwd)
    else:
        activity['details'] = 'Fichier : {}'.format(cwd)
        activity['assets']['large_image'] = 'unknown'

    try:
        rpc.set_activity(connection, activity)
    except NameError:
        logger.error('Discord is not running!')
    except BrokenPipeError:
        logger.error('Connection to Discord lost!')
