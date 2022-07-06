#!/bin/env python
# -*- encoding: utf-8 -*-
#-------------------------------------------------------------------------------
# Purpose:     txt转换成Excel
# Author:      xl
# Created:     2020-1-18
# update:      ****-**-**
#-------------------------------------------------------------------------------
import xlwt

txtname = r'C:\Users\renyu.lou\Desktop\pc\RCT3\matchresult\MatchResult_1543881359733383168_2022-07-04-17-14-31.log'
excelname = r'C:\Users\renyu.lou\Desktop\pc\RCT3\matchresult'

fopen = open(txtname, 'r',encoding='utf-8')
lines = fopen.readlines()

file = xlwt.Workbook(encoding='utf-8', style_compression=0)
# 新建一个sheet
sheet = file.add_sheet('data')

i = 0
for line in lines:
    line = line.strip('\n')
    line = line.split(' ')
    picName = line[0]
    x1 = line[1]
    y1 = line[2]
    x2 = line[3]
    y2 = line[4]
    className=line[5]

    sheet.write(i, 0, picName)
    sheet.write(i, 1, x1)
    sheet.write(i, 2, y1)
    sheet.write(i, 3, x2)
    sheet.write(i, 4, y2)
    sheet.write(i, 5, className)
    i = i + 1

file.save(excelname)