# rmrf

```rmrf``` is meant to *worldwidely* replace ```rm``` to delete files and folders. This is a safer version, as it doesn't really delete the files/folders, but just moves them to a temporary folder. This way, you can recover them if you made a mistake (You have less than 10 seconds).

## Why rmrf ?

I've made this tool because I'm tired of typing ```rm -rf``` and then regretting it. I've lost a lot of files and folders this way, and I'm sure I'm not the only one. So, I've decided to make a safer version of ```rm```.

## Output example
![rmrf output](img/demo.gif?raw=true "rmrf output")

## Installation
Well, first, you need Python. What's funny is that you can download Python with **[g8](https://www.github.com/MCXIV/g8)** hahaha.

Then, just type
```python3 setup.py install```
(You may need to install manually the dependencies, see ```requirements.txt```)

Create an alias like this to override the default ```rm``` command:
```alias rm=rmrf```

## Usage
Just type ```rm``` followed by the files or folders you want to delete.
If you made a mistake, you can recover the files by typing ```rmundo```: it will move the files back to their original location.

Be careful, you have less than 10 seconds to recover the files.

Alternatively, you can set the ```RMRF_TIMEOUT``` environment variable to change the timeout (in seconds).

## Examples
```rm file*```

```rm folder```

```rm file1 file2 file3```

```rm folder/file```

```rm file1 folder/file2```
