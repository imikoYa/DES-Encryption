'''
Name: DES Encryption
Python version: Python 2.x
Builder: miko
Email: love@immiko.net
Created time: 2021-10-8-18:24:09
'''


from Crypto.Cipher import DES
import binascii,sys
# 导入所需模块（可以不导入binascii和sys）

# DES加密
def encode(key,data):
    # 设置DES的加密方式 ECB （CBC需要另外再来一个iv值）
    des=DES.new(key,DES.MODE_ECB)
    # 这边是为了保证欲加密值即data值长度为8的倍数 这是DES规定所以没法突破
    # 差值用\x00填充
    data += (8 - len(data) % 8) * '\x00'
    en_data=des.encrypt(data)
    en_data_hex=binascii.b2a_hex(en_data)
    # 这边是可以替换成下面的句子 功能不变，只是decode或者encode在python2中是有的，可以不用导入binascii模块直接使用
    # en_data_hex=en_data.encode('hex')
    en_data_base=binascii.b2a_base64(en_data)
    # en_data_base=en_data.encode('base64')
    print '[+] Encode(HEX): '+en_data_hex
    print '[+] Encode(BASE64): '+en_data_base

# DES解密
def decode(key,data,horb):
    des=des.new(key,DES.MODE_ECB)
    # 判断传入值 不作为长期使用可以不写
    if horb =='hex':
        to_be_data=binascii.a2b_hex(data)
        # to_be_data=data.decode('hex')
    elif horb == 'base64':
        to_be_data=binascii.a2b_base64(data)
        # to_be_data=data.decode('base64')
    else:
        exit()
        print('[-] Error')
    fin_data=des.decrypt(to_be_data)
    print '[+] Decode: '+fin_data

# 定义主函数 key值必须为8位
if __name__=='__main__':
    key=data=mode=horb=''
    try:
        mode=sys.argv[1]
        key=sys.argv[2]
        data=sys.argv[3]
        horb=sys.argv[4]
    except:
        pass
    if mode=='-e':
        encode(key,data)
    elif mode=='-d':
        if not horb:
            print('[-] Encryption mode not define.')
        else:
            decrypt(key,data,horb)
    else:
        print('[*] Usage: python des.py -e/-d <key> <data> [Encryption mode (hex or base64)]')
