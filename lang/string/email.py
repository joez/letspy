#!/usr/bin/env python3


def fun(s):
    try:
        user, url = s.split('@')
        host, ext = url.split('.')
    except ValueError:
        return False

    if user.replace('-', '').replace('_', '').isalnum() \
            and host.isalnum() and ext.isalnum() \
            and 0 < len(ext) <= 3:
        return True
    else:
        return False


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = [input() for _ in range(n)]

print(sorted(filter_mail(emails)))
