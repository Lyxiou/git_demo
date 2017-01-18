# coding=utf-8

def check_is_chinese(uchar):
    """�ж�һ��unicode�Ƿ��Ǻ���"""
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
            return True
    else:
            return False 

def check_is_number(uchar):
        """�ж�һ��unicode�Ƿ�������"""
        if uchar >= u'\u0030' and uchar<=u'\u0039':
                return True
        else:
                return False 

def check_is_alphabet(uchar):
        """�ж�һ��unicode�Ƿ���Ӣ����ĸ"""
        if (uchar >= u'\u0041' and uchar<=u'\u005a') or (uchar >= u'\u0061' and uchar<=u'\u007a'):
                return True
        else:
                return False 

def check_is_other(uchar):
        """�ж��Ƿ�Ǻ��֣����ֺ�Ӣ���ַ�"""
        if not (check_is_chinese(uchar) or check_is_number(uchar) or check_is_alphabet(uchar)):
                return True
        else:
                return False
def check_is_banjiao(uchar):
    """�ж�һ��unicode�Ƿ��ǰ��"""
    for c in uchar:
        inside_code = ord(c)
        if inside_code<0x0020 or inside_code>0x7e:    #���ǰ�ǵ��ж�  
            return False
        else:
            return True
def check_name_len(uchar): 
    if (len(uchar)<=20):
        return True
    else:
        return False

def check_name_format_and_len(name): 
    if ((not check_is_other(name)) and (check_is_banjiao(name)) and check_name_len(name)):
        rst = True
    else:
        rst = False
    return rst
def check_chinese_name_format_and_len(name): 
    if ((not check_is_other(name)) and check_name_len(name)):
        rst = True
    else:
        rst = False
    return rst