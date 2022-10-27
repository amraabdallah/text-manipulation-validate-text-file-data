## Requirments:

* If the record has an FQDN Email address and has a valid ID number
* The script should print to the stdout: the $ID of $EMAIL is an even|odd number.
* If the record doesn't have a valid Email or ID, it should continue silently.

## The text file has the following data:

```
John john@domain.com 325
Susan 510
Jane jane@domain.com 131
Karl karl@domain.com
Bert bert@localhost 150
```

## Scripts

I created two scripts _with the same functionality_ which can process the text file to get the desired output
* The first one is a bash shell script [textMan.sh](./textMan.sh) 
* The other is a python script [textMan.py](./textMan.py)