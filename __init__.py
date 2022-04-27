"""
MIT License: Copyright (c) 2022 justkoi <https://github.com/iamjustkoi>
Full license text available in "LICENSE" file, located in the add-on's root directory.

Based on the "Anki Add-On Guide" <https://addon-docs.ankiweb.net/hooks-and-filters.html#legacy-hook-handling>.
as well as the add-on "ANTI-SUCK" <https://ankiweb.net/shared/info/1131698154> by Joseph Y.
"""
import json

import anki.hooks as hooks
import aqt.addons
from anki.cards import Card
# from anki.hooks import addHook
from aqt import mw, gui_hooks, deckconf
from PyQt5 import QtWidgets
default_key_name = "##Default"
default_leech_deck_name = "Leech"

{
    # TODO: Handle "##Default::Sub-deck" notation
    # TODO: Fix "Restore Defaults" button for config saving
    # TODO: Add feedback, support, and github links to config pages
}


def findDefaultLeechDeckId():
    config = mw.addonManager.getConfig(__name__)
    deck_id = config["0"]
    # Does the default deck key have a value and exist?
    # Can't ever be none due to the default value in config.json, which is added back by Anki
    if deck_id != ("-1" or None):
        return int(mw.col.decks.id(default_leech_deck_name)) if deck_id == "0" else int(deck_id)
    else:
        return None


def findTransferDeckIdForDeck(deck_id: int):
    result_did = -2  # No value found

    config = mw.addonManager.getConfig(__name__)
    # Set current deck's leech deck to none unless a value is found
    current_leech_did = config.get(str(deck_id))
    default_leech_did = findDefaultLeechDeckId()

    print(f"curr_did: {current_leech_did} (type: {type(current_leech_did)}), \n"
          f"def_did: {default_leech_did} (type: {type(default_leech_did)})")

    if current_leech_did:
        current_leech_did = int(current_leech_did)
        result_did = -1  # Empty value found
        # If deck's config value is not blank and not the default key
        if current_leech_did != -1 and current_leech_did != 0:
            result_did = current_leech_did  # Set-value found
        # If a default key exists and is what the current key is set to
        elif default_leech_did and current_leech_did == 0:
            result_did = 0  # Default value found

    print(f"res_id: {result_did}")

    return result_did


def onLeech(card: Card):
    """
Hook function that handles new leech-movement functions when the specified card is "leeched."

    :param card: Reference to card being leeched.
    """
    # config = mw.addonManager.getConfig(__name__)
    current_id = mw.col.decks.get_current_id()
    # config_default_key_id = config.get(default_id)

    transfer_did = findTransferDeckIdForDeck(current_id)
    default_did = findDefaultLeechDeckId()
    # Does default deck key exist and no value/default value was found?
    if default_did and transfer_did == (-2 or 0):
        # Move card to default leech deck
        card.did = default_did
    # Is the current deck's key-value set to a different deck and has a deck set?
    elif transfer_did != (-2 or -1):
        # Move card to leech deck
        card.did = transfer_did

    # Scheduler handles updates for leech cards so opting not to call an update using "card.flush()".

    # If the card was also in a cram/custom study deck, set it back to its original deck and due date:
    card.odid = 0
    if card.odue:
        card.due = card.odue
        card.odue = 0


def loadDeckConfForm(conf: deckconf.DeckConf):
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

    leech_did = findTransferDeckIdForDeck(conf.deck["id"])

    # No key: ""
    if leech_did == -2:
        leech_deck_line.setText("")  # Set text to empty
    # Empty key: "Original Deck Name"
    elif leech_did == -1:
        leech_deck_line.setText(conf.deck["name"])  # Set text to current deck
    # Default key: "##Default"
    elif leech_did == 0:
        leech_deck_line.setText(default_key_name)  # Set text to default key
    # Input key: "<Input Deck>"
    else:
        leech_deck_line.setText(mw.col.decks.name(leech_did))  # Set text to name of input deck

    print(f"ID found: {leech_did} \n"
          f"Out: {leech_deck_line.text()}")

    config_form.gridLayout_2.addWidget(leech_deck_line, 5, 1, 1, 2)


def saveDeckConfForm(conf: deckconf.DeckConf, deck, filtered_conf):
    """
Hook-Function for when the legacy deck config is saving.

Saves the input-data found in the created form-label object to addon config.

    :param conf: Deck config object of the deck being configured.
    :param deck: Deck object being configured.
    :param filtered_conf: Filtered deck config of the deck being configured.
    """
    leech_deck_line = conf.form.tab_2.findChild(QtWidgets.QLineEdit, "leechDeck")
    if not leech_deck_line:
        print("No line-input element found.")
        return

    addon_config = mw.addonManager.getConfig(__name__)
    deck_input_name = leech_deck_line.text()
    key_id = str(deck["id"])

    # No input: Remove key
    if deck_input_name == "" or not deck_input_name:
        addon_config.pop(key_id, None)
    # Same as parent: Set key to empty id
    elif deck_input_name == deck["name"]:
        addon_config[key_id] = "-1"
    # Default input: Set key to default id
    elif deck_input_name == default_key_name:
        addon_config[key_id] = "0"
    # Else: Set key to new deck-input
    else:
        leech_deck_id = str(mw.col.decks.id(deck_input_name))
        addon_config[key_id] = leech_deck_id

    print(f"in: {deck_input_name} \n"
          f"key_id: {key_id} \n"
          f"addon_config[key_id]: {addon_config.get(key_id)}")

    mw.addonManager.writeConfig(__name__, addon_config)


# Saved variable for checking which addon config is being loaded after the selection
selected_addon = ""


def addonSelected(dialog: aqt.addons.AddonsDialog, meta: aqt.addons.AddonMeta) -> object:
    """
Hook-function for when an addon is selected in the Addons dialog menu. Sets selected_addon to currently selected addon.
    :param dialog: Addons dialog menu object.
    :param meta: Meta object for selected addon.
    """
    global selected_addon
    selected_addon = meta.dir_name
    if selected_addon == __name__:
        print("Selected!")


# Anki always adds default config.json values if they're missing from meta.json
def loadingAddonConfJSON(json_str: str):
    if selected_addon != __name__:
        return json_str

    print(f"Load In:\n{json_str}")

    data = dict(json.loads(json_str))
    out_data = {}

    for key_id_str in data:
        # Default Leech Deck id:
        if key_id_str == "0":
            key_name = default_key_name
        # All other deck id's:
        else:
            key_name = mw.col.decks.name(int(key_id_str))

        if key_name != mw.col.tr.decks_no_deck():

            val_id = int(data[key_id_str])

            # deck-key leech deck is default?
            if val_id == 0:
                val_name = default_key_name
                if key_id_str == "0":
                    val_name = default_leech_deck_name

            # deck-key leech deck is blank or doesn't exist?
            elif val_id == -1 or mw.col.decks.name(val_id) == mw.col.tr.decks_no_deck():
                val_name = ""

            # otherwise:
            else:
                val_name = mw.col.decks.name(val_id)

            if val_name is None:
                aqt.utils.tooltip(f"Unable to load the value ID for key: \"{key_name}\": \"{data[key_id_str]}\"")
                print(f"Unable to load the value ID for key: \"{key_name}\": \"{data[key_id_str]}\"")
            elif key_name is None:
                aqt.utils.tooltip(f"Unable to load the key ID for key: \"{key_id_str}\"")
                print(f"Unable to load the key ID for key: \"{key_id_str}\"")
            else:
                # Add key and value to output data
                out_data[key_name] = val_name

    loading_json = json.dumps(out_data, indent=4, sort_keys=True, ensure_ascii=False).encode("utf8")
    print(f"Load Formatted: \n {loading_json.decode()}")

    return loading_json.decode()


def savingAddonConfJSON(json_str: str):
    if selected_addon != __name__:
        return json_str

    print(f"Save In:\n{json_str}")

    data = dict(json.loads(json_str))
    out_data = {}

    # No checks run since Anki automatically assigns decks to id's even if they don't already exist
    for key_name in data:
        # "##Default" set saved id to "0"
        if key_name == default_key_name:
            key_id_str = "0"
        # All other deck names set id to deck's id
        else:
            key_id_str = str(mw.col.decks.id(key_name))

        val_name = data[key_name]

        # Leech deck set to a default value? Save leech deck id: "0"
        if val_name == default_key_name:
            val_id = "0"
        # Leech deck set to none? Save leech deck id: "-1"
        elif val_name == "":
            val_id = "-1"
        # Save leech deck id: input deck name's id
        else:
            val_id = str(mw.col.decks.id(data[key_name]))

        out_data[key_id_str] = val_id

    # Handle default removed before Anki handles it on load and scheduling
    if out_data.get("0") is None:
        out_data["0"] = "-1"

    saving_json = json.dumps(out_data, indent=4, sort_keys=True, ensure_ascii=False).encode("utf8")
    print(f"Save Formatted: \n {saving_json.decode()}")

    return saving_json.decode()


# Leech card hook
hooks.card_did_leech.append(onLeech)
# Show config hook
gui_hooks.deck_conf_will_show.append(loadDeckConfForm)
# Save config hook
gui_hooks.deck_conf_will_save_config.append(saveDeckConfForm)

gui_hooks.addons_dialog_did_change_selected_addon.append(addonSelected)
gui_hooks.addon_config_editor_will_display_json.append(loadingAddonConfJSON)
gui_hooks.addon_config_editor_will_save_json.append(savingAddonConfJSON)
