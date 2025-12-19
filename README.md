🔐 Malicious Browser Extension PoC - Educational Security Research
<div align="center">

https://img.shields.io/badge/Python-3.8+-blue.svg
https://img.shields.io/badge/Flask-2.0+-lightgrey.svg
https://img.shields.io/badge/License-MIT-green.svg
https://img.shields.io/badge/Platform-Linux%2520%257C%2520Windows%2520%257C%2520macOS-orange.svg

⚠️ EDUCATIONAL USE ONLY

https://img.shields.io/badge/YouTube-Video_Tutorial-red.svg
https://img.shields.io/badge/Instagram-@jonastrikex-E4405F.svg
https://img.shields.io/badge/TikTok-@jonastrikex-000000.svg
</div>
🚨 CRITICAL WARNING - READ BEFORE PROCEEDING
<div align="center" style="border: 3px solid #ff4444; padding: 20px; border-radius: 10px; background-color: #fff0f0; margin: 20px 0;">

⚠️ FOR EDUCATIONAL PURPOSES ONLY ⚠️
THIS IS A TECHNICAL DEMONSTRATION IN A CONTROLLED ENVIRONMENT

NEVER use this knowledge to:

    Access accounts that don't belong to you

    Violate other people's privacy

    Perform illegal activities

LEGAL CONSEQUENCES:

    Unauthorized computer access is a CRIME in most countries

    Can result in severe fines and imprisonment

    Permanent damage to your professional career

✅ PERMITTED USE:

    Learning in isolated labs

    Authorized security research

    Improving personal/organizational defenses

    Ethical cybersecurity training

</div>
📹 Complete Video Explanation
<div align="center">

https://via.placeholder.com/800x450/ff0000/ffffff?text=WATCH+FULL+DEMONSTRATION

Click the image to watch the complete demonstration on YouTube (reemplaza el link con tu video real)
</div>
📖 Project Description

This repository contains an educational Proof of Concept (PoC) demonstrating Session Hijacking techniques through cookie theft. The objectives are:

    Demonstrate how an attacker could potentially access accounts without credentials

    Educate about the risks of unverified browser extensions

    Provide practical defense tools and knowledge

⚡ Technologies Used

    Python 3.8+ with Flask for the collector server

    JavaScript for malicious browser extensions (DEMO)

    HTML/CSS for the fake landing page

    Multi-browser support (Firefox and Chrome)

🗂️ Repository Structure
text

malicious-extension-poc/
├── malicious_v2/                    # Firefox-based extension (Manifest V2)
│   ├── manifest.json               # Extension configuration (Firefox format)
│   ├── background.js               # Background script that steals cookies
│   ├── content.js                  # Content script for page injection
│   └── icons/                      # Extension icons
│       ├── icon-48.png
│       └── icon-96.png
├── malicious_v3/                    # Chrome-based extension (Manifest V3)
│   ├── manifest.json               # Extension configuration (Chrome format)
│   ├── background.js               # Service worker that steals cookies
│   ├── content.js                  # Content script for page injection
│   ├── popup.html                  # Extension popup interface
│   └── icons/                      # Extension icons
│       ├── icon-48.png
│       └── icon-96.png
├── server/                         # Attacker's collector server
│   ├── server.py                   # Flask server for receiving stolen data
│   ├── requirements.txt            # Python dependencies
│   └── stolen_data.log             # Example of stolen data
└── web_page/                       # Fake landing page for the attack
    ├── index.html                  # Professional-looking fake website
    ├── Privacy_Shield_ProV5.2.1.xpi  # Firefox extension package
    └── Privacy_Shield_ProV5.2.1.zip  # Chrome extension package

🔬 How the Attack Works (Technical Overview)
Attack Architecture
<div align="center">

https://cookie.png
</div>

Key Components:

    Malicious Extensions (malicious_v2/, malicious_v3/)

        v2: Firefox-compatible (Manifest V2)

        v3: Chrome-compatible (Manifest V3)

        Both steal cookies from multiple websites

        Send stolen data to the attacker's server

    Collector Server (server/)

        Simple Flask application

        Receives POST requests with stolen cookies

        Logs all received data

    Fake Landing Page (web_page/)

        Professional-looking fake website to trick users into installing the extension

🌐 Connect with the Creator
<div align="center">

https://img.shields.io/badge/Portfolio-Website-blue?style=for-the-badge
https://img.shields.io/badge/Instagram-@jonastrikex-E4405F?style=for-the-badge&logo=instagram&logoColor=white
https://img.shields.io/badge/TikTok-@jonastrikex-000000?style=for-the-badge&logo=tiktok&logoColor=white
https://img.shields.io/badge/LinkedIn-Profile-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white
https://img.shields.io/badge/YouTube-Channel-FF0000?style=for-the-badge&logo=youtube&logoColor=white <!-- Pon tu canal real -->
</div><div align="center">

Found this useful?
⭐ Star this repo · 📢 Share responsibly · 🔔 Subscribe for more cybersecurity content

"Cybersecurity knowledge is a scalpel: in wrong hands it causes harm, in expert hands it saves digital lives."
</div>
📄 License

This project is licensed under the MIT License with Ethical Restrictions - see the LICENSE file for details.
