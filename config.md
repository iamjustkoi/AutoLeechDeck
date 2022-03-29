# Auto Leech Deck

### Placing a deck's leeches into a leech deck:

&nbsp;&nbsp;&nbsp;&nbsp;``{`` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``"Deck": "Leech Deck",`` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``"Another Deck": "Another Leech Deck",`` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``"Etc": "Leech Deck (can be used again)"`` <br>
&nbsp;&nbsp;&nbsp;&nbsp;``}``<br>

### Placing a deck's leeches into a leech sub-deck:

&nbsp;&nbsp;&nbsp;&nbsp;``{``<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``"Main Deck": "Main Deck::Sub-Deck",``<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``"Another Deck": "Main Deck::Sub-Deck"``<br>
&nbsp;&nbsp;&nbsp;&nbsp;``}``<br>

### Setting a default deck for leeches to be put in:
&nbsp;&nbsp;&nbsp;&nbsp;``{ "##Default": "Default Leech Deck" }``<br>

### Disabling leech-movement (including to the default deck):
&nbsp;&nbsp;&nbsp;&nbsp;``{ "Unmoving Deck": "" }``<br>
### &nbsp;&nbsp;&nbsp;&nbsp;Alternative method:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``{ "Unmoving Deck": "Unmoving Deck" }``<br>

### Disabling default leech-movement:
&nbsp;&nbsp;&nbsp;&nbsp;``{``~~`` "##Default": "Leeches" ``~~``}`` -> &nbsp;&nbsp;``{}`` &nbsp;&nbsp;✔<br>
### &nbsp;&nbsp;&nbsp;&nbsp;Alternative method:
&nbsp;&nbsp;&nbsp;&nbsp;``{"##Default": "" }``<br>


##### Can add/remove as many decks as needed.
##### Can disable moving leeches to the default deck by removing its assignment.

<!-- ![The San Juan Mountains are beautiful!](lofi_basic.png "San Juan Mountains") -->