# RealRestorer
This is a small automation project. Its function is to restore a PostgreSQL database in a development environment. It is designed to work together with Tecnativa's doodba-copier-template repository.

## How to setup
1. Navigate to your copier enviroment proyect and run the following command:
```
  mkdir backups
```
Inside the '/backups' folder we will save the backups of the database (SQL File and Filestore).

2. Then clone the repository in the copier enviroment project
```
  git clone https://github.com/LingerANR/RealRestorer.git
```  
3. Navigate to the repository directory
```
  cd RealRestorer
```
4. Execute the requeriments file
```
  pip install -r requirements.txt
```
5. Execute the main file
```
  python3 main.py
```
## How to use

- The proyect need to look like this
```
/doodba-copier-template-proyect
  |_ /backups
  |  |_ happydb_24_05_23.sql
  |  |_ filestore_happydb_24_05_23.tar.gz
  |_ /RealRestore
```
- When we run the main.py program, the first thing it will ask for is "Search Word".
Here the keyword of the files will be entered (to avoid copying and pasting)
```
Search Word: happydb
FILE FOUND: happydb_24_05_23
```
And that's it, the next thing is to specify the value of the variables:

```Data Base:``` The name of the database you want to designate. If a database with the same name already exists in your environment, it will delete the database and create a new one with the same name.

```Filestore Data Base:``` The name of the database that is inside the Filestore.

Ready! Now all that remains is to wait for the backup to be made :)

