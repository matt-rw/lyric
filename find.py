#!/usr/bin/env python
# For personal use only.

import argparse
import os
import sys

import requests
from bs4 import BeautifulSoup


def get_lyrics(artist: str, song: str) -> str | None:
    """Fetch lyrics with HTTP request.

    :param artist: Artist name with no spaces or caps.
    :param song: Song name with no spaces or caps.

    :return: String of lyrics if found, otherwise None.
    """
    base_url = 'https://www.azlyrics.com/lyrics/'

    source = requests.get(f'{base_url}/{artist}/{song}.html')
    soup = BeautifulSoup(source.text, 'html.parser')
    try:
        lyrics = soup.find('b').find_next('b').find_next('div')
    except AttributeError:
        return None

    return lyrics.get_text()


def format_name(name: str) -> str:
    """Format name for URL query.

    :param name:
    
    :return: String with replaced characters.
    """
    replacements = [' ', '.', ',', '-', ')', '(']
    replaced = ''
    for char in name:
        if char in replacements:
            continue
        replaced += char.lower()


def parse_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            'Tool to display song lyrics in a tty.\n\n'
            'examples:\n'
            '  find.py "Creedence Clearwater Revival" "Green River"\n'
            '  find.py creedenceclearwaterrevival greenriver\n'
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('artist', help='artist name')
    parser.add_argument('song', help='song name')
    parser.add_argument(
        '-f',
        '--file',
        action='store_true',
        help='save lyrics to text file'
    )
    parser.add_argument(
        '-t',
        '--title',
        action='store_true',
        help='add title of artist and song, as provided'
    )
    args = parser.parse_args()
    
    args.f_artist = format_name(args.artist)
    args.f_song = format_name(args.song)
    
    return args


if __name__ == '__main__':
    args = parse_args()
    lyrics = get_lyrics(args.f_artist, args.f_song)
    if not lyrics:
        print(f'Failed to find \'{args.song}\' by {args.artist}')
        sys.exit(1)
    if args.title:
        lyrics = f'{args.song} - {args.artist}\n{lyrics}'
    if args.file:
        file_path = f'{args.f_artist}-{args.f_song}.txt'
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(lyrics)
            print(f'Saved lyrics to \'{os.path.abspath(file.name)}\'')
    else:
        print(lyrics)
