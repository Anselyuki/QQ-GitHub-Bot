#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author         : yanyongyu
@Date           : 2020-09-21 00:05:16
@LastEditors    : yanyongyu
@LastEditTime   : 2021-01-01 17:53:00
@Description    : None
@GitHub         : https://github.com/yanyongyu
"""
__author__ = "yanyongyu"
__package__ = "github.plugins.github_help"

import inspect
from functools import reduce

from nonebot import on_command
from nonebot.adapters import Bot

from ... import _sub_plugins, github_config as config

help = on_command("help", priority=config.github_command_priority)
help.__doc__ = """
/help
获取帮助
"""


@help.handle()
async def handle(bot: Bot):
    matchers = reduce(lambda x, y: x.union(y.matcher), _sub_plugins, set())
    docs = "命令列表：\n"
    docs += "\n".join(
        map(lambda x: inspect.cleandoc(x.__doc__),
            filter(lambda x: x.__doc__, matchers)))
    await help.finish(docs)
