#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created on: 17/10/30
# Copyright (C) 2017 xuekun.zhuang <zhuangxuekun@imdada.cn>
# Licensed under the Dada tech.co.ltd - http://www.imdada.cn
import torch

#
# from torch.autograd import Variable
# x = Variable(torch.ones(2, 2), requires_grad = True)
# y = x + 2
# y.creator
#
# # y 是作为一个操作的结果创建的因此y有一个creator
# z = y
# out = z.mean()
#
# # 现在我们来使用反向传播
# out.backward(torch.Tensor([4]))
#
# # out.backward()和操作out.backward(torch.Tensor([1.0]))是等价的
# # 在此处输出 d(out)/dx
# print x.grad

# from torch.autograd import Variable
# x = torch.rand(5)
# x = Variable(x,requires_grad = True)
# y = x**2
# grads = torch.FloatTensor([1,2,3,4,5])
# y.backward(grads)#如果y是scalar的话，那么直接y.backward()，然后通过x.grad方式，就可以得到var的梯度
# print x.grad           #如果y不是scalar，那么只能通过传参的方式给x指定梯度


# import torch
# from torch.autograd import Variable
# w1 = Variable(torch.Tensor([1.0,2.0,3.0]),requires_grad=True)#需要求导的话，requires_grad=True属性是必须的。
# w2 = Variable(torch.Tensor([1.0,2.0,3.0]),requires_grad=True)
#
# z = w1*w2+w1 # 第二次BP出现问题就在这，不知道第一次BP之后销毁了啥。
# res = torch.mean(z)
# res.backward(torch.Tensor([2.0])) #第一次求导没问题
#
# print w1.grad

import torch
from torch.autograd import Variable

x = Variable(torch.ones(1)*3, requires_grad=True)
y = Variable(torch.ones(1)*4, requires_grad=True)
z = x.pow(2)+3*y.pow(2)     # z = x^2+3y^2, dz/dx=2x, dz/dy=6y
z.backward(torch.ones(1))   #纯标量结果可不写占位变量
print x.grad         # x = 3 时, dz/dx=2x=2*3=6
print y.grad         # y = 4 时, dz/dy=6y=6*4=24
print x.creator