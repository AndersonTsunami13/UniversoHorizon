import time
from datetime import datetime
import random
import os
import sys
from colorama import init, Fore, Style 
#importações aqui encima!

init(autoreset=True) 
# Inicializa o colorama

from dados import *
from config import *
from bios import bios_sequence
from boot import boot_sequence
from funcoes import *