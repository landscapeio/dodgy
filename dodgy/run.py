import re
import os
import mimetypes
import json
from dodgy.checks import check_file


IGNORE_PATHS = [re.compile(patt % {'sep': os.path.sep}) for patt in (
    r'(^|%(sep)s)\.[^\.]',   # ignores any files or directories starting with '.'
    r'^tests?%(sep)s?',
    r'%(sep)stests?(%(sep)s|$)',
)]


def list_files(start_path):
    filepaths = []
    for root, _, files in os.walk(start_path):
        for file_name in files:
            filepaths.append(os.path.join(root, file_name))
    return filepaths


def run_checks(directory):
    warnings = []

    filepaths = list_files(directory)
    for filepath in filepaths:
        relpath = os.path.relpath(filepath, directory)
        if any([ignore.search(relpath) for ignore in IGNORE_PATHS]):
            continue

        # this is a naive check to skip binary files, it's probably okay for now
        mimetype = mimetypes.guess_type(filepath)
        if mimetype[0] is None or not mimetype[0].startswith('text/'):
            continue

        for msg_parts in check_file(filepath):
            warnings.append({
                'path': relpath,
                'line': msg_parts[0],
                'code': msg_parts[1],
                'message': msg_parts[2]
            })

    return warnings


def run():
    warnings = run_checks(os.getcwd())
    print json.dumps({'warnings': warnings}, indent=2)


if __name__ == '__main__':
    run()
