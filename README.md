# Node.js for [a-Shell](https://holzschu.github.io/a-Shell_iOS)
A version of Node that I coded for ios a-Shell. It uses the jsc command, and it includes a fake NVM (Node Version Manager).

### Install (for a-Shell):

Run these commands in a-Shell:

```
mkdir -p ~/Documents/.nvm/bin
lg2 clone https://github.com/XRG2014/Node.js-a-Shell.git
cd Node.js-a-Shell.git
mv .nvm/bin/node.py ~/Documents/.nvm/bin
mv .nvm/bin/nvm.py ~/Documents/.nvm/bin
cd ..
rm -rfv Node.js-a-Shell.git
```

Now run **ONLY ONE PAIR** of commands shown below:

> _This one uses ```~/Documents/.bashrc```:_
```
echo 'alias nvm="python3 -ub ~/Documents/.nvm/bin/nvm.py"' | tee -a ~/Documents/.bashrc
echo 'alias node="python3 -ub ~/Documents/.nvm/bin/node.py"' | tee -a ~/Documents/.bashrc
```

> _This one uses ```~/Documents/.profile```:_
```
echo 'alias nvm="python3 -ub ~/Documents/.nvm/bin/nvm.py"' | tee -a ~/Documents/.profile
echo 'alias node="python3 -ub ~/Documents/.nvm/bin/node.py"' | tee -a ~/Documents/.profile
```

### Uninstall (for a-Shell)

Run these commands in a-Shell:

```
cd ~/Documents
rm -rfv .nvm
```

Now find these lines and remove them in ```~/Documents/.bashrc``` and ```~/Documents/.profile``` (if one file doesn't exist, then do the other one):

```
alias nvm="python3 -ub ~/Documents/.nvm/bin/nvm.py"
alias node="python3 -ub ~/Documents/.nvm/bin/node.py"
```
