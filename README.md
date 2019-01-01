# merge midi file as tracks in python
Merge two midi file into a single file with two tracks.

## Install dependencies
`
pip install midiutil mido
`

## Usage
`
from merge_midi import merge  
    
merge('A.mid', 'B.mid', 'new_song.mid', bpm=120)
`
