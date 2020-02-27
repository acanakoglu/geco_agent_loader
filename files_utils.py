import os


def get_file_name(path):
    return path.split('/')[-1]


def list_files(directory):
    files = os.listdir(directory)
    files = [os.path.join(directory, f) for f in files]
    return files


def get_files_triple(directory):
    ls_list = list_files(directory)
    meta_set = set(filter(lambda x: x.endswith("meta"), ls_list))
    return [(get_file_name(x), x, x + ".meta") for x in ls_list if x + ".meta" in meta_set]


# def get_schema_path(ls_list):
#     return next(filter(lambda x: x.endswith("schema.xml"), ls_list))  # possibly test.schema

# def parse_schema(schema_path):
#     #     schema_path = get_schema_path(ls_list)
#     with hdfs.open(schema_path) as f:
#         tree = ET.parse(f)
#         return [(x.text, x.get('type')) for x in tree.getiterator() if x.tag.endswith("field")]
#
#
#

