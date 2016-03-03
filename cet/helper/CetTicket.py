#!/usr/bin/env python
# coding=utf-8
import CetConfig
from random import randint
from ctypes import CDLL, c_char, c_int, byref, \
    create_string_buffer, Structure, Union

try:
    import requests
except ImportError:
    print 'You need to install requests to use full functions.'


def random_mac():
    return '%.2X-%.2X-%.2X-%.2X-%.2X-%.2X' % (randint(0, 16), randint(0, 16), 
                                              randint(0, 16), randint(0, 16), 
                                              randint(0, 16), randint(0, 16))


DES_cblock = c_char * 8
DES_LONG = c_int


class TicketNotFound(Exception):
    pass


class ks(Union):
    _fields_ = [
        ('cblock', DES_cblock),
        ('deslong', DES_LONG * 2)
    ]


class DES_key_schedule(Structure):
    _fields_ = [
        ('ks', ks * 16),
    ]


class CetCipher(object):

    ticket_number_key = '(YesuNRY'
    request_data_key = '?!btwNP^'

    DECRYPT = 0
    ENCRYPT = 1

    def __init__(self, libcrypto_path=None):
        if not libcrypto_path:
            from ctypes.util import find_library
            libcrypto_path = find_library('crypto')
            if not libcrypto_path:
                raise Exception('libcrypto(OpenSSL) not found')

        self.libcrypto = CDLL(libcrypto_path)

        if hasattr(self.libcrypto, 'OpenSSL_add_all_ciphers'):
            self.libcrypto.OpenSSL_add_all_ciphers()

    def process_data(self, indata, key, is_enc=1):
        length = len(indata)

        indata = create_string_buffer(indata, length)
        outdata = create_string_buffer(length)
        n = c_int(0)

        key = DES_cblock(*tuple(key))
        key_schedule = DES_key_schedule()

        self.libcrypto.DES_set_odd_parity(key)
        self.libcrypto.DES_set_key_checked(byref(key), byref(key_schedule))

        self.libcrypto.DES_cfb64_encrypt(byref(indata),
                                         byref(outdata),
                                         c_int(length),
                                         byref(key_schedule), byref(key), byref(n), c_int(is_enc))

        return outdata.raw

    def decrypt_ticket_number(self, ciphertext):
        ciphertext = ciphertext[2:]
        return self.process_data(ciphertext, self.ticket_number_key, is_enc=self.DECRYPT)

    def encrypt_ticket_number(self, ticket_number):
        ciphertext = self.process_data(ticket_number,
                                       self.ticket_number_key, is_enc=self.ENCRYPT)
        ciphertext = '\x35\x2c' + ciphertext
        return ciphertext

    def decrypt_request_data(self, ciphertext):
        return self.process_data(ciphertext, self.request_data_key, is_enc=self.DECRYPT)

    def encrypt_request_data(self, request_data):
        return self.process_data(request_data, self.request_data_key, is_enc=self.ENCRYPT)


class CetCipher(CetCipher):

    ticket_number_enc_key = ')XdsuORX'
    ticket_number_dec_key = '(YesuNRY'

    def encrypt_ticket_number(self, ticket_number):
        ciphertext = self.process_data(ticket_number,
                                       self.ticket_number_enc_key, is_enc=self.ENCRYPT)
        return ciphertext

    def decrypt_ticket_number(self, ciphertext):
        ciphertext = ciphertext[2:]
        return self.process_data(ciphertext, self.ticket_number_enc_key, is_enc=self.DECRYPT)


class CetTicket(object):

    """
        usage:
        ct = CetTicket()
        print ct.find_ticket_number(b'重庆', b'重庆邮电大学', b'刘晨凌', cet_type=2)
    """

    search_url = 'http://find.cet.99sushe.com/search'
    score_url = 'http://cet.99sushe.com/find'

    CET4 = 1
    CET6 = 2

    @classmethod
    def find_ticket_number(cls, province, school, name, examroom='', cet_type=1):
        cipher = CetCipher()

        province_id = CetConfig.PROVINCE[province]
        param_data = u'type=%d&provice=%d&school=%s&name=%s&examroom=%s&m=%s' % (cet_type, province_id,
                                                                                                school, name, 
                                                                                                examroom, random_mac())

        param_data = param_data.encode('gb2312')
        encrypted_data = cipher.encrypt_request_data(param_data)

        resp = requests.post(url=cls.search_url, data=encrypted_data)
        print resp.content
        ticket_number = cipher.decrypt_ticket_number(resp.content)
        if ticket_number == '':
                return {'Status': '0', 'Contact_us': 'wangyuan.info'}
        return ticket_number

    @classmethod
    def get_score(cls, ticket_number, name):
        name = name.encode('gb2312')

        params_dict = {
            'id': ticket_number,
            'name': name[:4]
        }

        resp = requests.post(url=cls.score_url,
                             data=params_dict,
                             headers={'Referer': 'http://cet.99sushe.com/'})
        score_data = resp.content.decode('gb2312')
        if len(score_data) < 10:
            return
        score_data = score_data.split(',')

        score = {
            'name': score_data[6],
            'school': score_data[5],
            'Listening': score_data[1],
            'Reading': score_data[2],
            'Writing': score_data[3],
            'Total': score_data[4],
            'Status': '1',
            'Contact_us': 'wangyuan.info'
        }
        return score
