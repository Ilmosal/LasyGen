#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python script for generating a latex document of lyrics for academic table parties.

Copyright Ilmo Salmenpera 2017
"""
import sys
import os

doc_root =  [
                "\documentclass[8pt]{extarticle}",
                "\usepackage[a5paper]{geometry}",
                "\usepackage[utf8]{inputenc}",
                "\usepackage[english]{babel}",
                "",
                "\usepackage{multicol}",
                "\setlength{\columnsep}{1cm}",
                "\setlength{\parindent}{0pt}",
                "",
                "\\begin{document}",
                "\\begin{multicols}{2}",
                "\\begin{flushleft}",
            ]

doc_end =   [
                "\end{flushleft}",
                "\end{multicols}",
                "\end{document}"
            ]

class Song:
    """
    Class for a song
    """
    def __init__(self, name, org_song, lyrics):
        self.name = name
        self.org_song = org_song
        self.lyrics = lyrics


def readSongs(path_to_folder):
    """
    Function that receives a folder as a parameter and reads all files in it and returns them as song objects
    
    Args:
        path_to_folder(str): path to the folder containing the songs

    Returns:
        list of song objects
    """
    files = os.listdir(path_to_folder)
    files.reverse()
    songs = []
    for file_name in files:
        f_song = open(path_to_folder + file_name, 'r')
        song_name = f_song.readline().strip()
        org_song = f_song.readline().strip()
        if org_song[0] == "-":
            org_song = None
        else:
            f_song.readline()
        lyrics = []
        for line in f_song:
            lyrics.append(line.strip())
        songs.append(Song(song_name, org_song, lyrics))

    return songs

def createLasy(songs):
    """
    Function for creating the whole document and pasteing it into the folder of the user.
    """
    lasy = doc_root
    song_numb = 1
    lasy.append("")
    for song in songs:
        title = "{0:02d}. {1}".format(song_numb, song.name)
        lasy.append("   \\textbf{" + title + "}")
        if song.org_song is not None:
            lasy.append("   " + song.org_song + "\\\\")
        lasy.append("   \leavevmode\\\\")
        for line in song.lyrics:
            if line == "":
                lasy.append("   \leavevmode\\\\")
            else:
                lasy.append("   " +line + "\\\\") 
        lasy.append("   \leavevmode\\\\")
        lasy.append(" ")
        song_numb += 1

    for line in doc_end:
        lasy.append(line)

    f_open = open("lasy.tex", "w")
    for line in lasy:
        f_open.write(line + "\n")

def main():
    if len(sys.argv) < 2:
        print("No song directory given for the program! Give the folder containing the files for the program as an argument!")
    else:
        songs = readSongs(sys.argv[1])
        createLasy(songs)

if __name__ == "__main__":
    main()
