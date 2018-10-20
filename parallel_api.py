# Parallel Request

# Re-try limit

# Welcome Server Perf - adjusting batch job count ( 0 ~ 50 / 30 was best )

# Duplicate Check

# next_url refresh period by category

import asyncio

import logging
import aiohttp


async def download(index: int, url: str, result: list):
    print("Fetching {} {}".format(index, url))
    try:
        async with aiohttp.ClientSession(read_timeout=1) as session:
            async with session.get(url) as res:
                if res.status == 200:
                    data = await res.json()
                    print(data['uuid'])
                    result.append((index, data['uuid']))

                    return True
                else:
                    # Error Handling
                    print("Error")
                    pass
    except Exception as e:
        print("Handled Error")
        logging.error(url + " " + str(e))
        print(str(type(e)) + str(e))


url_list = [
    'http://httpbin.org/uuid',
    'http://httpbin.org/uuid',
    'http://httpbin.org/uuid',
    'https://nghttp2.org/httpbin/status/404',
    'https://nghttp2.org/httpbin/status/500',
    'http://httpbin.org/uuid',
    'https://httpbin.org/delay/5',
    'http://httpbin.org/uuid'
]

if __name__ == '__main__':
    result = []
    tasks = [download(i, url, result) for i, url in enumerate(url_list)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    print('----------------')
    for u in result:
        print(u)


