# keyframes
Fast detection of  h.264 and h.265  keyframes in mpegts streams 

## Install
* pip install threefive
```smalltalk
python -mpip install threefive
```
* git clone the repo

```smalltalk
git clone https://github.com/futzu/keyframes
```
* install
```smalltalk
su -

cd keyframes

install keyframes.py /usr/local/bin/keyframes
```
## Run 
* local file
```
keyframes video.ts
```
* https
```
keyframes https://example.com/video.ts
```
* multicast
```
keyframes udp://@227.5.5.5:1234
```
