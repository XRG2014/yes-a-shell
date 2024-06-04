# The "Yes" command for iOS/iPadOS [a-Shell](https://holzschu.github.io/a-Shell_iOS)
The classic "Yes" command from linux now made for iOS/iPadOS a-Shell

> Coded in python

> Please note that this is not an official release of the "Yes" command, and that this program may not include every feature and some may be changed or tweaked

## Table of Contents:

- [Install](/#install)
- [Uninstall](/#uninstall)
- [Help Text](/#help-text)

### Install:

Run these commands in a-Shell:

```
mkdir -p ~/Documents/yes
curl https://github.com/XRG2014/yes-a-shell/blob/main/yes.py -o ~/Documents/yes.py
```

Now run **ONLY ONE** of the commands shown below:

> _This one uses ```~/Documents/.bashrc```_:

```
echo 'alias yes="python3 -ub ~/Documents/yes/yes.py"' | tee -a ~/Documents/.bashrc
```

> _This one uses ```~/Documents/.profile```_:

```
echo 'alias yes="python3 -ub ~/Documents/yes/yes.py"' | tee -a ~/Documents/.profile
```

### Uninstall:

Run this command in a-Shell:

```
rm -rfv ~/Documents/yes
```

Now find this line and remove it in ```~/Documents/.bashrc``` or ```~/Documents/.profile``` (Which ever file you used to install the yes command):

> If the line doesn't exist in a file then the "Yes" command might already be uninstalled

```
alias yes="python3 -ub ~/Documents/yes/yes.py"
```

### Help Text:

```
Usage: yes [STRING]...
  or:  yes OPTION
Repeatedly output a line with all specified STRING(s), or 'y'.
      --help        display this help and exit
      --version     output version information and exit
```
