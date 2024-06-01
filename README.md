# The "Yes" command for iOS/iPadOS [a-Shell](https://holzschu.github.io/a-Shell_iOS)
The classic "Yes" command from linux now made for iOS/iPadOS a-Shell.

> Coded in python

> This program does not include the --version flag

> Please note that this is not an official release of the "Yes" command, and that it may not include every feature

### Install:

Run these commands in a-Shell:

```
mkdir -p ~/Documents/bin/yes
curl https://github.com/XRG2014/yes-a-shell/blob/main/bin/yes.py -o ~/Documents/bin/yes.py
```

Now run **ONLY ONE** of the commands shown below:

> _This one uses ```~/Documents/.bashrc```_:

```
echo 'alias yes="python3 -ub ~/Documents/bin/yes/yes.py"' | tee -a ~/Documents/.bashrc
```

> _This one uses ```~/Documents/.profile```_:

```
echo 'alias yes="python3 -ub ~/Documents/bin/yes/yes.py"' | tee -a ~/Documents/.profile
```

### Uninstall:

Run this command in a-Shell:

```
rm -rfv ~/Documents/bin/yes
```

Now find this line and remove it in ```~/Documents/.bashrc``` and ```~/Documents/.profile```, or which ever file you used to install the yes command:

(If the line doesn't exist in a file then you can ignore it and/or go to the next one.)

```
alias yes="python3 -ub ~/Documents/bin/yes/yes.py"
```
