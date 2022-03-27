# coding=utf-8

import os

import requests

GITHUB_USER_SESSION = os.environ.get("GITHUB_USER_SESSION")
OAUTH_BINDING_URL = "https://leetcode-cn.com/accounts/github/login/?process=connect"


def gen_oauth_callback_url():
    assert GITHUB_USER_SESSION, "Please set environment variable GITHUB_USER_SESSION"

    resp = requests.get(OAUTH_BINDING_URL, allow_redirects=False)
    github_oauth_url = resp.headers["Location"]

    resp = requests.get(
        github_oauth_url,
        cookies={"user_session": GITHUB_USER_SESSION},
        allow_redirects=False,
    )
    callback_url = resp.headers["Location"]

    return callback_url
