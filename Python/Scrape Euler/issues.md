## Development Environment

**System**:	Mac OS X 10.9.5    
**Python**: 2.7.5

## Approach  

Problem was to get the number of problems solved on [Project Euler](https://www.projecteuler.net) given his username.
The data returned by project euler was in the form of an image only. So the image was to converted to text and the data was to be extracted from that.

Below is how I approached the problem

**1)** Check the _EXIF_ data returned by the image to get any relevant info.

On doing a quick google search to solve the problem, i came across an article which was about extracting EXIF data from an image. It wasn't clear to me what EXIF data was so I wrote a small piece of code for the image, but **nothing useful** came out of it. _Idea Dropped_

**2)** Use of _Tesseract OCR_ engine for python

Optical Character Recognition was the way to convert an image to text. First I had to install the tesseract engine for the library to work. 

To install tesseract the following had to be done
``` Shell
brew install tesseract
```
I faced an issue here which took a lot of my time. The command brew was not working as it had been partially installed. After going through Stackoverflow for a bit, i realised the problem. I reinstalled brew and got it to work after a few failed attempts. Then i installed the tesseract engine.

Two popular OCR libraries for Python are [pytesser](https://code.google.com/p/pytesser/) and [pytesseract](https://github.com/madmaze/pytesseract). I compared both of them, and realised both had the same perfomance. In the end, i picked up pytesseract for its easy installation procedure by pip 

```Python
pip install pytesseract
```


