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
    Class for a song.
    """
    def __init__(self, name, org_song, song_num, lyrics):
        self.name = name
        self.org_song = org_song
        self.song_num = song_num
        self.lyrics = lyrics

    def __cmp__(self, other):
        return self.song_num > other.song_num

def sortSongs(songs):
    sorted_songs = []
    for i in range(1, 1+len(songs)):
        for song in songs:
            if song.song_num == i:
                sorted_songs.append(song)
    return sorted_songs

def readSongs(path_to_folder):
    """
    Function that receives a folder as a parameter and reads all files in it and returns them as song objects
    
    Args:
        path_to_folder(str): path to the folder containing the songs

    Returns:
        list of song objects
    """
    files = os.listdir(path_to_folder)
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
        try:
            song_num = int((file_name.split("/")[-1]).split("_")[0])
        except:
            print("Song name not in a correct format: {0}".format(filename.split("/")[-1]))
            sys.exit()
        
        songs.append(Song(song_name, org_song, song_num, lyrics))

    songs = sortSongs(songs)
   
    for s in songs:
        print("{0} - {1}".format(s.song_num, s.name))
 
    return songs

def createLasy(songs, book_name):
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

    f_open = open(book_name, "w")
    for line in lasy:
        f_open.write(line + "\n")

def main():
    if len(sys.argv) < 2:
        print("No song directory given for the program! Give the folder containing the files for the program as an argument!")
    elif len(sys.argv) < 3:
        print("no book name given to the program! Generating it as lasy.tex")
        songs = readSongs(sys.argv[1])
        createLasy(songs, "lasy.tex")
    else:
        songs = readSongs(sys.argv[1])
        createLasy(songs, sys.argv[2])
    

if __name__ == "__main__":
    main()
