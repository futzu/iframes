# iframes
Fast detection of  h.264 and h.265  keyframes in mpegts streams 

## Install

* git clone the repo

```smalltalk
git clone https://github.com/futzu/iframes
```
* install
```smalltalk
su -

cd keyframes

install iframes.py /usr/local/bin/iframes
```
## Run 
* local file
```
iframes video.ts
```
* https
```
iframes https://example.com/video.ts
```
* multicast
```
iframes udp://@227.5.5.5:1234
```
