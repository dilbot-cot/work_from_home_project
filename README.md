# Work From Home Log

This application is designed to keep a log of work from home activities for a given range of dates.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need Python 3 installed on your machine. This application is developed using Python 3.9, but it should work with any version of Python 3.

### Installing

To get this project running on your local machine, follow these steps:

1. Clone the repository or download the project as a zip file and extract it.
2. Navigate to the project root directory in the terminal.
3. Make the shell script executable by running the command `chmod +x run.sh`.
4. Run the shell script with the command `./run.sh` to start the application.

## Usage

When the program starts, it will attempt to load previous entries from `WFH_log.csv` on your desktop. If the file does not exist or has been moved or renamed, the program will start a new log and prompt you to enter whether you worked from home for each weekday from July 1, 2023, to June 30, 2024.

You can enter `y` for Yes, `n` for No, or `exit` to stop the program. For the start and end times, please enter them in a 24-hour format (hh:mm).

The log of your work from home activities will be saved as `WFH_log.csv` on your desktop. The file will contain the date, whether you worked from home, and your start and end times. It will also show the total hours you worked from home at the end of the file.

Please note: If you remove, rename, or delete the `WFH_log.csv` file, the program will not be able to load previous data, and you will be prompted to enter data starting from July 1, 2023.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

* OpenAI for providing the language model GPT-4 that helped create this project.