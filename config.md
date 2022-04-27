# Auto Leech Deck

### Placing a Deck's Leeches Into a Leech Deck:
##### Assign with a "Deck: Sub-Deck" pattern using the JSON format, with commas splitting all, new key-value pairs.
&nbsp;&nbsp;&nbsp;&nbsp;``{`` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``"Deck": "Leech Deck",`` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``"Another Deck": "Another Leech Deck",`` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``"Etc": "Leech Deck (can be used more than once)"`` <br>
&nbsp;&nbsp;&nbsp;&nbsp;``}``<br>

### Placing a Deck's Leeches Into a Leech Sub-Deck:
##### Insert a double-colon between the parent deck and its sub-deck in the assignment.
&nbsp;&nbsp;&nbsp;&nbsp;``{``<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``"Main Deck": "Main Deck::Sub-Deck",``<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``"Another Deck": "Main Deck::Sub-Deck"``<br>
&nbsp;&nbsp;&nbsp;&nbsp;``}``<br>

### Setting a Default Deck for Leeches To Be Put In:
##### Assign the deck to the value "##Default".
##### This is the deck that will be used when no assignment is found for a deck.
&nbsp;&nbsp;&nbsp;&nbsp;``{ "##Default": "Default Leech Deck" }``<br>

### Disabling Leech-Deck Movement (including movement to the default deck):
##### Assign the deck back to itself or set it to an empty value.
&nbsp;&nbsp;&nbsp;&nbsp;``{ "Static Deck": "Static Deck" }``<br>
<!-- ### &nbsp;&nbsp;&nbsp;&nbsp;Alternative method: -->
&nbsp;&nbsp;&nbsp;&nbsp;``{ "Static Deck": "" }``<br>

### Disabling Default Leech-Movement:
##### Assign the default deck to an empty value.
&nbsp;&nbsp;&nbsp;&nbsp;``{ "##Default": "" }``<br>