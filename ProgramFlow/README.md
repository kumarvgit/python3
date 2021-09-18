### anything which has __iter__ ot __getItem__ is an iterable
### String is immutable
### reassignment gives a new value i.e creates a new object hence id of 
> object id is going to change unlike java where reassignment is allowed

### MOst function which operate on object does not return any value like list.sort() - this sorts the list directly

### Dict needs an immutable object as key

#### Data and time is stored as 32 bit signed integer since 1 jan 1970, this is going to overflow sometime in Feb, 2038 since it will go out of range of int, on 32bit combuters

#### it is a good idea to convert the time to UTC otherwise it would not be possible to tell if the date was changed because e.g. 1:30 AM on 25 oct there is no way to tell if this time is before clock shift or after time shift 
