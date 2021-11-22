### variable naming convention
    1 cannot start with number
    2 can contain _ and numbers
    3 variables are case sensative
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

#### starts with underscore var or func it is considered protected
####  underscore is called throw away variable
> a throw away variable
> name, this is escape char\_, _ = person_details
> print(name)
> print(_)

#### We can define function inside function in python
#### non local
> nonlocal scope rather it is in the parent function i.e. enclosing scope
> we can not re assign a value in non local scope
> effectively nonlocal tab_stop = 0 will give error
> unlike global in shadowing case python creats a local variable but in nonlocal case it wont create the variable

#### LEGB - PYTHON variable resolution stratgey
> L local
> E enclosing
> G global
> B Builtins

#### Fields are called attributes in python
#### methods are bound to class and will have self on the other hand functions dont have self in their defs
#### Python conventions 
    1 Class: template for creating objects. All objects created using the same class will have the same characteristics.
    2 Object: an instance of a class.
    3 Instantiate: create an instance of a class.
    4 Method: a function defined in a class.
    5 Attribute: a variable bound to an instance of a class.
    6 Instance objects are only bound to a an instance of the object but not to class
        > kettle obj has 2 attribute make and proce,
        > if we add dynamically a variable called power to instance k1 then instance variable 
        > k2 will not have access to the same

## Init is not a constructor
> Init method is not necessarly a constructor in beyond python 2.2 
since in python the object creation is a two step process
    1. new method creates an object
    2. init method provides customization to it which is called by new method

#### Data mangling
> When we start a var or a method name with __ python
> automatically mangles the data i.e. it prefixe the attribut name
> with _<class_name><VAR_NAME>
> e.g. a var in class is __amount in Accounts class the effective variable name would be
> _Accounts__amount


#### raw strings (changes the way python interprets the string with or without escape chars) -> r"i can include \t in string"
#### every thing in python is an object including a method
    
#### Python does not have construtor overloading constructor, same is achieved through named params
#### Overriding a method is equal to same name no matter if params changes

#### *args - Unpacks a tuple
#### **kwargs unpacks a dictionary
#### rage is a generator