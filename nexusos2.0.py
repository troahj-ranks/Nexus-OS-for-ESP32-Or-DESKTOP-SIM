
import tkinter as tk
from tkinter import messagebox
import random
import time

# =====================================================
# NEXUS OS - DESKTOP SIMULATOR
# Version 1.0
# Created for T-Embed CC1101 Plus ESP32-S3
# =====================================================

BG = "#080D18"
PANEL = "#101A2B"
PANEL2 = "#142238"
BLUE = "#16C8FF"
WHITE = "#E8F5FF"
GREY = "#8296AD"
GREEN = "#28E89A"

root = tk.Tk()
root.title("NEXUS OS | Desktop Simulator")
root.geometry("1150x720")
root.minsize(950, 620)
root.configure(bg=BG)

current_page = None
page_frame = None


def clear_page():
    global page_frame

    if page_frame:
        page_frame.destroy()

    page_frame = tk.Frame(root, bg=BG)
    page_frame.pack(
        side="right",
        fill="both",
        expand=True,
        padx=25,
        pady=20
    )


def heading(title, subtitle):
    tk.Label(
        page_frame,
        text=title,
        font=("Segoe UI", 25, "bold"),
        fg=WHITE,
        bg=BG
    ).pack(anchor="w")

    tk.Label(
        page_frame,
        text=subtitle,
        font=("Segoe UI", 10),
        fg=GREY,
        bg=BG
    ).pack(anchor="w", pady=(3, 20))


def card(parent, title, description):
    box = tk.Frame(
        parent,
        bg=PANEL,
        highlightbackground="#203650",
        highlightthickness=1
    )

    box.pack(
        fill="x",
        pady=7,
        ipady=8
    )

    tk.Label(
        box,
        text=title,
        bg=PANEL,
        fg=BLUE,
        font=("Segoe UI", 13, "bold")
    ).pack(anchor="w", padx=15, pady=(12, 3))

    tk.Label(
        box,
        text=description,
        bg=PANEL,
        fg=GREY,
        font=("Segoe UI", 10)
    ).pack(anchor="w", padx=15, pady=(0, 12))

    return box


def action_button(parent, text, command):
    return tk.Button(
        parent,
        text=text,
        command=command,
        bg=PANEL2,
        fg=BLUE,
        activebackground=BLUE,
        activeforeground=BG,
        relief="flat",
        bd=0,
        padx=16,
        pady=9,
        cursor="hand2",
        font=("Segoe UI", 10, "bold")
    )


# =====================================================
# DASHBOARD
# =====================================================

def dashboard():
    clear_page()

    heading(
        "NEXUS DASHBOARD",
        "Welcome to your personal embedded toolkit."
    )

    tk.Label(
        page_frame,
        text="SYSTEM ONLINE",
        bg=BG,
        fg=GREEN,
        font=("Segoe UI", 12, "bold")
    ).pack(anchor="w", pady=5)

    cards = tk.Frame(page_frame, bg=BG)
    cards.pack(fill="x", pady=15)

    stats = [
        ("DEVICE", "T-Embed CC1101+"),
        ("PROCESSOR", "ESP32-S3"),
        ("MODE", "DESKTOP SIM"),
        ("VERSION", "NEXUS 1.0")
    ]

    for name, value in stats:
        box = tk.Frame(cards, bg=PANEL, padx=15, pady=18)
        box.pack(side="left", expand=True, fill="x", padx=5)

        tk.Label(
            box,
            text=name,
            bg=PANEL,
            fg=GREY,
            font=("Segoe UI", 9, "bold")
        ).pack(anchor="w")

        tk.Label(
            box,
            text=value,
            bg=PANEL,
            fg=BLUE,
            font=("Segoe UI", 11, "bold")
        ).pack(anchor="w", pady=5)

    card(
        page_frame,
        "WELCOME TO NEXUS",
        "Your custom ESP32 toolkit simulator is ready."
    )

    card(
        page_frame,
        "AVAILABLE MODULES",
        "Wi-Fi | Bluetooth | NFC | Infrared | Sub-GHz"
    )

    card(
        page_frame,
        "SYSTEM NOTICE",
        "All radio and hardware functions are simulated."
    )


# =====================================================
# SIMULATED WIFI
# =====================================================

def wifi_page():
    clear_page()

    heading(
        "WI-FI LAB",
        "Wireless network discovery simulator"
    )

    output = tk.Text(
        page_frame,
        bg="#050A12",
        fg=GREEN,
        insertbackground=WHITE,
        font=("Consolas", 11),
        height=15,
        relief="flat",
        padx=12,
        pady=12
    )

    output.pack(fill="both", expand=True)

    def scan():
        output.delete("1.0", "end")
        output.insert("end", "NEXUS WI-FI SIMULATOR\n")
        output.insert("end", "Starting simulated scan...\n\n")

        networks = [
            "Home_Network",
            "NEXUS_GUEST",
            "TP-Link_Demo",
            "Wireless_Test",
            "Office_WiFi"
        ]

        for network in networks:
            signal = random.randint(35, 99)

            output.insert(
                "end",
                f"[DEMO] {network:<22} "
                f"Signal: {signal}%\n"
            )

        output.insert(
            "end",
            "\nSimulation completed successfully."
        )

    action_button(
        page_frame,
        "START SIMULATED SCAN",
        scan
    ).pack(anchor="w", pady=15)


# =====================================================
# SUB GHZ
# =====================================================

def subghz_page():
    clear_page()

    heading(
        "SUB-GHZ LAB",
        "CC1101 signal analysis simulator"
    )

    output = tk.Text(
        page_frame,
        bg="#050A12",
        fg=BLUE,
        font=("Consolas", 11),
        height=12,
        relief="flat",
        padx=12,
        pady=12
    )

    output.pack(fill="both", expand=True)

    def analyse():
        output.insert(
            "end",
            "\n[SIMULATION] Signal analysis started\n"
        )

        output.insert(
            "end",
            f"[SIMULATION] Frequency: "
            f"{random.choice([315, 433, 868, 915])} MHz\n"
        )

        output.insert(
            "end",
            f"[SIMULATION] Signal strength: "
            f"{random.randint(-90, -35)} dBm\n"
        )

        output.insert(
            "end",
            "[SIMULATION] Analysis complete\n"
        )

    action_button(
        page_frame,
        "ANALYSE DEMO SIGNAL",
        analyse
    ).pack(anchor="w", pady=15)


# =====================================================
# INFRARED
# =====================================================

def ir_page():
    clear_page()

    heading(
        "INFRARED LAB",
        "Virtual infrared remote control"
    )

    output = tk.Label(
        page_frame,
        text="REMOTE READY",
        bg=PANEL,
        fg=GREEN,
        font=("Consolas", 15),
        pady=20
    )

    output.pack(fill="x", pady=15)

    def remote(command):
        output.config(
            text=f"SIMULATED IR COMMAND: {command}"
        )

    for command in ["POWER", "VOLUME +", "VOLUME -",
                    "CHANNEL +", "CHANNEL -", "MUTE"]:
        action_button(
            page_frame,
            command,
            lambda c=command: remote(c)
        ).pack(fill="x", pady=4)


# =====================================================
# NFC
# =====================================================

def nfc_page():
    clear_page()

    heading(
        "NFC LAB",
        "Virtual NFC tag information"
    )

    output = tk.Label(
        page_frame,
        text="NO DEMO TAG SELECTED",
        bg=PANEL,
        fg=BLUE,
        font=("Consolas", 13),
        pady=25
    )

    output.pack(fill="x", pady=15)

    def read_tag():
        output.config(
            text=(
                "SIMULATED NFC TAG\n\n"
                "Type: Demo tag\n"
                "Status: Available\n"
                "Read mode: Simulation"
            )
        )

    action_button(
        page_frame,
        "READ DEMO TAG",
        read_tag
    ).pack(anchor="w")


# =====================================================
# BLUETOOTH
# =====================================================

def bluetooth_page():
    clear_page()

    heading(
        "BLUETOOTH LAB",
        "Virtual Bluetooth device discovery"
    )

    output = tk.Text(
        page_frame,
        bg="#050A12",
        fg=GREEN,
        font=("Consolas", 11),
        height=15,
        relief="flat",
        padx=12,
        pady=12
    )

    output.pack(fill="both", expand=True)

    def discover():
        output.delete("1.0", "end")

        output.insert(
            "end",
            "NEXUS BLUETOOTH SIMULATOR\n\n"
        )

        devices = [
            "Demo Headphones",
            "Virtual Speaker",
            "Test Controller",
            "NEXUS Device"
        ]

        for device in devices:
            output.insert(
                "end",
                f"[DEMO DEVICE] {device}\n"
            )

        output.insert(
            "end",
            "\nDiscovery finished."
        )

    action_button(
        page_frame,
        "DISCOVER DEMO DEVICES",
        discover
    ).pack(anchor="w", pady=15)


# =====================================================
# TERMINAL
# =====================================================

def terminal_page():
    clear_page()

    heading(
        "NEXUS TERMINAL",
        "Custom operating system command interface"
    )

    output = tk.Text(
        page_frame,
        bg="#03070D",
        fg=GREEN,
        font=("Consolas", 11),
        height=17,
        relief="flat",
        padx=12,
        pady=12
    )

    output.pack(fill="both", expand=True)

    output.insert(
        "end",
        "NEXUS OS [Version 1.0]\n"
        "Type HELP to see available commands.\n\n"
    )

    entry = tk.Entry(
        page_frame,
        bg=PANEL,
        fg=WHITE,
        insertbackground=WHITE,
        font=("Consolas", 12),
        relief="flat"
    )

    entry.pack(fill="x", pady=12, ipady=10)

    def execute(event=None):
        command = entry.get().strip().lower()
        entry.delete(0, "end")

        output.insert("end", f"\nNEXUS> {command}\n")

        commands = {
            "help": (
                "COMMANDS:\n"
                "HELP - Show commands\n"
                "CLEAR - Clear terminal\n"
                "VERSION - Show version\n"
                "STATUS - Show system status\n"
                "TIME - Show current time\n"
            ),
            "version": "NEXUS OS Version 1.0",
            "status": "SYSTEM ONLINE | DESKTOP SIMULATOR",
            "time": time.strftime("%H:%M:%S")
        }

        if command == "clear":
            output.delete("1.0", "end")
            return

        output.insert(
            "end",
            commands.get(
                command,
                "Unknown command. Type HELP."
            ) + "\n"
        )

        output.see("end")

    entry.bind("<Return>", execute)


# =====================================================
# SETTINGS
# =====================================================

def settings_page():
    clear_page()

    heading(
        "SYSTEM SETTINGS",
        "NEXUS OS configuration"
    )

    card(
        page_frame,
        "OPERATING SYSTEM",
        "NEXUS OS Desktop Simulator"
    )

    card(
        page_frame,
        "HARDWARE TARGET",
        "LILYGO T-Embed CC1101 Plus"
    )

    card(
        page_frame,
        "PROCESSOR",
        "ESP32-S3"
    )

    card(
        page_frame,
        "BUILD",
        "NEXUS-1001 | Version 1.0"
    )

    card(
        page_frame,
        "DEVELOPER",
        "NEXUS OS Custom Project"
    )


# =====================================================
# SIDEBAR
# =====================================================

sidebar = tk.Frame(
    root,
    bg="#0B1423",
    width=225
)

sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

tk.Label(
    sidebar,
    text="NEXUS",
    bg="#0B1423",
    fg=BLUE,
    font=("Segoe UI", 25, "bold")
).pack(pady=(25, 0))

tk.Label(
    sidebar,
    text="OPERATING SYSTEM",
    bg="#0B1423",
    fg=GREY,
    font=("Segoe UI", 8, "bold")
).pack(pady=(0, 25))


def nav(name, command):
    button = tk.Button(
        sidebar,
        text="   " + name,
        command=command,
        bg="#0B1423",
        fg=WHITE,
        activebackground=PANEL2,
        activeforeground=BLUE,
        font=("Segoe UI", 11),
        relief="flat",
        bd=0,
        anchor="w",
        padx=18,
        pady=12,
        cursor="hand2"
    )

    button.pack(fill="x", padx=8, pady=2)


nav("⌂   Dashboard", dashboard)
nav("◉   Wi-Fi Lab", wifi_page)
nav("◉   Sub-GHz Lab", subghz_page)
nav("◉   Infrared Lab", ir_page)
nav("◉   NFC Lab", nfc_page)
nav("◉   Bluetooth Lab", bluetooth_page)
nav(">_   Terminal", terminal_page)
nav("⚙   Settings", settings_page)

tk.Frame(
    sidebar,
    bg="#203650",
    height=1
).pack(fill="x", padx=15, pady=20)

tk.Label(
    sidebar,
    text="NEXUS CORE 1.0\nESP32-S3 TARGET\nSIMULATION MODE",
    bg="#0B1423",
    fg=GREY,
    font=("Consolas", 8),
    justify="left"
).pack(side="bottom", anchor="w", padx=18, pady=20)


# =====================================================
# TOP STATUS BAR
# =====================================================

topbar = tk.Frame(
    root,
    bg=BG
)

topbar.pack(side="top", fill="x", padx=25, pady=(12, 0))

tk.Label(
    topbar,
    text="NEXUS OS  /  DESKTOP ENVIRONMENT",
    bg=BG,
    fg=GREY,
    font=("Segoe UI", 9, "bold")
).pack(side="left")

clock = tk.Label(
    topbar,
    text="",
    bg=BG,
    fg=BLUE,
    font=("Consolas", 11)
)

clock.pack(side="right")


def update_clock():
    clock.config(text=time.strftime("%H:%M:%S"))
    root.after(1000, update_clock)


# =====================================================
# START
# =====================================================

dashboard()
update_clock()

root.mainloop()

