#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Run synchronous code as asynchronous.

Forces any module NOT compatible with asyncio to run Ok with asyncio.
This enables to seamlessly mix sync and async code, see docs for examples.
"""


import asyncio
# import atexit  # See Line 105.
import functools
import threading


###############################################################################


class _AsyncCall(object):

    """Represents a low level sync code fragment to be run asynchronously."""
    __slots__ = ("event_loop", "sync_code", "args", "kwargs")

    def __init__(self, event_loop, sync_code):
        self.event_loop, self.sync_code = event_loop, sync_code

    def __repr__(self):
        return "<{0}: {1}>".format(self.__class__.__name__,
                                   repr(self.sync_code))

    async def __call__(self, *args, **kwargs):
        return self.sync_code(*args, **kwargs)


class _AsyncProcessingCall(object):

    """A low level sync code fragment to be run asynchronously on a Process."""
    __slots__ = ("event_loop", "sync_code", "args", "kwargs")

    def __init__(self, event_loop, sync_code):
        self.event_loop, self.sync_code = event_loop, sync_code

    def __repr__(self):
        return "<{0}: {1}>".format(self.__class__.__name__,
                                   repr(self.sync_code))

    async def __call__(self, *args, **kwargs):
        return await self.event_loop.run_in_executor(
            None, functools.partial(self.sync_code, *args, **kwargs))


class _AsyncThreadingCall(object):

    """A low level sync code fragment to be run asynchronously on a Thread."""
    __slots__ = ("event_loop", "sync_code", "args", "kwargs", "tread")

    def __init__(self, event_loop, sync_code, tread=None):
        self.event_loop, self.sync_code = event_loop, sync_code
        self.tread = tread

    def __repr__(self):
        return "<{0}: {1}>".format(self.__class__.__name__,
                                   repr(self.sync_code))

    def _run_future(self, sync_function, future):
        try:
            future.set_result(sync_function())
        except Exception as error:
            future.set_exception(error)
        self.tread = None
        return self.tread

    async def _run_thread(self, sync_function, future):
        tread = threading.Thread(target=self._run_future, name="angler",
                                 args=(sync_function, future))
        tread.start()
        self.tread = tread
        return self.tread

    async def __call__(self, *args, **kwargs):
        sync_function = functools.partial(self.sync_code, *args, **kwargs)
        future, results = asyncio.Future(), None
        asyncio.ensure_future(self._run_thread(sync_function, future),
                              loop=self.event_loop)
        future_done, asyncio_sleep = future.done, asyncio.sleep  # Optimization
        while True:
            if future_done():
                results = future.result()
                break
            await asyncio_sleep(.1)
        return results


###############################################################################


class Sync2Async(object):

    """Run Sync code as Async."""
    __slots__ = ("args", "kwargs")

    event_loop = asyncio.get_event_loop()
    # atexit.register(asyncio.get_event_loop().close)  # Use if hangs at exit.

    @classmethod
    def get_event_loop(cls, *args, **kwargs):
        return cls.event_loop

    @classmethod
    async def run_async(cls, *args, **kwargs):
        if cls.event_loop:
            event_loop, sync_code, args = cls.event_loop, args[0], args[1:]
        else:
            event_loop, sync_code, args = args[0], args[1], args[2:]
        return await _AsyncCall(event_loop, sync_code)(*args, **kwargs)

    @classmethod
    async def run_async_on_process(cls, *args, **kwargs):
        if cls.event_loop:
            event_loop, sync_code, args = cls.event_loop, args[0], args[1:]
        else:
            event_loop, sync_code, args = args[0], args[1], args[2:]
        return await _AsyncProcessingCall(
            event_loop, sync_code)(*args, **kwargs)

    @classmethod
    async def run_async_on_thread(cls, *args, **kwargs):
        if cls.event_loop:
            event_loop, sync_code, args = cls.event_loop, args[0], args[1:]
        else:
            event_loop, sync_code, args = args[0], args[1], args[2:]
        return await _AsyncThreadingCall(
            event_loop, sync_code)(*args, **kwargs)

    def __setattr__(self, *args, **kwargs):
        raise TypeError("Anglers Sync2Async object is inmmutable read-only.")

    def __delattr__(self, *args, **kwargs):
        raise TypeError("Anglers Sync2Async object is inmmutable read-only.")
