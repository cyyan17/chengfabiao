# -*- coding: utf-8 -*-

from django.db import models

class Data(models.Model):
	pr1 = models.CharField(u"乘数",max_length=10)
	pr2 = models.CharField(u"被乘数",max_length=10)
	result = models.CharField(u"结果",max_length=10)
<<<<<<< HEAD
=======
	
>>>>>>> cb996c206b06ce37be7e1fd1af1320c6573c9039
