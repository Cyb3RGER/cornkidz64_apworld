# Corn Kidz 64 Setup Guide

## Required Software

- [Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases)
- [This AP world](#todo)
- [BepInEx 5.4+](https://github.com/BepInEx/BepInEx/releases/tag/v5.4.23.2)
- [This Game Mod](#todo)

## Installation Procedures

### Installing the apworld

- Place ``cornkidz64.apworld`` in ``custom_worlds`` of your AP installation.

For more information about .apworlds
see [here](https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/apworld%20specification.md)

### Installing the Game Mod

- Navigate to the games installation folder.
  - In Steam, you can right-click the title and select ``Manage -> Browse local files``.
- Extract the content of the BepInEx zip into the games folder
- Start the game and exit again.
- Navigate to ``BepInEx\plugins`` in the games folder.
- Create a folder ``CornKidzAP`` and extract the content of the game mod zip into it.


## Create a Config (.yaml) File

### What is a config file and why do I need one?

See the guide on setting up a basic YAML at the Archipelago setup
guide: [Basic Multiworld Setup Guide](https://archipelago.gg/tutorial/Archipelago/setup/en)

### Where do I get a config file?

A default yaml is included in the download. Alternative you can use the Web Host when running from source.

### Verifying your config file

If you would like to validate your config file to make sure it works, you may do so on the YAML Validator page. YAML
validator page: [YAML Validation page](https://archipelago.gg/mysterycheck)

## Joining a MultiWorld Game

After the games launch screen an Archipelago UI in the top left corner should appear. Enter the servers hostname and post and your slot name and password, then hit ``Connect``. 


## Hosting a MultiWorld game

The recommended way to host a game is to use the Archipelago hosting service. The process is relatively simple:

1. Collect config files from your players.
2. Place the config files in the ``Players`` folder in your Archipelago install
3. Run ``ArchipelagoGenerate.exe`` and location the resulting zip in the ``output`` folder
4. Upload that zip file to the Host Game page.
    - Generate page: [WebHost Host Game Page](https://archipelago.gg/uploads)
5. Click "Create New Room". This will take you to the server page. Provide the link to this page to your players, so
   they may download their patch files from there.
6. Note that a link to a MultiWorld Tracker is at the top of the room page. The tracker shows the progress of all
   players in the game. Any observers may also be given the link to this page.
7. Once all players have joined, you may begin playing.

## Troubleshooting

ToDo?
