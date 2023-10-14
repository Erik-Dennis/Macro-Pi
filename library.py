import os

localServerIP = "10.0.0.195"
serverSessionNumber = ":1"

def chrome():
    os.system(f'screen -S chrome -dm ssh {localServerIP} "export DISPLAY={serverSessionNumber} && flatpak run com.google.Chrome"')
    
def discord():
    os.system(f'screen -S discord -dm ssh {localServerIP} "export DISPLAY={serverSessionNumber} && flatpak run com.discordapp.Discord"')

def lutris():
    os.system(f'screen -S lutris -dm ssh {localServerIP} "export DISPLAY={serverSessionNumber} && flatpak run net.lutris.Lutris"')

def OBS():
    os.system(f'screen -S OBS -dm ssh {localServerIP} "export DISPLAY={serverSessionNumber} && flatpak run com.obsproject.Studio"')

def spotify():
    os.system(f'screen -S spotify -dm ssh {localServerIP} "export DISPLAY={serverSessionNumber} && flatpak run com.spotify.Client"')

def steam():
    os.system(f'screen -S steam -dm ssh {localServerIP} "export DISPLAY={serverSessionNumber} && flatpak run com.valvesoftware.Steam"')

def shutdown():
    os.system("shutdown 0")