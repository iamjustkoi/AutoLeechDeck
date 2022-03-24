"""
MIT License: Copyright (c) 2022 justkoi <https://github.com/iamjustkoi>
Full license text available in "LICENSE" file, located in the add-on's root directory.

Based on the "Anki Add-On Guide" <https://addon-docs.ankiweb.net/hooks-and-filters.html#legacy-hook-handling>.
as well as the add-on "ANTI-SUCK" <https://ankiweb.net/shared/info/1131698154> by Joseph Y.
"""

from anki.cards import Card
from anki.hooks import addHook
from aqt import mw, gui_hooks, deckconf
from PyQt5 import QtWidgets


# TODO: Add feedback, support, and github links to config pages


def getTransferDeckId(deck_name: str):
    """
        Getter method for the leech-deck id based on what value the deck-key holds in the addon's config file.

        :return: The transfer deck id for the input deck name, if found. <br>
         Otherwise: -1 for no key found, 0 for empty value found, or a 1 for "##Default" assignment found.
    """
    config = mw.addonManager.getConfig(__name__)
    config_deck_name = config.get(deck_name)
    default_deck_name = config.get('##Default')

    # Get deck id from config:
    transfer_did = -1
    # If config deck-value exists:
    if config_deck_name or config_deck_name == "":
        transfer_did = 0
        if config_deck_name != "" and config_deck_name != "##Default":
            transfer_did = mw.col.decks.id(config_deck_name)
        elif default_deck_name and config_deck_name == "##Default":
            transfer_did = 1

    print(f"LEECH MOVER: t-did: {transfer_did}"
          f", conf-dname: {str(config_deck_name)}"
          f", conf-def-dname: {str(default_deck_name)}")

    return transfer_did


def onLeech(card: Card):
    """
        Hook function that handles new leech-movement functions when the specified card is "leeched."

        :param card: Reference to card being added to the leech deck.
    """
    config = mw.addonManager.getConfig(__name__)
    key = mw.col.decks.current().get('name')

    transfer_did = getTransferDeckId(key)
    if transfer_did == (-1 or 1) and config["##Default"]:
        card.did = mw.col.decks.id(config["##Default"])
    elif transfer_did != 0:
        card.did = transfer_did

    # Scheduler handles updates for leech cards so opting not to call an update using "card.flush()".

    # If the card was also in a cram/custom study deck, set it back to its original deck and due date:
    card.odid = 0
    if card.odue:
        card.due = card.odue
        card.odue = 0


def updateDeckConfForm(conf: deckconf.DeckConf):
    """
    Hook-Function for when the legacy deck config is opened in Anki.

    Creates a form input label and edits its text to reflect current addon config settings.

    :param conf: Deck config object of the deck being configured.
    """
    config_form = conf.form

    leech_deck_label = QtWidgets.QLabel(config_form.tab_2)
    leech_deck_label.setObjectName("label_leech_deck")
    leech_deck_label.setText("Leech deck")
    config_form.gridLayout_2.addWidget(leech_deck_label, 5, 0, 1, 1)

    leech_deck_line = QtWidgets.QLineEdit(config_form.tab_2)
    leech_deck_line.setObjectName("leechDeck")
    leech_did = getTransferDeckId(conf.deck["name"])

    # No key: ""
    if leech_did == -1:
        leech_deck_line.setText("")
    # Empty: "Original Deck Name"
    elif leech_did == 0:
        leech_deck_line.setText(conf.deck["name"])
    # ##Defualt: "##Default"
    elif leech_did == 1:
        leech_deck_line.setText("##Default")
    # Deck: "Deck Name"
    else:
        leech_deck_line.setText(mw.col.decks.name(leech_did))

    config_form.gridLayout_2.addWidget(leech_deck_line, 5, 1, 1, 2)


def saveDataToAddonConf(conf: deckconf.DeckConf, deck, filtered_conf):
    """
    Hook-Function for when the legacy deck config is saving.

    Saves the input-data found in the created form-label object to addon config.

    :param conf: Deck config object of the deck being configured.
    :param deck: Deck object being configured.
    :param filtered_conf: Filtered deck config of the deck being configured.
    """
    leech_deck_line = conf.form.tab_2.findChild(QtWidgets.QLineEdit, "leechDeck")
    if leech_deck_line:

        addon_config = mw.addonManager.getConfig(__name__)
        key = deck["name"]
        leech_deck_name = leech_deck_line.text()

        # Default: Use input as leech deck.
        addon_config[key] = leech_deck_name

        # No input: Remove key.
        if leech_deck_name == "":
            addon_config.pop(key, None)
        # Input same as parent-deck key: Disable leech movement for key/deck.
        elif leech_deck_name == key:
            addon_config[key] = ""

        mw.addonManager.writeConfig(__name__, addon_config)


addHook("leech", onLeech)
addon_module = __name__.split(".")[0]
# Show config hook
gui_hooks.deck_conf_will_show.append(updateDeckConfForm)
# Saving config hook
gui_hooks.deck_conf_will_save_config.append(saveDataToAddonConf)
