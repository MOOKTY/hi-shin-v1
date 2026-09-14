# Hi Shin V1

> A menu-driven Python security utility for inspecting system information, working with local files, analyzing failed-login records, resolving network information, scanning TCP ports, and viewing active INET connections.

Hi Shin V1 is presented in two distinct editions. The Standard Edition source is open and included in this repository. The GUI Edition remains closed source and is distributed only as a compiled Windows installer.

## Editions

| Edition | Interface | Source availability | Distribution |
|---|---|---|---|
| **Standard Edition** | Python CLI | Open source | `src/HiShinV1.py` |
| **GUI Edition** | Windows graphical application | Closed source | Compiled installer in [GitHub Releases](https://github.com/MOOKTY/hi-shin-v1/releases/tag/v1.0.0) |

## Standard Edition — Open Source

The Standard Edition provides a numbered terminal menu built from the original Hi Shin V1 Python source.

### Features

- Display the operating-system name, release, version, or all three
- List files in the current directory
- Display a file's size and modification timestamp
- Check whether a path exists
- Display running processes
- Display the current working directory
- Read a text or log file and inspect `login_failed` entries
- Extract IP information using the source's existing token-splitting logic
- Flag IPs appearing in failed-login entries three or more times
- Perform domain/DNS lookup and reverse DNS lookup
- Resolve a TCP service name from a port number
- Scan a predefined collection of common TCP ports
- Scan a custom sequential TCP port range
- Display active INET connections, addresses, status, and PID

The port scanners use IPv4 TCP sockets, `connect_ex()`, sequential scanning, and an approximately one-second socket timeout.

### Requirements

- Python 3
- `psutil`

### Installation

```console
git clone https://github.com/MOOKTY/hi-shin-v1.git
cd hi-shin-v1
python -m venv .venv
```

Activate the environment, then install the single external dependency:

```console
python -m pip install -r requirements.txt
```

### Usage

```console
python src/HiShinV1.py
```

This starts the original interactive main menu:

```text
===== Main Menu =====
1- System Information
2- OS Module
3- Network Tools
4- File Analyzer
5- Active Connections
0- Exit
```

Only scan systems and networks you own or have explicit permission to test.

### Known limitations

- TCP port scanning is sequential and can be slow across large ranges.
- Custom port input is converted directly to integers and is not range-validated.
- DNS and socket results depend on local network conditions and permissions.
- Process and connection information may require elevated operating-system permissions.
- The file analyzer expects failed-login lines to match the source's existing whitespace and `key=value` layout.
- The tool does not perform vulnerability detection, exploitation, intrusion detection, or malware analysis.

### Version and author

- Standard Edition: Hi Shin V1
- Author: **MOOKTY**

## GUI Edition — Windows

**GUI source code is private. Only the compiled Windows installer is publicly distributed.**

The GUI Edition is a closed-source Windows graphical edition, version **1.0.0**. Its installer is available from the [Hi Shin V1 v1.0.0 release](https://github.com/MOOKTY/hi-shin-v1/releases/tag/v1.0.0).

```text
Filename: Hi-Shin-V1-Setup.exe
SHA-256: 8b98693150d6b53c7a4b52a0b2f4d71aa3a652c2609a9ae1e343db2d53dfa2f1
```

The installer is not stored in the repository tree or Git history. No GUI source code is included in this repository, its branches, workflows, archives, or release assets.

## Project structure

```text
hi-shin-v1/
├── src/
│   └── HiShinV1.py
├── assets/
│   └── Hi-Shin-V1.ico
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## License boundary

The [MIT License](LICENSE) applies only to the Standard Edition source and repository documentation. It does not apply to, expose, or license the private source code of the closed-source GUI Edition. The GUI Edition is publicly distributed only as a compiled installer.

## Author

**MOOKTY**  
[GitHub profile](https://github.com/MOOKTY)
