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

Optical Character Recognition was the way to convert an image to text. _Accepted Method_

# Issues

First I had to install the tesseract engine for the library to work. 

To install tesseract the following had to be done
``` shell
brew install tesseract
```
**1)Brew not working**

I faced an issue here which took a lot of my time. The command brew was not working as it had been partially installed. After going through Stackoverflow for a bit, i realised the problem. I reinstalled brew and got it to work after a few failed attempts. Then i installed the tesseract engine.

Two popular OCR libraries for Python are [pytesser](https://code.google.com/p/pytesser/) and [pytesseract](https://github.com/madmaze/pytesseract). I compared both of them, and realised both had the same perfomance. In the end, i picked up pytesseract for its easy installation procedure by pip 

```python
pip install pytesseract
```

**2) Poor performance of the libraries**

The libraries on use gave poor results. This is what the [output](https://github.com/SambitAcharya/Mini-Projects/blob/master/Python/Scrape%20Euler/out.txt) was for the follwing image [input](https://projecteuler.net/profile/praveen97uma.png).  

I cropped the image to the specific required region for better performance, but it was still _unsatisfactory_.

I suspected that the problem was with the **quality** of the SPOJ image. So to enhance the quality, i used some functions provided by PIL. But it **did not** result in any increase in performance.




