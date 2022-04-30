# Auto Leech Deck
Add-on for Anki that automatically moves cards to user-assigned decks as soon as they're leeched.  
Supports Anki 2.1+.  

## Installation
Can be installed from the add-on page on [Ankiweb](https://ankiweb.net).  

> 1122334 (I Am Just A Placeholder)

Or by pasting these numbers into Anki (Tools -> Add-ons -> Get Add-ons...).

## How To Use

To assign decks or make any changes you can either edit the add-on's config file or go to a deck's legacy options window (Shift-clicking on "Options") and assigning a deck there.  

The options menu input uses the same formatting as assigning the deck in the config, except without any quotes/brackets (e.g. things like "Leech Deck", "Parent::Child", etc.)

Also, quick note, the decks get saved using their ID's instead of their names, so renaming or moving them shouldn't break any assignments.

### Assigning a Leech Deck
#### Use the pattern {"Deck": "Sub-Deck"} (JSON Format):
```json
{
    "Deck": "Leech Deck",
    "Another Deck": "Another Leech Deck",
}
```
##### It's possible to add as many leech decks as you might want, and multiple decks can be assigned  the same leech deck too.

### Using Sub-Decks
#### Insert two colons between the parent deck and its sub-deck:
```json
{
    "Main Deck": "Main Deck::Sub-Deck",
    "Another Deck": "Main Deck::Sub-Deck"
}
```

### Setting a Default Leech Deck
#### Place the deck in the "##Default" key:
```json
{ "##Default": "Default Leech Deck" }
```
##### Cards get put into the default deck if a parent deck doesn't have a leech deck assigned to it or leech movement is disabled in some way.

### Disabling Auto-Movement for a Deck
#### Set the leech deck to itself or you can make it a blank assignment:
```json
{ "Static Deck": "Static Deck" }
```
```json
{ "Static Deck": "" }
```

### Disabling Auto-Movement to the Default Leech Deck
#### Set the "##Default" key to a blank value:
```json
{ "##Default": "" }
```
##### This cancels all movement by default, unless a deck gets assigned its own leech deck to move to. <br><br>

Best of luck, have fun!

<div align="center">Socials/Support:</div><br>

<div align="center"><a href="https://github.com/iamjustkoi/AutoLeechDeck"><img src="https://i.imgur.com/O9GP8el.png"></a>&nbsp;&nbsp;<a href="https://twitter.com/home"><img src="https://i.imgur.com/EcvLG65.png"></a>&nbsp;&nbsp;<a href="https://ko-fi.com/iamjustkoi"><img src="https://i.imgur.com/9LyzzhD.png"></a>&nbsp;&nbsp;<a href="https://i.imgur.com/EUX61X3.png"><img src="https://i.imgur.com/0iuIV8b.png"></a></div>