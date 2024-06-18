# File Sorting Script

This Python script helps organize files in a specified directory into categorized folders based on file extensions. It supports custom sorting rules through a configuration file and allows modifications to these rules via command line arguments.

## Features

- **Automatic Sorting:** Moves files into predefined or custom folders based on their extensions.
- **Configuration Flexibility:** Users can define, modify, or delete sorting rules in a JSON configuration file.
- **Other Category:** Unmatched files are moved to an 'Other' folder, ensuring all files are sorted.
- **Self-exclusion:** The script and its configuration file are automatically excluded from sorting.

## Installation

To use this script, you need Python installed on your system. Python 3.6 or higher is recommended. You can download Python from [python.org](https://www.python.org/downloads/).

 **Clone the repository**:

   ```bash
   git clone https://github.com/your_username/FlexiSort.git
   cd  FlexiSort
   ```

##Configuring Sorting Rules

The default configuration file config.json will be created in the directory where you run the script if it does not exist. You can modify this file directly, or use the script commands to alter sorting rules:
Add a new rule:

python run.py /path/to/directory --action add --folder "NewFolder" --pattern "\\.file_extension$"

Modify an existing rule:
python run.py /path/to/directory --action modify --folder "ExistingFolder" --pattern "\\.new_pattern$"

## Usage

To sort files in a directory, run the script from the command line with the directory path:

```bash
python run.py /path/to/directory
```

### Configuration

The default configuration file `config.json` will be created in the directory where you run the script if it does not exist. You have two options for modifying this configuration:

1. **Direct Modification**: Open the `config.json` file in a text editor and modify the sorting rules as needed. Each rule associates file extensions with a designated folder.

2. **Using Script Commands**: You can also modify the configuration by running the script with specific command-line arguments. Here are the commands you can use:

#### Add a new rule:

```bash
python run.py /path/to/directory --action add --folder "NewFolder" --pattern "\.(file_extension)$"
```

#### Modify an existing rule:

```bash
python run.py /path/to/directory --action modify --folder "ExistingFolder" --pattern "\.(new_pattern)$"
```

#### Delete an existing rule or folder:

```bash
python run.py /path/to/directory --action delete --folder "FolderName"
```

To delete an entire folder category, omit the `--pattern` argument.

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**. 🙌

If you have suggestions for how we could improve the script or additional features you think would be useful, your contributions are welcome! Here’s how you can contribute:

1. **Fork the Repository**: Fork the project on GitHub. This means you’ll have your own copy of the project that you can modify.

2. **Create your Feature Branch**: From your fork, create a branch with a name that describes the feature or improvement you’d like to make. For example:
   ```bash
   git checkout -b feature/YourFeature
   ```
