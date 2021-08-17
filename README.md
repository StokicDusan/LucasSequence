# Lucas Sequence

Lucas Sequence L is a sequence of numbers such that L(n) = L(n-1) + L(n-2)

## What does the script do?
The script prints numbers of the Lucas Sequence on the command line or just the last number given the number if iterations.

## `lucasSequence.py` :
This script is ready to use script which uses three arguments. The 
arguments determine the values for L(0) and L(1) and how many iterations to go through, respectively.

### lucas_sequence:
Function prints numbers divided by a space character.  
Invoking the script runs this function.
### lucas_sequence_timer:
Function prints numbers divided by a space character and 
the time taken for the calculation.
### lucas_sequence_last:
Function prints the last number in the sequence.
### lucas_sequence_last_timer:
Function prints the last number in the sequence and 
the time taken for the calculation.
## Installing the dependencies

### Used packages
This script require the time, math, sys and doctest package.

## How to use it
#### 1. Clone this repository:
```zsh
$> git clone https://github.com/StokicDusan/LucasSequence
$> cd LucasSequence/
```
#### 2. Launch:
In the command line simply invoke the script with three arguments:
```zsh
$> python lucasSequence.py argv1 argv2 argv3 
```
* argv1, argv2:  
Any integer 
* argv3:  
Any positive integer  

:warning: *Note:* Other inputs will result in an error


Invoking the script with no or less arguments will run testmod().
