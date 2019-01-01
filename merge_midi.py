# -*- coding: utf-8 -*-
"""
Created on Fri May 25 19:36:35 2018

@author: Hudson huang
"""
#!/usr/bin/env python

from midiutil import MIDIFile
from mido import MidiFile

def merge(mid_1_path, mid_2_path, mid_output_path, bpm=120):
    mid1 = MidiFile(mid_1_path)
    mid2 = MidiFile(mid_2_path)
    midx = MidiFile(type=2)
    
    for i, track in enumerate(mid1.tracks):
        print('Track {}: {}'.format(i, track.name))
        if i>0:
            midx.tracks.append(track)
    #    for msg in track:
    #        print(msg)
            
    for i, track in enumerate(mid2.tracks):
        print('Track {}: {}'.format(i, track.name))
        if i>0:
            midx.tracks.append(track)
    #    for msg in track:
    #        print(msg)
    
    midx.ticks_per_beat  = bpm*2
    midx.save(mid_output_path)

if __name__ == "__main__":
    merge('chrods.mid', 'drum.mid', 'new_song.mid', bpm=120)
