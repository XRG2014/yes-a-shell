# Node.js-a-Shell
A version of Node that I coded for ios a-Shell. It uses the jsc command, and it includes a fake NVM (Node Version Manager).

### Install (for a-Shell):

Run these commands in a-Shell:

```
cd ~/Documents
mkdir -p .nvm/bin
lg2 clone https://github.com/XRG2014/Node.js-a-Shell.git
cd Node.js-a-Shell.git
mv .nvm/bin/node.py ../.nvm/bin
mv .nvm/bin/nvm.py ../.nvm/bin
cd ..
rm -rfv Node.js-a-Shell.git
```

Now add these lines to ```~/Documents/.bashrc``` or ```~/Documents/.profile```:

```
alias nvm="python3 -ub ~/Documents/.nvm/bin/nvm.py"
alias node="python3 -ub ~/Documents/.nvm/bin/node.py"
```

### Uninstall (for a-Shell)

Run these commands in a-Shell:

```
cd ~/Documents
rm -rfv .nvm
```

Now find these lines and remove them in ```~/Documents/.bashrc``` and ```~/Documents/.profile``` (if they exist):

```
alias nvm="python3 -ub ~/Documents/.nvm/bin/nvm.py"
alias node="python3 -ub ~/Documents/.nvm/bin/node.py"
```
