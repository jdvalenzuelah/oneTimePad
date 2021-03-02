# One time pad encrypt

## Usage

#### Install requirements:
```shell
$ pip install -r requirements.txt
```

#### Encrypt a file
```shell
$ python oneTimePad.py test.txt
```

Will generate 2 files `enc.txt`, with the encrypted message, and `key.txt`, with the key to decrypt a message.

#### Decrypt a file

Pass path to encrypted file and path to key file

```shell
$ py oneTimePad.py enc.txt key.txt
```

will print to stdout the decrypted content