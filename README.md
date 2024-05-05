# Yes command for iOS/iPadOS [a-Shell](https://holzschu.github.io/a-Shell_iOS)
The classic yes command from linux now made for iOS/iPadOS a-Shell. Coded in python.

### Install (for a-Shell):

Run these commands in a-Shell:

```
mkdir -p ~/Documents/bin/yes
curl https://github.com/XRG2014/Yes-a-Shell/blob/main/bin/yes.py -o ~/Documents/bin/yes.py
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

### Uninstall (for a-Shell)

Run this command in a-Shell:

```
rm -rfv ~/Documents/bin/yes
```

Now find this line and remove it in ```~/Documents/.bashrc``` and ```~/Documents/.profile``` (If one file doesn't exist, then do the other one. And if the line doesn't exist in one of the files, then just ignore it.):

```
alias yes="python3 -ub ~/Documents/bin/yes/yes.py"
```
