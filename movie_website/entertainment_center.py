# -*- coding: UTF-8 -*-
# Created by xiongwei at 2018/1/6

import media
import fresh_tomatoes

# 星球大战8
star_war8 = media.Movie('星球大战8', '影片故事紧接《星球大战：原力觉醒》，讲述了遥远的银河系中恐怖政权“第一秩序”袭击新共和国首都之后的事。',  # noqa
                        'http://r1.ykimg.com/051600005A45C44A859B5D05D40B24F8',
                        'http://v.youku.com/v_show/id_XMzIwNDczMDk3Ng==.html')

# 黑客帝国
the_matrix = media.Movie('黑客帝国', '影片讲述了一名年轻的网络黑客尼奥发现看似正常的现实世界实际上是由一个名为“矩阵”的计算机人工智能系统控制的，尼奥在一名神秘女郎崔妮蒂的引导下见到了黑客组织的首领墨菲斯，三人走上了抗争矩阵征途的故事。',  # noqa
                         'http://r1.ykimg.com/051600005355D8A967379F515D060676',
                         'http://v.youku.com/v_show/id_XMzQ3ODkyODY0.html')

# 寻龙诀
key_to_dragon = media.Movie('寻龙诀', '《寻龙诀》根据盗墓小说《鬼吹灯》改编而成。',
                            'http://r1.ykimg.com/05160000564AC5B367BC3C288201BE68',
                            'http://v.youku.com/v_show/id_XODk5Njg0Mjg0.html')

# 夏洛特烦恼
bye_to_looser = media.Movie('夏洛特烦恼', '中年屌丝穿越回高中时代，实现人生巅峰',
                            'http://r1.ykimg.com/051600005963387C859B5C052006F32F',
                            'http://v.youku.com/v_show/id_XMTMzNTUwMTM5Mg==.html')

# 羞羞的铁拳
never_say_die = media.Movie('羞羞的铁拳', '男女灵魂互换追寻人生的意义',
                            'http://r1.ykimg.com/051600005A30DEBDADBDD3BCB4005B40',
                            'http://v.youku.com/v_show/id_XMjk4MzM1NzMwNA==.html')

# 驴得水
mr_donkey = media.Movie('驴得水', '该片改编自周申、刘露的同名话剧作品，由任素汐、大力、裴魁山等人主演。',
                        'http://r1.ykimg.com/051600005822D54567BC3C26670B31EB',
                        'http://v.youku.com/v_show/id_XMTczMjY2NDg0MA==.html')

# 需要展示的电影集合
movies = [star_war8, the_matrix, key_to_dragon, bye_to_looser, never_say_die, mr_donkey]
# 生成电影页面并在浏览器中打开
fresh_tomatoes.open_movies_page(movies)
