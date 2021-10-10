[![Contributors][contributors-shield]][contributors-url]
[![Commit-activity][commit-activity-shield]][commit-activity-url]
[![Issues][issues-shield]][issues-url]
[![Repo-size][repo-size-shield]][repo-size-url]
[![License][license-shield]][license-url]  
[![Forks][forks-shield]][forks-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

# Welcome to LucasSequence

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
```bash
$ git clone https://github.com/StokicDusan/LucasSequence
$ cd LucasSequence/
```
#### 2. Launch:
In the command line simply invoke the script with three arguments:
```bash
$ python lucasSequence.py argv1 argv2 argv3 
```
* argv1, argv2:  
Any integer 
* argv3:  
Any positive integer  

:warning: *Note:* Other inputs will result in an error

Invoking the script with no or less arguments will run testmod().

## Examples

The following code block shows examles of calling the lucasSequence script from terminal.
```bash
$ python3 lucasSequence.py 0 0 6
0 0 0 0 0 0 

$ python3 lucasSequence.py 2 1 10
2 1 3 4 7 11 18 29 47 76 

$ python3 lucasSequence.py 1 1 12
1 1 2 3 5 8 13 21 34 55 89 144 

$ python3 lucasSequence.py 2308 4261 5
2308 4261 6569 10830 17399

$ python3 lucasSequence.py 5 -20 4
5 -20 -15 -35
```

## Provide Feedback 👍

If you encounter any bugs or have suggestions, please file an issue in the
[Issues][issues-url]
section of the project.

[contributors-shield]: https://img.shields.io/github/contributors/StokicDusan/LucasSequence
[contributors-url]: https://github.com/StokicDusan/LucasSequence/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/StokicDusan/LucasSequence?style=social
[forks-url]: https://github.com/StokicDusan/LucasSequence/network/members
[issues-shield]: https://img.shields.io/github/issues/StokicDusan/LucasSequence
[issues-url]: https://github.com/StokicDusan/LucasSequence/issues
[commit-activity-shield]: https://img.shields.io/github/last-commit/StokicDusan/LucasSequence
[commit-activity-url]: https://github.com/StokicDusan/LucasSequence/graphs/commit-activity
[license-url]: https://github.com/StokicDusan/LucasSequence/blob/main/LICENSE
[license-shield]: https://img.shields.io/github/license/StokicDusan/LucasSequence
[repo-size-shield]: https://img.shields.io/github/repo-size/StokicDusan/LucasSequence
[repo-size-url]: https://img.shields.io/github/repo-size/StokicDusan/LucasSequence
[linkedin-shield]: https://img.shields.io/badge/LinkedIn-0077B5?style=plastice&logo=linkedin&logoColor=white
[linkedin-url]: https://linkedin.com/in/stokicdusan
