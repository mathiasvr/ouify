# ouify

Annotate MAC addresses with vendor names, similar to Wireshark captures, based on [OUI/IAB data](https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=manuf).

## usage
`ouify.py` reads line separated MAC addresses from `stdin`:
```bash
$ ouify.py < mac-addresses.txt
```

### example
As shown below, MAC addresses in various formats are supported:
```bash
$ printf "F8:77:B8:C0:FF:EE\n0C3021fedabe\nFF-FF-FF-FF-FF-FF" | ouify.py

SamsungE_c0:ff:ee
Apple_fe:da:be
Broadcast_ff:ff:ff
```

### optional arguments
```
-h, --help    show this help message and exit
-f, --full    print whole MAC address instead of suffix
-u, --update  update Wireshark OUI definition file
```

## license
[MIT](https://mvr.mit-license.org)
