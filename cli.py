import argparse as ags

parser = ags.ArgumentParser()
parser.add_argument("filename")
parser.add_argument("name_json_file")


args = parser.parse_args()
arquivo_html = args.filename
