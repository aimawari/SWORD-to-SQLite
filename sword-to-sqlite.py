from pysword.modules import SwordModules
import argparse 
import sys
import sqlite3
import time

if sys.version_info > (3, 0):
    from past.builtins import xrange

def loadingBar(count,total,size):
    percent = float(count)/float(total)*100
    sys.stdout.write("\r" + str(int(count)).rjust(3,'0')+"/"+str(int(total)).rjust(3,'0') + ' [' + '='*int(percent/10)*size + ' '*(10-int(percent/10))*size + ']')

def generate_sqlite(source, bible_version):
    # Create sqlite file
    db = sqlite3.connect(bible_version+".sqlite", isolation_level=None)

    # Create table if not exists
    db.cursor().execute("CREATE TABLE IF NOT EXISTS key_"+bible_version+" (book Int,name varchar);")
    db.cursor().execute("CREATE TABLE IF NOT EXISTS "+bible_version+" (book Int,chapter Int,verse Int,text varchar);")

    # Define query
    query_key = "INSERT INTO key_"+bible_version+" values (?,?)"
    query_verse = "INSERT INTO "+bible_version+" values (?,?,?,?)"
    query_delete = "DELETE FROM "

    # Remove table if any exists
    db.cursor().execute(query_delete+"key_"+bible_version)
    db.cursor().execute(query_delete+bible_version)

    # Get books data from module
    modules = SwordModules(source)
    found_modules = modules.parse_modules()
    bible = modules.get_bible_from_module(bible_version)

    books = bible.get_structure()._books['ot'] + bible.get_structure()._books['nt']
    
    for idx,book in enumerate(books, start=1):
        loadingBar(idx,len(books),2)
        db.cursor().execute(query_key,(idx,book.name))
        for chapter in xrange(1, book.num_chapters+1):
            for verse in xrange(1, len(book.get_indicies(chapter))+1 ):
                db.cursor().execute(query_verse,(idx,chapter,verse,bible.get(books=[book.name], chapters=[chapter], verses=[verse])))

    print("Yay!!")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--source', help='Zipped module file location (EX: KJV.zip)')
    parser.add_argument('-bv','--bible_version', help='Name of the module (EX: KJV)')
    args = parser.parse_args()

    generate_sqlite(args.source, args.bible_version)

if __name__ == "__main__": main()
