# Phone book

## Preview

![Preview](https://github.com/fiskirton/phonebook.github.io/blob/master/book.gif)

## Installing
### Dependencies
```
npyscreen>=4.10.5
python>=3.7
pip>=19.0.3
```
### Pip
```sh
pip install --user git+https://github.com/fiskirton/Phone-book.git
```
#### Run
```sh
phonebook
```
### Git clone
```sh
git clone https://github.com/fiskirton/Phone-book.git
cd Phone-book
pip install -r requirements.txt
```
#### Run
```sh
cd /path/to/Phone-book
python phonebook.py
```


## Key-bindings
* `←` `↑` `↓` `→` `TAB` - navigation
* `Shift+q` - exit
* `Shift+c` - restore list
* `e` - edit selected record
* `d` - delete selected record

## Functions
### Notice: <br>
>Only Latin characters and number in first and last name(can't start with numbers)<br>
>The phone number starts with 8 or +7<br>
>Date of birth is optional<br>

* `Add record` - add new record
* `Search` - search on any field or field combination
* `Delete(name&surname)` - delete a record by name and surname
* `Delete(number)` - delete a record by phone number (if there are several records with this number
they will be displayed on the screen)
* `Get age` - get the age of a person by name and surname
* `Get near birthdays` - get a list of nearby birthday
* `Search by age(>, <, = N)' - find people whose age is less than, greater than or equal to a given N
* `Clear records list` - delete all records
