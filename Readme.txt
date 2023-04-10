The script extracts a specified database from a mysqldump file and writes it to an output file.
The "--database" argument is used to specify the name of the database to extract, the "--dump" argument is used to specify the mysqldump file, the "--outfile" argument 
is used to specify the name of the output file.

Example:
Dump.sql stores x, y, z databases. We just want to print database x to file.

options:
  -h, --help                        Show this help message and exit
  --database DATABASE, -D DATABASE  Name of the database to extract
  --dump DUMP, -d DUMP              Mysqldump file
  --outfile OUTFILE, -o OUTFILE     Name of the file for output
						
> python.exe .\split_dump.py --database x --dump dump.sql --outfile x_dump.sql
