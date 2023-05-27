# RealRestorer
This is a small automation project. Its function is to restore a PostgreSQL database in a development environment. It is designed to work together with Tecnativa's doodba-copier-template repository.

## How to use
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
