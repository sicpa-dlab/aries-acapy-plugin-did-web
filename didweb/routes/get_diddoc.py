from aiohttp import web
from aiohttp_apispec import querystring_schema
from aiohttp_apispec.decorators import docs
from aries_cloudagent.admin.request_context import AdminRequestContext
from aries_cloudagent.storage.base import BaseStorage
from aries_cloudagent.wallet.base import BaseWallet

from ..didweb_manager import DIDWebManager
from .openapi_config import OPENAPI_TAG
from .schemas import DIDWebSchema


@docs(
    tags=[OPENAPI_TAG], summary="Gets DIDDoc for specified did:web"
)
@querystring_schema(DIDWebSchema())
async def fetch_diddoc(request: web.Request):
    did = request.query.get("did")
    if not did:
        raise web.HTTPBadRequest(reason="Request query must include DID")

    context: AdminRequestContext = request["context"]

    async with context.profile.session() as session:
        manager = DIDWebManager(
            session.inject(BaseWallet),
            session.inject(BaseStorage)
        )

        diddoc = await manager.get_diddoc(did)

    return web.Response(text=diddoc.to_json())
