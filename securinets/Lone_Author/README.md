```
Lone_Author_Writeup
```
Trying to open zip file threw an error. So I examined its headers. They should look like PK\x03\x04 or PK\x05\x06 or PK\x07\x08. However they are PKF\x03\x04. In the next occurance of PK, the letter immediate to PK is l and so on. They are as follows
```
PKF
PKl
PKa
PKg
PK{
PKM
PK3
PK3
PKt
PK_M
PK3
PK_1
```
It is evident that we are in right direction. We got first part of flag as "Flag{M33t_M3_1. Removed these extra chars from file and saved it as lone_fixed.zip. Ran binwalk on lone_fixed.zip and it found 0.zip,"qr_ps.tif", 0e68542470, secret.zip. secret.zip and 0.zip are had an image with name "export.png" and we need password to unlock it.
```
han@kali:~/Desktop/ctf/asd/la » binwalk -e lone_fixed.zip 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Zip archive data, at least v2.0 to extract, compressed size: 8001, uncompressed size: 156370, name: qr_ps.tif
8068          0x1F84          Zip archive data, at least v2.0 to extract, compressed size: 29, uncompressed size: 32, name: 0e68542470
8165          0x1FE5          Zip archive data, at least v1.0 to extract, compressed size: 11132, uncompressed size: 11132, name: secret.zip
19343         0x4B8F          End of Zip archive
```
file 0e68542470 hinted to look at .tiff
```
han@kali:~/Desktop/ctf/asd/la/_lone_fixed.zip.extracted » cat 0e68542470 
Man, you have to this this TIFF!%     
```
It looked like a partial qr code. Then I examined exifdata of the file and found password for both zip files in author comments of exifdata as "0xNOX**". Use it to extract the image "export.png" and it has second part of flag
```
han@kali:~/Desktop/ctf/asd/la/_lone_fixed.zip.extracted » exiftool qr_ps.tif                                  1 ↵
ExifTool Version Number         : 10.65
File Name                       : qr_ps.tif
Directory                       : .
File Size                       : 153 kB
File Modification Date/Time     : 2018:03:21 12:18:49-04:00
File Access Date/Time           : 2018:03:26 03:38:16-04:00
File Inode Change Date/Time     : 2018:03:21 12:18:49-04:00
File Permissions                : rwxrwxrwx
File Type                       : TIFF
File Type Extension             : tif
MIME Type                       : image/tiff
Exif Byte Order                 : Little-endian (Intel, II)
Subfile Type                    : Full-resolution Image
Image Width                     : 175
Image Height                    : 175
Bits Per Sample                 : 8 8 8 8
Compression                     : Uncompressed
Photometric Interpretation      : RGB
Strip Offsets                   : 33870
Orientation                     : Horizontal (normal)
Samples Per Pixel               : 4
Rows Per Strip                  : 175
Strip Byte Counts               : 122500
X Resolution                    : 72
Y Resolution                    : 72
Planar Configuration            : Chunky
Resolution Unit                 : inches
Software                        : Adobe Photoshop CC 2015 (Windows)
Modify Date                     : 2018:03:21 17:04:04
Extra Samples                   : Associated Alpha
XMP Toolkit                     : Image::ExifTool 10.75
Format                          : image/tiff
Author                          : Password to the second part is 0xNOX**
Color Mode                      : RGB
Create Date                     : 2018:03:21 16:53:01+01:00
Creator Tool                    : Adobe Photoshop CC 2015 (Windows)
Metadata Date                   : 2018:03:21 17:04:04+01:00
Derived From Document ID        : xmp.did:2af6b33f-3c7b-a24b-9843-1996a1b84602
Derived From Instance ID        : xmp.iid:3f770dda-d0ca-a143-b15f-e83cc237e3e5
Derived From Original Document ID: xmp.did:0697a83c-7578-eb46-9563-317a5fd69d58
Document ID                     : adobe:docid:photoshop:73c987be-2d21-11e8-b06c-dfbcca89ae7a
History Action                  : created, saved, saved, converted, derived, saved, saved, converted, derived, saved
History Instance ID             : xmp.iid:0697a83c-7578-eb46-9563-317a5fd69d58, xmp.iid:481c4c0f-3e35-6445-b934-e4c85439f5c1, xmp.iid:a626861d-83ab-2741-bffa-670135153615, xmp.iid:2af6b33f-3c7b-a24b-9843-1996a1b84602, xmp.iid:3f770dda-d0ca-a143-b15f-e83cc237e3e5, xmp.iid:ff12e802-eabc-8546-abc4-fd24b1476556
History Software Agent          : Adobe Photoshop CC 2015 (Windows), Adobe Photoshop CC 2015 (Windows), Adobe Photoshop CC 2015 (Windows), Adobe Photoshop CC 2015 (Windows), Adobe Photoshop CC 2015 (Windows), Adobe Photoshop CC 2015 (Windows)
History When                    : 2018:03:21 16:53:01+01:00, 2018:03:21 17:01:41+01:00, 2018:03:21 17:03:52+01:00, 2018:03:21 17:03:52+01:00, 2018:03:21 17:04:04+01:00, 2018:03:21 17:04:04+01:00
History Changed                 : /, /, /, /, /
History Parameters              : from image/png to application/vnd.adobe.photoshop, converted from image/png to application/vnd.adobe.photoshop, from application/vnd.adobe.photoshop to image/tiff, converted from application/vnd.adobe.photoshop to image/tiff
Instance ID                     : xmp.iid:ff12e802-eabc-8546-abc4-fd24b1476556
Original Document ID            : xmp.did:0697a83c-7578-eb46-9563-317a5fd69d58
IPTC Digest                     : 00000000000000000000000000000000
Displayed Units X               : inches
Displayed Units Y               : inches
Print Style                     : Centered
Print Position                  : 0 0
Print Scale                     : 1
Alpha Channels Names            : Transparency
Global Angle                    : 30
Global Altitude                 : 30
URL List                        : 
Slices Group Name               : 
Num Slices                      : 1
Pixel Aspect Ratio              : 1
Photoshop Thumbnail             : (Binary data 3889 bytes, use -b option to extract)
Has Real Merged Data            : Yes
Writer Name                     : Adobe Photoshop
Reader Name                     : Adobe Photoshop CC 2015
Color Space                     : Uncalibrated
Exif Image Width                : 175
Exif Image Height               : 175
Image Source Data               : (Binary data 19892 bytes, use -b option to extract)
Image Size                      : 175x175
Megapixels                      : 0.031

```
![Alt text](_lone_fixed.zip.extracted/export.png?raw=true "Title")
Second part of flag is: n_tHe_p4RK_T0mOrrOW

flag : Flag{M33t_M3_1n_tHe_p4RK_T0mOrrOW}
