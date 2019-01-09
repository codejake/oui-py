# oui.py - Get the registered vendor for a MAC address or a portion thereof.

## Usage: oui <mac address>
The MAC address can be in most any format of between 6 and 12 digits -- 
even partial MAC addresses, as long as the first 6 digits are in there.
Eg. aabb.ccdd.eeff, aa:bb:cc:dd:ee:ff, aa:bb:cc, aabb.c, aa:bb:cc:dd etc.

## Example usage

```
$ oui 88:e9:fe:xx:yy:zz
88:E9:FE	Apple	Apple, Inc.
```