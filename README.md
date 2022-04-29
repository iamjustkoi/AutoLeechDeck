# Auto Leech Deck
Add-on for Anki that automatically moves cards to user-assigned decks as soon as they're leeched.  
Supports Anki 2.1+.  

## Installation
Can be installed from the add-on page on [Ankiweb](https://ankiweb.net).  

> 1122334 (I Am Just A Placeholder)

Or by pasting these numbers into Anki (Tools -> Add-ons -> Get Add-ons...).

## How To Use

To assign decks or make any changes you can either edit the add-on's config file or go to a deck's legacy options window (Shift-clicking on "Options") and assigning a deck there.  

The options menu input uses the same formatting as assigning the deck in the config, except without any quotes or brackets (e.g. "Assigned Deck, Parent::Child, etc.")

Also, the decks get saved using ID's instead of their names, so renaming or moving them shouldn't break of these settings.

### Assigning a Leech Deck
#### Use the pattern {"Deck": "Sub-Deck"} (JSON Format):
```json
{
    "Deck": "Leech Deck",
    "Another Deck": "Another Leech Deck",
}
```
##### Can add as many assignments as needed and also have multiple decks assigned to the same leech deck.

### Using Sub-Decks
#### Insert two colons between the parent deck and its sub-deck when setting its value:
```json
{
    "Main Deck": "Main Deck::Sub-Deck",
    "Another Deck": "Main Deck::Sub-Deck"
}
```

### Setting a Default Leech Deck
#### Set the deck to the "##Default" key:
```json
{ "##Default": "Default Leech Deck" }
```
##### This is where leeched cards get put if there's no leech deck assigned to the main deck.

### Disabling Auto-Movement for a Deck
#### Set the leech deck to the main deck or you can make it blank:
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
##### This cancels movement to the default deck for any decks that don't have a leech deck already set.  

Good luck, have fun!
