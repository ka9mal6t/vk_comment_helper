<div align="center">

# Helper for comment VK
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
</div>

# Table of contents  
1. [Tech Stack](#Stack) 
2. [Features](#Features)
3. [Config](#Files)
4. [Run Locally](#run)
5. [Feedback](#Feedback)
6. [License](#License)
<div id="Stack">

## Tech Stack  

**Client:** Python, Selenium
</div>
<div id="Features">

## Features  

- Fast spam
- Take screenshots
- Random choose comment
</div>
<div id="Files">

## Files

...is read from `config.py`

Format:
```python
APP_ID = 123456
```
* `APP_ID` must be obtained from VK Developers. [VK Developers](https://dev.vk.com/);

...is read from `chromdriver.exe`
* `chromdriver.exe` must be obtained from Google (the browser and driver versions must match). [Google Driver](https://chromedriver.chromium.org/downloads)

...is read from `messages.txt`
```txt
message1
message2
```

...is read from `links.txt`
```txt
https://vk.com/wall-example1
https://vk.com/wall-example2
https://vk.com/wall-example3
```
</div>
<div id="run">

## Run Locally  

Clone the project  

~~~bash  
  git clone https://github.com/ka9mal6t/
~~~

Go to the project directory  

~~~bash  
  cd 
~~~

Install dependencies and add [files](#Files)

~~~bash  
pip install -r requirements.txt
~~~

Start the server  

~~~bash  
python main.py
~~~

</div>
<div id="Feedback">

## Feedback

If you have any feedback, please reach out to us at [vladimyr.kilko@gmail.com](mailto:vladimyr.kilko@gmail.com)
</div>
<div id="License">

## License

[MIT](LICENSE)
</div>