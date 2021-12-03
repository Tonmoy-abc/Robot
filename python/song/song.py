import subprocess

from pywhatkit import playonyt


def play(name):
  try:
    playonyt(name)
  except:
    exit()

def stop():
  cmd = subprocess.run(["taskkill", "/im", "chrome.exe"], capture_output=True).stdout.decode()
  cmd = cmd.split(" ")
  cmd = cmd[0].replace(":","")
  if cmd == "SUCCESS":
    return "Stoped"
  else:
    return "Aready Stopted"
