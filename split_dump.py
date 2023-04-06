import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--database","-D",help="Name of the database to extract")
parser.add_argument("--dump","-d",help="mysqldump file")
parser.add_argument("--outfile","-o",help="Name of the file for output")
args = parser.parse_args()
print(f"Extracting {args.database} database from {args.dump}")

try: 
    outfile = open(args.outfile, "a", encoding='utf-8')
    with open(args.dump, "r",encoding='utf-8') as dump_file: 
       find = False
       for line in dump_file:
           if line.startswith("CREATE DATABASE /*!32312 IF NOT EXISTS*/"):
               print(line);

           if line.startswith(f"CREATE DATABASE /*!32312 IF NOT EXISTS*/") and find == True:
               find = False
               print(f"CREATE DATABASE /*!32312 IF NOT EXISTS*/ `{args.database}`");

           if line.startswith(f"CREATE DATABASE /*!32312 IF NOT EXISTS*/ `{args.database}`"):
               find = True
               print(f"CREATE DATABASE /*!32312 IF NOT EXISTS*/ `{args.database}`");

           if find == True:
               outfile.write(line)
    outfile.close()


except FileNotFoundError:
    print("Dump dosyası boştur")
