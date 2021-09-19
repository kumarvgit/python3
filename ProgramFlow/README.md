### anything which has __iter__ ot __getItem__ is an iterable
### String is immutable
### reassignment gives a new value i.e creates a new object hence id of 
> object id is going to change unlike java where reassignment is allowed

### MOst function which operate on object does not return any value like list.sort() - this sorts the list directly

### Dict needs an immutable object as key

#### Data and time is stored as 32 bit signed integer since 1 jan 1970, this is going to overflow sometime in Feb, 2038 since it will go out of range of int, on 32bit combuters

#### it is a good idea to convert the time to UTC otherwise it would not be possible to tell if the date was changed because e.g. 1:30 AM on 25 oct there is no way to tell if this time is before clock shift or after time shift 

#### adding parenthesis to a function calls a function but if we do not add () then it is assignment to something
> fi() calling
> command=fi assignment ro command

#### if arg starts with * then it is a variable number of params

#### Shadow variable -> when we define a local variable as same name as outer world i.e. the caller, this function can not access the variable in caller function since local variable is of same name. this is called shadowing
#### when we shadow a global variable python creates a local variable and we no longer have access to global variable, this is only possible when we are reassigning the variable but not the read or accessing the variable

#### global keyword inside the functions directs python to access global scope of the variable and modify it

#### starts with _ var or func it is considered protected