import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

logger = logging.getLogger(__name__)

BANNER = r"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                       _ooOoo_                                ║
║                      o8888888o                               ║
║                      88" . "88                               ║
║                      (| -_- |)                               ║
║                      O\  =  /O                               ║
║                   ____/`---'\____                            ║
║                 .'  \\|     |//  `.                          ║
║                /  \\|||  :  |||//  \                         ║
║               /  _||||| -:- |||||-  \                        ║
║               |   | \\\  -  /// |   |                        ║
║               | \_|  ''\---/''  |   |                        ║
║               \  .-\__  `-`  ___/-. /                        ║
║             ___`. .'  /--.--\  `. . ___                      ║
║           ."" '<  `.___\_<|>_/___.'  >'"".                   ║
║         | | :  `- \`.;`\ _ /`;.`/ - ` : | |                  ║
║         \  \ `-.   \_ __\ /__ _/   .-` /  /                  ║
║  =======`-.____`-.___\_____/___.-`____.-'=======             ║
║                                                              ║
║                 IntelligentAssistant v2.0                    ║
║          智能客服 AI 系统 | Multi-Agent · Memory · RAG         ║
║                                                              ║
║                    我佛慈悲 永无 BUG                           ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(BANNER, flush=True)
    logger.info("IntelligentAssistant 已就绪")
    try:
        yield
    finally:
        logger.info("IntelligentAssistant 已关闭")
