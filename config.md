# Auto Leech Deck Config

## Assigning a Leech Deck

#### Use the pattern {"Deck": "Sub-Deck"} (JSON Format):

&nbsp;&nbsp;&nbsp;&nbsp;`{`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"Deck": "Leech Deck",`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"Another Deck": "Another Leech Deck",`  
&nbsp;&nbsp;&nbsp;&nbsp;`}`

##### Can add as many assignments as needed and also have multiple decks assigned to the same leech deck.

## Using Sub-Decks

#### Insert two colons between the parent deck and its sub-deck when setting its value:

&nbsp;&nbsp;&nbsp;&nbsp;`{`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"Main Deck": "Main Deck::Sub-Deck",`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"Another Deck": "Main Deck::Sub-Deck"`  
&nbsp;&nbsp;&nbsp;&nbsp;`}`

## Setting a Default Leech Deck

#### Set the deck to the "##Default" key:

&nbsp;&nbsp;&nbsp;&nbsp;`{ "##Default": "Default Leech Deck" }`

##### This is where leeched cards get put if there's no leech deck assigned to the main deck.

## Disabling Auto-Movement for a Deck

#### Set the leech deck to the main deck or you can make it blank:

&nbsp;&nbsp;&nbsp;&nbsp;`{ "Static Deck": "Static Deck" }`  
&nbsp;&nbsp;&nbsp;&nbsp;`{ "Static Deck": "" }`

## Disabling Auto-Movement to the Default Leech Deck

#### Set the "##Default" key to a blank value:

&nbsp;&nbsp;&nbsp;&nbsp;`{ "##Default": "" }`

##### This cancels movement to the default deck for any decks that don't have a leech deck already set.

---

<center><a href="https://github.com/iamjustkoi/AutoLeechDeck"><img src="../../addons21/auto_leech_deck/raw/GitHub-Mark-Light.png"></a>&nbsp;&nbsp;<a href="https://ko-fi.com/iamjustkoi"><img src="../../addons21/auto_leech_deck/raw/kofilogo_blue.png"></a>&nbsp;&nbsp;<a href="https://www.patreon.com/iamjustkoi"><img src="../../addons21/auto_leech_deck/raw/patreon.png"></a></center>



