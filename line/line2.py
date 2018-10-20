#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

msg = {
    200: "OK",
    201: "CREATED",
    403: "FORBIDDEN",
    404: "NOT_FOUND",
    405: "METHOD_NOT_ALLOWED"
}

user = {}

def get_message(code):
    return str(code) + ' ' + msg[code]

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    msg_list = []
    for _ in range(n):
        split = sys.stdin.readline().strip().split(' ')
        method = split[0]
        url = split[1]
        if len(split) > 2:
            body = split[2]
        else:
            body = ''

        if not '/users/' in url:
            msg_list.append(get_message(404))
            continue

        if '/users' in url and not '/data' in url:
            if method != 'POST':
                msg_list.append(get_message(405))
                continue

            user_id = url.replace('/users/', '')
            if user_id in user:
                msg_list.append(get_message(403))
                continue
            else:
                msg_list.append(get_message(201))
                user[user_id] = ''
                continue

        if '/data' in url:
            user_id = url.replace('/users/', '').replace('/data', '')
            if method == 'GET':
                if body:
                    msg_list.append(get_message(405))
                    continue
                if user_id in user:
                    if user[user_id]:
                        composite_msg = get_message(200) + ' ' + user[user_id]
                        msg_list.append(composite_msg)
                    else:
                        msg_list.append(get_message(404))
                    continue
                else:
                    msg_list.append(get_message(403))
                    continue

            elif method == 'POST':
                if not user_id in user:
                    msg_list.append(get_message(403))
                    continue
                else:
                    value = body.replace('value=', '')
                    user[user_id] = value
                    msg_list.append(get_message(200))
                    continue

    for msg in msg_list:
        print(msg)