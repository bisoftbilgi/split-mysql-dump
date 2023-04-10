The script extracts a specified database from a mysqldump file and writes it to an output file.
The "--database" argument is used to specify the name of the database to extract, the "--dump" argument is used to specify the mysqldump file, the "--outfile" argument 
is used to specify the name of the output file.

Example:
Dump.sql stores x, y, z databases. We just want to print database x to file.

> python.exe .\split_dump.py --database x --dump dump.sql --outfile x_dump.sql