# -*- coding: utf-8 -*-
"""
用于正式环境的全局配置
"""
from settings import APP_ID


# ===============================================================================
# 数据库设置, 正式环境数据库设置
# ===============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 默认用mysql
<<<<<<< HEAD
        'NAME': APP_ID,                        # 数据库名 (默认与APP_ID相同)
        'USER': 'root',                            # 你的数据库user
        'PASSWORD': 'OIraQ3SJ_x',                        # 你的数据库password
        'HOST': '192.168.26.131',                   		   # 数据库HOST
=======
        'NAME': 'chengfb',                        # 数据库名 (默认与APP_ID相同)
        'USER': 'root',                            # 你的数据库user
        'PASSWORD': 'OIraQ3SJ_x',                        # 你的数据库password
        'HOST': '192.168.26.131',              # 数据库HOST
>>>>>>> cb996c206b06ce37be7e1fd1af1320c6573c9039
        'PORT': '3306',                        # 默认3306
    },
}
