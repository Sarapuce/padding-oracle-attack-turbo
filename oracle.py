import requests
import sys

def oracle(encrypted):
  payload = encrypted.hex().upper()
  r = requests.get(f"http://challenge01.root-me.org/realiste/ch12/index.aspx?c={payload}")
  return "Padding Error" not in r.text

