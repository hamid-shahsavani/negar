---

![](https://img.shields.io/github/stars/SYS113/negar.svg)
![](https://img.shields.io/badge/language-python-orange.svg)
![](https://img.shields.io/github/forks/SYS113/negar.svg)
![](https://img.shields.io/github/release/SYS113/negar.svg)
![](https://img.shields.io/github/issues/SYS113/negar.svg)
![](https://img.shields.io/badge/license-MIT-informational.svg)
---
## what is <ins>negar</ins>
### &nbsp;&nbsp;&nbsp;&nbsp; call negar in python source and write log in a file</ins> ...<br />
---
## description
  + #### text
    ```python
      text = 'x' 
      # write 'text' in log file
    ```
  + #### file
    ```python
      file = 'log.txt' 
      # write log to 'log.txt'
    ```
  + #### size
    ```python
      size = 55
      # set 'size' for log file size
    ```
---
## usage
  + #### method one :blush:
    ```python
      import negar
      negar.log('hello world!')
    ```
  + #### method two :smile:
    ```python
      from negar import log
      log(text = 'negar', file = 'log.txt', size = 2)
    ```
---
## tips
  + #### default size : 2
  + #### size range : 1 to 5 number
  + #### default log file : log.txt
  + #### previously defined log file size can'not be resized!


