## SWORD to SQLite – Generate .sqlite files from SWORD Project

Generate .sqlite files from [SWORD project](http://crosswire.org/sword/modules/ModDisp.jsp?modType=Bibles) 

```
key_KJV (Table name is changed depend on BIBLE_VERSION)
| book | name    |
|------|---------|
| 1    | Genesis |
| 2    | Exodus  |
| ...  | ...     |

KJV (Table name is changed depend on BIBLE_VERSION)

| book | chapter | verse | text                                                   |
|------|---------|-------|--------------------------------------------------------|
| 1    | 1       | 1     | In the beginning God created the heaven and the earth. |
| 1    | 1       | 2     | And the earth was without form, and void; ...          |
| ...  | ...     | ...   | ...                                                    |
```



### How to

This project require pysword. Please install : `pip install pysword`

```
python3 sword-to-sqlite.py -s SOURCE -bv BIBLE_VERSION
```
or
```
python3 sword-to-sqlite.py --source SOURCE --bible_version BIBLE_VERSION
```

| Tables        |  Description                              |
| ------------- | ---------------------------------------:  |
| SOURCE        | Zipped module file location (EX: KJV.zip) |
| BIBLE_VERSION | Name of the module (EX: KJV)              |

#### Example
```
python3 sword-to-sqlite.py -s KJV.zip -bv KJV
```
