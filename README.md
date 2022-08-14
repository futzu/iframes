# iframes
Fast detection of iframes in mpegts streams 

## Install
* pip install new_reader
```smalltalk
python3 -mpip install new_reader
```
* git clone the repo

```smalltalk
git clone https://github.com/futzu/iframes
```
* install
```smalltalk
su -

cd  iframes

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
