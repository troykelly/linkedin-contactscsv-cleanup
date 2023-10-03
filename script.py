import pandas as pd
import argparse
import os
import logging
import unittest

from tqdm import tqdm
from pathlib import Path

REQUIRED_COLUMNS = ['FirstName', 'LastName', 'Emails', 'PhoneNumbers']

logging.basicConfig(filename='app.log', level=logging.INFO)


def csv_cleanup(source_file, destination_file, dry_run):
    filename, file_extension = os.path.splitext(source_file)
    if file_extension != '.csv':
        raise ValueError("File is not a CSV")

    if not os.path.isfile(source_file):
        raise FileNotFoundError("File does not exist")

    df = pd.read_csv(source_file, dtype=str)  # read the csv as string
    df.fillna('', inplace=True)  # fill all NaN values with empty string
    if not set(REQUIRED_COLUMNS).issubset(df.columns):
        raise Exception('CSV file does not contain required columns.')

    progress_bar = tqdm(total=len(df), desc='Processing',
                        bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}', dynamic_ncols=True)

    df['FirstName'] = df.apply(lambda row: row['FirstName'].replace(
        row['LastName'], '') if row['LastName'] in row['FirstName'] else row['FirstName'], axis=1)
    df['FirstName'] = df['FirstName'].str.strip()
    df['LastName'] = df['LastName'].str.strip()

    df = df.groupby(['FirstName', 'LastName', 'PhoneNumbers',
                    'Emails'], as_index=False).first()

    progress_bar.close()

    if dry_run:
        print(df)
    else:
        logging.info(f'Total rows processed: {len(df)}')
        df.to_csv(destination_file, index=False)


def main():
    parser = argparse.ArgumentParser(
        description='Clean up a LinkedIn contacts CSV file.')
    parser.add_argument('--source', required=True,
                        help='Source LinkedIn CSV file to be cleaned.')
    parser.add_argument('--destination', help='Destination LinkedIn CSV file.')
    parser.add_argument('--dry-run', action='store_true',
                        help='Run the clean-up in dry run mode without making changes.')

    args = parser.parse_args()

    if args.destination is None:
        filename, file_extension = os.path.splitext(args.source)
        args.destination = filename + '-updated' + file_extension

    csv_cleanup(args.source, args.destination, args.dry_run)


if __name__ == "__main__":
    main()
