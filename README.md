# iframes
Fast detection of iframes in mpegts streams 

## Install
* pip install new_reader
```smalltalk
python3 -mpip install iframes
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
## Output
* iframe pts
```smalltalk
14648.092267
14648.342511
14648.509344
14648.7596
14649.009844
14649.2601
14649.426933
14649.6605
14649.910744
14650.161
14650.411244
14650.6615
14650.911744
14651.162
14651.412244
14651.6625
14651.912744
14652.163
14652.413244
14652.6635
14652.847011
14653.097267
14653.347511
14653.597767
14653.848011
14654.081578
14654.315144
14654.565389
14654.815644
14655.065889
14655.316144
14655.566389
14655.816644
14656.066889
14656.317144
14656.433933
14656.684178
14656.934433
14657.184678
14657.434933
```
