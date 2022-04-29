# Auto Leech Deck

## Assigning a Leech Deck
#### Use the pattern {"Deck": "Sub-Deck"} (JSON Format):
&nbsp;&nbsp;&nbsp;&nbsp;``{`` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``"Deck": "Leech Deck",`` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``"Another Deck": "Another Leech Deck",`` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``"Etc": "Leech Deck (can be used more than once)"`` <br>
&nbsp;&nbsp;&nbsp;&nbsp;``}``<br>

## Using Sub-Decks
#### Insert two colons between the parent deck and its sub-deck when setting its value:
&nbsp;&nbsp;&nbsp;&nbsp;``{``<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``"Main Deck": "Main Deck::Sub-Deck",``<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``"Another Deck": "Main Deck::Sub-Deck"``<br>
&nbsp;&nbsp;&nbsp;&nbsp;``}``<br>

## Setting a Default Leech Deck
#### Set the deck to the "##Default" key:
&nbsp;&nbsp;&nbsp;&nbsp;``{ "##Default": "Default Leech Deck" }``<br>
##### This is where leeched cards get put if there's no leech deck assigned to the main deck.

## Disabling Auto-Movement for a Deck
#### Set the leech deck to the main deck or you can make it blank:
&nbsp;&nbsp;&nbsp;&nbsp;``{ "Static Deck": "Static Deck" }``<br>
<!-- ### &nbsp;&nbsp;&nbsp;&nbsp;Alternative method: -->
&nbsp;&nbsp;&nbsp;&nbsp;``{ "Static Deck": "" }``<br>

## Disabling Auto-Movement to the Default Leech Deck
#### Set the "##Default" key to a blank value:
&nbsp;&nbsp;&nbsp;&nbsp;``{ "##Default": "" }``<br>
##### This cancels movement to the default deck for any decks that don't have a leech deck already set.

