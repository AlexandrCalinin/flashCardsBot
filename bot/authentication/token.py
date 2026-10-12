import httpx

from bot.config import get_config


async def get_token() -> str:
    config = get_config()
    async with httpx.AsyncClient(base_url="https://dashboard.tutorium.io") as client:
        response = await client.post(
            "/api/auth/login", json={"email": config.tutorium_email, "password": config.tutorium_password}
        )
        response.raise_for_status()
        token = client.cookies.get("token")
        if not token:
            raise RuntimeError(f"No token cookie. Status {response.status_code}, body: {response.text[:200]}")
        return token
