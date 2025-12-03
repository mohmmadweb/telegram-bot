from setuptools import setup, find_packages

setup(
    name="telegram-management-dashboard",
    version="0.1.0",  # این عدد توسط اسکریپت‌ها آپدیت می‌شود
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "sqlalchemy",
        "telethon",
        # سایر وابستگی‌هایت را اینجا اضافه کن
    ],
    author="Mohammad Web",
    author_email="mohmmadweb@gmail.com",
    description="A comprehensive Telegram Automation Dashboard",
)