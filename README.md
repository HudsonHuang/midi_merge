# merge midi tracks in python

## Install dependencies
`
pip install midiutil mido
`

## Usage
`
from merge_midi import merge  
    
merge('A.mid', 'B.mid', 'new_song.mid', bpm=120)
`
