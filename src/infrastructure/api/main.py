from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute
from src.application.interfaces.dice import DiceService
from src.infrastructure.container import Container

# コンテナのインスタンス化
container = Container()

app = FastAPI()

# CORSの設定
origins = ["http://localhost:3000"]  # Reactの開発サーバー

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "OPTIONS"],
    allow_headers=["*"],
    max_age=86400,  # プリフライトリクエストのキャッシュ時間（24時間）
)

def get_dice_service() -> DiceService:
    """DiceServiceの依存性を注入する"""
    return container.dice_service()

@app.get("/api/roll")
async def roll_dice(dice_service: DiceService = Depends(get_dice_service)):
    """サイコロを振るエンドポイント"""
    return dice_service.roll()

@app.get("/api/current")
async def get_current_face(dice_service: DiceService = Depends(get_dice_service)):
    """現在のサイコロの面を取得するエンドポイント"""
    try:
        return dice_service.get_current_face()
    except ValueError as e:
        return JSONResponse(
            status_code=200,
            content={"error": str(e)}
        )

@app.options("/api/{path:path}")
async def options_handler():
    """OPTIONSリクエストのハンドラー"""
    return JSONResponse(
        content={},
        headers={
            "Access-Control-Allow-Origin": origins[0],
            "Access-Control-Allow-Methods": "GET, OPTIONS",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Max-Age": "86400",
        }
    )

@app.exception_handler(404)
async def not_found_handler(request: Request, exc: HTTPException):
    """404エラーハンドラー"""
    return JSONResponse(
        status_code=404,
        content={"error": "Not Found"}
    )

# 存在しないパスへのアクセスを404にリダイレクト
@app.get("/api/{path:path}")
async def catch_all():
    """存在しないパスへのアクセスを処理する"""
    raise HTTPException(status_code=404, detail="Not Found") 