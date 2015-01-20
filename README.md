### How it works

This is a Python 2.7 app that:

* Scrapes the BBC news homepage (http://www.bbc.co.uk/news/)
* Finds the most shared articles in the "Most Popular" table
* Searches for the article's the most commom word
* Uses the words as hashtags on Twitter to know what is going on


### Version
1.0

### Requirements

In order to run this app you'll need:

* [beautifulsoup4](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [twython](https://twython.readthedocs.org/en/latest/)

You'll also need a [Twitter API Key and Token](https://apps.twitter.com/app/7800816/keys)

Change the constants in /models/twitter.py with your credentials.

- To install via pip, run the requirements.txt file:
```sh
pip install -r requirements.txt
```

### Running the App

Call the run.py file from the console:

```sh
$ python run.py
```

### Testing the App

Tests depends on the mock lib:

* [mock](https://docs.python.org/3/library/unittest.mock.html)

I used unittest, so just run the /tests package as unittest Python run.

### License

The MIT License (MIT)

Copyright (c) [2015] [Thiago Marini]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

