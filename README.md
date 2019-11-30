<p align="center">
  <img width="350" height="350" src="https://raw.githubusercontent.com/sys113/negar/master/negar.png">
</p>

---
<div align="center">
  
![](https://img.shields.io/github/stars/SYS113/negar.svg)
![](https://img.shields.io/badge/language-python-orange.svg)
![](https://img.shields.io/github/forks/SYS113/negar.svg)
![](https://img.shields.io/github/release/SYS113/negar.svg)
![](https://img.shields.io/github/issues/SYS113/negar.svg)
![](https://img.shields.io/badge/license-MIT-informational.svg)
</div>

---
## *what is <ins>negar</ins>*
*call <ins>negar</ins> in your python source code and log to a file</ins> ...<br />*

---
## *install*

+ #### *installation by pip*

      # linux
      
      sudo python3 -m pip install negar
      
      # windows
      
      py -m pip install negar
      
+ #### *installation by setup.py*

      # linux
      
      git clone https://github.com/sys113/negar.git
      cd negar
      sudo python3 setup.py install
      
      # windows
      
      download https://github.com/sys113/negar/archive/master.zip and extract ...
      cd negar-master
      py setup.y install
      
 
    


---
## *example*
+ #### *[method one](https://github.com/sys113/negar/raw/master/example/method-one.gif)*
+ #### *[method two](https://raw.githubusercontent.com/sys113/negar/master/example/method-two.gif)*
---
## *review*
<p align="center">
  <img src="https://raw.githubusercontent.com/sys113/negar/master/example/example.png">
</p>

---
## *description*
  + #### *text*
    ```python
      # write 'text' to log file
      text = 'negar' 
    ```
  + #### *save*
    ```python
      # write log to 'negar-log.txt'
      save = 'negar-log.txt' 
    ```
  + #### *size*
    ```python
      # set 'size' for log file 
      size = 2
    ```
---
## *usage*
  + #### *method one*
    ```python
      # good
      import negar
      name = 'SYS113'
      negar.log('name value is '+str(name)+' ...')
    ```
  + #### *method two* 
    ```python
      # excellent
      from negar import log
      name = 'SYS113'
      log(text = 'name value is '+str(name)+' ...', save = 'negar.txt', size = 3)
    ```
---
## *tips*
+ *log file default size is 2 ...*
+ *log file size range is 1 ... 5 number ...*
+ *maximum size of python file name support is 15 character ...*
+ *maximum number to numbering lines support is 9999999 ...*
+ *maximum python source code line number support is 999999 ...*
+ *default log file name is log.txt ...*
+ *previously defined log file size can'not be resized!<br />*
---
## *copyright*
*copyright <ins>SYS113</ins> - <ins>2019</ins>.*

---
## *license* 
*<ins>MIT</ins> license , please see <ins>LICENSE</ins> file.*

---
## *donate* 
+ *for <ins>iranian</ins> users &nbsp; :  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <ins>  id pay </ins> &nbsp;&nbsp;&nbsp;&nbsp; - &nbsp;&nbsp;  https://idpay.ir/sys113*
+ *for <ins>global</ins> users &nbsp; : &nbsp;<ins>BTC wallet id</ins>&nbsp; - &nbsp; 149JgUmFqG6MvFg79Ldrvdk2bN35ByhMuw*
---
## *contact me* 
* *[Email](https://051.SYS113@gmail.com)*
* *[Telegram](https://t.me/SYS113/)*
* *[Instagram](https://instagram.com/sys113/)*
---
## *last world*
*hope this is <ins>negar</ins> useful to you and enjoy it.*

---
<div align="center">

*negar logo ❤️ mohamad moradiyani*
</div>

---
