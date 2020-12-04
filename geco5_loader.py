from tqdm import tqdm
from string_utils import StringIteratorIO
from db_utils import db
from files_utils import *
from general_utils import chromosomes

import sys

# print(len(sys.argv))

if len(sys.argv) == 4:
    directory = sys.argv[1]
    database_name = sys.argv[2]
    table = sys.argv[3]
else:
    # input!!!!
    directory = '/Users/canakoglu/GMQL-sources/geco_agent_loader/input/'
    database_name = 'GRCh38_TCGA_gene_expression_2018_12'
    table = 'arif.gene_expression_arif_test1'
binning = False
bin_size = 100000

is_reduced_columns = False
reduced_columns = {0, 1, 2, 3, 8, 9}

pos_chr = 0
pos_strand = 3

all_ids = db.get_item_ids(database_name)

files = get_files_triple(directory)


# print(files)

def lines(files, database):
    aaa = 0
    bbb = 0
    # files = files[:100]
    for file_name, reg_file, meta_file in tqdm(files):
        # print(aaa)
        item_id = all_ids[file_name]  # get_item_id(database, file_name)
        item_id = item_id
        # print(file_name, item_id)

        with open(reg_file) as f:
            for line_number, line in enumerate(f):
                # if aaa % 1000 == 0 :
                #     print(aaa , bbb)

                line = line.rstrip('\n')
                line_split = line.split('\t')

                if is_reduced_columns:
                    line_split = [x[1] for x in enumerate(line_split) if x[0] in reduced_columns]

                if line_split[pos_chr] not in chromosomes:
                    # NOTE: becarefull about the new chromsomes
                    #                 print(file_name, splitted[0])
                    # gives error
                    # SKIP THE LINE
                    print(f'ERROR in the chromosome File:{file_name}:{line_number}, error: {line_split[pos_chr]}')
                    continue
                else:
                    line_split[pos_chr] = str(chromosomes[line_split[0]])

                if pos_strand >= 0:
                    if line_split[pos_strand] == '+':
                        line_split[pos_strand] = '1'
                    elif line_split[pos_strand] == '-':
                        line_split[pos_strand] = '-1'
                    else:
                        line_split[pos_strand] = '0'

                # one base conversion!!!!
                line_split[1] = str(int(line_split[1]) - 1)

                line_joined = "\t".join(line_split)

                aaa += 1
                if not binning:
                    y_str = f"{item_id}\t{line_joined}\n"
                    yield y_str

                else:
                    start_bin = int(line_split[1]) // bin_size
                    end_bin = int(line_split[2]) // bin_size
                    y_str = f"{item_id}\t{line_joined}\t{{}}\t{start_bin}\n"

                    for b in range(start_bin, end_bin + 1):
                        bbb += 1

                        yield y_str.format(b)

        # break
    print("aaa", aaa, "bbb", bbb)


str_io = StringIteratorIO(lines(files, database_name))
# copy_from(None, f'region_repository.{table}')


db.copy_from(str_io, table)

# for x in str_io:
#     print(x)
