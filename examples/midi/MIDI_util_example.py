# MIDI_util_example.py

from cedargrove_MIDI_util import *

note = 61
print('note_lexo helper (note-to-name, name-to-note)', note, note_lexo(note))

name = 'G#7'
print('note_lexo helper (note-to-name, name-to-note)', name, note_lexo(name))

note = 61
print('note_name helper (note-to-name)', note, note_name(note))

name = 'G#7'
print('name_note helper (name-to-note)', name, name_note(name))

note = 60
print('note_freq helper (name-to-frequency)', note, note_freq(note))

freq = 262
print('freq_note helper (frequency-to-name)', freq, freq_note(freq))
