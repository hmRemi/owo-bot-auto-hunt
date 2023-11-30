# Owo Bot Auto Hunt

This Python script automates the usage of a specific Discord bot command, in this case, targeting the "owo" bot's 'hunt' command. The script sends the 'wh' command every 15 seconds and includes automated captcha detection to handle verification prompts, exiting the program when a captcha is encountered.

![Owo Bot Auto Hunt](https://img.shields.io/badge/version-1.0.0-FF7F7F)
![Owo Bot Auto Hunt](https://img.shields.io/badge/author-%E2%9C%9F-FF7F7F)

---

## Features

- **Captcha Detection:** Detects captcha prompts and automatically exits the program to handle verifications.
- **Real-Time Stats:** Monitor the number of successful hits and failed attempts.
- **Console Title:** Get real-time statistics in the console title, including the gathered items from hunt.

---

## Milestones

- **10 Stars** - Better Error Handling
- **25 Stars** - Improve performance
- **50 Stars** - Add AI Captcha Solving

---

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Getting Started

### Prerequisites

To run the Owo Bot Auto Hunt, you will need the following:

- Python 3.x
- Requests library

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Devuxious/Owo-Bot-Auto-Hunt.git
   ```
  
2. Install the required dependencies:
   
   ```bash
   pip install requests
   ```
   
3. Run the script:
   ```bash
   python main.py
   ```


## Usage

1. Configure the program in the config.py file with the required variables:
   ```
   token = ''
   channel_id = ''
   randomize_delay = True
   min_random_delay = 1
   max_random_delay = 5
   base_delay = 12
   command = 'wh'
   ```

## Contributing

We welcome contributions from the community! If you'd like to contribute to the project, please follow these steps:

1. **Fork the Project:** Start by forking the project to your own GitHub account using the "Fork" button at the top right of this repository.
2. **Create a New Branch:** Create a new branch in your forked repository. This branch will be dedicated to your feature, enhancement, or bug fix.
3. **Make Changes:** Implement your desired changes, whether it's a new feature, improvement, or fixing a bug. Please ensure your code adheres to the project's coding standards.
4. **Commit Your Changes:** Commit your changes with clear and concise commit messages that describe the purpose of each change.
5. **Push to Your Fork:** Push your changes to your forked repository on GitHub.
6. **Create a Pull Request:** Once you've pushed your changes to your fork, go to the original repository and create a pull request. Provide a detailed description of your changes and why they are valuable.

## License

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.

---

If you have any questions, issues, or suggestions, feel free to open an [issue](https://github.com/Devuxious/Owo-Bot-Auto-Hunt/issues).


<p align="center">
  <img src="https://img.shields.io/github/license/Devuxious/Owo-Bot-Auto-Hunt.svg?style=for-the-badge&labelColor=black&color=FF7F7F&logo=IOTA"/>
  <img src="https://img.shields.io/github/stars/Devuxious/Owo-Bot-Auto-Hunt.svg?style=for-the-badge&labelColor=black&color=FF7F7F&logo=IOTA"/>
  <img src="https://img.shields.io/github/languages/top/Devuxious/Owo-Bot-Auto-Hunt.svg?style=for-the-badge&labelColor=black&color=FF7F7F&logo=python"/>
</p>
