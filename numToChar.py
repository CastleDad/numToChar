# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 21:14:31 2016
数字转换为汉字
@author: zq
"""

numChar = '零一二三四五六七八九'.decode('utf8')
unitChar = '园十百千万十百千亿十百千兆十百千'.decode('utf8')

def toChar(num):
    numStr = str(abs(num))
    n = len(numStr)

    if n > 16:
        return '数字太大'.decode('utf8')
        
    output = ''.decode('utf8')
    
    for i in range(n):
        numC = numChar[int(numStr[i])] #第i位的值汉字
        unitC = unitChar[n-i-1] #第i位的单位汉字
        #如果该位为0,且该位不是万位也不是各位，则只加‘零’不加单位
        if int(numStr[i]) == 0 and \
            (i != n-1 and i != n-5 and i != n-9 and i != n-13):
            output = output + numC
        else:
            output = output + numC + unitC

        #去除园万亿兆前的零            
        if (output[-1] == unitChar[4] or output[-1] == unitChar[0] or \
            output[-1] == unitChar[8] or output[-1] == unitChar[12]) \
            and n != 1:
            while output[-2] == numChar[0]:
                output = output[:-2] + output[-1]
                
    if num < 0:
        output = '负'.decode('utf8') + output
        
    return output


if __name__ == '__main__':
    print toChar(1298382012093000)
