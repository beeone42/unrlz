# unrlz

unrar rlz

## need libunrar:

- get UnRAR source: http://www.rarlab.com/rar_add.htm (http://www.rarlab.com/rar/unrarsrc-5.4.5.tar.gz)
- install libunrar (see http://doublecmd.sourceforge.net/forum/viewtopic.php?f=5&t=2267):

```
sudo apt-get update
sudo apt-get install build-essential
wget http://www.rarlab.com/rar/unrarsrc-5.4.5.tar.gz
tar xvfz unrarsrc-5.4.5.tar.gz
cd unrar
make -f makefile lib
sudo make install-lib
sudo ldconfig
```

## install python unrar (https://pypi.python.org/pypi/unrar/):

```
sudo apt-get install python-pip
pip install unrar
```
