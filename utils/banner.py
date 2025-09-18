import random

colores = ["red", "green", "yellow", "blue", "magenta", "cyan", "white", "orange"]

def obtener_color_aleatorio():
    color = random.choice(colores)
    if color == "orange":
        return "\033[1;38;5;208m"
    return color

def generar_banner():
    color = obtener_color_aleatorio()

    # Hacker-style cyber grid background
    hacker_bg = r"""
╔════════════════════════════════════════════════════════════════════════════╗
║ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ║
║ ░▒▒░░▒▒░░▒▒░░▒▒░░▒▒░░▒▒░░▒▒░░▒▒░░▒▒░░▒▒░░▒▒░░▒▒░░▒▒░░▒▒░░▒▒░░▒▒░░▒▒░░▒▒░░▒▒░ ║
║ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ║
╚════════════════════════════════════════════════════════════════════════════╝
    """

    # Main banner with your name: DARKBOSS1BD
    banner_text = r"""
                   (                   
 (  (       (      )\ )  
 )\))(   '  )\    (()/(     
((_)()\ )((((_)(   /(_))  
_(())\_)())\ _ )\ (_))_|    
\ \((_)/ /(_)_\(_)| |_       
 \ \/\/ /  / _ \  | __|    
  \_/\_/  /_/ \_\ |_|      

           \033[1;97m>> \033[1;91mDARKBOSS1BD \033[1;97m<<\033[0m
    """

    full_banner = hacker_bg + "\n" + banner_text

    if color.startswith("\033"):
        return f"{color}{full_banner}\033[0m"
    else:
        from termcolor import colored
        return colored(full_banner, color, attrs=["bold"])

uso = "\033[1;36mUsage:\033[0m\n  python3 waf_detection_tool.py [option]"

opciones = """
\033[1;35m🔥 l      \033[0m\033[1;37mShow list of supported WAFs.\033[0m
\033[1;35m🔥 h      \033[0m\033[1;37mShow this help message.\033[0m
\033[1;35m🔥 v      \033[0m\033[1;37mShow tool version.\033[0m
\033[1;35m🔥 [URL]  \033[0m\033[1;37mAnalyze the provided URL to detect a WAF.\033[0m
"""

ejemplo = "\033[1;36mExample:\033[0m\n  python3 website-waf-detection-tool-by-darkboss1bd.py https://example.com  "

def mostrar_ayuda_completa():
    print(generar_banner())  
    print(uso)
    print(opciones)
    print(ejemplo)

# ———————————————————————————————————————————————————————————————
# 💀 DARKBOSS1BD — Elite Cyber Operator
#
# 📬 Telegram: https://t.me/darkvaiadmin
# 🌐 Official Site: https://serialkey.top/
#
# 🔓 WAF Detection • Premium Keys • Ethical Hacking Tools
# ———————————————————————————————————————————————————————————————
