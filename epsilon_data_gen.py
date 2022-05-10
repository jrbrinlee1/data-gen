import math
import random
import string
import argparse

# configure argument parser
PARSER = argparse.ArgumentParser(description="A program that generates data similar to Epsilon's data", epilog="Thanks!")

PARSER.add_argument("-r", "--record-count",    help="approximate number of records to generate", default="10000")
PARSER.add_argument(      "--unique-segs",     help="unique values / cardinality of the segs field", default="1000")
PARSER.add_argument(      "--unique-vendor",   help="unique values / cardinality of the vendor_type_owner_list field", default="1000")
PARSER.add_argument(      "--max-segs",        help="max seg values associated with a single record", default="10")
PARSER.add_argument(      "--min-segs",        help="min seg values associated with a single record", default="1")
PARSER.add_argument(      "--max-vendor",      help="max vendor values associated with a single record", default="10")
PARSER.add_argument(      "--min-vendor",      help="min vendor values associated with a single record", default="1")
PARSER.add_argument("-f", "--file-count",      help="number of files to write to", default="1")

# parse args and store in dict()
ARGV = PARSER.parse_args()
argv = vars(ARGV)

# make sure we have int vals as args
try:
	for k, v in argv.items():
		argv[k] = int(v)
except ValueError:
	print(f"ERROR: '{v}' is not an int - the value of {k} should be an int")
	exit()

# generate list of id_types, segments, and vendor_type_owner_list vals (segs and vendor_types may contain dups)
id_types = ['type0001', 'type0002', 'type0003']
segs = [''.join(random.choices(string.ascii_letters + string.digits, k=4)) for _ in range(argv["unique_segs"])]
vendor_types = [''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(15, 100))) for _ in range(argv["unique_vendor"])]

for i in range(argv["file_count"]):
	with open(f"data_{i}.csv", "w") as f:
		for i in range(math.ceil(argv["record_count"] / argv["file_count"])):
			# pick an id_type, random number of segments, and random number of vendor_type_owner vals - then, write record to file
			id_type = random.choices(id_types)[0]
			seg_list = ",".join(random.sample(segs, math.floor(random.triangular(argv["min_segs"],argv["max_segs"],1))))
			vendor_list = ",".join(random.sample(vendor_types, math.floor(random.triangular(argv["min_vendor"],argv["max_vendor"],1))))
			f.write(f'{"".join(random.choices(string.ascii_letters + string.digits, k=32))},{id_type},"{seg_list}","{vendor_list}"\n')

