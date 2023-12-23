# YouTube Video Downloader

A simple Python-based YouTube video downloader with support for Windows and macOS.

## Features

- Download YouTube videos easily.
- Available as an executable for both Windows (.exe) and macOS.
- Cross-platform support.

## Getting Started

### Prerequisites

- For Windows: No additional prerequisites.
- For macOS: No additional prerequisites.

### Dependencies

- [PyQt5](https://pypi.org/project/PyQt5/): Python bindings for Qt.
- [yt-dlp](https://github.com/yt-dlp/yt-dlp): A YouTube video downloader library.

### Download

You can download the latest release from the [Releases](https://github.com/your-username/your-repo/releases) page.

### Usage

1. **Windows:**
   - Double-click on the `your-app-name.exe` file to run the application.
   - If Windows Defender flags the application, follow [these steps](#disabling-windows-defender) to proceed.

2. **macOS:**
   - Run the executable in the terminal: `./your-app-name`.
   - If you encounter issues due to macOS security, [follow these steps](#disabling-macos-gatekeeper).

### Disabling Windows Defender

To run the application on Windows without interruptions from Windows Defender, follow these steps:

1. Open Windows Security.
2. Go to "Virus & threat protection."
3. Click on "Manage settings" under Virus & threat protection settings.
4. Scroll down to the "Exclusions" section and add the directory containing the application to the exclusion list.

### Disabling macOS Gatekeeper

To run the application on macOS without interruptions from Gatekeeper, follow these steps:

1. Open the terminal.
2. Run the command: `sudo xattr -r -d com.apple.quarantine /path/to/your-app-name`.

## Contributing

If you have suggestions, improvements, or want to report issues, feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
