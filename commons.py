# Phosphous Administration Suite
# Written with <3 by TheMemeSniper
# "Commons" module

import os
from colorama import Fore

# The Commons module is a hub for all of the variables Phosphorus needs to function.
# The below variables should not be edited. The variables you can edit are below them.

### DO NOT EDIT THESE VARIABLES ###
SCRDIR = os.path.dirname(os.path.realpath(__file__)) 
# Tell scripts where they are

RESET = Fore.WHITE
INFO = f"[{Fore.CYAN}:INFO:{RESET}]: "
WARN = f"[{Fore.YELLOW}:WARN:{RESET}]: "
ERR = f"[{Fore.RED}:ERR:{RESET}]: "
SUCCESS = f"[{Fore.GREEN}:SUCCESS:{RESET}]: "
# Colors!!!! Yay!!!!

SUDOERS = os.path(f"{SCRDIR}/sudoers.py")
# Pointer to the sudoers file for `privesc`.
# Can be edited, but isn't recommended.

### DO NOT EDIT THESE VARIABLES ###

### THESE VARIABLES CAN BE EDITED ###

TOKEN = ""
# And now, an obligitory mention of token safety.
# DO NOT under any circumstances share your bot's token.
# Because of Phosphorus' default permissions, anyone with the token **will have admin rights on every server the bot is in.**
# Admin rights are very dangerous, with them, you can do anything.
# Do not share your token.

OWNERS = [391271835901362198]
# List of userids that can use special commands like `shutdown`, `restart`, `eval` and most dangerously `shell`.
# Do not put any userids of people you don't know, they will have the ability to run any code on your server.

BLACKLIST = []
# Serverids that the bot will refuse to be in.
# If a serverid is in this list and the bot's joined servers, the bot will immediately leave.

### THESE VARIABLES CAN BE EDITED ###


