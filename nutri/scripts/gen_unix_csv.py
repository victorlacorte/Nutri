import csv

from nutri.taco_client import fmt_description
from nutri.taco_meta import TacoHeader


def main():
    fieldnames = TacoHeader._fields
    # restval = 'NA'
    # extrasaction = 'ignore'
    # dialect = 'unix'
    with open('nutri/data/Taco_4a_edicao_2011.csv', 'r') as fin, \
         open('nutri/data/taco_unix.csv', 'w') as fout:
        reader = csv.DictReader(
                    fin,
                    fieldnames=fieldnames,
                    dialect='excel')
        writer = csv.DictWriter(
                    fout,
                    fieldnames=fieldnames,
                    dialect='unix',
                    restval='NA')
        # Skip reader's header
        next(reader)
        writer.writeheader()
        for row in reader:
            for k, v in row.items():
                if v == '' or v == ' ':
                    row[k] = 'NA'
                else:
                    row[k] = v.strip()
            row['description'] = fmt_description(row.get('description'))
            writer.writerow(row)
