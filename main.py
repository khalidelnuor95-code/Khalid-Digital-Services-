from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.db import Base, engine
from app.models import entities  # noqa
from app.api.routes import router
from app.core.db import SessionLocal
from app.models.entities import Service
from sqlalchemy import select

Base.metadata.create_all(bind=engine)
with SessionLocal() as db:
    defaults = [
        ("mikrotik-hotspot", "كروت MikroTik Hotspot", "mikrotik"),
        ("mikrotik-pppoe", "اشتراكات MikroTik PPPoE", "mikrotik"),
        ("starlink-bill", "متابعة وسداد فواتير Starlink", "starlink"),
        ("starlink-verification-assistance", "مساعدة طلبات Starlink", "starlink"),
        ("games-giftcards", "بطاقات وشحن الألعاب", "gaming"),
        ("netflix-giftcards", "بطاقات Netflix المعتمدة", "entertainment"),
        ("bein-renewal", "تجديد beIN عبر موزع معتمد", "entertainment"),
    ]
    for code, name, category in defaults:
        if not db.scalar(select(Service).where(Service.code == code)):
            db.add(Service(code=code, name=name, category=category))
    db.commit()
app = FastAPI(title=settings.app_name, version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=settings.cors_origins.split(","), allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(router, prefix="/api/v1")
