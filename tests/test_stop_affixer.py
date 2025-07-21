import sys

sys.path.append("../qalsadi")
import stop_affixer

affixer = stop_affixer.stopword_affixer()
x = affixer.vocalize("إِلَى", "و", "", "ه")
print(x)
