import os

if os.name == "nt":
    os.system("")


class C:
    RST = "\033[0m"
    BLD = "\033[1m"
    DIM = "\033[2m"
    BLK = "\033[30m"
    RED = "\033[31m"
    GRN = "\033[32m"
    YEL = "\033[33m"
    BLU = "\033[34m"
    MAG = "\033[35m"
    CYN = "\033[36m"
    WHT = "\033[37m"
    GRY = "\033[90m"
    BRED = "\033[91m"
    BGRN = "\033[92m"
    BYEL = "\033[93m"
    BBLU = "\033[94m"
    BMAG = "\033[95m"
    BCYN = "\033[96m"
    ACC = "\033[96m"
    ACC2 = "\033[36m"
    HI = "\033[97m"


def ok(msg):    print(f"  {C.BGRN}[+]{C.RST} {msg}")
def info(msg):  print(f"  {C.BCYN}[*]{C.RST} {msg}")
def warn(msg):  print(f"  {C.BYEL}[!]{C.RST} {msg}")
def err(msg):   print(f"  {C.BRED}[-]{C.RST} {msg}")


def label(k, v, color=None):
    color = color or C.WHT
    print(f"  {C.DIM}{k:<22}{C.RST} {color}{v}{C.RST}")


def section(title):
    print()
    print(f"  {C.BLD}{C.BCYN}▎{C.RST} {C.BLD}{C.HI}{title}{C.RST}")
    print()
