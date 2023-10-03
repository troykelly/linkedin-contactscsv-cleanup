# LinkedIn Contacts CSV Cleanup Script

Managing a list of LinkedIn contacts effectively ensures you make the most of your network. This Python script aims to help you keep your LinkedIn contacts neat, accurate, and free from duplications.

## Description

This script has been finely tuned for cleaning up exported LinkedIn contact CSV files. It addresses the case of older LinkedIn accounts having repeated last names within the first name field and smartly merges duplicate contacts based on name, phone number, or email fields.

The script ensures strong validation of user inputs, creating a backup of original data for added safety. It showcases a progress bar during processing and maintains a detailed log of changes for later review. It also features a dry-run mode that shows the user how the cleaned data would appear before making permanent changes.

## Features

- Robust input validation for file existence, CSV format, and necessary columns
- Backup creation before processing
- Sophisticated algorithm to identify duplicates and merge them
- Detailed logging of changes
- Progress indication for better user experience
- Unit tests ensuring reliability
- Detailed report generation after CSV cleanup

## Requirements

* Python 3
* pandas (version 1.2.1)
* tqdm (version 4.61.2)

You can install required Python packages through pip as follows:

```bash
pip install -r requirements.txt
```

## Usage

The script can be used with command-line arguments as follows:

- `--source` PATH : Specifies the path of the source LinkedIn CSV file to be cleaned up. This argument is mandatory.
- `--destination` PATH : Specifies the path where the cleaned CSV data would be saved. If this argument is not provided, an '-updated' suffix will be added to the original file name.
- `--dry-run` : Enables a dry-run mode showcasing the cleaned-up data without actually overwriting the source file. This argument is optional.

An example of running the script:

```bash
python script.py --source contacts.csv
```

This command will clean up the file named 'contacts.csv' and will save the cleaned data into a new file named 'contacts-updated.csv'.

To specify a destination file:

```bash
python script.py --source contacts.csv --destination cleaned.csv
```

To run the script in dry-run mode:

```bash
python script.py --source contacts.csv --dry-run
```

Running unit tests:

```bash
python test_script.py
```
Please replace `script.py` with your actual script filename and `test_script.py` with the actual name of your test script.

## Contributing

Your contributions to this open-source project are most welcome. Feel free to fork the project, make desired changes, and open a pull request to contribute. For a major overhaul, we recommend opening an issue first to discuss the proposed changes.

## License

This project is licensed under the [Apache License 2.0](./LICENSE).
