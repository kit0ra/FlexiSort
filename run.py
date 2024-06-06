import os
import shutil
import json
import re
import argparse
import sys

def load_config(config_path):
    # Check if config exists, create default if not
    if not os.path.exists(config_path):
        print("Configuration file not found. Creating a default configuration.")
        config = {
            "Programs": ["\\.exe$", "\\.bat$", "\\.py$", "\\.sh$"],
            "Images": ["\\.jpg$", "\\.png$", "\\.gif$", "\\.bmp$", "\\.svg$"],
            "Documents": ["\\.pdf$", "\\.docx$", "\\.txt$", "\\.odt$", "\\.xlsx$", "\\.pptx$"],
            "Videos": ["\\.mp4$", "\\.mov$", "\\.avi$", "\\.mkv$"],
            "Music": ["\\.mp3$", "\\.wav$", "\\.aac$", "\\.flac$"],
            "Other": []  # This will catch all unmatched files
        }
        save_config(config, config_path)
        return config
    else:
        print("Loading configuration file.")
        with open(config_path, 'r') as file:
            return json.load(file)

def save_config(config, config_path):
    with open(config_path, 'w') as file:
        json.dump(config, file, indent=4)
        print(f"Configuration saved to {config_path}")

def sort_files(directory, config, script_name, config_name):
    other_folder_path = os.path.join(directory, "Other")
    if "Other" not in config:
        config["Other"] = []  # Ensure there's an Other category in the config
        print("Adding 'Other' category to configuration.")
    if not os.path.exists(other_folder_path):
        os.makedirs(other_folder_path)
        
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and filename not in [script_name, config_name]:
            placed = False
            for folder, patterns in config.items():
                for pattern in patterns:
                    if re.search(pattern, filename):
                        target_folder = os.path.join(directory, folder)
                        if not os.path.exists(target_folder):
                            os.makedirs(target_folder)
                        shutil.move(file_path, os.path.join(target_folder, filename))
                        placed = True
                        break
                if placed:
                    break
            if not placed:
                shutil.move(file_path, os.path.join(other_folder_path, filename))
                print(f"Moved to 'Other': {filename}")

def modify_config(action, folder, pattern, config_path):
    config = load_config(config_path)
    if action == 'add':
        if folder in config:
            if pattern not in config[folder]:
                config[folder].append(pattern)
        else:
            config[folder] = [pattern]
    elif action == 'modify':
        if folder in config:
            config[folder] = [pattern]
        else:
            print("Folder not found in config.")
    elif action == 'delete':
        if folder in config:
            if pattern:
                if pattern in config[folder]:
                    config[folder].remove(pattern)
                    if not config[folder]:  # Remove folder if empty
                        del config[folder]
            else:
                del config[folder]
        else:
            print("Folder not found in config.")
    save_config(config, config_path)

def main():
    script_name = os.path.basename(sys.argv[0])
    parser = argparse.ArgumentParser(description="Sort files in a directory based on a configuration file.")
    parser.add_argument('directory', type=str, help="The directory to sort.")
    parser.add_argument('--config', type=str, default='config.json', help="Path to the configuration file.")
    parser.add_argument('--action', type=str, choices=['add', 'modify', 'delete'], help="Action to modify the config file.")
    parser.add_argument('--folder', type=str, help="Folder name for config modification.")
    parser.add_argument('--pattern', type=str, help="Regex pattern for the specified folder.")

    args = parser.parse_args()
    config_name = os.path.basename(args.config)

    if args.action:
        if not all([args.folder, args.pattern or args.action == 'delete']):
            print("Error: Folder and pattern must be specified for adding or modifying.")
            return
        modify_config(args.action, args.folder, args.pattern, args.config)
    else:
        config = load_config(args.config)
        sort_files(args.directory, config, script_name, config_name)

if __name__ == '__main__':
    main()
