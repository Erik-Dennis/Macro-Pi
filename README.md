# Macro-Pi

This is a project for a touchscreen raspberry pi that utilizes python and shell scripting to launch various programs on a server machine.
This is designed for Linux and most of the buttons are flatpak launch requests. In order for this to work you will need to change the variables for
your local IP Address, and the tty session, as well as enable ssh and ssh-keys for automatic login. The requests all start a different ssh session 
using screen and detatching, this was to reduce what was needed to install for this to work. The alternative is installing screen on the server device
and moving screen into the requests.

You will need to install screen for this to work.
