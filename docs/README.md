# Meshtastic Linux Client Documentation

Welcome to the official docs for the Meshtastic Linux Client!

Built for Linux Mint, Ubuntu, Debian — Secure, Off-Grid Communications.

---

## 🚀 Quick Start

1. Clone the repository:

    ```bash
    git clone https://github.com/YOUR_USERNAME/meshtastic-linux-client.git
    cd meshtastic-linux-client
    ```

1. Install dependencies:

    ```bash
    sudo apt install python3-pip
    pip3 install -r requirements.txt
    ```

1. Run the app:

    ```bash
    python3 main.py
    ```

---

## 🛰️ Main Features

- Bluetooth scanning for Meshtastic devices
- Full messaging support
- Secure AES encryption (per message and per channel)
- Firmware updates
- Mesh network topology map
- Chat search with highlighted matches
- Light and Dark mode toggle
- Backup/Restore settings
- Auto-connect to nearest node

---

## 🔒 Secure Messaging

- Enable encryption in Settings.
- Set per-channel keys under "Channel Encryption."
- Toggle per-message encryption when sending chats.

---

## 🛠️ Troubleshooting

| Issue | Fix |
|:---|:---|
| App won't launch | Install deps with `pip3 install -r requirements.txt` |
| Bluetooth not finding nodes | Enable BLE ads and check the Bluetooth service |
| Mesh map empty | Check that multiple nodes are powered and linked |
| Message decryption fails | Verify the correct key is set for that channel |

---

## 📜 License

MIT License - free to use, modify, and distribute.

---

## 🤝 Contributing

Pull Requests welcome!  
Open an Issue to report bugs, suggest features, or just say hi!

---
