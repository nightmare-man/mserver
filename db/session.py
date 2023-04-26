from contextlib import asynccontextmanager
from functools import wraps

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
engine = create_async_engine("sqlite+aiosqlite:///./master.db",echo=True)
Session=sessionmaker(engine)

""" 
    用该装饰器装饰的，都变成 一个可以用with as 管理的资源，
    进入with时会执行yield之前的，as 的会返回yield 的
    出with范围 时会执行yield之后的代码。

    异步的Session不支持用with 或者async with来自动管理，所以才有这样
"""
@asynccontextmanager
async def open_session(async_session_cls=Session, commit=False):
    async_session=async_session_cls()
    try:
        yield async_session 
        if commit:
            await async_session.commit()
    except:
        await async_session.r ollback()
        raise
    finally:
         await async_session.close()

def atomicity(commit=False):
    def wrapper(func):
        @wraps(func)
        async def decorator(*args,**kwargs):
            session = kwargs.get("session")
            if not session:
                async with open_session(Session,commit=commit) as session:
                    kwargs["session"] = session
                    r = await func(*args, **kwargs)
            else:
                r = await func(*args, **kwargs)
            return r
        return decorator
    return wrapper
