from httpx import AsyncClient


async def test_healthz(client: AsyncClient) -> None:
    resp = await client.get("/system/healthz")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


async def test_metrics(client: AsyncClient) -> None:
    resp = await client.get("/system/metrics")
    assert resp.status_code == 200
    assert "text/plain" in resp.headers["content-type"]
