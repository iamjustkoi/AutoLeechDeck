# Auto Leech Deck Config

## Assigning a Leech Deck

#### Use the pattern {"Deck": "Sub-Deck"} (JSON Format):

&nbsp;&nbsp;&nbsp;&nbsp;`{`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"Deck": "Leech Deck",`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"Another Deck": "Another Leech Deck",`  
&nbsp;&nbsp;&nbsp;&nbsp;`}`

##### It's possible to add as many leech decks as you might want, and multiple decks can be assigned  the same leech deck too.

## Using Sub-Decks

#### Insert two colons between the parent deck and its sub-deck:

&nbsp;&nbsp;&nbsp;&nbsp;`{`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"Main Deck": "Main Deck::Sub-Deck",`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"Another Deck": "Main Deck::Sub-Deck"`  
&nbsp;&nbsp;&nbsp;&nbsp;`}`

## Setting a Default Leech Deck

#### Place the deck in the "##Default" key:

&nbsp;&nbsp;&nbsp;&nbsp;`{ "##Default": "Default Leech Deck" }`

##### Cards get put into the default deck if a parent deck doesn't have a leech deck assigned to it or leech movement is disabled in some way.

## Disabling Auto-Movement for a Deck

#### Set the leech deck to itself or you can make it a blank assignment:

&nbsp;&nbsp;&nbsp;&nbsp;`{ "Static Deck": "Static Deck" }`  
&nbsp;&nbsp;&nbsp;&nbsp;`{ "Static Deck": "" }`

## Disabling Auto-Movement to the Default Leech Deck

#### Set the "##Default" key to a blank value:

&nbsp;&nbsp;&nbsp;&nbsp;`{ "##Default": "" }`

##### This cancels all movement by default, unless a deck gets assigned its own leech deck to move to.
---
Please report any issues you run into on <a href="https://github.com/iamjustkoi/AutoLeechDeck/issues">Github</a>.  
<center>Socials/Support:</center><br>
<center><a href="https://github.com/iamjustkoi/AutoLeechDeck"><img src="../../addons21/auto_leech_deck/raw/GitHub-Mark-Light.png"></a>&nbsp;&nbsp;<a href="https://twitter.com/iamjustkoi"><img src="../../addons21/auto_leech_deck/raw/twitter-social.png"></a>&nbsp;&nbsp;<a href="https://ko-fi.com/iamjustkoi"><img src="../../addons21/auto_leech_deck/raw/kofilogo_blue.png"></a>&nbsp;&nbsp;<a href="https://www.patreon.com/iamjustkoi"><img src="../../addons21/auto_leech_deck/raw/patreon.png"></a></center>



